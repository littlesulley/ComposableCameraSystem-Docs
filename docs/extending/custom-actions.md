# Custom Actions

A custom action is a class derived from `UComposableCameraActionBase` that hooks into the camera's pre- or post-tick delegates. Actions sit outside the node chain — they don't produce or transform the pose the way nodes do. Instead, they read the current pose, run arbitrary logic, and optionally write back a modified pose. Use them for transient effects that don't belong in the permanent node composition: smooth one-shot moves, timed rotations, pitch resets, or any gameplay-triggered behavior that should expire on its own.

## When to write an action

Write an action when the effect is:

- **Temporary** — it should expire after some duration, condition, or when the camera switches.
- **Self-contained** — it doesn't need to modify node parameters (that's a [modifier](custom-modifiers.md)) or add per-frame evaluation logic to the camera's permanent chain (that's a [node](custom-nodes.md)).
- **Fire-and-forget** — gameplay code triggers it with `AddAction` and never touches it again; the action manages its own lifecycle.

If the effect is always part of this camera's behavior, write a node. If the effect mutates an existing node's parameters conditionally, write a modifier.

## The action contract

Every action subclass has two overridable hooks:

- **`CanExecute(DeltaTime, CurrentPose) → bool`** — a predicate called each frame when the action's `ExpirationType` includes `Condition`. Return `false` to expire the action.
- **`OnExecute(DeltaTime, CurrentPose, OutPose)`** — the main logic. Reads the current camera pose, does its work, and writes `OutPose`. Called every frame the action is alive.

Both are `BlueprintNativeEvent`s, so they work in C++ and Blueprint.

## Execution timing

Each action declares when it runs relative to the camera tick via `ExecutionType`:

| Value | When it runs |
|---|---|
| `PreCameraTick` | Before the camera's node chain evaluates |
| `PostCameraTick` | After the camera's node chain evaluates |

