
# UComposableCameraScreenSpaceConstraintsNode { #ucomposablecamerascreenspaceconstraintsnode }

```cpp
#include <ComposableCameraScreenSpaceConstraintsNode.h>
```

> **Inherits:** [`UComposableCameraCameraNodeBase`](../uobjects-other/UComposableCameraCameraNodeBase.md#ucomposablecameracameranodebase)

Node for constraining a pivot position in screen using either translation or rotation.

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `TObjectPtr< AActor >` | [`PivotActor`](#pivotactor-8)  |  |
| `EComposableCameraScreenSpaceMethod` | [`Method`](#method-2)  |  |
| `FVector2D` | [`SafeZoneCenter`](#safezonecenter-1)  |  |
| `FVector2D` | [`SafeZoneWidth`](#safezonewidth-1)  |  |
| `FVector2D` | [`SafeZoneHeight`](#safezoneheight-1)  |  |

---

#### PivotActor { #pivotactor-8 }

```cpp
TObjectPtr< AActor > PivotActor
```

---

#### Method { #method-2 }

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
|  | [`UComposableCameraScreenSpaceConstraintsNode`](#ucomposablecamerascreenspaceconstraintsnode-1) `inline` |  |
| `void` | [`OnInitialize_Implementation`](#oninitialize_implementation-19) `virtual` |  |
| `void` | [`OnTickNode_Implementation`](#onticknode_implementation-27) `virtual` |  |
| `void` | [`GetPinDeclarations_Implementation`](#getpindeclarations_implementation-26) `virtual` `const` |  |
| `void` | [`DrawNodeDebug`](#drawnodedebug-14) `virtual` `const` | Called each frame when the `CCS.Debug.Viewport` CVar is enabled, for every node on the currently running camera. Override to draw world-space debug gizmos via `DrawDebugHelpers` (DrawDebugSphere, DrawDebugLine, etc.) that visualise this node's runtime state — e.g. a pivot sphere for PivotOffsetNode, a look-at line for LookAtNode, the collision trace for CollisionPushNode, a sampled spline path for SplineNode. |
| `void` | [`DrawNodeDebug2D`](#drawnodedebug2d-2) `virtual` `const` | 2D counterpart to DrawNodeDebug. Fires from a separate UDebugDrawService hook on the "Game" channel — which means it runs during PIE-possessed play (and standalone), NOT during F8 eject (editor viewport doesn't route through the game channel). That lines up with what 2D overlays are good for: screen-space debug that the player-eye perspective answers and an external view cannot (safe-zone rectangles, projected pivot markers, HUD-space gizmos). |

---

#### UComposableCameraScreenSpaceConstraintsNode { #ucomposablecamerascreenspaceconstraintsnode-1 }

`inline`

```cpp
inline UComposableCameraScreenSpaceConstraintsNode()
```

---

#### OnInitialize_Implementation { #oninitialize_implementation-19 }

`virtual`

```cpp
virtual void OnInitialize_Implementation()
```

---

#### OnTickNode_Implementation { #onticknode_implementation-27 }

`virtual`

```cpp
virtual void OnTickNode_Implementation(float DeltaTime, const FComposableCameraPose & CurrentCameraPose, FComposableCameraPose & OutCameraPose)
```

---

#### GetPinDeclarations_Implementation { #getpindeclarations_implementation-26 }

`virtual` `const`

```cpp
virtual void GetPinDeclarations_Implementation(TArray< FComposableCameraNodePinDeclaration > & OutPins) const
```

---

#### DrawNodeDebug { #drawnodedebug-14 }

`virtual` `const`

```cpp
virtual void DrawNodeDebug(UWorld * World, bool bViewerIsOutsideCamera) const
```

Called each frame when the `CCS.Debug.Viewport` CVar is enabled, for every node on the currently running camera. Override to draw world-space debug gizmos via `DrawDebugHelpers` (DrawDebugSphere, DrawDebugLine, etc.) that visualise this node's runtime state — e.g. a pivot sphere for PivotOffsetNode, a look-at line for LookAtNode, the collision trace for CollisionPushNode, a sampled spline path for SplineNode.

Access the owning camera via `OwningCamera` and current-frame pin values via the usual `GetInputPinValue<T>()` / member-read path — this hook fires AFTER TickNode, so pin-backed UPROPERTYs still hold the resolved values from the most recent evaluation.

`bViewerIsOutsideCamera` mirrors the ticker's frustum-draw flag: true when the viewer is observing the camera from outside (F8 eject, SIE, or `CCS.Debug.Viewport.AlwaysShow`), false when the player is looking through the camera. Most gizmos (pivot spheres at distant characters, lines to look-at targets, spline polylines far in the world) can ignore this and draw unconditionally. Gizmos that sit AT the camera's own position (e.g. `CollisionPushNode`'s self-collision sphere) should gate on this bool so they don't hermetically seal the player inside the wireframe during live gameplay.

Default implementation does nothing. Compiled out in shipping builds.

---

#### DrawNodeDebug2D { #drawnodedebug2d-2 }

`virtual` `const`

```cpp
virtual void DrawNodeDebug2D(UCanvas * Canvas, APlayerController * PC) const
```

2D counterpart to DrawNodeDebug. Fires from a separate UDebugDrawService hook on the "Game" channel — which means it runs during PIE-possessed play (and standalone), NOT during F8 eject (editor viewport doesn't route through the game channel). That lines up with what 2D overlays are good for: screen-space debug that the player-eye perspective answers and an external view cannot (safe-zone rectangles, projected pivot markers, HUD-space gizmos).

Canvas provides the 2D surface; PC is the local player controller whose view is being rendered (for ProjectWorldToScreen and aspect ratio queries). Either may be null in edge cases — always check.

Default implementation does nothing. Compiled out in shipping builds.

### Private Methods

| Return | Name | Description |
|--------|------|-------------|
| `FVector` | [`EnsureWithinBoundsTranslation`](#ensurewithinboundstranslation-1)  |  |
| `FRotator` | [`EnsureWithinBoundsRotation`](#ensurewithinboundsrotation-1)  |  |
| `std::pair< float, float >` | [`GetTanHalfHORAndAspectRatio`](#gettanhalfhorandaspectratio-1)  |  |
| `std::pair< float, float >` | [`CalibrateRotationOffsetNewton`](#calibraterotationoffsetnewton-1)  |  |
| `FVector` | [`GetCurrentPivot`](#getcurrentpivot-1) `const` |  |

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

`const`

```cpp
FVector GetCurrentPivot() const
```
