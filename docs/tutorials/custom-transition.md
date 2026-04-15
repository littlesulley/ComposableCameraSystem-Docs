# Tutorial: Writing a Custom Transition

Author a C++ transition that implements a **bounce-and-settle** blend — the output overshoots the target slightly around 70% progress, then settles back to it — and wire it into the project's transition table for one specific `(Source, Target)` pair. Along the way we'll unit-test it without spinning up a PCM or a level.

If you haven't read the [Custom Transitions](../extending/custom-transitions.md) authoring recipe, skim it first — this tutorial assumes familiarity with the four-phase lifecycle and the pose-only contract.

## 1. Pick the blend shape

A bounce-and-settle curve passes through the target, overshoots by some amount, and settles. A tidy formulation:

```
t ∈ [0, 1]
base(t) = smoothstep(t)                         // monotonically increases to 1
bounce(t) = k · (1 − t) · sin(π · t · freq)     // sine decaying with (1-t)
shape(t) = base(t) + bounce(t)
```

At `t=0`, both terms are 0. At `t=1`, `base=1` and `bounce=0`, so shape reaches exactly 1. In the middle, the sine term pushes `shape` above 1 briefly — the overshoot we want.

This is a scalar blend weight. Pass it to `FComposableCameraPose::BlendBy` and the per-field blending (position, rotation, FOV, lens) is handled for us.

## 2. Create the class

**Folder placement:**

- `Source/ComposableCameraSystem/Public/Transitions/ComposableCameraBounceTransition.h`
- `Source/ComposableCameraSystem/Private/Transitions/ComposableCameraBounceTransition.cpp`

**Header:**

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

**Source:**

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

Two notes on the implementation:

- We don't override `OnBeginPlay_Implementation` because we don't cache any per-instance state — the curve is stateless. If you add history-dependent behavior (e.g. recover velocity from `InitParams`), that's where it goes.
- `GetPercentage()` is provided by the base class and already goes `0 → 1` over `TransitionDuration`. Don't track progress yourself.

## 3. Compile in the IDE

Close the editor if it's running, then compile the `ComposableCameraSystem` module in Rider or Visual Studio. A new transition class is a reflection change, so Live Coding won't pick it up — you need a full editor restart after this compile.

If the compile fails, read the error carefully. Most common first-time failures:

- **`unresolved external symbol` for the transition base's methods** — check the `_API` macro on your new class (`COMPOSABLECAMERASYSTEM_API`) is spelled correctly.
- **`no matching function for call to 'BlendBy'`** — the static helper lives on `FComposableCameraPose`. Include the pose header transitively via `ComposableCameraTransitionBase.h`, which already imports it.
- **`UCLASS` spec rejected** — don't add `Abstract` on your concrete subclass; the base already carries `DefaultToInstanced, EditInlineNew`, which you inherit automatically.

## 4. Unit-test it (no PCM required)

One of the design benefits of the pose-only contract is that transitions are trivially testable in isolation. Add this to your project's automation test module (or any editor-only test target):

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
    // Source pose and previous pose the same — zero velocity, fine for a static test.
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

Run it from **Session Frontend → Automation → ComposableCameraSystem.Transitions.Bounce**. Green = transition behaves as designed, no PCM / level / camera required.

## 5. Author it as an instanced subobject

Restart the editor (or Live Coding if you added no new classes — but we did, so full restart). Open `CT_StatueOrbit` from the previous tutorial. In Details → Transitions → `EnterTransition`, click the dropdown — `Bounce & Settle` now appears alongside the shipped transitions. Assign it, set `OvershootAmount = 0.25`, `TransitionDuration = 1.0`.

Save, play, push the cutscene context — the blend into the orbit camera now has the bounce-and-settle character we authored.

## 6. Wire it into the transition table for one specific pair

Authoring per-camera `EnterTransition` is fine for "whenever any source enters this camera, blend like so". For targeted `(Source, Target)` routing — "only when gameplay enters *this particular* cutscene, use the bounce" — use the transition table.

1. Content Browser → right-click → **Composable Camera System → Transition Table Data Asset**. Name it `DT_TransitionTable`.
2. Add a row:
    - `SourceTypeAsset` = `CT_ThirdPersonFollow`
    - `TargetTypeAsset` = `CT_StatueOrbit`
    - `Transition` = new `UComposableCameraBounceTransition` instance, `OvershootAmount = 0.35`, `TransitionDuration = 1.2`.
3. **Project Settings → ComposableCameraSystem → TransitionTable** → assign `DT_TransitionTable`.

Now the resolution chain lands on tier 2 (transition table) for that specific pair *before* it falls through to tier 4 (target's EnterTransition). Other sources entering `CT_StatueOrbit` continue to get the plain EnterTransition authored on the type asset; only the follow → orbit path uses the bounce.

!!! note "No wildcards in the table — by design"
    The table does exact-match only on `(Source, Target)`. If you want "any source → this target", use the target's `EnterTransition` (tier 4). If you want "this source → any target", use the source's `ExitTransition` (tier 3). Wildcards in the table would silently shadow those per-asset defaults; the resolution chain intentionally doesn't support them.

## 7. Polish

Two small improvements worth considering before shipping a custom transition:

**Clamp shape near the endpoints.** If `OvershootAmount` is large and `BounceFrequency > 1`, the curve can briefly go *below* 0 near the start or *above* 1 near the end due to numerical drift. Add a final `FMath::Clamp(Shape, -0.2f, 1.2f)` if you want to bound the overshoot regardless of parameter values.

**Implement `OnFinished`.** The base class sets `bFinished` for you, but if you want the transition to fire a gameplay event on completion (camera shake, SFX), bind `OnTransitionFinishesDelegate` from gameplay code — don't override the `OnFinished` BP event in C++.

## Where next

- [Custom Transitions](../extending/custom-transitions.md) — reference page for authoring, including the `DrivingTransition` wrapping pattern and velocity recovery via `InitParams`.
- [Transitions & Blending](../user-guide/transitions-and-blending.md) — tuning guidance and worked scenarios for the transition table.
- [Transitions Catalog](../reference/transitions.md) — per-class field reference for all nine shipped transitions, in case one of them already does what you need.
