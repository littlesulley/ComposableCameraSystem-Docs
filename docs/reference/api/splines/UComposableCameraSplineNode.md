
# UComposableCameraSplineNode { #ucomposablecamerasplinenode }

```cpp
#include <ComposableCameraSplineNode.h>
```

> **Inherits:** [`UComposableCameraCameraNodeBase`](../uobjects-other/UComposableCameraCameraNodeBase.md#ucomposablecameracameranodebase)

Node for placing the camera on a given spline.

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `EComposableCameraSplineNodeSplineType` | [`SplineType`](#splinetype)  |  |
| `TObjectPtr< ACameraRig_Rail >` | [`Rail`](#rail)  |  |
| `EComposableCameraSplineNodeMoveMethod` | [`MoveMethod`](#movemethod)  |  |
| `TObjectPtr< AActor >` | [`ClosestMoveMethodPivotActor`](#closestmovemethodpivotactor)  |  |
| `TObjectPtr< UCurveFloat >` | [`AutomaticMoveCurve`](#automaticmovecurve)  |  |
| `float` | [`Duration`](#duration-3)  |  |
| `bool` | [`bLoop`](#bloop)  |  |
| `UComposableCameraInterpolatorBase *` | [`MoveInterpolator`](#moveinterpolator)  |  |
| `float` | [`MoveOffset`](#moveoffset)  |  |
| `bool` | [`bLockOrientationOnSpline`](#blockorientationonspline)  |  |

---

#### SplineType { #splinetype }

```cpp
EComposableCameraSplineNodeSplineType SplineType {  }
```

---

#### Rail { #rail }

```cpp
TObjectPtr< ACameraRig_Rail > Rail { nullptr }
```

---

#### MoveMethod { #movemethod }

```cpp
EComposableCameraSplineNodeMoveMethod MoveMethod {  }
```

---

#### ClosestMoveMethodPivotActor { #closestmovemethodpivotactor }

```cpp
TObjectPtr< AActor > ClosestMoveMethodPivotActor { nullptr }
```

---

#### AutomaticMoveCurve { #automaticmovecurve }

```cpp
TObjectPtr< UCurveFloat > AutomaticMoveCurve { nullptr }
```

---

#### Duration { #duration-3 }

```cpp
float Duration { 3.0f }
```

---

#### bLoop { #bloop }

```cpp
bool bLoop { false }
```

---

#### MoveInterpolator { #moveinterpolator }

```cpp
UComposableCameraInterpolatorBase * MoveInterpolator
```

---

#### MoveOffset { #moveoffset }

```cpp
float MoveOffset { 0.f }
```

---

#### bLockOrientationOnSpline { #blockorientationonspline }

```cpp
bool bLockOrientationOnSpline { false }
```

### Public Methods

| Return | Name | Description |
|--------|------|-------------|
| `void` | [`OnInitialize_Implementation`](#oninitialize_implementation-1) `virtual` |  |
| `void` | [`OnTickNode_Implementation`](#onticknode_implementation-1) `virtual` |  |
| `void` | [`GetPinDeclarations_Implementation`](#getpindeclarations_implementation-1) `virtual` `const` |  |

---

#### OnInitialize_Implementation { #oninitialize_implementation-1 }

`virtual`

```cpp
virtual void OnInitialize_Implementation()
```

---

#### OnTickNode_Implementation { #onticknode_implementation-1 }

`virtual`

```cpp
virtual void OnTickNode_Implementation(float DeltaTime, const FComposableCameraPose & CurrentCameraPose, FComposableCameraPose & OutCameraPose)
```

---

#### GetPinDeclarations_Implementation { #getpindeclarations_implementation-1 }

`virtual` `const`

```cpp
virtual void GetPinDeclarations_Implementation(TArray< FComposableCameraNodePinDeclaration > & OutPins) const
```

### Private Attributes

| Return | Name | Description |
|--------|------|-------------|
| `TUniquePtr< TCameraInterpolator< TValueTypeWrapper< double > > >` | [`MoveInterpolator_T`](#moveinterpolator_t)  |  |
| `IComposableCameraSplineInterface *` | [`SplineInterface`](#splineinterface)  |  |
| `float` | [`ElapsedTimeForAutomaticMethod`](#elapsedtimeforautomaticmethod)  |  |
| `bool` | [`bFirstLapIfLoop`](#bfirstlapifloop)  |  |

---

#### MoveInterpolator_T { #moveinterpolator_t }

```cpp
TUniquePtr< TCameraInterpolator< TValueTypeWrapper< double > > > MoveInterpolator_T
```

---

#### SplineInterface { #splineinterface }

```cpp
IComposableCameraSplineInterface * SplineInterface
```

---

#### ElapsedTimeForAutomaticMethod { #elapsedtimeforautomaticmethod }

```cpp
float ElapsedTimeForAutomaticMethod { 0.0f }
```

---

#### bFirstLapIfLoop { #bfirstlapifloop }

```cpp
bool bFirstLapIfLoop { true }
```

### Private Methods

| Return | Name | Description |
|--------|------|-------------|
| `void` | [`UpdateCameraPoseByBuiltInSpline`](#updatecameraposebybuiltinspline)  |  |
| `void` | [`UpdateCameraPoseByBezierSpline`](#updatecameraposebybezierspline)  |  |
| `void` | [`UpdateCameraPoseByHermiteSpline`](#updatecameraposebyhermitespline)  |  |
| `void` | [`UpdateCameraPoseByBasicSpline`](#updatecameraposebybasicspline)  |  |
| `void` | [`UpdateCameraPoseByNURBSpline`](#updatecameraposebynurbspline)  |  |

---

#### UpdateCameraPoseByBuiltInSpline { #updatecameraposebybuiltinspline }

```cpp
void UpdateCameraPoseByBuiltInSpline(FVector & OutPosition, FRotator & OutRotation, const FComposableCameraPose & CurrentCameraPose, float DeltaTime)
```

---

#### UpdateCameraPoseByBezierSpline { #updatecameraposebybezierspline }

```cpp
void UpdateCameraPoseByBezierSpline(FVector & OutPosition, FRotator & OutRotation, const FComposableCameraPose & CurrentCameraPose, float DeltaTime)
```

---

#### UpdateCameraPoseByHermiteSpline { #updatecameraposebyhermitespline }

```cpp
void UpdateCameraPoseByHermiteSpline(FVector & OutPosition, FRotator & OutRotation, const FComposableCameraPose & CurrentCameraPose, float DeltaTime)
```

---

#### UpdateCameraPoseByBasicSpline { #updatecameraposebybasicspline }

```cpp
void UpdateCameraPoseByBasicSpline(FVector & OutPosition, FRotator & OutRotation, const FComposableCameraPose & CurrentCameraPose, float DeltaTime)
```

---

#### UpdateCameraPoseByNURBSpline { #updatecameraposebynurbspline }

```cpp
void UpdateCameraPoseByNURBSpline(FVector & OutPosition, FRotator & OutRotation, const FComposableCameraPose & CurrentCameraPose, float DeltaTime)
```
