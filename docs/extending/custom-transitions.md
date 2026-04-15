# Custom Transitions

A custom transition is a C++ class derived from `UComposableCameraTransitionBase` that blends two input poses into one output pose each frame. This is the smallest of the four recipes — the pose-only contract keeps the authoring surface narrow, which makes transitions both easy to write and genuinely reusable across any camera pair and any context boundary.

## When to write a transition

Write a transition when your feature is **"how to get from pose A to pose B"** — a new easing curve, a new physics-plausible blend, a context-aware modulation of an existing blend. If your feature authors or mutates a pose per frame *without* blending between two poses, write a [node](custom-nodes.md) instead.

## The four-phase lifecycle

Every transition moves through four phases. You only override the middle two.

| Phase | Override? | Fires |
|---|---|---|
| `TransitionEnabled(InitParams)` | No — base handles it | Once, when the transition is first wired into the tree. Caches `InitParams` (source/previous source poses, delta time) for later. |
| `OnBeginPlay_Implementation(DeltaTime, Source, Target)` | Yes | Once, on the first `Evaluate` frame. Use this to construct internal state derived from the source/target (polynomial coefficients, spline control points). |
| `OnEvaluate_Implementation(DeltaTime, Source, Target)` | Yes — required | Every frame thereafter. Receives live source/target poses and `Percentage ∈ [0, 1]`. Returns the blended pose. |
| `OnFinished` | Optional | Once, when `RemainingTime` drops to zero. Blueprint-implementable event — the C++ base handles the `bFinished` flag. |

`Percentage`, `RemainingTime`, and `TransitionTime` are all maintained on the base class and accessible as `UPROPERTY`s / BP-pure accessors. You do not advance them yourself.

## A minimal example

```cpp
// MyEaseTransition.h
#pragma once

#include "CoreMinimal.h"
#include "Transitions/ComposableCameraTransitionBase.h"
#include "MyEaseTransition.generated.h"

UCLASS(meta = (DisplayName = "My Ease"))
class MYPROJECT_API UMyEaseTransition : public UComposableCameraTransitionBase
{
    GENERATED_BODY()

public:
    UPROPERTY(EditAnywhere, meta = (ClampMin = "0.1", ClampMax = "10.0"))
    float Exponent = 2.0f;

protected:
    virtual FComposableCameraPose OnEvaluate_Implementation(
        float DeltaTime,
        const FComposableCameraPose& CurrentSourcePose,
        const FComposableCameraPose& CurrentTargetPose) override;
};
```

```cpp
// MyEaseTransition.cpp
#include "MyEaseTransition.h"

FComposableCameraPose UMyEaseTransition::OnEvaluate_Implementation(
    float DeltaTime,
    const FComposableCameraPose& CurrentSourcePose,
    const FComposableCameraPose& CurrentTargetPose)
{
    const float T = FMath::Pow(GetPercentage(), Exponent);
    return FComposableCameraPose::BlendBy(CurrentSourcePose, CurrentTargetPose, T);
}
```

That's the whole transition. No hooks into the PCM, no director awareness, no context-stack plumbing. The base class drives lifecycle; you contribute the math.

## Working with `InitParams` — velocity and source snapshots

The base class exposes a `UPROPERTY FComposableCameraTransitionInitParams InitParams` populated in `TransitionEnabled`. It carries:

- `CurrentSourcePose` — the blended output the player was just seeing, at the moment the transition was created.
- `PreviousSourcePose` — the frame-before version.
- `DeltaTime` — the frame delta at creation.

Velocity-aware transitions (inertialization, physics-plausible easing) read these in `OnBeginPlay_Implementation` and derive velocity as `(Current − Previous) / DeltaTime`. Without that snapshot, a blend starting while the source camera is mid-motion would visibly kink at `t=0` as velocity snapped to zero.

Transitions that don't care about velocity (linear, cubic, smoothstep) can ignore `InitParams` entirely.

```cpp
void UMyInertializedTransition::OnBeginPlay_Implementation(
    float DeltaTime,
    const FComposableCameraPose& CurrentSourcePose,
    const FComposableCameraPose& CurrentTargetPose)
{
    const FVector InitialVelocity =
        (InitParams.CurrentSourcePose.Location - InitParams.PreviousSourcePose.Location)
        / FMath::Max(InitParams.DeltaTime, KINDA_SMALL_NUMBER);

    // Build a 5th-order polynomial that matches source position + velocity at t=0
    // and target position with zero velocity/acceleration at t=1...
    ComputePolynomial(
        CurrentSourcePose.Location,
        InitialVelocity,
        CurrentTargetPose.Location,
        GetTransitionTime());
}
```

`OnEvaluate_Implementation` then reads the stored polynomial coefficients and evaluates them at `GetPercentage()`.

## Live source, live target

