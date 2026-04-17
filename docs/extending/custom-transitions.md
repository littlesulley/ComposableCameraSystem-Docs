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

All C++ code can be translated into blueprint implementation.

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

## Worked example: bounce-and-settle transition

This section walks through a complete transition implementation — a bounce-and-settle blend where the output overshoots the target slightly around 70% progress, then settles back. We'll also unit-test it and wire it into the transition table.

### Pick the blend shape

A bounce-and-settle curve passes through the target, overshoots by some amount, and settles. A tidy formulation:

```
t ∈ [0, 1]
base(t) = smoothstep(t)                         // monotonically increases to 1
bounce(t) = k · (1 − t) · sin(π · t · freq)     // sine decaying with (1-t)
shape(t) = base(t) + bounce(t)
```

At `t=0`, both terms are 0. At `t=1`, `base=1` and `bounce=0`, so shape reaches exactly 1. In the middle, the sine term pushes `shape` above 1 briefly — the overshoot.

This is a scalar blend weight. Pass it to `FComposableCameraPose::BlendBy` and the per-field blending (position, rotation, FOV, lens) is handled for us.

### The class

```cpp
// ComposableCameraBounceTransition.h
#pragma once

#include "CoreMinimal.h"
#include "Transitions/ComposableCameraTransitionBase.h"
#include "ComposableCameraBounceTransition.generated.h"

/** Smoothstep base plus a decaying-sine overshoot. */
UCLASS(meta = (DisplayName = "Bounce & Settle"))
class COMPOSABLECAMERASYSTEM_API UComposableCameraBounceTransition
    : public UComposableCameraTransitionBase
{
    GENERATED_BODY()

public:
    /** Overshoot amplitude. 0 behaves like Smoothstep. Typical values 0.1 – 0.4. */
    UPROPERTY(EditAnywhere, meta = (ClampMin = "0.0", ClampMax = "1.0"))
    float OvershootAmount = 0.2f;

    /** Oscillation frequency in half-cycles across [0, 1]. 1 overshoots once; 2 overshoots-and-undershoots. */
    UPROPERTY(EditAnywhere, meta = (ClampMin = "0.5", ClampMax = "4.0"))
    float BounceFrequency = 1.0f;

protected:
    virtual FComposableCameraPose OnEvaluate_Implementation(
        float DeltaTime,
        const FComposableCameraPose& CurrentSourcePose,
        const FComposableCameraPose& CurrentTargetPose) override;
};
```

```cpp
// ComposableCameraBounceTransition.cpp
#include "Transitions/ComposableCameraBounceTransition.h"

FComposableCameraPose UComposableCameraBounceTransition::OnEvaluate_Implementation(
    float DeltaTime,
    const FComposableCameraPose& CurrentSourcePose,
    const FComposableCameraPose& CurrentTargetPose)
{
    const float t = GetPercentage();
    const float Base = t * t * (3.0f - 2.0f * t); // smoothstep
    const float Bounce = OvershootAmount
        * (1.0f - t)
        * FMath::Sin(PI * t * BounceFrequency);

    const float Shape = Base + Bounce;
    return FComposableCameraPose::BlendBy(
        CurrentSourcePose, CurrentTargetPose, Shape);
}
```

Two notes: we don't override `OnBeginPlay_Implementation` because the curve is stateless — no cached per-instance state needed. And `GetPercentage()` from the base class already goes `0 → 1` over `TransitionDuration`; don't track progress yourself.

### Unit test (no PCM required)

One of the design benefits of the pose-only contract is that transitions are trivially testable in isolation:

