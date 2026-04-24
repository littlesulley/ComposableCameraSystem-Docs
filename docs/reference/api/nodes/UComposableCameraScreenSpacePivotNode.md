
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
| `TObjectPtr< AActor >` | [`PivotActor`](#pivotactor-5)  |  |
| `float` | [`PivotWorldUpOffset`](#pivotworldupoffset)  |  |
| `EComposableCameraScreenSpaceMethod` | [`Method`](#method)  |  |
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

#### PivotActor { #pivotactor-5 }

```cpp
TObjectPtr< AActor > PivotActor
```

---

#### PivotWorldUpOffset { #pivotworldupoffset }

```cpp
float PivotWorldUpOffset { 0.f }
```

---

#### Method { #method }

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
| `void` | [`OnInitialize_Implementation`](#oninitialize_implementation-13) `virtual` |  |
| `void` | [`OnTickNode_Implementation`](#onticknode_implementation-21) `virtual` |  |
| `void` | [`GetPinDeclarations_Implementation`](#getpindeclarations_implementation-19) `virtual` `const` |  |
| `void` | [`DrawNodeDebug`](#drawnodedebug-10) `virtual` `const` | Called each frame when the `CCS.Debug.Viewport` CVar is enabled, for every node on the currently running camera. Override to draw world-space debug gizmos via `DrawDebugHelpers` (DrawDebugSphere, DrawDebugLine, etc.) that visualise this node's runtime state — e.g. a pivot sphere for PivotOffsetNode, a look-at line for LookAtNode, the collision trace for CollisionPushNode, a sampled spline path for SplineNode. |
| `void` | [`DrawNodeDebug2D`](#drawnodedebug2d-1) `virtual` `const` | 2D counterpart to DrawNodeDebug. Fires from a separate UDebugDrawService hook on the "Game" channel — which means it runs during PIE-possessed play (and standalone), NOT during F8 eject (editor viewport doesn't route through the game channel). That lines up with what 2D overlays are good for: screen-space debug that the player-eye perspective answers and an external view cannot (safe-zone rectangles, projected pivot markers, HUD-space gizmos). |

---

#### OnInitialize_Implementation { #oninitialize_implementation-13 }

`virtual`

```cpp
virtual void OnInitialize_Implementation()
```

---

#### OnTickNode_Implementation { #onticknode_implementation-21 }

`virtual`

```cpp
virtual void OnTickNode_Implementation(float DeltaTime, const FComposableCameraPose & CurrentCameraPose, FComposableCameraPose & OutCameraPose)
```

---

#### GetPinDeclarations_Implementation { #getpindeclarations_implementation-19 }

`virtual` `const`

```cpp
virtual void GetPinDeclarations_Implementation(TArray< FComposableCameraNodePinDeclaration > & OutPins) const
```

---

#### DrawNodeDebug { #drawnodedebug-10 }

`virtual` `const`

```cpp
virtual void DrawNodeDebug(UWorld * World, bool bViewerIsOutsideCamera) const
```

Called each frame when the `CCS.Debug.Viewport` CVar is enabled, for every node on the currently running camera. Override to draw world-space debug gizmos via `DrawDebugHelpers` (DrawDebugSphere, DrawDebugLine, etc.) that visualise this node's runtime state — e.g. a pivot sphere for PivotOffsetNode, a look-at line for LookAtNode, the collision trace for CollisionPushNode, a sampled spline path for SplineNode.

Access the owning camera via `OwningCamera` and current-frame pin values via the usual `GetInputPinValue<T>()` / member-read path — this hook fires AFTER TickNode, so pin-backed UPROPERTYs still hold the resolved values from the most recent evaluation.

`bViewerIsOutsideCamera` mirrors the ticker's frustum-draw flag: true when the viewer is observing the camera from outside (F8 eject, SIE, or `CCS.Debug.Viewport.AlwaysShow`), false when the player is looking through the camera. Most gizmos (pivot spheres at distant characters, lines to look-at targets, spline polylines far in the world) can ignore this and draw unconditionally. Gizmos that sit AT the camera's own position (e.g. `CollisionPushNode`'s self-collision sphere) should gate on this bool so they don't hermetically seal the player inside the wireframe during live gameplay.

Default implementation does nothing. Compiled out in shipping builds.

---

#### DrawNodeDebug2D { #drawnodedebug2d-1 }

`virtual` `const`

```cpp
virtual void DrawNodeDebug2D(UCanvas * Canvas, APlayerController * PC) const
```

2D counterpart to DrawNodeDebug. Fires from a separate UDebugDrawService hook on the "Game" channel — which means it runs during PIE-possessed play (and standalone), NOT during F8 eject (editor viewport doesn't route through the game channel). That lines up with what 2D overlays are good for: screen-space debug that the player-eye perspective answers and an external view cannot (safe-zone rectangles, projected pivot markers, HUD-space gizmos).

Canvas provides the 2D surface; PC is the local player controller whose view is being rendered (for ProjectWorldToScreen and aspect ratio queries). Either may be null in edge cases — always check.

Default implementation does nothing. Compiled out in shipping builds.

### Private Attributes

| Return | Name | Description |
|--------|------|-------------|
| `TUniquePtr< TCameraInterpolator< TValueTypeWrapper< double > > >` | [`XInterpolator_T`](#xinterpolator_t)  |  |
| `TUniquePtr< TCameraInterpolator< TValueTypeWrapper< double > > >` | [`YInterpolator_T`](#yinterpolator_t)  |  |
| `TUniquePtr< TCameraInterpolator< TValueTypeWrapper< double > > >` | [`ZInterpolator_T`](#zinterpolator_t)  |  |
| `TUniquePtr< TCameraInterpolator< TValueTypeWrapper< double > > >` | [`YawInterpolator_T`](#yawinterpolator_t)  |  |
| `TUniquePtr< TCameraInterpolator< TValueTypeWrapper< double > > >` | [`PitchInterpolator_T`](#pitchinterpolator_t)  |  |

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
| `FVector` | [`GetCurrentPivot`](#getcurrentpivot) `const` |  |

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

`const`

```cpp
FVector GetCurrentPivot() const
```