Most actions use `PostCameraTick` — they layer on top of whatever the node chain produces. Use `PreCameraTick` when you want the node chain to correct after your action (e.g. the action sets a rough rotation, and the node chain's `LookAtNode` refines it).

## Expiration types

Actions expire through one or more of these modes (combinable as a bitmask):

| Flag | Behavior |
|---|---|
| `Instant` | Runs for exactly one frame, then expires |
| `Duration` | Runs for `Duration` seconds, then expires |
| `Manual` | Runs indefinitely until you call `ExpireAction()` from code |
| `Condition` | Runs until `CanExecute()` returns `false` |

Combine flags for "whichever comes first" behavior — `Duration | Condition` means the action expires when either the timer runs out or the condition fails.

## Camera-scoped vs. persistent

The `bOnlyForCurrentCamera` flag (default `true`) controls lifetime across camera switches:

- **Camera-scoped** (`true`): the action auto-expires when the running camera changes. A smooth-rotate action targeting the current camera won't linger after a transition.
- **Persistent** (`false`): the action survives camera switches. Use this for effects that should span the entire gameplay session or context.

Only one instance of a given action class can be active at a time. `AddAction` returns `nullptr` if the same class is already registered.

## C++ authoring

Actions are the extension type most likely to involve per-frame math, so C++ is the natural fit. The pattern:

```cpp
// LookAtTargetAction.h
#pragma once

#include "CoreMinimal.h"
#include "Actions/ComposableCameraActionBase.h"
#include "LookAtTargetAction.generated.h"

/**
 * Smoothly rotates the camera to face a world target over
 * the action's duration. Expires early if the rotation is
 * within AngleTolerance degrees of the target direction.
 */
UCLASS(meta = (DisplayName = "Look At Target"))
class YOURPROJECT_API ULookAtTargetAction
    : public UComposableCameraActionBase
{
    GENERATED_BODY()

public:
    ULookAtTargetAction();

    /** World-space position to look at. */
    UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Look At")
    FVector TargetLocation = FVector::ZeroVector;

    /** Interpolation speed (degrees per second). */
    UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Look At",
              meta = (ClampMin = "10.0", ClampMax = "720.0"))
    float RotationSpeed = 180.0f;

    /** If the remaining angle is below this, expire early. */
    UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Look At",
              meta = (ClampMin = "0.1", ClampMax = "10.0"))
    float AngleTolerance = 1.5f;

protected:
    virtual bool CanExecute_Implementation(
        float DeltaTime,
        const FComposableCameraPose& CurrentPose) override;

    virtual void OnExecute_Implementation(
        float DeltaTime,
        const FComposableCameraPose& CurrentPose,
        FComposableCameraPose& OutPose) override;
};
```

```cpp
// LookAtTargetAction.cpp
#include "Actions/LookAtTargetAction.h"

ULookAtTargetAction::ULookAtTargetAction()
{
    // Run after the camera's node chain has produced its pose.
    ExecutionType = EComposableCameraActionExecutionType::PostCameraTick;

    // Expire when either the timer runs out OR CanExecute returns false.
    ExpirationType = EComposableCameraActionExpirationType::Duration
                   | EComposableCameraActionExpirationType::Condition;

    // Default duration — callers can override before or after AddAction.
    Duration = 1.5f;
}

bool ULookAtTargetAction::CanExecute_Implementation(
    float DeltaTime,
    const FComposableCameraPose& CurrentPose)
{
    const FVector ToTarget =
        (TargetLocation - CurrentPose.Location).GetSafeNormal();
    const FVector Forward =
        CurrentPose.Rotation.Vector();

    const float AngleDeg =
        FMath::RadiansToDegrees(FMath::Acos(
            FMath::Clamp(FVector::DotProduct(Forward, ToTarget),
                         -1.0f, 1.0f)));

    // Keep running if we haven't reached the tolerance yet.
    return AngleDeg > AngleTolerance;
}

void ULookAtTargetAction::OnExecute_Implementation(
    float DeltaTime,
    const FComposableCameraPose& CurrentPose,
    FComposableCameraPose& OutPose)
{
    OutPose = CurrentPose;

    const FRotator DesiredRotation =
        (TargetLocation - CurrentPose.Location).Rotation();

    const float MaxStep = RotationSpeed * DeltaTime;
    OutPose.Rotation = FMath::RInterpConstantTo(
        CurrentPose.Rotation, DesiredRotation, DeltaTime, MaxStep);
}
```

Two things to note:

- `CanExecute` fires every frame because the expiration type includes `Condition`. When it returns `false`, the action is expired immediately — even if the `Duration` timer hasn't run out yet.
- `OnExecute` uses `FMath::RInterpConstantTo` for a constant angular-velocity turn. For an ease-in/ease-out feel, swap to `FMath::RInterpTo` (exponential decay) or use `FQuat::Slerp` with a custom alpha curve.

## Blueprint authoring

The base class is `Blueprintable`, so the same action is achievable without C++:

1. Content Browser → right-click → Blueprint Class → `ComposableCameraActionBase`. Name it `BP_LookAtTargetAction`.
2. In Class Defaults, set `ExecutionType = PostCameraTick`, `ExpirationType = Duration | Condition`, `Duration = 1.5`.
3. Add variables: `TargetLocation` (Vector), `RotationSpeed` (Float, default 180), `AngleTolerance` (Float, default 1.5).
4. Override **Can Execute** — compute the angle, return `AngleDeg > AngleTolerance`.
5. Override **On Execute** — compute the desired rotation, interpolate, write `OutPose`.

The logic is identical; the only difference is the authoring surface.

## Triggering from gameplay

Wire `AddAction` and configure the returned instance:

```
On Item Picked Up (or On Enemy Spotted, etc.)
  └─> Get Composable Camera Player Camera Manager (Index 0) ─┐
  └─> Add Action
        PCM:                    ↑
        Action Class:           LookAtTargetAction
        bOnlyForCurrentCamera:  true
      └─> (return value) Cast to LookAtTargetAction
          └─> Set Target Location = (item/enemy world position)
          └─> Set Duration = 1.0
```

`AddAction` returns the created action instance, so you can configure its `UPROPERTY` fields immediately after creation. Setting `bOnlyForCurrentCamera = true` means the action auto-expires if the camera transitions away before the turn finishes.

## Folder placement

| File | Location |
|---|---|
| Action class header | `Source/ComposableCameraSystem/Public/Actions/MyAction.h` |
| Action class source | `Source/ComposableCameraSystem/Private/Actions/MyAction.cpp` |

For project-side actions, mirror the `Public/Actions` / `Private/Actions` layout in your project module.

## Hot-path rule

`OnExecute` runs once per frame per active action. Keep it allocation-free: no `FString::Printf`, no dynamic array growth, no `NewObject`. Cache any expensive state in the constructor or when properties are set.

`CanExecute` also runs every frame when condition-based expiration is active. The same constraint applies.

## Verifying with showdebug

Open `showdebug camera` during PIE while the action is active. Under **Camera Actions**, you should see:

```
Camera Actions
    LookAtTargetAction (camera-scoped)
```

When the action expires, it disappears from the list.

## Tuning tips

- **Turn feels too mechanical.** `RInterpConstantTo` produces constant-speed rotation. Switch to `FMath::RInterpTo` with a speed of `~6.0` for an exponential-decay feel (fast start, slow settle). Or use `FQuat::Slerp` with a custom alpha curve for full control.
- **Camera fights the node chain.** The action runs `PostCameraTick`, so it writes *after* the node chain. If the node chain includes a `LookAtNode` with a hard constraint, the next frame's node chain will snap the rotation back. Either soften the `LookAtNode` constraint during the action, or set `ExecutionType = PreCameraTick` so the action runs first and the node chain corrects after.
- **Want the turn to survive a camera switch.** Set `bOnlyForCurrentCamera = false`. Be aware that a persistent action keeps rotating even on cameras that don't expect it.
- **Need to cancel the action early from code.** Call `ExpireAction` on the Blueprint library, or call `ExpireAction()` on the action instance directly.

## Common pitfalls

- **Action doesn't run.** `AddAction` returns `nullptr` — another instance of the same class is already active. Only one action per class is allowed at a time. Expire the old one first, or use a different class for concurrent targets.
- **Camera snaps back after the action finishes.** The node chain's `LookAtNode` or `ControlRotateNode` immediately reasserts its rotation on the next frame. This is expected — the action is a temporary overlay, not a permanent change.
- **Action doesn't expire when `CanExecute` returns false.** `ExpirationType` doesn't include `Condition`. The condition check only fires if the `Condition` flag is set in the bitmask.
- **Persistent action keeps rotating on a cutscene camera.** `bOnlyForCurrentCamera = false` means the action survives camera switches. Set it to `true` unless you explicitly need cross-camera persistence.

---

*See also:* [Camera Actions](../user-guide/camera-actions.md) for the full user-guide walkthrough; [Actions API Reference](../reference/api/actions/UComposableCameraActionBase.md) for the class interface; [Custom Nodes](custom-nodes.md) if you need permanent per-frame work rather than a temporary overlay.