A frequent source of confusion: `CurrentSourcePose` and `CurrentTargetPose` passed to `OnEvaluate_Implementation` are **live** — re-evaluated every frame by their owning cameras. If you cache the source pose once in `OnBeginPlay_Implementation` and blend against that cached value, you're blending to a stale source. That's sometimes correct (spline transitions *intentionally* snapshot their control points once), but usually you should treat both inputs as live.

`InitParams` is the snapshot; the `OnEvaluate` arguments are the live values. Pick accordingly.

## The pose-blend helper

`FComposableCameraPose::BlendBy(Source, Target, t)` handles location, rotation (quaternion slerp), FOV, focal length, aperture, and all the other lens fields in one call. Prefer it over manual field-by-field interpolation — it encodes the projection-mode snapping rule (ortho ↔ perspective snaps at `t=0.5`) and other contract details you don't want to reimplement.

For full control (e.g. inertialization uses the result of a polynomial as the blend weight, not linear time), compute your `t` and hand it to `BlendBy`.

## Wrapping another transition (the `DrivingTransition` pattern)

Some transitions take another transition as input and post-process its output. `DynamicDeocclusionTransition` does this — it delegates the base blend to a `DrivingTransition` and then pushes the output off occluders. You can do the same:

```cpp
UCLASS()
class UMyClampedTransition : public UComposableCameraTransitionBase
{
    GENERATED_BODY()

    UPROPERTY(EditAnywhere, Instanced)
    TObjectPtr<UComposableCameraTransitionBase> DrivingTransition;

protected:
    virtual void OnBeginPlay_Implementation(float Dt, const FComposableCameraPose& S, const FComposableCameraPose& T) override
    {
        if (DrivingTransition)
        {
            DrivingTransition->TransitionEnabled(InitParams);
            DrivingTransition->SetTransitionTime(GetTransitionTime());
        }
    }

    virtual FComposableCameraPose OnEvaluate_Implementation(float Dt, const FComposableCameraPose& S, const FComposableCameraPose& T) override
    {
        FComposableCameraPose Base = DrivingTransition
            ? DrivingTransition->Evaluate(Dt, S, T)
            : FComposableCameraPose::BlendBy(S, T, GetPercentage());
        return ApplyMyPostProcess(Base);
    }
};
```

Mark the field `Instanced` so the wrapped transition is authored per-instance in the Details panel, and keep it `Editable` + `Instanced` but **not** `DefaultToInstanced` at the field level — the base class already declares that on the class.

## Class specifiers — match the shipped pattern

```cpp
UCLASS(meta = (DisplayName = "My Transition"))
class MYPROJECT_API UMyTransition : public UComposableCameraTransitionBase
```

The base is declared `UCLASS(Abstract, DefaultToInstanced, EditInlineNew, ClassGroup = ComposableCameraSystem, CollapseCategories)` — your concrete subclass inherits `DefaultToInstanced` / `EditInlineNew`, which is what lets transitions be authored as instanced subobjects on type assets and modifier data assets. Don't override those specifiers on your subclass.

## Folder placement

| File | Location |
|---|---|
| Header | `Source/ComposableCameraSystem/Public/Transitions/MyTransition.h` |
| Source | `Source/ComposableCameraSystem/Private/Transitions/MyTransition.cpp` |

## Testing in isolation

A new transition is the easiest of the extension types to unit-test because it has no external dependencies:

1. Construct via `NewObject`.
2. Populate an `FComposableCameraTransitionInitParams` by hand.
3. Call `TransitionEnabled(InitParams)` then `SetTransitionTime(1.0f)`.
4. Construct synthetic source/target poses and drive `Evaluate(DeltaTime, Source, Target)` in a loop.
5. Assert on the returned pose at specific `GetPercentage()` values (0, 0.25, 0.5, 0.75, 1.0).

No PCM, no cameras, no level required.

## Hot-path rule

`OnEvaluate_Implementation` runs once per frame per active transition, and there can be several during a nested blend. No allocation: preallocate polynomial coefficient arrays, spline control buffers, and feeler result storage in `OnBeginPlay_Implementation`.

## Using your transition

Once compiled, your transition appears in any of the places a transition can be authored:

- The target camera type asset's `EnterTransition` / `ExitTransition` fields.
- A `UComposableCameraTransitionTableDataAsset` row.
- A `UComposableCameraNodeModifierDataAsset`'s `OverrideEnterTransition` / `OverrideExitTransition`.
- As a `DrivingTransition` inside another composed transition.
- As a caller-supplied `TransitionOverride` on any activation Blueprint call.

There is no registration step — the class is discovered via reflection once it's compiled.

---

*See also:* [Transitions Catalog](../reference/transitions.md) for the shipped set; [Concepts → Transitions](../user-guide/concepts/transitions.md) for the five-tier resolution chain and why the pose-only contract matters; [Custom Nodes](custom-nodes.md) if you need per-frame pose authoring rather than blending.
