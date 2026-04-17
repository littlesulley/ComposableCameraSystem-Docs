# Tutorial: Writing a Custom Modifier

Add a **sprint FOV bump** — when the player sprints, the active gameplay camera's field of view widens from its authored default to a snappier 95°, blending in and out smoothly via a reactivation transition. When the sprint ends, the camera settles back to its normal FOV.

This tutorial assumes you have a gameplay camera with a `FieldOfViewNode` already running (the [Follow Camera](follow-camera.md) tutorial produces one). If you don't, any camera with a `FieldOfViewNode` in its chain works.

## 0. What we're actually building

From the player's perspective: they hold the sprint button, the viewport gradually widens for a subtle speed feel, and when they release it, the view narrows back. The camera doesn't snap — both directions blend.

From the system's perspective:

1. A modifier class targets `UComposableCameraFieldOfViewNode` and overrides its `FieldOfView` property.
2. A modifier data asset wraps that class, sets a priority and camera tag filter, and optionally supplies transition overrides for the reactivation blend.
3. Gameplay code calls `AddModifier` on sprint start and `RemoveModifier` on sprint end.
4. The PCM's modifier manager detects that the effective modifier for `FieldOfViewNode` changed, triggers a seamless reactivation, and blends the running camera into a fresh instance with the new FOV applied.

You author steps 1–3. The PCM handles step 4.

## 1. Create the modifier class (Blueprint)

Content Browser → right-click → **Blueprint Class** → search for `ComposableCameraModifierBase`. Name it `BP_SprintFOVBump`.

Open it. In the **Class Defaults** panel, find `NodeClass` and set it to `ComposableCameraFieldOfViewNode`. This tells the system "this modifier only applies to FieldOfView nodes" — the manager won't hand it a `LookAtNode` or a `PivotOffsetNode`.

!!! warning "NodeClass is CDO-level"
    `NodeClass` must be set on the Class Default Object, not on a placed or spawned instance. It's the modifier's identity — "I am a FieldOfView modifier". If it's unset, the modifier silently does nothing.

## 2. Implement `ApplyModifier`

In the Event Graph, add an override for **Apply Modifier**. The event gives you a `Node` reference typed as the base class. Cast it to `ComposableCameraFieldOfViewNode` and set the property:

```
Event ApplyModifier (Node)
  → Cast to ComposableCameraFieldOfViewNode
      → Set FieldOfView = 95.0
```

That's the entire modifier logic. `ApplyModifier` runs once at camera activation (not every frame), so the cost is negligible.

Compile and save.

!!! tip "Parameterize the FOV"
    For a more reusable modifier, add a `UPROPERTY(EditAnywhere)` variable `SprintFOV` (default `95.0`) on the Blueprint and use it instead of a hardcoded value. Then each data asset that references the modifier can set a different sprint FOV without duplicating the class.

## 3. Create the data asset wrapper

Content Browser → right-click → **Composable Camera System → Node Modifier Data Asset**. Name it `DA_SprintFOVModifier`.

Open it and configure:

| Field | Value | Why |
|---|---|---|
| **Modifiers** | Add one entry: `BP_SprintFOVBump` | The modifier class from step 1 |
| **Priority** | `10` | Wins over any lower-priority group also targeting `FieldOfViewNode`. Typical gameplay modifiers live in the 1–20 range. |
| **CameraTags** | `Gameplay.ThirdPerson` | Only applies to cameras whose type asset carries this tag. Keeps cutscene cameras unaffected. |
| **OverrideEnterTransition** | (optional) An `InertializedTransition` with `TransitionDuration = 0.25` | A quick blend in when the modifier activates — faster than the camera's default `EnterTransition`. |
| **OverrideExitTransition** | (optional) An `InertializedTransition` with `TransitionDuration = 0.35` | A slightly longer blend out when the modifier is removed — the return to normal FOV feels smoother if it's slower than the snap in. |

Save.

!!! note "Tag your camera"
    For `CameraTags` to work, the target camera's type asset must carry a matching tag. Open `CT_ThirdPersonFollow` (or your gameplay camera), find `CameraTag` in the Details panel, and set it to `Gameplay.ThirdPerson` if it isn't already.

## 4. Wire up sprint input

Open your character (or player controller) Blueprint. You need two events: sprint start and sprint end.

