# Tutorial: Writing a Custom Action

Author a **look-at-target** action — when gameplay code fires it, the camera smoothly rotates to face a world target over a configurable duration, then expires on its own. If the target is reached early (within a tolerance), the action expires via its condition check rather than waiting for the timer.

This tutorial assumes you have a gameplay camera running (the [Follow Camera](follow-camera.md) tutorial produces one). The action doesn't care which camera is active — it operates on the final pose.

## 0. What we're actually building

From the player's perspective: a gameplay event (picking up an item, spotting an enemy) triggers a smooth camera turn toward the point of interest, then control returns to normal. The turn doesn't snap and doesn't fight the node chain — it layers on top of it.

From the system's perspective:

1. A custom `UComposableCameraActionBase` subclass overrides `OnExecute` to interpolate the camera rotation toward a target, and overrides `CanExecute` to expire when the rotation is close enough.
2. The action uses `PostCameraTick` execution (runs after the node chain) and `Duration | Condition` expiration (whichever limit is hit first).
3. Gameplay code calls `AddAction` with the target location. The action auto-expires when done — no cleanup code needed.

## 1. Create the action class

This tutorial uses C++ because actions often involve per-frame math that's cleaner in code. A Blueprint implementation works too — the base class is `Blueprintable` — but C++ is the natural fit here.

**Folder placement:**

- `Source/YourProject/Public/Actions/LookAtTargetAction.h`
- `Source/YourProject/Private/Actions/LookAtTargetAction.cpp`

**Header:**

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

**Source:**

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
    // Compute the angle between the camera's forward and the target.
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

    // Desired rotation: look from the current camera position
    // toward the target.
    const FRotator DesiredRotation =
        (TargetLocation - CurrentPose.Location).Rotation();

    // Interpolate toward the desired rotation at RotationSpeed.
    const float MaxStep = RotationSpeed * DeltaTime;
    OutPose.Rotation = FMath::RInterpConstantTo(
        CurrentPose.Rotation, DesiredRotation, DeltaTime, MaxStep);
}
```

Two things to note:

- `CanExecute` fires every frame because the expiration type includes `Condition`. When it returns `false`, the action is expired immediately — even if the `Duration` timer hasn't run out yet. This gives us "reach the target early → stop" behavior for free.
- `OnExecute` uses `FMath::RInterpConstantTo` for a constant angular-velocity turn. For an ease-in / ease-out feel, swap to `FMath::RInterpTo` (exponential decay) or roll a custom curve.

## 2. Compile

Close the editor and compile in your IDE. This is a new `UCLASS`, so Live Coding won't pick it up — you need a full editor restart.

## 3. Trigger the action from Blueprint

Open your gameplay Blueprint (character, trigger, AI controller — wherever the "look at this" event fires). Wire:

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

`Add Action` returns the created action instance, so you can configure its `UPROPERTY` fields immediately after creation. Setting `bOnlyForCurrentCamera = true` (the default) means the action auto-expires if the camera transitions away before the turn finishes — no dangling turns on a camera that's no longer active.

## 4. Play

Enter PIE. Trigger the event. You should see:

1. The camera smoothly rotates toward the target at `RotationSpeed` degrees per second.
2. If the rotation reaches within `AngleTolerance` degrees of the target before `Duration` expires, the action stops early.
3. If the target is far away and the duration runs out first, the action stops at whatever rotation it reached.
4. After the action expires, normal stick-driven orbit resumes immediately — the node chain takes over.

Open `showdebug composablecamera` during the turn. Under **Camera Actions**, you should see:

```
Camera Actions
    LookAtTargetAction (camera-scoped)
```

When the action expires, it disappears from the list.

## 5. Tuning

A few adjustments once you see it running:

- **Turn feels too mechanical.** `RInterpConstantTo` produces a constant-speed rotation. Switch to `FMath::RInterpTo` with a speed of `~6.0` for an exponential-decay feel (fast start, slow settle). Or use `FQuat::Slerp` with a custom alpha curve for full control.
- **Camera fights the node chain.** The action runs `PostCameraTick`, so it writes *after* the node chain. If the node chain includes a `LookAtNode` with hard constraint, the next frame's node chain will snap the rotation back. Either soften the `LookAtNode` constraint during the action, or set `ExecutionType = PreCameraTick` so the action runs first and the node chain corrects after.
- **Want the turn to survive a camera switch.** Set `bOnlyForCurrentCamera = false` to make the action persistent. Be aware that a persistent action keeps rotating even on cameras that don't expect it — use with care.
- **Need to cancel the action early from code.** Call `ExpireAction` on the Blueprint library, or call `ExpireAction()` on the action instance directly.

## 6. Making it Blueprint-only

If you prefer not to write C++ for this, the same action is achievable in Blueprint:

1. Content Browser → right-click → Blueprint Class → `ComposableCameraActionBase`. Name it `BP_LookAtTargetAction`.
2. In Class Defaults, set `ExecutionType = PostCameraTick`, `ExpirationType = Duration | Condition`, `Duration = 1.5`.
3. Add variables: `TargetLocation` (Vector), `RotationSpeed` (Float, default 180), `AngleTolerance` (Float, default 1.5).
4. Override **Can Execute** — compute the angle, return `AngleDeg > AngleTolerance`.
5. Override **On Execute** — compute `DesiredRotation`, interpolate, write `OutPose`.

The logic is identical; the only difference is the authoring surface.

## Common pitfalls

- **Action doesn't run.** `AddAction` returns `nullptr` — another instance of the same class is already active. Only one action per class is allowed at a time. Expire the old one first, or use a different class for concurrent look-at targets.
- **Camera snaps back after the action finishes.** The node chain's `LookAtNode` or `ControlRotateNode` immediately reasserts its rotation on the next frame. This is expected — the action is a temporary overlay, not a permanent change. If you want the rotation to persist, either disable the competing node for the duration, or treat the action's final rotation as input to the node chain (e.g. via a context variable).
- **Action doesn't expire when `CanExecute` returns false.** `ExpirationType` doesn't include `Condition`. The condition check only fires if the `Condition` flag is set in the bitmask.
- **Persistent action keeps rotating on a cutscene camera.** `bOnlyForCurrentCamera = false` means the action survives camera switches. Set it to `true` unless you explicitly need cross-camera persistence.

## Where next

- [Camera Actions](../user-guide/camera-actions.md) — the full authoring guide: execution timing, expiration types, camera-scoped vs. persistent, shipped actions.
- [Concepts → Actions](../user-guide/concepts/actions.md) — the conceptual model: where actions sit relative to nodes and modifiers.
- [`UComposableCameraActionBase` API](../reference/api/actions/UComposableCameraActionBase.md) — full class reference.
