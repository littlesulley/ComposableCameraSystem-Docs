
# UComposableCameraReceivePivotActorNode { #ucomposablecamerareceivepivotactornode }

```cpp
#include <ComposableCameraReceivePivotActorNode.h>
```

> **Inherits:** [`UComposableCameraCameraNodeBase`](../uobjects-other/UComposableCameraCameraNodeBase.md#ucomposablecameracameranodebase)

Reads a pivot actor's location and publishes it as the pivot position for downstream nodes. This node runs every tick.

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `TObjectPtr< AActor >` | [`PivotActor`](#pivotactor-7)  |  |
| `bool` | [`bUseBoneForPivot`](#buseboneforpivot)  |  |
| `FName` | [`BoneName`](#bonename-5)  |  |

---

#### PivotActor { #pivotactor-7 }

```cpp
TObjectPtr< AActor > PivotActor
```

---

#### bUseBoneForPivot { #buseboneforpivot }

```cpp
bool bUseBoneForPivot { false }
```

---

#### BoneName { #bonename-5 }

```cpp
FName BoneName
```

### Public Methods

| Return | Name | Description |
|--------|------|-------------|
|  | [`UComposableCameraReceivePivotActorNode`](#ucomposablecamerareceivepivotactornode-1) `inline` |  |
| `void` | [`OnInitialize_Implementation`](#oninitialize_implementation-17) `virtual` |  |
| `void` | [`OnTickNode_Implementation`](#onticknode_implementation-25) `virtual` |  |
| `void` | [`GetPinDeclarations_Implementation`](#getpindeclarations_implementation-23) `virtual` `const` |  |
| `EComposableCameraNodePatchCompatibility` | [`GetPatchCompatibility_Implementation`](#getpatchcompatibility_implementation-3) `virtual` `const` `inline` |  |
| `void` | [`DrawNodeDebug`](#drawnodedebug-12) `virtual` `const` | Called each frame when the `CCS.Debug.Viewport` CVar is enabled, for every node on the currently running camera. Override to draw world-space debug gizmos via `DrawDebugHelpers` (DrawDebugSphere, DrawDebugLine, etc.) that visualise this node's runtime state — e.g. a pivot sphere for PivotOffsetNode, a look-at line for LookAtNode, the collision trace for CollisionPushNode, a sampled spline path for SplineNode. |

---

#### UComposableCameraReceivePivotActorNode { #ucomposablecamerareceivepivotactornode-1 }

`inline`

```cpp
inline UComposableCameraReceivePivotActorNode()
```

---

#### OnInitialize_Implementation { #oninitialize_implementation-17 }

`virtual`

```cpp
virtual void OnInitialize_Implementation()
```

---

#### OnTickNode_Implementation { #onticknode_implementation-25 }

`virtual`

```cpp
virtual void OnTickNode_Implementation(float DeltaTime, const FComposableCameraPose & CurrentCameraPose, FComposableCameraPose & OutCameraPose)
```

---

#### GetPinDeclarations_Implementation { #getpindeclarations_implementation-23 }

`virtual` `const`

```cpp
virtual void GetPinDeclarations_Implementation(TArray< FComposableCameraNodePinDeclaration > & OutPins) const
```

---

#### GetPatchCompatibility_Implementation { #getpatchcompatibility_implementation-3 }

`virtual` `const` `inline`

```cpp
virtual inline EComposableCameraNodePatchCompatibility GetPatchCompatibility_Implementation() const
```

---

#### DrawNodeDebug { #drawnodedebug-12 }

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
| `USkeletalMeshComponent *` | [`SkeletalMeshComponentForPivotActor`](#skeletalmeshcomponentforpivotactor-1)  |  |

---

#### SkeletalMeshComponentForPivotActor { #skeletalmeshcomponentforpivotactor-1 }

```cpp
USkeletalMeshComponent * SkeletalMeshComponentForPivotActor { nullptr }
```