**Sprint start:**

```
On Sprint Started
  └─> Get Composable Camera Player Camera Manager (Index 0) ─┐
  └─> Add Modifier (PCM: ↑, Modifier Asset: DA_SprintFOVModifier)
```

**Sprint end:**

```
On Sprint Ended
  └─> Get Composable Camera Player Camera Manager (Index 0) ─┐
  └─> Remove Modifier (PCM: ↑, Modifier Asset: DA_SprintFOVModifier)
```

`Add Modifier` and `Remove Modifier` are on `UComposableCameraBlueprintLibrary`. Both take a world context, a resolved PCM pointer, and the `UComposableCameraNodeModifierDataAsset` to add or remove.

## 5. Play

Enter PIE. Sprint. You should see:

1. A smooth inertialized blend from 70° (or whatever your camera's authored default is) to 95° as the modifier kicks in.
2. The wider FOV holds for the duration of the sprint.
3. A smooth inertialized blend back to the default FOV when sprint ends.

Open `showdebug composablecamera` during the sprint. Under **Effective Modifiers**, you should see:

```
[Camera Node] ComposableCameraFieldOfViewNode:
    [Modifier] BP_SprintFOVBump_C from [Asset] DA_SprintFOVModifier with priority 10
```

When sprint ends, that entry disappears.

## 6. The C++ alternative

The Blueprint flow above is the recommended path for most modifiers. If you prefer C++ (for shipping in a module, for non-trivial math, or for consistency with a C++ codebase), the equivalent is short:

**Header** (`Source/YourProject/Public/Modifiers/SprintFOVBumpModifier.h`):

```cpp
#pragma once

#include "CoreMinimal.h"
#include "Modifiers/ComposableCameraModifierBase.h"
#include "SprintFOVBumpModifier.generated.h"

UCLASS(meta = (DisplayName = "Sprint FOV Bump"))
class YOURPROJECT_API USprintFOVBumpModifier
    : public UComposableCameraModifierBase
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

**Source** (`Source/YourProject/Private/Modifiers/SprintFOVBumpModifier.cpp`):

```cpp
#include "Modifiers/SprintFOVBumpModifier.h"
#include "Nodes/ComposableCameraFieldOfViewNode.h"

USprintFOVBumpModifier::USprintFOVBumpModifier()
{
    NodeClass = UComposableCameraFieldOfViewNode::StaticClass();
}

void USprintFOVBumpModifier::ApplyModifier_Implementation(
    UComposableCameraCameraNodeBase* Node)
{
    if (auto* FOVNode = Cast<UComposableCameraFieldOfViewNode>(Node))
    {
        FOVNode->FieldOfView = SprintFOV;
    }
}
```

Compile, restart the editor (new `UCLASS` = full restart), then create a `DA_SprintFOVModifier` data asset referencing this C++ class instead of the Blueprint one. The rest of the wiring is identical.

## Common pitfalls

- **Modifier doesn't apply — camera has no matching tag.** Check `CameraTag` on the type asset and `CameraTags` on the data asset. Empty `CameraTags` means "all cameras" (risky); a specific tag means the camera must carry it.
- **Modifier applies but snaps instead of blends.** The camera's `EnterTransition` is null, and the data asset's `OverrideEnterTransition` is also null — so the reactivation is a hard cut. Set one of them.
- **Two modifiers fight — wrong one wins.** Higher `Priority` wins per `(camera, node class)`. There is no stacking. If you need additive effects on the same node class, compose them inside a single `ApplyModifier`.
- **Modifier applies to the cutscene camera.** `CameraTags` is empty, so it matches everything. Set it to a specific gameplay tag.
- **Transient camera ignores the modifier.** Transient cameras skip modifier resolution entirely. Clear `bIsTransient` on the activation params if the camera needs to be modifier-aware.

## Where next

- [Custom Modifiers](../extending/custom-modifiers.md) — the full authoring recipe, including priority semantics, reactivation transition overrides, and the hot-path rule.
- [Concepts → Modifiers](../user-guide/concepts/modifiers.md) — the conceptual model: priority resolution, tag scoping, reactivation lifecycle.
- [Modifier Catalog](../reference/modifiers.md) — field reference for the shipped modifier base class and data asset.
