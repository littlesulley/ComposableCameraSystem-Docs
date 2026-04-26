
# UComposableCameraPivotOffsetNode { #ucomposablecamerapivotoffsetnode }

```cpp
#include <ComposableCameraPivotOffsetNode.h>
```

> **Inherits:** [`UComposableCameraCameraNodeBase`](../uobjects-other/UComposableCameraCameraNodeBase.md#ucomposablecameracameranodebase)

Node for adjusting the pivot position by applying an offset in world/camera/actor local space. <br/>
If using camera space, the CurrentCameraPose parameter in the Tick function will be used. <br/>
@ InputParameter PivotOffsetType: In which space you'd like to apply offset, can be world, camera, or actor local. <br/>
@ InputParameter ActorForLocalSpace: The actor determining the local space if you choose actor local space. <br/>
@ InputParameter PivotOffset: The offset. <br/>
This node runs every tick.

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `FVector` | [`PivotPosition`](#pivotposition-1)  |  |
| `ECameraPivotOffset` | [`PivotOffsetType`](#pivotoffsettype)  |  |
| `TSoftObjectPtr< AActor >` | [`ActorForLocalSpace`](#actorforlocalspace)  |  |
| `FVector` | [`PivotOffset`](#pivotoffset-1)  |  |

---

#### PivotPosition { #pivotposition-1 }

```cpp
FVector PivotPosition { FVector::ZeroVector }
```

---

#### PivotOffsetType { #pivotoffsettype }

```cpp
ECameraPivotOffset PivotOffsetType = 
```

---

#### ActorForLocalSpace { #actorforlocalspace }

```cpp
TSoftObjectPtr< AActor > ActorForLocalSpace = nullptr
```

---

#### PivotOffset { #pivotoffset-1 }

```cpp
FVector PivotOffset = FVector::ZeroVector
```

### Public Methods

| Return | Name | Description |
|--------|------|-------------|
|  | [`UComposableCameraPivotOffsetNode`](#ucomposablecamerapivotoffsetnode-1) `inline` |  |
| `void` | [`OnInitialize_Implementation`](#oninitialize_implementation-6) `virtual` |  |
| `void` | [`OnTickNode_Implementation`](#onticknode_implementation-9) `virtual` |  |
| `void` | [`GetPinDeclarations_Implementation`](#getpindeclarations_implementation-9) `virtual` `const` |  |
| `void` | [`DrawNodeDebug`](#drawnodedebug-5) `virtual` `const` | Called each frame when the `CCS.Debug.Viewport` CVar is enabled, for every node on the currently running camera. Override to draw world-space debug gizmos via `DrawDebugHelpers` (DrawDebugSphere, DrawDebugLine, etc.) that visualise this node's runtime state — e.g. a pivot sphere for PivotOffsetNode, a look-at line for LookAtNode, the collision trace for CollisionPushNode, a sampled spline path for SplineNode. |

---

#### UComposableCameraPivotOffsetNode { #ucomposablecamerapivotoffsetnode-1 }

`inline`

```cpp
inline UComposableCameraPivotOffsetNode()
```

---

#### OnInitialize_Implementation { #oninitialize_implementation-6 }

`virtual`

```cpp
virtual void OnInitialize_Implementation()
```

---

#### OnTickNode_Implementation { #onticknode_implementation-9 }

`virtual`

```cpp
virtual void OnTickNode_Implementation(float DeltaTime, const FComposableCameraPose & CurrentCameraPose, FComposableCameraPose & OutCameraPose)
```

---

#### GetPinDeclarations_Implementation { #getpindeclarations_implementation-9 }

`virtual` `const`

```cpp
virtual void GetPinDeclarations_Implementation(TArray< FComposableCameraNodePinDeclaration > & OutPins) const
```

---

#### DrawNodeDebug { #drawnodedebug-5 }

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
| `FVector` | [`LastComputedPivot`](#lastcomputedpivot)  | Cache of the final post-offset pivot this frame, written in UpdatePivotOffset and read by DrawNodeDebug. Output pins are not re-readable by name so we keep a mirror; only present in non-shipping builds. |

---

#### LastComputedPivot { #lastcomputedpivot }

```cpp
FVector LastComputedPivot { FVector::ZeroVector }
```

Cache of the final post-offset pivot this frame, written in UpdatePivotOffset and read by DrawNodeDebug. Output pins are not re-readable by name so we keep a mirror; only present in non-shipping builds.

### Private Methods

| Return | Name | Description |
|--------|------|-------------|
| `void` | [`UpdatePivotOffset`](#updatepivotoffset)  |  |

---

#### UpdatePivotOffset { #updatepivotoffset }

```cpp
void UpdatePivotOffset(const FVector & InPivot, const FComposableCameraPose & CurrentCameraPose)
```
