
# UComposableCameraPathGuidedTransition { #ucomposablecamerapathguidedtransition }

```cpp
#include <ComposableCameraPathGuidedTransition.h>
```

> **Inherits:** [`UComposableCameraTransitionBase`](UComposableCameraTransitionBase.md#ucomposablecameratransitionbase)

A transition which utilizes a path　(spline) to guide its position during transition. This transition leverages two InertializedTransitions to achieve smoothness. An intermediate camera will be spawned as a wrapper for the spline. So this transition will be more expensive than other transitions.

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `TObjectPtr< UComposableCameraTransitionBase >` | [`DrivingTransition`](#drivingtransition)  |  |
| `EComposableCameraPathGuidedTransitionType` | [`Type`](#type)  |  |
| `TSoftObjectPtr< ACameraRig_Rail >` | [`RailActor`](#railactor)  |  |
| `FVector2D` | [`GuideRange`](#guiderange)  |  |
| `TObjectPtr< UCurveFloat >` | [`SplineMoveCurve`](#splinemovecurve)  |  |

---

#### DrivingTransition { #drivingtransition }

```cpp
TObjectPtr< UComposableCameraTransitionBase > DrivingTransition
```

---

#### Type { #type }

```cpp
EComposableCameraPathGuidedTransitionType Type {  }
```

---

#### RailActor { #railactor }

```cpp
TSoftObjectPtr< ACameraRig_Rail > RailActor
```

---

#### GuideRange { #guiderange }

```cpp
FVector2D GuideRange { 0.25, 0.75 }
```

---

#### SplineMoveCurve { #splinemovecurve }

```cpp
TObjectPtr< UCurveFloat > SplineMoveCurve
```

### Public Methods

| Return | Name | Description |
|--------|------|-------------|
| `void` | [`OnBeginPlay_Implementation`](#onbeginplay_implementation-2) `virtual` |  |
| `FComposableCameraPose` | [`OnEvaluate_Implementation`](#onevaluate_implementation-6) `virtual` |  |
| `float` | [`GetBlendWeightAt`](#getblendweightat-5) `virtual` `const` | Evaluate the transition's timing curve at a given normalized progress in [0, 1]. Returns the blend weight this transition would apply at that progress — i.e. the shape of its Percentage-over-duration curve. |
| `void` | [`BeginDestroy`](#begindestroy-2) `virtual` |  |
| `void` | [`DrawTransitionDebug`](#drawtransitiondebug-6) `virtual` `const` | Per-transition world-space debug hook. |

---

#### OnBeginPlay_Implementation { #onbeginplay_implementation-2 }

`virtual`

```cpp
virtual void OnBeginPlay_Implementation(float DeltaTime, const FComposableCameraPose & CurrentSourcePose, const FComposableCameraPose & CurrentTargetPose)
```

---

#### OnEvaluate_Implementation { #onevaluate_implementation-6 }

`virtual`

```cpp
virtual FComposableCameraPose OnEvaluate_Implementation(float DeltaTime, const FComposableCameraPose & CurrentSourcePose, const FComposableCameraPose & CurrentTargetPose)
```

---

#### GetBlendWeightAt { #getblendweightat-5 }

`virtual` `const`

```cpp
virtual float GetBlendWeightAt(float NormalizedTime) const
```

Evaluate the transition's timing curve at a given normalized progress in [0, 1]. Returns the blend weight this transition would apply at that progress — i.e. the shape of its Percentage-over-duration curve.

Used exclusively by the debug panel to render a sparkline preview of the blend curve on top of the transition's progress bar. The call site is a one-per-frame-per-active-transition sample loop, so the implementation must stay cheap (no allocations, no state reads that mutate). NOT used on the runtime evaluation hot path — real blend weight is still derived from `Percentage` in `OnEvaluate` so that per-transition state (polynomials, curves, etc.) keeps driving it.

Default implementation returns the input unchanged, giving a linear diagonal — the right fallback for transitions whose concept of "blend weight" isn't a simple scalar of normalized time (Inertialized position path, for example, is a polynomial trajectory, not a scalar lerp; showing a diagonal there still reads as "progress = time" which is accurate for its rotational / overall progression).

Concrete overrides should be pure math — no reads of `RemainingTime`, `TransitionTime`, or any internal state. Use only the `NormalizedTime` argument plus the transition's authored UPROPERTYs (Exp, bSmootherStep, EvaluationCurveType, etc.).

---

#### BeginDestroy { #begindestroy-2 }

`virtual`

```cpp
virtual void BeginDestroy()
```

---

#### DrawTransitionDebug { #drawtransitiondebug-6 }

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
| `TObjectPtr< AComposableCameraCameraBase >` | [`IntermediateCamera`](#intermediatecamera)  |  |
| `TObjectPtr< ACameraRig_Rail >` | [`Rail`](#rail-1)  |  |
| `TObjectPtr< UComposableCameraInertializedTransition >` | [`EnterTransition`](#entertransition-4)  |  |
| `TObjectPtr< UComposableCameraInertializedTransition >` | [`ExitTransition`](#exittransition-1)  |  |
| `TObjectPtr< USplineComponent >` | [`InternalSpline`](#internalspline)  |  |
| `TObjectPtr< AActor >` | [`DebugSplineActor`](#debugsplineactor)  |  |

---

#### IntermediateCamera { #intermediatecamera }

```cpp
TObjectPtr< AComposableCameraCameraBase > IntermediateCamera { nullptr }
```

---

#### Rail { #rail-1 }

```cpp
TObjectPtr< ACameraRig_Rail > Rail { nullptr }
```

---

#### EnterTransition { #entertransition-4 }

```cpp
TObjectPtr< UComposableCameraInertializedTransition > EnterTransition { nullptr }
```

---

#### ExitTransition { #exittransition-1 }

```cpp
TObjectPtr< UComposableCameraInertializedTransition > ExitTransition { nullptr }
```

---

#### InternalSpline { #internalspline }

```cpp
TObjectPtr< USplineComponent > InternalSpline { nullptr }
```

---

#### DebugSplineActor { #debugsplineactor }

```cpp
TObjectPtr< AActor > DebugSplineActor { nullptr }
```

### Private Methods

| Return | Name | Description |
|--------|------|-------------|
| `bool` | [`ResolveAndValidateRail`](#resolveandvalidaterail)  |  |
| `void` | [`DestroySpawnedActors`](#destroyspawnedactors)  |  |
| `bool` | [`BuildInternalSpline`](#buildinternalspline)  | Returns true on success, false if any spawn / duplicate step returned null (caller should DestroySpawnedActors and degrade to a hard cut). |

---

#### ResolveAndValidateRail { #resolveandvalidaterail }

```cpp
bool ResolveAndValidateRail()
```

---

#### DestroySpawnedActors { #destroyspawnedactors }

```cpp
void DestroySpawnedActors()
```

---

#### BuildInternalSpline { #buildinternalspline }

```cpp
bool BuildInternalSpline(const FComposableCameraPose & CurrentTargetPose, float DeltaTime)
```

Returns true on success, false if any spawn / duplicate step returned null (caller should DestroySpawnedActors and degrade to a hard cut).
