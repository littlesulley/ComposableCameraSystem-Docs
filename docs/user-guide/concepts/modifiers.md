# Modifiers

A modifier is a runtime-added override that targets a specific **node class** and alters that node's parameters before it ticks. Modifiers let you change how the current camera behaves without creating a new camera type or editing the active type asset.

Examples of things modifiers are good for:

- Halving the `LookAtNode`'s look-at weight during a stunned state.
- Pushing `FieldOfViewNode`'s FOV by +10° during a sprint.
- Disabling `CollisionPushNode` for a boss-room flyover, then re-enabling it on exit.
- Temporarily swapping `ControlRotateNode`'s input-rate multiplier during a zoomed aim.

Modifiers do **not** add or remove nodes — they only tweak the parameters of nodes that are already part of the active camera.

## Not Unreal's `UCameraModifier`

If you've used UE's built-in `UCameraModifier`, the names are similar but the level of the system is different. UE's modifiers sit at the Player Camera Manager level and post-process the final view. ComposableCameraSystem's modifiers sit *underneath* the PCM's final output — they target individual nodes inside the active camera, before its evaluation runs.

In practice that means:

- UE's modifiers run last and see only the finished pose.
- ComposableCameraSystem modifiers run first, at the per-node parameter level, and every node downstream sees their effect.

The two are not interchangeable and don't interact.

## Architecture at a glance

```
UComposableCameraModifierBase (abstract, Blueprintable)
  - NodeClass: TSubclassOf<UComposableCameraCameraNodeBase>
  - Priority: int32
  - ApplyModifier(...): Blueprint-implementable override

UComposableCameraNodeModifierDataAsset
  - Wraps modifier instances as standalone data assets

UComposableCameraModifierManager  (owned by the PCM)
  - AddModifier / RemoveModifier
  - Maintains the set of all active modifiers
  - Computes the effective modifier per node class
  - Triggers reactivation when the effective set changes
```

- **`UComposableCameraModifierBase`** is an abstract, `Blueprintable` class. You subclass it (C++ or Blueprint), declare the `NodeClass` it targets, and override `ApplyModifier` to mutate that node's parameters. Priority is a simple `int32`.
- **`UComposableCameraNodeModifierDataAsset`** wraps a modifier instance so it can live in the Content Browser as a standalone data asset. Registered with a purple color + custom thumbnail under "Composable Camera System".
- **`UComposableCameraModifierManager`** is created by the PCM and is the single source of truth for which modifiers are active.

## Priority — one modifier wins per node class

When multiple modifiers target the same `NodeClass`, **only the highest-priority one is active**. This is by design. If you stack a "sprint FOV +10°" modifier and a "stunned FOV -20°" modifier on `FieldOfViewNode`, you don't get +10 − 20 = -10; you get whichever one has higher priority. If you want additive effects, author a single modifier that folds the logic into one `ApplyModifier` call.

The "effective modifier" is recomputed whenever the set of active modifiers changes.

## Reactivation on modifier changes

When the effective modifier for the running camera's node class changes (either because a modifier was added, removed, or because the priority ordering shifted), the system doesn't just "re-read" parameters on the live node — it performs a **seamless reactivation**:

1. The PCM detects the change via `OnModifierChanged()`.
2. It checks whether the running camera uses a node of the affected class. If not, nothing happens.
3. If affected, a fresh camera of the same type is spawned, and the old camera is transitioned away using whatever transition the [five-tier resolution chain](transitions.md#the-five-tier-resolution-chain) resolves for that pair — typically the camera's own `EnterTransition`.

From the player's perspective this looks like a short, clean blend into a camera that now behaves with the new modifier applied.

The reactivation path shares the same infrastructure as all other type-asset activations — it reads `SourceTypeAsset` and `SourceParameterBlock` off the running camera, restores them into `PendingTypeAsset` / `PendingParameterBlock`, and calls through `OnTypeAssetCameraConstructed` to rebuild the new camera's node list, runtime data block, and exec chains. Nothing about this path is modifier-specific; it's the general "same camera, fresh instance" path.

## Adding and removing modifiers at runtime

From Blueprint, use the `Add Modifier` and `Remove Modifier` nodes on `UComposableCameraBlueprintLibrary`. Both take a world-context object, a player index, and the modifier instance (or a `UComposableCameraNodeModifierDataAsset` wrapping one).

From C++, call through the PCM's `ModifierManager` directly if you already have a reference:

```cpp
PCM->ModifierManager->AddModifier(MyModifierInstance);
// later...
PCM->ModifierManager->RemoveModifier(MyModifierInstance);
```

Modifiers can be added and removed at any time — the manager handles the reactivation machinery on your behalf.

## Scoping

Modifiers have no built-in scoping (they're not per-camera or per-context). An active modifier affects any camera whose node list contains its target class, on any context. Scope is typically managed by gameplay code — you add the modifier when the condition starts and remove it when the condition ends.

For one-shot, camera-scoped overrides (e.g. "only while this camera is running"), prefer [Actions](../../reference/api/actions/UComposableCameraActionBase.md) instead, which are expired automatically when a camera transitions away.

## In summary

- Modifiers target a **node class**, not a specific node instance or camera.
- **Highest priority wins** per node class; there's no stacking.
- Adding, removing, or changing the effective modifier triggers a **seamless reactivation** of the running camera, not a live-property patch.
- They sit below the PCM's final output, affecting node parameters before evaluation — unrelated to Unreal's built-in `UCameraModifier`.

This concludes the concepts tour. From here:

- If you want to start authoring, jump to [Authoring Camera Types](../authoring-camera-types.md).
- If you want the full catalog of shipped nodes/transitions/modifiers, see [Reference](../../reference/index.md).
- If you want to write your own nodes/transitions/modifiers, see [Extending](../../extending/index.md).
