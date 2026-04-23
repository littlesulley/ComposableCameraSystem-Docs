# Custom Modifiers

A custom modifier is a class derived from `UComposableCameraModifierBase` that mutates a specific node class's parameters before evaluation. Modifiers are authored in **Blueprint** most of the time — the base class is `Blueprintable` and most modifier effects are small enough that the BP overhead is irrelevant. This page covers both BP and C++ flows, and when to reach for either.

## When to write a modifier

Write a modifier when the effect is:

- **Conditional** — only applied in certain gameplay states (sprinting, aiming, stunned, in debug camera).
- **A parameter tweak** — it mutates an existing node's fields rather than adding new per-frame work.
- **Targeted at a specific node class** — `FieldOfViewNode.FOV`, `ControlRotateNode.HorizontalSpeed`, `PivotDampingNode.Interpolator.Speed`.

If the effect is always on, author it as a node configuration. If the effect needs new per-frame logic that no existing node provides, [write a new node](custom-nodes.md).

!!! warning "Non-transient cameras only"
    Modifiers are resolved on non-transient cameras only. Cinematic intros and short-lived overlays activated with `bIsTransient = true` skip modifier resolution entirely. If a cinematic needs to be modifier-aware, clear `bIsTransient` on its activation params.

## The authoring model

There are two classes you'll work with:

`UComposableCameraModifierBase` — the thing that does the work. Declares `NodeClass` and `ApplyModifier(Node)`. Abstract, Blueprintable.

`UComposableCameraNodeModifierDataAsset` — the Content-Browser wrapper that groups modifiers and adds routing metadata (priority, camera tags, enter/exit transition overrides). This is the asset gameplay code adds and removes.

You almost always author both: a modifier class (BP or C++) that defines the effect, and a data asset that references one or more modifier instances and ties them to a tag + priority.

## Blueprint authoring — the common path

**Step 1: create a modifier Blueprint.**

Content Browser → right-click → Blueprint Class → search for `ComposableCameraModifierBase`. Name it something like `BP_SprintFOVBump`.

**Step 2: set `NodeClass` on the Class Default Object.**

Open the BP, find `NodeClass` in the Details panel, set it to the node class you want to target (e.g. `FieldOfViewNode`). This is a **CDO-level** configuration — not something you set per-instance. Also create an editable float variable `FieldOfView` as the new value.

**Step 3: implement `ApplyModifier` as a BP event.**

The event gets a `Node` reference typed as `UComposableCameraCameraNodeBase`. Cast it to your concrete node class and mutate its parameters:

```
Event ApplyModifier (Node)
    → Cast to FieldOfViewNode
        → Set FieldOfView (Target: Cast result, Wire the pin of FieldOfView variable)
```

That's the entire modifier. Compile and save.

![[assets/images/Pasted image 20260417181332.png]]

**Step 4: create the data asset wrapper.**

Content Browser → right-click → Miscellaneous → Data Asset → pick `ComposableCameraNodeModifierDataAsset`. Or use the direct entry under **Composable Camera System → Node Modifier Data Asset** (purple thumbnail).

In the asset:

- Add your `BP_SprintFOVBump` modifier to the `Modifiers` array.
- Set `FieldOfView` value (e.g. 100).
- Set `Priority` (higher wins when two groups target the same node class on the same camera).
- Set `CameraTags` (e.g. `Gameplay.ThirdPerson` — the modifier applies to any camera whose type asset carries this tag).
- Optionally set `OverrideEnterTransition` / `OverrideExitTransition` for the reactivation blend when the modifier is added/removed.

![[assets/images/Pasted image 20260417181434.png]]

**Step 5: add and remove at runtime.**

From gameplay Blueprint or C++:

```cpp
AComposableCameraPlayerCameraManager* PCM =
    UComposableCameraBlueprintLibrary::GetComposableCameraPlayerCameraManager(WorldContext, /*PlayerIndex*/ 0);
UComposableCameraBlueprintLibrary::AddModifier(WorldContext, PCM, SprintModifierAsset);
// ... later:
UComposableCameraBlueprintLibrary::RemoveModifier(WorldContext, PCM, SprintModifierAsset);
```

The PCM's `UComposableCameraModifierManager` handles tag matching, priority resolution, and any reactivation blend.

![[assets/images/CustomModifiers.gif]]

## C++ authoring — when to reach for it

Most modifiers do not need C++. Reach for it when:

