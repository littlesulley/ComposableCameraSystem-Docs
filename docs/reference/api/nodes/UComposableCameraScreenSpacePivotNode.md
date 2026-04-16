
# UComposableCameraScreenSpacePivotNode { #ucomposablecamerascreenspacepivotnode }

```cpp
#include <ComposableCameraScreenSpacePivotNode.h>
```

> **Inherits:** [`UComposableCameraCameraNodeBase`](../uobjects-other/UComposableCameraCameraNodeBase.md#ucomposablecameracameranodebase)

Node for positioning the given pivot point in the given screen space.

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `EComposableCameraScreenSpacePivotSource` | [`PivotSource`](#pivotsource)  |  |
| `FVector` | [`PivotWorldPosition`](#pivotworldposition)  |  |
| `TObjectPtr< AActor >` | [`PivotActor`](#pivotactor-1)  |  |
| `float` | [`PivotWorldUpOffset`](#pivotworldupoffset)  |  |
| `EComposableCameraScreenSpaceMethod` | [`Method`](#method-1)  |  |
| `FComposableCameraScreenSpaceTranslationParams` | [`TranslationParams`](#translationparams)  |  |
| `FComposableCameraScreenSpaceRotationParams` | [`RotationParams`](#rotationparams)  |  |
| `FVector2D` | [`SafeZoneCenter`](#safezonecenter)  |  |
| `FVector2D` | [`SafeZoneWidth`](#safezonewidth)  |  |
| `FVector2D` | [`SafeZoneHeight`](#safezoneheight)  |  |

---

#### PivotSource { #pivotsource }

```cpp
EComposableCameraScreenSpacePivotSource PivotSource {  }
```

---

#### PivotWorldPosition { #pivotworldposition }

```cpp
FVector PivotWorldPosition { FVector::ZeroVector }
```

---

#### PivotActor { #pivotactor-1 }

```cpp
TObjectPtr< AActor > PivotActor
```

---

#### PivotWorldUpOffset { #pivotworldupoffset }

```cpp
float PivotWorldUpOffset { 0.f }
```

---

#### Method { #method-1 }

```cpp
EComposableCameraScreenSpaceMethod Method
```

---

#### TranslationParams { #translationparams }

```cpp
FComposableCameraScreenSpaceTranslationParams TranslationParams
```

---

#### RotationParams { #rotationparams }

```cpp
FComposableCameraScreenSpaceRotationParams RotationParams
```

---

#### SafeZoneCenter { #safezonecenter }

```cpp
FVector2D SafeZoneCenter { 0.0, 0.0 }
```

---

#### SafeZoneWidth { #safezonewidth }

```cpp
FVector2D SafeZoneWidth { -0.1, 0.1 }
```

---

#### SafeZoneHeight { #safezoneheight }

```cpp
FVector2D SafeZoneHeight { -0.1, 0.1 }
```

### Public Methods

| Return | Name | Description |
|--------|------|-------------|
| `void` | [`OnInitialize_Implementation`](#oninitialize_implementation-10) `virtual` |  |
| `void` | [`OnTickNode_Implementation`](#onticknode_implementation-16) `virtual` |  |
| `void` | [`BeginDestroy`](#begindestroy-1) `virtual` |  |
| `void` | [`GetPinDeclarations_Implementation`](#getpindeclarations_implementation-16) `virtual` `const` |  |

---

#### OnInitialize_Implementation { #oninitialize_implementation-10 }

`virtual`

```cpp
virtual void OnInitialize_Implementation()
```

---

#### OnTickNode_Implementation { #onticknode_implementation-16 }

`virtual`

```cpp
virtual void OnTickNode_Implementation(float DeltaTime, const FComposableCameraPose & CurrentCameraPose, FComposableCameraPose & OutCameraPose)
```

---

#### BeginDestroy { #begindestroy-1 }

`virtual`

```cpp
virtual void BeginDestroy()
```

---

#### GetPinDeclarations_Implementation { #getpindeclarations_implementation-16 }

`virtual` `const`

```cpp
virtual void GetPinDeclarations_Implementation(TArray< FComposableCameraNodePinDeclaration > & OutPins) const
```

### Private Attributes

| Return | Name | Description |
|--------|------|-------------|
| `TUniquePtr< TCameraInterpolator< TValueTypeWrapper< double > > >` | [`XInterpolator_T`](#xinterpolator_t)  |  |
| `TUniquePtr< TCameraInterpolator< TValueTypeWrapper< double > > >` | [`YInterpolator_T`](#yinterpolator_t)  |  |
| `TUniquePtr< TCameraInterpolator< TValueTypeWrapper< double > > >` | [`ZInterpolator_T`](#zinterpolator_t)  |  |
| `TUniquePtr< TCameraInterpolator< TValueTypeWrapper< double > > >` | [`YawInterpolator_T`](#yawinterpolator_t)  |  |
| `TUniquePtr< TCameraInterpolator< TValueTypeWrapper< double > > >` | [`PitchInterpolator_T`](#pitchinterpolator_t)  |  |
| `FDelegateHandle` | [`DrawDebugHandle`](#drawdebughandle)  |  |

---

#### XInterpolator_T { #xinterpolator_t }

```cpp
TUniquePtr< TCameraInterpolator< TValueTypeWrapper< double > > > XInterpolator_T
```

---

#### YInterpolator_T { #yinterpolator_t }

```cpp
TUniquePtr< TCameraInterpolator< TValueTypeWrapper< double > > > YInterpolator_T
```

---

#### ZInterpolator_T { #zinterpolator_t }

```cpp
TUniquePtr< TCameraInterpolator< TValueTypeWrapper< double > > > ZInterpolator_T
```

---

#### YawInterpolator_T { #yawinterpolator_t }

```cpp
TUniquePtr< TCameraInterpolator< TValueTypeWrapper< double > > > YawInterpolator_T
```

---

#### PitchInterpolator_T { #pitchinterpolator_t }

```cpp
TUniquePtr< TCameraInterpolator< TValueTypeWrapper< double > > > PitchInterpolator_T
```

---

#### DrawDebugHandle { #drawdebughandle }

```cpp
FDelegateHandle DrawDebugHandle
```

### Private Methods

| Return | Name | Description |
|--------|------|-------------|
| `void` | [`EnsureWithinBoundsTranslation`](#ensurewithinboundstranslation)  |  |
| `void` | [`EnsureWithinBoundsRotation`](#ensurewithinboundsrotation)  |  |
| `std::pair< float, float >` | [`GetTanHalfHORAndAspectRatio`](#gettanhalfhorandaspectratio)  |  |
| `FVector` | [`GetScreenSpaceTranslateAmount`](#getscreenspacetranslateamount)  |  |
| `std::pair< float, float >` | [`CalibrateRotationOffsetLM`](#calibraterotationoffsetlm)  |  |
| `std::pair< float, float >` | [`CalibrateRotationOffsetNewton`](#calibraterotationoffsetnewton)  |  |
| `FRotator` | [`GetScreenSpaceRotateAmount`](#getscreenspacerotateamount)  |  |
| `FVector` | [`GetCurrentPivot`](#getcurrentpivot)  |  |
| `void` | [`DrawDebugInfo`](#drawdebuginfo)  |  |

---

#### EnsureWithinBoundsTranslation { #ensurewithinboundstranslation }

```cpp
void EnsureWithinBoundsTranslation(const FVector & CameraSpacePivotPosition, FVector & CameraSpaceDampedOffset, const float & AspectRatio, const float & TanHalfHOR, const float & CameraDistance)
```

---

#### EnsureWithinBoundsRotation { #ensurewithinboundsrotation }

```cpp
void EnsureWithinBoundsRotation(const FRotator & CameraRotation, const FVector & LookAtRotation, FRotator & DeltaRotation, float AspectRatio, float DegTanHalfHor)
```

---

#### GetTanHalfHORAndAspectRatio { #gettanhalfhorandaspectratio }

```cpp
std::pair< float, float > GetTanHalfHORAndAspectRatio(const FComposableCameraPose & OutCameraPose)
```

---

#### GetScreenSpaceTranslateAmount { #getscreenspacetranslateamount }

```cpp
FVector GetScreenSpaceTranslateAmount(const FVector & Pivot, const FComposableCameraPose & OutCameraPose, float DeltaTime)
```

---

#### CalibrateRotationOffsetLM { #calibraterotationoffsetlm }

```cpp
std::pair< float, float > CalibrateRotationOffsetLM(float TanHalfHOR, float AspectRatio, FVector Direction, FRotator LookAtRotation, float ScreenX, float ScreenY)
```

---

#### CalibrateRotationOffsetNewton { #calibraterotationoffsetnewton }

```cpp
std::pair< float, float > CalibrateRotationOffsetNewton(float TanHalfHOR, float AspectRatio, FVector Direction, FRotator LookAtRotation, float ScreenX, float ScreenY)
```

---

#### GetScreenSpaceRotateAmount { #getscreenspacerotateamount }

```cpp
FRotator GetScreenSpaceRotateAmount(const FVector & Pivot, const FComposableCameraPose & OutCameraPose, float DeltaTime)
```

---

#### GetCurrentPivot { #getcurrentpivot }

```cpp
FVector GetCurrentPivot()
```

---

#### DrawDebugInfo { #drawdebuginfo }

```cpp
void DrawDebugInfo(AHUD * HUD, UCanvas * Canvas)
```
