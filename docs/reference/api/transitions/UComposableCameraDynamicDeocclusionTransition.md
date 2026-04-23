
# UComposableCameraDynamicDeocclusionTransition { #ucomposablecameradynamicdeocclusiontransition }

```cpp
#include <ComposableCameraDynamicDeocclusionTransition.h>
```

> **Inherits:** [`UComposableCameraTransitionBase`](UComposableCameraTransitionBase.md#ucomposablecameratransitionbase)

A dynamically deocclusive transition.

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `UComposableCameraTransitionBase *` | [`DrivingTransition`](#drivingtransition-1)  |  |
| `TArray< FComposableCameraRayFeeler >` | [`Feelers`](#feelers)  |  |
| `TEnumAsByte< ETraceTypeQuery >` | [`TraceChannel`](#tracechannel)  |  |
| `TArray< TSoftClassPtr< AActor > >` | [`ActorTypesToIgnore`](#actortypestoignore-1)  |  |
| `float` | [`DeocclusionSpeed`](#deocclusionspeed)  |  |
| `float` | [`ResumeWaitingTime`](#resumewaitingtime)  |  |
| `float` | [`DeadPercentage`](#deadpercentage)  |  |
| `float` | [`ResumeSpeed`](#resumespeed)  |  |

---

#### DrivingTransition { #drivingtransition-1 }

```cpp
UComposableCameraTransitionBase * DrivingTransition
```

---

#### Feelers { #feelers }

```cpp
TArray< FComposableCameraRayFeeler > Feelers
```

---

#### TraceChannel { #tracechannel }

```cpp
TEnumAsByte< ETraceTypeQuery > TraceChannel
```

---

#### ActorTypesToIgnore { #actortypestoignore-1 }

```cpp
TArray< TSoftClassPtr< AActor > > ActorTypesToIgnore
```

---

#### DeocclusionSpeed { #deocclusionspeed }

```cpp
float DeocclusionSpeed { 1.f }
```

---

#### ResumeWaitingTime { #resumewaitingtime }

```cpp
float ResumeWaitingTime { 0.2f }
```

---

#### DeadPercentage { #deadpercentage }

```cpp
float DeadPercentage { 0.8f }
```

---

#### ResumeSpeed { #resumespeed }

```cpp
float ResumeSpeed { 0.8f }
```

### Public Methods

| Return | Name | Description |
|--------|------|-------------|
| `void` | [`OnBeginPlay_Implementation`](#onbeginplay_implementation-5) `virtual` |  |
| `FComposableCameraPose` | [`OnEvaluate_Implementation`](#onevaluate_implementation-10) `virtual` |  |
| `float` | [`GetBlendWeightAt`](#getblendweightat-7) `virtual` `const` | Evaluate the transition's timing curve at a given normalized progress in [0, 1]. Returns the blend weight this transition would apply at that progress — i.e. the shape of its Percentage-over-duration curve. |
| `void` | [`DrawTransitionDebug`](#drawtransitiondebug-9) `virtual` `const` | Per-transition world-space debug hook. |

---

#### OnBeginPlay_Implementation { #onbeginplay_implementation-5 }

`virtual`

```cpp
virtual void OnBeginPlay_Implementation(float DeltaTime, const FComposableCameraPose & CurrentSourcePose, const FComposableCameraPose & CurrentTargetPose)
```

---

#### OnEvaluate_Implementation { #onevaluate_implementation-10 }

`virtual`

```cpp
virtual FComposableCameraPose OnEvaluate_Implementation(float DeltaTime, const FComposableCameraPose & CurrentSourcePose, const FComposableCameraPose & CurrentTargetPose)
```

---

#### GetBlendWeightAt { #getblendweightat-7 }

`virtual` `const`

```cpp
virtual float GetBlendWeightAt(float NormalizedTime) const
```

Evaluate the transition's timing curve at a given normalized progress in [0, 1]. Returns the blend weight this transition would apply at that progress — i.e. the shape of its Percentage-over-duration curve.

Used exclusively by the debug panel to render a sparkline preview of the blend curve on top of the transition's progress bar. The call site is a one-per-frame-per-active-transition sample loop, so the implementation must stay cheap (no allocations, no state reads that mutate). NOT used on the runtime evaluation hot path — real blend weight is still derived from `Percentage` in `OnEvaluate` so that per-transition state (polynomials, curves, etc.) keeps driving it.

Default implementation returns the input unchanged, giving a linear diagonal — the right fallback for transitions whose concept of "blend weight" isn't a simple scalar of normalized time (Inertialized position path, for example, is a polynomial trajectory, not a scalar lerp; showing a diagonal there still reads as "progress = time" which is accurate for its rotational / overall progression).

Concrete overrides should be pure math — no reads of `RemainingTime`, `TransitionTime`, or any internal state. Use only the `NormalizedTime` argument plus the transition's authored UPROPERTYs (Exp, bSmootherStep, EvaluationCurveType, etc.).

---

#### DrawTransitionDebug { #drawtransitiondebug-9 }

`virtual` `const`

```cpp
virtual void DrawTransitionDebug(UWorld * World, bool bViewerIsOutsideCamera) const
```

Per-transition world-space debug hook.

Invoked from `[UComposableCameraEvaluationTree::DrawTransitionsDebug](../core/UComposableCameraEvaluationTree.md#drawtransitionsdebug)` while `CCS.Debug.Viewport` is on, once per frame for every transition that currently sits in an Inner node of the active director's tree (and, recursively, of any referenced director's tree — inter-context blends see both sides).

Default implementation is empty. Concrete transitions override, check their own `CCS.Debug.Viewport.Transitions.<Name>` CVar, and usually call `DrawStandardTransitionDebug` plus any type-specific extras (spline curve sample, feeler rays, etc.).

**Parameters**

* `World` World to draw into. Routes through the world's LineBatcher, so the draw is visible in every viewport that renders this world (game + F8-ejected editor). 

* `bViewerIsOutsideCamera` True when the player is NOT viewing through the camera (F8 eject / SIE). Overrides use this to skip gizmos that would occlude the near plane — mostly the source/target frustum pyramids.

Compiled out in shipping builds.

### Private Attributes

| Return | Name | Description |
|--------|------|-------------|
| `FVector` | [`PreviousOffset`](#previousoffset)  |  |
| `float` | [`ElapsedWaitingTime`](#elapsedwaitingtime)  |  |
| `TArray< AActor * >` | [`ActorsToIgnore`](#actorstoignore)  |  |
| `EDrawDebugTrace::Type` | [`DrawDebugType`](#drawdebugtype)  |  |

---

#### PreviousOffset { #previousoffset }

```cpp
FVector PreviousOffset { FVector::ZeroVector }
```

---

#### ElapsedWaitingTime { #elapsedwaitingtime }

```cpp
float ElapsedWaitingTime { 0.f }
```

---

#### ActorsToIgnore { #actorstoignore }

```cpp
TArray< AActor * > ActorsToIgnore
```

---

#### DrawDebugType { #drawdebugtype }

```cpp
EDrawDebugTrace::Type DrawDebugType
```
