
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

### Private Attributes

| Return | Name | Description |
|--------|------|-------------|
| `ComposableCameraInitializer< FRotator, ComposableCameraRotationalInertializer >` | [`RotationalInertializer`](#rotationalinertializer)  |  |
| `ComposableCameraInitializer< FVector, ComposableCameraIndependentPositionalInertializer >` | [`PositionalInertializer`](#positionalinertializer)  |  |

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

### Private Methods

| Return | Name | Description |
|--------|------|-------------|
| `float` | [`GetActualBlendTime`](#getactualblendtime)  |  |

---

#### GetActualBlendTime { #getactualblendtime }

```cpp
float GetActualBlendTime(float DeltaTime, const FComposableCameraPose & LastSourceCameraPose, const FComposableCameraPose & ThisSourceCameraPose, const FComposableCameraPose & CurrentTargetPose)
```
