
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

### Private Methods

| Return | Name | Description |
|--------|------|-------------|
| `void` | [`DrawDebugSpline`](#drawdebugspline)  |  |

---

#### DrawDebugSpline { #drawdebugspline }

```cpp
void DrawDebugSpline(const FComposableCameraPose & StartPose, const FComposableCameraPose & TargetPose)
```
