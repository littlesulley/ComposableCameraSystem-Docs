
# UComposableCameraCompositionPreservingTransition { #ucomposablecameracompositionpreservingtransition }

```cpp
#include <ComposableCameraCompositionPreservingTransition.h>
```

> **Inherits:** [`UComposableCameraTransitionBase`](UComposableCameraTransitionBase.md#ucomposablecameratransitionbase)

Rebuilds the source side of a transition so a moving subject keeps its
transition-start composition while rotation follows a driving transition.

This transition wraps another transition. The wrapped `DrivingTransition`
evaluates the normal source-to-target blend and supplies both rotation and
blend percentage. CompositionPreserving then blends non-transform pose fields,
overwrites rotation with the driving rotation, and recomputes camera position
around the selected subject.

At transition start, the source-camera local subject offset is captured. Each
tick, the target-camera local subject offset is recomputed from the live target
pose and live subject location. Blending from the captured source offset to the
live target offset makes alpha = 1 converge to `CurrentTargetPose`, avoiding a
snap when the evaluation tree collapses to the target camera.

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `TObjectPtr< UComposableCameraTransitionBase >` | [`DrivingTransition`](#drivingtransition) | Transition that drives rotation and the non-rotation blend percentage. |
| `EComposableCameraActorInputSource` | [`SubjectActorSource`](#subjectactorsource) | Subject whose initial source-camera composition should be preserved. |
| `TObjectPtr< AActor >` | [`SubjectActor`](#subjectactor) | Explicit subject when `SubjectActorSource` is `ExplicitActor`. |

---

#### DrivingTransition { #drivingtransition }

```cpp
TObjectPtr< UComposableCameraTransitionBase > DrivingTransition { nullptr }
```

Transition that drives rotation and the non-rotation blend percentage.

If the wrapper `TransitionTime` is unset or zero and the driving transition has
a positive transition time, the wrapper adopts the driving transition duration
on begin play so it does not finish before the driving transition can evaluate.

---

#### SubjectActorSource { #subjectactorsource }

```cpp
EComposableCameraActorInputSource SubjectActorSource { EComposableCameraActorInputSource::ControllerControlledPawn }
```

Subject whose initial source-camera composition should be preserved.

`ControllerControlledPawn` resolves through the owning player camera manager
cached by [`UComposableCameraTransitionBase`](UComposableCameraTransitionBase.md#ucomposablecameratransitionbase), so multi-controller worlds use the PCM owner
rather than a world-first controller fallback.

---

#### SubjectActor { #subjectactor }

```cpp
TObjectPtr< AActor > SubjectActor { nullptr }
```

Explicit subject when `SubjectActorSource` is `ExplicitActor`.

### Public Methods

| Return | Name | Description |
|--------|------|-------------|
| `void` | [`OnBeginPlay_Implementation`](#onbeginplay_implementation) `virtual` | Initializes the driving transition and captures the source-side subject composition. |
| `FComposableCameraPose` | [`OnEvaluate_Implementation`](#onevaluate_implementation) `virtual` | Evaluates the driving transition and rebuilds the output pose around the live subject. |
| `float` | [`GetBlendWeightAt`](#getblendweightat) `virtual` `const` | Delegates the debug-panel blend curve to the driving transition when present. |
| `void` | [`DrawTransitionDebug`](#drawtransitiondebug) `virtual` `const` | Draws the standard transition debug markers plus the tracked-subject line. |

---

#### OnBeginPlay_Implementation { #onbeginplay_implementation }

`virtual`

```cpp
virtual void OnBeginPlay_Implementation(float DeltaTime, const FComposableCameraPose & CurrentSourcePose, const FComposableCameraPose & CurrentTargetPose)
```

Initializes `DrivingTransition`, synchronizes its transition time, resets its
state, and captures the subject offset in source-camera local space.

---

#### OnEvaluate_Implementation { #onevaluate_implementation }

`virtual`

```cpp
virtual FComposableCameraPose OnEvaluate_Implementation(float DeltaTime, const FComposableCameraPose & CurrentSourcePose, const FComposableCameraPose & CurrentTargetPose)
```

Evaluates `DrivingTransition(CurrentSourcePose, CurrentTargetPose)`, uses the
driving pose rotation as `R'`, and rebuilds the camera location as:

```text
SubjectLocation - R'.RotateVector(Lerp(CapturedSourceOffset, LiveTargetOffset, Percentage))
```

If the driving transition is missing, the method logs a warning and falls back
to `CurrentTargetPose`. If the subject cannot be captured or later becomes
invalid, it returns the driving pose unchanged.

---

#### GetBlendWeightAt { #getblendweightat }

`virtual` `const`

```cpp
virtual float GetBlendWeightAt(float NormalizedTime) const
```

Delegates to `DrivingTransition->GetBlendWeightAt(NormalizedTime)` when a
driving transition is assigned. Otherwise returns the clamped normalized time.

---

#### DrawTransitionDebug { #drawtransitiondebug }

`virtual` `const`

```cpp
virtual void DrawTransitionDebug(UWorld * World, bool bViewerIsOutsideCamera) const
```

Compiled out in shipping builds. Enabled by
`CCS.Debug.Viewport.Transitions.CompositionPreserving 1` or by
`CCS.Debug.Viewport.Transitions.All 1`, with `CCS.Debug.Viewport 1` as the
master switch. Draws the standard transition markers in turquoise and, when the
subject resolves, a line from the source endpoint to the subject.