- The effect is **performance-sensitive** and runs on many cameras (the BP VM overhead per activation is not per-frame, but you still want C++ if you're allocating in the effect).
- The effect is **reusable across projects** and you want it shipped in a module rather than as a Blueprint asset.
- The effect needs **non-trivial math** that's painful to express in BP graph form.

The C++ pattern:

```cpp
// SprintFOVBumpModifier.h
#pragma once

#include "CoreMinimal.h"
#include "Modifiers/ComposableCameraModifierBase.h"
#include "SprintFOVBumpModifier.generated.h"

UCLASS(meta = (DisplayName = "Sprint FOV Bump"))
class MYPROJECT_API USprintFOVBumpModifier : public UComposableCameraModifierBase
{
    GENERATED_BODY()

public:
    USprintFOVBumpModifier();

    UPROPERTY(EditAnywhere, Category = "Sprint")
    float SprintFOV = 95.0f;

protected:
    virtual void ApplyModifier_Implementation(
        UComposableCameraCameraNodeBase* Node) override;
};
```

```cpp
// SprintFOVBumpModifier.cpp
#include "SprintFOVBumpModifier.h"
#include "Nodes/ComposableCameraFieldOfViewNode.h"

USprintFOVBumpModifier::USprintFOVBumpModifier()
{
    NodeClass = UComposableCameraFieldOfViewNode::StaticClass();
}

void USprintFOVBumpModifier::ApplyModifier_Implementation(
    UComposableCameraCameraNodeBase* Node)
{
    if (UComposableCameraFieldOfViewNode* FOVNode =
            Cast<UComposableCameraFieldOfViewNode>(Node))
    {
        FOVNode->FieldOfView = SprintFOV;
    }
}
```

Then author a `UComposableCameraNodeModifierDataAsset` the same way as the BP flow, adding a default-constructed `USprintFOVBumpModifier` to its `Modifiers` array.

## Priority and tag semantics (restated — these bite)

Two modifier groups can both target the same camera and the same node class. When that happens:

- Only the **higher-priority** group's modifier fires for that node class on that camera.
- Priority is per-(camera, node class) pair — a group can win on `FieldOfViewNode` and lose on `ControlRotateNode` simultaneously.
- There is **no stacking within a single `NodeClass`**.

If you want additive effects on the same node class (sprint +10° FOV *and* zoom −5° FOV), compose them inside a single modifier's `ApplyModifier` — don't rely on the manager to stack.

Camera tag matching uses `FGameplayTagContainer::HasAny`, not `HasAll`:

- A group tagged `Gameplay.ThirdPerson` applies to any camera whose tag set contains `Gameplay.ThirdPerson`, regardless of what other tags the camera carries.
- Empty `CameraTags` means "applies to all cameras" — use sparingly, it's an easy way to accidentally tweak a cutscene camera.

## Reactivation transition overrides

Adding or removing a modifier group can cause the running camera to reactivate (because its effective modifier for some node class changed). That reactivation picks a transition through this chain:

1. If adding → `OverrideEnterTransition` on the incoming group, if set.
2. If removing → `OverrideExitTransition` on the outgoing group, if set.
3. Otherwise → the [five-tier resolution chain](../user-guide/concepts/transitions.md#the-five-tier-resolution-chain), starting from the target camera's `EnterTransition`.

Use the overrides surgically — they exist so a specific modifier effect can blend differently from the camera's default, without forcing a transition table entry or a caller-supplied override at every add/remove site.

## Folder placement

| File | Location |
|---|---|
| Modifier class header | `Source/ComposableCameraSystem/Public/Modifiers/MyModifier.h` |
| Modifier class source | `Source/ComposableCameraSystem/Private/Modifiers/MyModifier.cpp` |

For project-side modifiers, mirror the `Public/Modifiers` / `Private/Modifiers` layout in your project module.

## Hot-path rule

`ApplyModifier` runs at **activation time**, not every frame. Allocations are allowed here — cache a reference, allocate a buffer, whatever the effect requires. But the node you mutate *will* be ticked every frame afterward, so don't set it up in a way that causes the node's tick to allocate. Prefer scalar assignments over array reallocations on the target node's fields.

## Testing

1. Construct the modifier asset in the editor and add it to a simple modifier data asset.
2. In PIE, activate a camera whose tag set matches the modifier's `CameraTags`.
3. Call `AddModifier` / `RemoveModifier` from a console command or input mapping.
4. Visually verify the effect, and (optionally) assert on the node's parameter values via a Gameplay Debugger extension.

For C++ modifiers, also write a unit-style test that constructs the modifier, constructs the target node, calls `ApplyModifier` directly, and asserts on the mutated fields. No PCM required for that path.

### Verifying with debug tools

Open `showdebug camera` during PIE while the modifier is active. Under **Effective Modifiers**, you should see your modifier listed:

```
[Camera Node] ComposableCameraFieldOfViewNode:
    [Modifier] BP_SprintFOVBump_C from [Asset] DA_SprintFOVModifier with priority 10
```

You can also use `CCS.Dump.Camera` to copy the running camera's full state — including all modifier-affected node parameters — to the clipboard as plain text, which is more convenient when cross-checking parameter values against expected output. When the modifier is removed, the entry disappears from both `showdebug camera` and `CCS.Dump.Camera`. This is the quickest way to confirm tag matching and priority resolution are working as expected.

## Common pitfalls

- **Modifier doesn't apply — camera has no matching tag.** Check `CameraTag` on the type asset and `CameraTags` on the data asset. Empty `CameraTags` means "all cameras" (risky); a specific tag means the camera must carry it.
- **Modifier applies but snaps instead of blends.** The camera's `EnterTransition` is null, and the data asset's `OverrideEnterTransition` is also null — so the reactivation is a hard cut. Set one of them.
- **Two modifiers fight — wrong one wins.** Higher `Priority` wins per `(camera, node class)`. There is no stacking. If you need additive effects on the same node class, compose them inside a single `ApplyModifier`.
- **Modifier applies to the cutscene camera.** `CameraTags` is empty, so it matches everything. Set it to a specific gameplay tag.
- **Transient camera ignores the modifier.** Transient cameras skip modifier resolution entirely. Clear `bIsTransient` on the activation params if the camera needs to be modifier-aware.

---

*See also:* [Modifiers Catalog](../reference/modifiers.md) for the exact field semantics; [Concepts → Modifiers](../user-guide/concepts/modifiers.md) for the full lifecycle and resolution model; [Custom Nodes](custom-nodes.md) if the effect needs per-frame work rather than a parameter tweak.
