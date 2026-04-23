
# UComposableCameraTransitionBase { #ucomposablecameratransitionbase }

```cpp
#include <ComposableCameraTransitionBase.h>
```

> **Inherits:** `UObject`
> **Subclassed by:** [`UComposableCameraCubicTransition`](UComposableCameraCubicTransition.md#ucomposablecameracubictransition), [`UComposableCameraCylindricalTransition`](UComposableCameraCylindricalTransition.md#ucomposablecameracylindricaltransition), [`UComposableCameraDynamicDeocclusionTransition`](UComposableCameraDynamicDeocclusionTransition.md#ucomposablecameradynamicdeocclusiontransition), [`UComposableCameraEaseTransition`](UComposableCameraEaseTransition.md#ucomposablecameraeasetransition), [`UComposableCameraInertializedTransition`](UComposableCameraInertializedTransition.md#ucomposablecamerainertializedtransition), [`UComposableCameraLinearTransition`](UComposableCameraLinearTransition.md#ucomposablecameralineartransition), [`UComposableCameraPathGuidedTransition`](UComposableCameraPathGuidedTransition.md#ucomposablecamerapathguidedtransition), [`UComposableCameraSmoothTransition`](UComposableCameraSmoothTransition.md#ucomposablecamerasmoothtransition), [`UComposableCameraSplineTransition`](UComposableCameraSplineTransition.md#ucomposablecamerasplinetransition), [`UComposableCameraViewTargetTransition`](UComposableCameraViewTargetTransition.md#ucomposablecameraviewtargettransition)

Base class for transition evaluation.

Transitions are pose-only operators: they receive source and target poses each tick, maintain their own internal blend state, and output a blended pose. They never reference cameras or Directors directly.

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `FOnTransitionFinishes` | [`OnTransitionFinishesDelegate`](#ontransitionfinishesdelegate)  |  |
| `FTransitionDebugSnapshot` | [`LastDebugSource`](#lastdebugsource)  |  |
| `FTransitionDebugSnapshot` | [`LastDebugTarget`](#lastdebugtarget)  |  |
| `FTransitionDebugSnapshot` | [`LastDebugBlended`](#lastdebugblended)  |  |

---

#### OnTransitionFinishesDelegate { #ontransitionfinishesdelegate }

```cpp
FOnTransitionFinishes OnTransitionFinishesDelegate
```

---

#### LastDebugSource { #lastdebugsource }

```cpp
FTransitionDebugSnapshot LastDebugSource
```

---

#### LastDebugTarget { #lastdebugtarget }

```cpp
FTransitionDebugSnapshot LastDebugTarget
```

---

#### LastDebugBlended { #lastdebugblended }

```cpp
FTransitionDebugSnapshot LastDebugBlended
```

### Public Methods

| Return | Name | Description |
|--------|------|-------------|
| `FComposableCameraPose` | [`Evaluate`](#evaluate-6)  | Evaluate the transition for this frame, blending between source and target poses. |
| `void` | [`TransitionEnabled`](#transitionenabled)  | Initialize the transition with source pose data. Called once before the first Evaluate. |
| `void` | [`TransitionFinished`](#transitionfinished)  | Mark the transition as finished. |
| `void` | [`SetTransitionTime`](#settransitiontime)  |  |
| `void` | [`ResetTransitionState`](#resettransitionstate)  |  |
| `bool` | [`IsFinished`](#isfinished-1) `const` `inline` |  |
| `float` | [`GetRemainingTime`](#getremainingtime) `const` `inline` |  |
| `float` | [`GetTransitionTime`](#gettransitiontime) `const` `inline` |  |
| `float` | [`GetPercentage`](#getpercentage) `const` `inline` |  |
| `float` | [`GetBlendWeightAt`](#getblendweightat-1) `virtual` `const` `inline` | Evaluate the transition's timing curve at a given normalized progress in [0, 1]. Returns the blend weight this transition would apply at that progress — i.e. the shape of its Percentage-over-duration curve. |
| `void` | [`DrawTransitionDebug`](#drawtransitiondebug-1) `virtual` `const` `inline` | Per-transition world-space debug hook. |

---

#### Evaluate { #evaluate-6 }

```cpp
FComposableCameraPose Evaluate(float DeltaTime, const FComposableCameraPose & CurrentSourcePose, const FComposableCameraPose & CurrentTargetPose)
```

Evaluate the transition for this frame, blending between source and target poses.

---

#### TransitionEnabled { #transitionenabled }

```cpp
void TransitionEnabled(const FComposableCameraTransitionInitParams & InInitParams)
```

Initialize the transition with source pose data. Called once before the first Evaluate.

---

#### TransitionFinished { #transitionfinished }

```cpp
void TransitionFinished()
```

Mark the transition as finished.

---

#### SetTransitionTime { #settransitiontime }

```cpp
void SetTransitionTime(float NewTransitionTime)
```

---

#### ResetTransitionState { #resettransitionstate }

```cpp
void ResetTransitionState()
```

---

#### IsFinished { #isfinished-1 }

`const` `inline`

```cpp
inline bool IsFinished() const
```

---

#### GetRemainingTime { #getremainingtime }

`const` `inline`

```cpp
inline float GetRemainingTime() const
```

---

#### GetTransitionTime { #gettransitiontime }

`const` `inline`

```cpp
inline float GetTransitionTime() const
```

---

#### GetPercentage { #getpercentage }

`const` `inline`

```cpp
inline float GetPercentage() const
```

---

#### GetBlendWeightAt { #getblendweightat-1 }

`virtual` `const` `inline`

```cpp
virtual inline float GetBlendWeightAt(float NormalizedTime) const
```

Evaluate the transition's timing curve at a given normalized progress in [0, 1]. Returns the blend weight this transition would apply at that progress — i.e. the shape of its Percentage-over-duration curve.

Used exclusively by the debug panel to render a sparkline preview of the blend curve on top of the transition's progress bar. The call site is a one-per-frame-per-active-transition sample loop, so the implementation must stay cheap (no allocations, no state reads that mutate). NOT used on the runtime evaluation hot path — real blend weight is still derived from `Percentage` in `OnEvaluate` so that per-transition state (polynomials, curves, etc.) keeps driving it.

Default implementation returns the input unchanged, giving a linear diagonal — the right fallback for transitions whose concept of "blend weight" isn't a simple scalar of normalized time (Inertialized position path, for example, is a polynomial trajectory, not a scalar lerp; showing a diagonal there still reads as "progress = time" which is accurate for its rotational / overall progression).

Concrete overrides should be pure math — no reads of `RemainingTime`, `TransitionTime`, or any internal state. Use only the `NormalizedTime` argument plus the transition's authored UPROPERTYs (Exp, bSmootherStep, EvaluationCurveType, etc.).

---

#### DrawTransitionDebug { #drawtransitiondebug-1 }

`virtual` `const` `inline`

```cpp
virtual inline void DrawTransitionDebug(class UWorld * World, bool bViewerIsOutsideCamera) const
```

Per-transition world-space debug hook.

Invoked from `[UComposableCameraEvaluationTree::DrawTransitionsDebug](../core/UComposableCameraEvaluationTree.md#drawtransitionsdebug)` while `CCS.Debug.Viewport` is on, once per frame for every transition that currently sits in an Inner node of the active director's tree (and, recursively, of any referenced director's tree — inter-context blends see both sides).

Default implementation is empty. Concrete transitions override, check their own `CCS.Debug.Viewport.Transitions.<Name>` CVar, and usually call `DrawStandardTransitionDebug` plus any type-specific extras (spline curve sample, feeler rays, etc.).

**Parameters**

* `World` World to draw into. Routes through the world's LineBatcher, so the draw is visible in every viewport that renders this world (game + F8-ejected editor). 

* `bViewerIsOutsideCamera` True when the player is NOT viewing through the camera (F8 eject / SIE). Overrides use this to skip gizmos that would occlude the near plane — mostly the source/target frustum pyramids.

Compiled out in shipping builds.

### Protected Attributes

| Return | Name | Description |
|--------|------|-------------|
| `float` | [`TransitionTime`](#transitiontime)  |  |
| `float` | [`RemainingTime`](#remainingtime)  |  |
| `bool` | [`bFinished`](#bfinished)  |  |
| `bool` | [`bFirstFrame`](#bfirstframe)  |  |
| `FComposableCameraTransitionInitParams` | [`InitParams`](#initparams)  |  |
| `float` | [`Percentage`](#percentage)  |  |

---

#### TransitionTime { #transitiontime }

```cpp
float TransitionTime
```

---

#### RemainingTime { #remainingtime }

```cpp
float RemainingTime
```

---

#### bFinished { #bfinished }

```cpp
bool bFinished { false }
```

---

#### bFirstFrame { #bfirstframe }

```cpp
bool bFirstFrame { true }
```

---

#### InitParams { #initparams }

```cpp
FComposableCameraTransitionInitParams InitParams
```

---

#### Percentage { #percentage }

```cpp
float Percentage { 0.f }
```

### Protected Methods

| Return | Name | Description |
|--------|------|-------------|
| `void` | [`OnBeginPlay`](#onbeginplay)  | Begin Play event. Called on the first frame of the transition, before the first OnEvaluate. <br/> |
| `void` | [`OnBeginPlay_Implementation`](#onbeginplay_implementation) `virtual` `inline` |  |
| `FComposableCameraPose` | [`OnEvaluate`](#onevaluate)  | Event to customize the evaluation function for each tick. When calling this function, RemainingTime has already been decremented, and assured to not go below 0. <br/> |
| `FComposableCameraPose` | [`OnEvaluate_Implementation`](#onevaluate_implementation-1) `virtual` `inline` |  |
| `void` | [`OnFinished`](#onfinished-1)  | Event when the transition finishes. The base class simply sets bFinished to true. |
| `void` | [`DrawStandardTransitionDebug`](#drawstandardtransitiondebug) `const` | Shared helper that paints the canonical source / target / progress endpoint markers. Each concrete transition's override still needs to draw its OWN path polyline (straight line, arc, polynomial, spline, rail, etc.) on top of these markers — the helper is deliberately silent about path shape because that's per-transition-type. |

---

#### OnBeginPlay { #onbeginplay }

```cpp
void OnBeginPlay(float DeltaTime, const FComposableCameraPose & CurrentSourcePose, const FComposableCameraPose & CurrentTargetPose)
```

Begin Play event. Called on the first frame of the transition, before the first OnEvaluate. <br/>
Use this to construct or initialize internal parameters specialized for this type of transition. <br/>

**Parameters**

* `DeltaTime` World delta time. <br/>

* `CurrentSourcePose` Current source camera pose. <br/>

* `CurrentTargetPose` Current target camera pose. <br/>

---

#### OnBeginPlay_Implementation { #onbeginplay_implementation }

`virtual` `inline`

```cpp
virtual inline void OnBeginPlay_Implementation(float DeltaTime, const FComposableCameraPose & CurrentSourcePose, const FComposableCameraPose & CurrentTargetPose)
```

---

#### OnEvaluate { #onevaluate }

```cpp
FComposableCameraPose OnEvaluate(float DeltaTime, const FComposableCameraPose & CurrentSourcePose, const FComposableCameraPose & CurrentTargetPose)
```

Event to customize the evaluation function for each tick. When calling this function, RemainingTime has already been decremented, and assured to not go below 0. <br/>

**Parameters**

* `DeltaTime` World delta time. <br/>

* `CurrentSourcePose` Current source camera pose. <br/>

* `CurrentTargetPose` Current target camera pose. <br/>

**Returns**

Returns the new blended camera pose.

---

#### OnEvaluate_Implementation { #onevaluate_implementation-1 }

`virtual` `inline`

```cpp
virtual inline FComposableCameraPose OnEvaluate_Implementation(float DeltaTime, const FComposableCameraPose & CurrentSourcePose, const FComposableCameraPose & CurrentTargetPose)
```

---

#### OnFinished { #onfinished-1 }

```cpp
void OnFinished()
```

Event when the transition finishes. The base class simply sets bFinished to true.

---

#### DrawStandardTransitionDebug { #drawstandardtransitiondebug }

`const`

```cpp
void DrawStandardTransitionDebug(class UWorld * World, bool bViewerIsOutsideCamera, const FColor & AccentColor) const
```

Shared helper that paints the canonical source / target / progress endpoint markers. Each concrete transition's override still needs to draw its OWN path polyline (straight line, arc, polynomial, spline, rail, etc.) on top of these markers — the helper is deliberately silent about path shape because that's per-transition-type.

Always drawn (possessed play + F8 eject):

* Green sphere at LastDebugSource.Position (r = 15)

* Blue sphere at LastDebugTarget.Position (r = 15)

* AccentColor sphere at LastDebugBlended.Position (r = 20) — the actual camera position this frame. For non-linear transitions (Spline, Cylindrical, Inertialized, PathGuided) this will visibly sit off the straight source-to-target axis.

F8 / SIE only (drawn when bViewerIsOutsideCamera is true):

* Half-scale green frustum at the source pose.

* Half-scale blue frustum at the target pose.

Frustums are intentionally skipped in possessed play: the blended frustum is already drawn by the camera-level frustum path, and source/target frustums would pile up against the near plane.

AccentColor should be distinct from every node-gizmo color in the codebase (see `Docs/TechDoc.md §3.20.4` for the reserved-color table).
