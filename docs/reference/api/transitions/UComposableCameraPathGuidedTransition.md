
# UComposableCameraPathGuidedTransition { #ucomposablecamerapathguidedtransition }

```cpp
#include <ComposableCameraPathGuidedTransition.h>
```

> **Inherits:** [`UComposableCameraTransitionBase`](UComposableCameraTransitionBase.md#ucomposablecameratransitionbase)

A transition which utilizes a path　(spline) to guide its position during transition. This transition leverages two InertializedTransitions to achieve smoothness. An intermediate camera will be spawned as a wrapper for the spline. So this transition will be more expensive than other transitions.

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `UComposableCameraTransitionBase *` | [`DrivingTransition`](#drivingtransition)  |  |
| `EComposableCameraPathGuidedTransitionType` | [`Type`](#type)  |  |
| `TSoftObjectPtr< ACameraRig_Rail >` | [`RailActor`](#railactor)  |  |
| `FVector2D` | [`GuideRange`](#guiderange)  |  |
| `UCurveFloat *` | [`SplineMoveCurve`](#splinemovecurve)  |  |

---

#### DrivingTransition { #drivingtransition }

```cpp
UComposableCameraTransitionBase * DrivingTransition
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
UCurveFloat * SplineMoveCurve
```

### Public Methods

| Return | Name | Description |
|--------|------|-------------|
| `void` | [`OnBeginPlay_Implementation`](#onbeginplay_implementation-2) `virtual` |  |
| `FComposableCameraPose` | [`OnEvaluate_Implementation`](#onevaluate_implementation-6) `virtual` |  |

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

### Private Attributes

| Return | Name | Description |
|--------|------|-------------|
| `AComposableCameraCameraBase *` | [`IntermediateCamera`](#intermediatecamera)  |  |
| `ACameraRig_Rail *` | [`Rail`](#rail-1)  |  |
| `UComposableCameraInertializedTransition *` | [`EnterTransition`](#entertransition-2)  |  |
| `UComposableCameraInertializedTransition *` | [`ExitTransition`](#exittransition-1)  |  |
| `USplineComponent *` | [`InternalSpline`](#internalspline)  |  |
| `AActor *` | [`DebugSplineActor`](#debugsplineactor)  |  |

---

#### IntermediateCamera { #intermediatecamera }

```cpp
AComposableCameraCameraBase * IntermediateCamera { nullptr }
```

---

#### Rail { #rail-1 }

```cpp
ACameraRig_Rail * Rail
```

---

#### EnterTransition { #entertransition-2 }

```cpp
UComposableCameraInertializedTransition * EnterTransition { nullptr }
```

---

#### ExitTransition { #exittransition-1 }

```cpp
UComposableCameraInertializedTransition * ExitTransition { nullptr }
```

---

#### InternalSpline { #internalspline }

```cpp
USplineComponent * InternalSpline
```

---

#### DebugSplineActor { #debugsplineactor }

```cpp
AActor * DebugSplineActor
```

### Private Methods

| Return | Name | Description |
|--------|------|-------------|
| `void` | [`BuildInternalSpline`](#buildinternalspline)  |  |

---

#### BuildInternalSpline { #buildinternalspline }

```cpp
void BuildInternalSpline(const FComposableCameraPose & CurrentTargetPose, float DeltaTime)
```
