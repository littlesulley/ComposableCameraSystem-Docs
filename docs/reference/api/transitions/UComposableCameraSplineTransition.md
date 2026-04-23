
# UComposableCameraSplineTransition { #ucomposablecamerasplinetransition }

```cpp
#include <ComposableCameraSplineTransition.h>
```

> **Inherits:** [`UComposableCameraTransitionBase`](UComposableCameraTransitionBase.md#ucomposablecameratransitionbase)

Spline transition.

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `EComposableCameraSplineTransitionType` | [`SplineType`](#splinetype-1)  |  |
| `EComposableCameraSplineTransitionEvaluationCurveType` | [`EvaluationCurveType`](#evaluationcurvetype)  |  |
| `FVector` | [`StartTangent`](#starttangent)  |  |
| `FVector` | [`EndTangent`](#endtangent)  |  |
| `FVector` | [`StartControlPoint`](#startcontrolpoint)  |  |
| `FVector` | [`EndControlPoint`](#endcontrolpoint)  |  |
| `TArray< FVector >` | [`ControlPoints`](#controlpoints)  |  |
| `float` | [`ArcAngle`](#arcangle)  |  |
| `float` | [`ArcRoll`](#arcroll)  |  |

---

#### SplineType { #splinetype-1 }

```cpp
EComposableCameraSplineTransitionType SplineType {  }
```

---

#### EvaluationCurveType { #evaluationcurvetype }

```cpp
EComposableCameraSplineTransitionEvaluationCurveType EvaluationCurveType {  }
```

---

#### StartTangent { #starttangent }

```cpp
FVector StartTangent { 0.f, 100.f, 0.f }
```

---

#### EndTangent { #endtangent }

```cpp
FVector EndTangent { 0.f, 100.f, 0.f }
```

---

#### StartControlPoint { #startcontrolpoint }

```cpp
FVector StartControlPoint { 0.f, 100.f, 0.f }
```

---

#### EndControlPoint { #endcontrolpoint }

```cpp
FVector EndControlPoint { 0.f, 100.f, 0.f }
```

---

#### ControlPoints { #controlpoints }

```cpp
TArray< FVector > ControlPoints
```

---

#### ArcAngle { #arcangle }

```cpp
float ArcAngle { 180.f }
```

---

#### ArcRoll { #arcroll }

```cpp
float ArcRoll { 0.f }
```

### Public Methods

| Return | Name | Description |
|--------|------|-------------|
| `void` | [`OnBeginPlay_Implementation`](#onbeginplay_implementation-1) `virtual` |  |
| `FComposableCameraPose` | [`OnEvaluate_Implementation`](#onevaluate_implementation-5) `virtual` |  |
| `float` | [`GetBlendWeightAt`](#getblendweightat-4) `virtual` `const` | Evaluate the transition's timing curve at a given normalized progress in [0, 1]. Returns the blend weight this transition would apply at that progress — i.e. the shape of its Percentage-over-duration curve. |
| `void` | [`DrawTransitionDebug`](#drawtransitiondebug-5) `virtual` `const` | Per-transition world-space debug hook. |

---

#### OnBeginPlay_Implementation { #onbeginplay_implementation-1 }

`virtual`

```cpp
virtual void OnBeginPlay_Implementation(float DeltaTime, const FComposableCameraPose & CurrentSourcePose, const FComposableCameraPose & CurrentTargetPose)
```

---

#### OnEvaluate_Implementation { #onevaluate_implementation-5 }

`virtual`

```cpp
virtual FComposableCameraPose OnEvaluate_Implementation(float DeltaTime, const FComposableCameraPose & CurrentSourcePose, const FComposableCameraPose & CurrentTargetPose)
```

---

#### GetBlendWeightAt { #getblendweightat-4 }

`virtual` `const`

```cpp
virtual float GetBlendWeightAt(float NormalizedTime) const
```

Evaluate the transition's timing curve at a given normalized progress in [0, 1]. Returns the blend weight this transition would apply at that progress — i.e. the shape of its Percentage-over-duration curve.

Used exclusively by the debug panel to render a sparkline preview of the blend curve on top of the transition's progress bar. The call site is a one-per-frame-per-active-transition sample loop, so the implementation must stay cheap (no allocations, no state reads that mutate). NOT used on the runtime evaluation hot path — real blend weight is still derived from `Percentage` in `OnEvaluate` so that per-transition state (polynomials, curves, etc.) keeps driving it.

Default implementation returns the input unchanged, giving a linear diagonal — the right fallback for transitions whose concept of "blend weight" isn't a simple scalar of normalized time (Inertialized position path, for example, is a polynomial trajectory, not a scalar lerp; showing a diagonal there still reads as "progress = time" which is accurate for its rotational / overall progression).

Concrete overrides should be pure math — no reads of `RemainingTime`, `TransitionTime`, or any internal state. Use only the `NormalizedTime` argument plus the transition's authored UPROPERTYs (Exp, bSmootherStep, EvaluationCurveType, etc.).

---

#### DrawTransitionDebug { #drawtransitiondebug-5 }

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

### Private Methods

| Return | Name | Description |
|--------|------|-------------|
| `FVector` | [`EvaluatePositionOnCurve`](#evaluatepositiononcurve) `const` | Evaluate the current spline configuration at parameter t ∈ [0, 1]. Used by both OnEvaluate (with `t = BlendWeight`) and DrawTransitionDebug (to sample the whole curve). The two call sites must agree exactly or the debug draw would lie about where the camera will go, so they share one helper. |

---

#### EvaluatePositionOnCurve { #evaluatepositiononcurve }

`const`

```cpp
FVector EvaluatePositionOnCurve(float t, const FVector & StartPos, const FVector & EndPos) const
```

Evaluate the current spline configuration at parameter t ∈ [0, 1]. Used by both OnEvaluate (with `t = BlendWeight`) and DrawTransitionDebug (to sample the whole curve). The two call sites must agree exactly or the debug draw would lie about where the camera will go, so they share one helper.

**Parameters**

* `t` Normalized curve parameter. 

* `StartPos` Spline start (source pose position for the active blend). 

* `EndPos` Spline end (target pose position for the active blend).
