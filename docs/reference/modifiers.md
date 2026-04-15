# Modifier Catalog

Modifiers target a specific **node class** and mutate that node's parameters before it ticks. See [Concepts → Modifiers](../user-guide/concepts/modifiers.md) for the full lifecycle and resolution semantics; this page catalogs the shipped types.

## `UComposableCameraModifierBase`

*Abstract. Blueprintable.*

The base class every modifier derives from. It has two members and expects subclasses (C++ or Blueprint) to fill them in:

| Member | Type | Purpose |
|---|---|---|
| `NodeClass` | `TSubclassOf<UComposableCameraCameraNodeBase>` | Which node class this modifier targets. Set on the **Class Default Object** — do not edit per-instance. |
| `ApplyModifier(Node)` | `BlueprintImplementableEvent` | Called once during activation with the matching node instance. Mutate the node's parameters here. |

The plugin does not ship any concrete subclasses — modifiers are entirely user-authored. See [Extending → Custom Modifiers](../extending/custom-modifiers.md) for the authoring recipe.

!!! warning "Non-transient cameras only"
    Modifiers can only be applied to non-transient cameras. A transient camera (activated with `bIsTransient = true` on `FComposableCameraActivationParams`) skips modifier resolution entirely. Cinematic intros and short-lived overlays are typical transient cameras — if you need them modifier-aware, clear `bIsTransient`.

## `UComposableCameraNodeModifierDataAsset`

*Concrete. The authoring wrapper.*

A `UDataAsset` that groups one or more modifier instances together and attaches routing metadata. This is the unit you add and remove at runtime — individual modifier instances are not directly managed by the modifier manager.

| Field | Type | Purpose |
|---|---|---|
| `Modifiers` | `TArray<UComposableCameraModifierBase*>` (instanced) | The modifier instances in this group. You can pack several modifiers targeting different node classes into one asset. |
| `OverrideEnterTransition` | `UComposableCameraTransitionBase*` (instanced) | Transition used when this group reactivates the camera on add. Falls back to the camera's default transition if null. |
| `OverrideExitTransition` | `UComposableCameraTransitionBase*` (instanced) | Transition used when this group reactivates the camera on remove. Falls back to the camera's default transition if null. |
| `CameraTags` | `FGameplayTagContainer` | Gameplay tags identifying which cameras this group applies to. Only cameras whose tags match this container are affected. |
| `Priority` | `int32` (≥ 0) | When two groups both target the same node class for the same camera, the higher-priority group's modifier wins. |

Registered in the Content Browser under **Composable Camera System → Node Modifier Data Asset** with a purple color and a custom SVG thumbnail.

### Why the wrapper

A modifier on its own is an instanced subobject — it can't live in the Content Browser and can't be referenced from multiple places. The data asset exists so designers can:

- Tune a modifier once in the asset and reference it from many Blueprints.
- Ship a library of preset gameplay effects (sprint FOV bump, aim-in pitch damping, stun shake) as named assets.
- Route via gameplay tags and priority without writing any gameplay code.

## Priority — one group wins per (camera, node class)

When two `UComposableCameraNodeModifierDataAsset`s both target the same camera (by gameplay tags) and both contain a modifier for the same `NodeClass`, only the higher-`Priority` group's modifier is active. This resolution happens in `FComposableCameraModifierData::UpdateEffectiveModifiers` each time the modifier set changes.

If you want additive behavior (sprint +10° FOV *and* zoom −5° FOV applied together), either:

- put both effects in a single modifier's `ApplyModifier` (authored as one Blueprint event), or
- split them into modifiers targeting different node classes — e.g. `FieldOfViewNode` for the FOV bump and a dedicated `ZoomNode` for the zoom — so each wins its own class-level contest independently.

There is no stacking within a single `NodeClass`.

## Camera tags — which cameras a group applies to

Every camera carries a `FGameplayTagContainer` (declared on its type asset). When a modifier group's `CameraTags` container is non-empty, the modifier manager only considers the group for cameras whose tags match.

- Empty `CameraTags` → "applies to all cameras". Use sparingly.
- One or more tags → "applies only to cameras with any of these tags". Standard usage.

Tag matching is via `FGameplayTagContainer::HasAny`, not `HasAll` — a group tagged `Gameplay.ThirdPerson` matches any camera that carries `Gameplay.ThirdPerson` in its tag set, even if the camera carries additional tags.

## Enter/exit transition overrides

When adding or removing a modifier group causes a reactivation (because the effective modifier for some node class changed on the running camera), the reactivation uses a transition resolved through:

1. If adding → `OverrideEnterTransition` on the incoming group, if set.
2. If removing → `OverrideExitTransition` on the outgoing group, if set.
3. Otherwise → the [five-tier resolution chain](../user-guide/transitions-and-blending.md#five-tier-resolution-chain-in-practice), starting from the target camera's `EnterTransition`.

This gives modifier authors a surgical tool for "when this effect is added/removed, blend differently than the camera's default" — without forcing a table entry or a caller-supplied override at every activation site.

## `UComposableCameraModifierManager`

*Runtime manager, owned by the PCM. Not user-facing.*

The manager maintains:

- `ModifierData` — the map of `FGameplayTag → TMap<NodeClass, TArray<FModifierEntry>>`, holding every active modifier indexed by camera tag and node class.
- `EffectiveModifiers` — the computed map of `NodeClass → FModifierEntry` for the currently running camera, representing whatever wins the per-node-class priority contest.

Two public entry points drive the manager:

```cpp
void AddModifier(UComposableCameraNodeModifierDataAsset* ModifierAsset);
void RemoveModifier(UComposableCameraNodeModifierDataAsset* ModifierAsset);
```

Both funnel through `UpdateEffectiveModifiers`, which returns a `(bChanged, Transition*)` pair. If `bChanged` is true, the PCM triggers a reactivation using the returned transition.

Gameplay code should always go through `UComposableCameraBlueprintLibrary::AddModifier` / `RemoveModifier` rather than poking the manager directly — the library takes the world-context object and the player index and resolves the correct PCM for you.

---

*See also:* [Concepts → Modifiers](../user-guide/concepts/modifiers.md), [Extending → Custom Modifiers](../extending/custom-modifiers.md), [Blueprint API → Modifiers](../user-guide/blueprint-api.md#modifiers).
