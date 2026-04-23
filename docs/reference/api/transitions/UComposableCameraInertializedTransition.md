
# UComposableCameraInertializedTransition { #ucomposablecamerainertializedtransition }

```cpp
#include <ComposableCameraInertializedTransition.h>
```

> **Inherits:** [`UComposableCameraTransitionBase`](UComposableCameraTransitionBase.md#ucomposablecameratransitionbase)

Inertialized transition.

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `bool` | [`bAutoTransitionTime`](#bautotransitiontime)  |  |
| `float` | [`MaxAcceleration`](#maxacceleration)  |  |
| `UCurveFloat *` | [`AdditiveCurve`](#additivecurve)  |  |
| `float` | [`AdditiveCurveWeight`](#additivecurveweight)  |  |
| `float` | [`AdditiveCurveShape`](#additivecurveshape)  |  |

---

#### bAutoTransitionTime { #bautotransitiontime }

```cpp
bool bAutoTransitionTime { false }
```

---

#### MaxAcceleration { #maxacceleration }

```cpp
float MaxAcceleration { 100.f }
```

---

#### AdditiveCurve { #additivecurve }

```cpp
UCurveFloat * AdditiveCurve
```

---

#### AdditiveCurveWeight { #additivecurveweight }

```cpp
float AdditiveCurveWeight { 0.5f }
```

---

#### AdditiveCurveShape { #additivecurveshape }

```cpp
float AdditiveCurveShape { 10.f }
```

### Public Methods

| Return | Name | Description |
|--------|------|-------------|
| `void` | [`OnBeginPlay_Implementation`](#onbeginplay_implementation-4) `virtual` |  |
| `FComposableCameraPose` | [`OnEvaluate_Implementation`](#onevaluate_implementation-9) `virtual` |  |
| `void` | [`DrawTransitionDebug`](#drawtransitiondebug-8) `virtual` `const` | Per-transition world-space debug hook. |

---

#### OnBeginPlay_Implementation { #onbeginplay_implementation-4 }

`virtual`

```cpp
virtual void OnBeginPlay_Implementation(float DeltaTime, const FComposableCameraPose & CurrentSourcePose, const FComposableCameraPose & CurrentTargetPose)
```

---

#### OnEvaluate_Implementation { #onevaluate_implementation-9 }

`virtual`

```cpp
virtual FComposableCameraPose OnEvaluate_Implementation(float DeltaTime, const FComposableCameraPose & CurrentSourcePose, const FComposableCameraPose & CurrentTargetPose)
```

---

#### DrawTransitionDebug { #drawtransitiondebug-8 }

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
| `ComposableCameraInitializer< FRotator, ComposableCameraRotationalInertializer >` | [`RotationalInertializer`](#rotationalinertializer)  |  |
| `ComposableCameraInitializer< FVector, ComposableCameraIndependentPositionalInertializer >` | [`PositionalInertializer`](#positionalinertializer)  |  |
| `TArray< FVector >` | [`DebugPathOffsets`](#debugpathoffsets)  |  |

---

#### RotationalInertializer { #rotationalinertializer }

```cpp
ComposableCameraInitializer< FRotator, ComposableCameraRotationalInertializer > RotationalInertializer
```

---

#### PositionalInertializer { #positionalinertializer }

```cpp
ComposableCameraInitializer< FVector, ComposableCameraIndependentPositionalInertializer > PositionalInertializer
```

---

#### DebugPathOffsets { #debugpathoffsets }

```cpp
TArray< FVector > DebugPathOffsets
```

### Private Methods

| Return | Name | Description |
|--------|------|-------------|
| `float` | [`GetActualBlendTime`](#getactualblendtime)  |  |

---

#### GetActualBlendTime { #getactualblendtime }

```cpp
float GetActualBlendTime(float DeltaTime, const FComposableCameraPose & LastSourceCameraPose, const FComposableCameraPose & ThisSourceCameraPose, const FComposableCameraPose & CurrentTargetPose)
```
