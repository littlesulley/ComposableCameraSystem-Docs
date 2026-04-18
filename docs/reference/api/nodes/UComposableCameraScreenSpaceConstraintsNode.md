
# UComposableCameraScreenSpaceConstraintsNode { #ucomposablecamerascreenspaceconstraintsnode }

```cpp
#include <ComposableCameraScreenSpaceConstraintsNode.h>
```

> **Inherits:** [`UComposableCameraCameraNodeBase`](../uobjects-other/UComposableCameraCameraNodeBase.md#ucomposablecameracameranodebase)

Node for constraining a pivot position in screen using either translation or rotation.

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `TObjectPtr< AActor >` | [`PivotActor`](#pivotactor-3)  |  |
| `EComposableCameraScreenSpaceMethod` | [`Method`](#method-3)  |  |
| `FVector2D` | [`SafeZoneCenter`](#safezonecenter-1)  |  |
| `FVector2D` | [`SafeZoneWidth`](#safezonewidth-1)  |  |
| `FVector2D` | [`SafeZoneHeight`](#safezoneheight-1)  |  |

---

#### PivotActor { #pivotactor-3 }

```cpp
TObjectPtr< AActor > PivotActor
```

---

#### Method { #method-3 }

```cpp
EComposableCameraScreenSpaceMethod Method
```

---

#### SafeZoneCenter { #safezonecenter-1 }

```cpp
FVector2D SafeZoneCenter { 0.0, 0.0 }
```

---

#### SafeZoneWidth { #safezonewidth-1 }

```cpp
FVector2D SafeZoneWidth { -0.1, 0.1 }
```

---

#### SafeZoneHeight { #safezoneheight-1 }

```cpp
FVector2D SafeZoneHeight { -0.1, 0.1 }
```

### Public Methods

| Return | Name | Description |
|--------|------|-------------|
| `void` | [`OnInitialize_Implementation`](#oninitialize_implementation-14) `virtual` |  |
| `void` | [`OnTickNode_Implementation`](#onticknode_implementation-20) `virtual` |  |
| `void` | [`BeginDestroy`](#begindestroy-3) `virtual` |  |
| `void` | [`GetPinDeclarations_Implementation`](#getpindeclarations_implementation-21) `virtual` `const` |  |

---

#### OnInitialize_Implementation { #oninitialize_implementation-14 }

`virtual`

```cpp
virtual void OnInitialize_Implementation()
```

---

#### OnTickNode_Implementation { #onticknode_implementation-20 }

`virtual`

```cpp
virtual void OnTickNode_Implementation(float DeltaTime, const FComposableCameraPose & CurrentCameraPose, FComposableCameraPose & OutCameraPose)
```

---

#### BeginDestroy { #begindestroy-3 }

`virtual`

```cpp
virtual void BeginDestroy()
```

---

#### GetPinDeclarations_Implementation { #getpindeclarations_implementation-21 }

`virtual` `const`

```cpp
virtual void GetPinDeclarations_Implementation(TArray< FComposableCameraNodePinDeclaration > & OutPins) const
```

### Private Methods

| Return | Name | Description |
|--------|------|-------------|
| `FVector` | [`EnsureWithinBoundsTranslation`](#ensurewithinboundstranslation-1)  |  |
| `FRotator` | [`EnsureWithinBoundsRotation`](#ensurewithinboundsrotation-1)  |  |
| `std::pair< float, float >` | [`GetTanHalfHORAndAspectRatio`](#gettanhalfhorandaspectratio-1)  |  |
| `std::pair< float, float >` | [`CalibrateRotationOffsetNewton`](#calibraterotationoffsetnewton-1)  |  |
| `FVector` | [`GetCurrentPivot`](#getcurrentpivot-1)  |  |

---

#### EnsureWithinBoundsTranslation { #ensurewithinboundstranslation-1 }

```cpp
FVector EnsureWithinBoundsTranslation(const FVector & Pivot, const FComposableCameraPose & CurrentPose, const float & AspectRatio, const float & TanHalfHOR)
```

---

#### EnsureWithinBoundsRotation { #ensurewithinboundsrotation-1 }

```cpp
FRotator EnsureWithinBoundsRotation(const FVector & Pivot, const FComposableCameraPose & CurrentPose, float AspectRatio, float DegTanHalfHor)
```

---

#### GetTanHalfHORAndAspectRatio { #gettanhalfhorandaspectratio-1 }

```cpp
std::pair< float, float > GetTanHalfHORAndAspectRatio(const FComposableCameraPose & OutCameraPose)
```

---

#### CalibrateRotationOffsetNewton { #calibraterotationoffsetnewton-1 }

```cpp
std::pair< float, float > CalibrateRotationOffsetNewton(float TanHalfHOR, float AspectRatio, FVector Direction, FRotator LookAtRotation, float ScreenX, float ScreenY)
```

---

#### GetCurrentPivot { #getcurrentpivot-1 }

```cpp
FVector GetCurrentPivot()
```
