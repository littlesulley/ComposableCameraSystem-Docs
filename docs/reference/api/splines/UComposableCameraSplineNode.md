
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
| `float` | [`Duration`](#duration-4)  |  |
| `bool` | [`bLoop`](#bloop)  |  |
| `TObjectPtr< UComposableCameraInterpolatorBase >` | [`MoveInterpolator`](#moveinterpolator)  |  |
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

#### Duration { #duration-4 }

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
TObjectPtr< UComposableCameraInterpolatorBase > MoveInterpolator
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
|  | [`UComposableCameraSplineNode`](#ucomposablecamerasplinenode-1) `inline` |  |
| `void` | [`OnInitialize_Implementation`](#oninitialize_implementation-2) `virtual` |  |
| `void` | [`OnTickNode_Implementation`](#onticknode_implementation-3) `virtual` |  |
| `void` | [`GetPinDeclarations_Implementation`](#getpindeclarations_implementation-3) `virtual` `const` |  |
| `void` | [`DrawNodeDebug`](#drawnodedebug-2) `virtual` `const` | Called each frame when the `CCS.Debug.Viewport` CVar is enabled, for every node on the currently running camera. Override to draw world-space debug gizmos via `DrawDebugHelpers` (DrawDebugSphere, DrawDebugLine, etc.) that visualise this node's runtime state — e.g. a pivot sphere for PivotOffsetNode, a look-at line for LookAtNode, the collision trace for CollisionPushNode, a sampled spline path for SplineNode. |

---

#### UComposableCameraSplineNode { #ucomposablecamerasplinenode-1 }

`inline`

```cpp
inline UComposableCameraSplineNode()
```

---

#### OnInitialize_Implementation { #oninitialize_implementation-2 }

`virtual`

```cpp
virtual void OnInitialize_Implementation()
```

---

#### OnTickNode_Implementation { #onticknode_implementation-3 }

`virtual`

```cpp
virtual void OnTickNode_Implementation(float DeltaTime, const FComposableCameraPose & CurrentCameraPose, FComposableCameraPose & OutCameraPose)
```

---

#### GetPinDeclarations_Implementation { #getpindeclarations_implementation-3 }

`virtual` `const`

```cpp
virtual void GetPinDeclarations_Implementation(TArray< FComposableCameraNodePinDeclaration > & OutPins) const
```

---

#### DrawNodeDebug { #drawnodedebug-2 }

`virtual` `const`

```cpp
virtual void DrawNodeDebug(UWorld * World, bool bViewerIsOutsideCamera) const
```

Called each frame when the `CCS.Debug.Viewport` CVar is enabled, for every node on the currently running camera. Override to draw world-space debug gizmos via `DrawDebugHelpers` (DrawDebugSphere, DrawDebugLine, etc.) that visualise this node's runtime state — e.g. a pivot sphere for PivotOffsetNode, a look-at line for LookAtNode, the collision trace for CollisionPushNode, a sampled spline path for SplineNode.

Access the owning camera via `OwningCamera` and current-frame pin values via the usual `GetInputPinValue<T>()` / member-read path — this hook fires AFTER TickNode, so pin-backed UPROPERTYs still hold the resolved values from the most recent evaluation.

`bViewerIsOutsideCamera` mirrors the ticker's frustum-draw flag: true when the viewer is observing the camera from outside (F8 eject, SIE, or `CCS.Debug.Viewport.AlwaysShow`), false when the player is looking through the camera. Most gizmos (pivot spheres at distant characters, lines to look-at targets, spline polylines far in the world) can ignore this and draw unconditionally. Gizmos that sit AT the camera's own position (e.g. `CollisionPushNode`'s self-collision sphere) should gate on this bool so they don't hermetically seal the player inside the wireframe during live gameplay.

Default implementation does nothing. Compiled out in shipping builds.

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