```cpp
IMPLEMENT_SIMPLE_AUTOMATION_TEST(
    FBounceTransitionTest,
    "ComposableCameraSystem.Transitions.Bounce",
    EAutomationTestFlags::EditorContext | EAutomationTestFlags::EngineFilter)

bool FBounceTransitionTest::RunTest(const FString& Parameters)
{
    auto* Transition = NewObject<UComposableCameraBounceTransition>();
    Transition->OvershootAmount = 0.3f;
    Transition->BounceFrequency = 1.0f;

    FComposableCameraTransitionInitParams Init;
    Init.CurrentSourcePose.Location = FVector(0, 0, 0);
    Init.PreviousSourcePose.Location = FVector(0, 0, 0);
    Init.DeltaTime = 1.0f / 60.0f;

    Transition->TransitionEnabled(Init);
    Transition->SetTransitionTime(1.0f);

    FComposableCameraPose Source; Source.Location = FVector(0, 0, 0);
    FComposableCameraPose Target; Target.Location = FVector(100, 0, 0);

    // Drive the blend manually at 60 fps for 1 second.
    FComposableCameraPose Last;
    float MaxX = 0.f;
    for (int32 Frame = 0; Frame < 60; ++Frame)
    {
        Last = Transition->Evaluate(1.0f / 60.0f, Source, Target);
        MaxX = FMath::Max(MaxX, Last.Location.X);
    }

    // The overshoot should push X past the target at some point.
    TestTrue(TEXT("overshoots target"), MaxX > 100.0f);
    // And by the end we should be exactly on the target.
    TestEqual(TEXT("settles on target"), Last.Location.X, 100.0f, 0.5f);
    return true;
}
```

Run it from **Session Frontend → Automation → ComposableCameraSystem.Transitions.Bounce**. Green means the transition behaves as designed.

### Wire it into the transition table

Authoring per-camera `EnterTransition` is fine for "whenever any source enters this camera, blend like so". For targeted `(Source, Target)` routing — "only when gameplay enters *this particular* cutscene, use the bounce" — use the transition table:

1. Content Browser → right-click → **Composable Camera System → Transition Table Data Asset**. Name it `DT_TransitionTable`.
2. Add a row:
    - `SourceTypeAsset` = `CT_ThirdPersonFollow`
    - `TargetTypeAsset` = `CT_StatueOrbit`
    - `Transition` = new `UComposableCameraBounceTransition` instance, `OvershootAmount = 0.35`, `TransitionDuration = 1.2`.
3. **Project Settings → ComposableCameraSystem → TransitionTable** → assign `DT_TransitionTable`.

The resolution chain lands on tier 2 (transition table) for that pair *before* it falls through to tier 4 (target's EnterTransition). Other sources entering `CT_StatueOrbit` continue to get the plain EnterTransition; only the follow → orbit path uses the bounce.

!!! note "No wildcards in the table — by design"
    The table does exact-match only on `(Source, Target)`. If you want "any source → this target", use the target's `EnterTransition` (tier 4). If you want "this source → any target", use the source's `ExitTransition` (tier 3). Wildcards would silently shadow those per-asset defaults.

### Polish tips

**Clamp shape near the endpoints.** If `OvershootAmount` is large and `BounceFrequency > 1`, the curve can briefly go below 0 near the start or above 1 near the end. Add `FMath::Clamp(Shape, -0.2f, 1.2f)` if you want bounded overshoot regardless of parameter values.

**Completion events.** The base class sets `bFinished` for you. If you want the transition to fire a gameplay event on completion (camera shake, SFX), bind `OnTransitionFinishesDelegate` from gameplay code — don't override the `OnFinished` BP event in C++.

### Common compile issues

- **`unresolved external symbol`** — check the `_API` macro on your class is spelled correctly (`COMPOSABLECAMERASYSTEM_API`).
- **`no matching function for call to 'BlendBy'`** — the helper lives on `FComposableCameraPose`. It's included transitively via `ComposableCameraTransitionBase.h`.
- **`UCLASS` spec rejected** — don't add `Abstract` on your concrete subclass; you inherit `DefaultToInstanced, EditInlineNew` from the base.

A new transition class is a reflection change, so Live Coding won't pick it up — you need a full editor restart after compiling.

---

*See also:* [Transitions Catalog](../reference/transitions.md) for the shipped set; [Concepts → Transitions](../user-guide/concepts/transitions.md) for the five-tier resolution chain and why the pose-only contract matters; [Custom Nodes](custom-nodes.md) if you need per-frame pose authoring rather than blending.
