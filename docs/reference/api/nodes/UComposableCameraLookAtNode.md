
# UComposableCameraLookAtNode { #ucomposablecameralookatnode }

```cpp
#include <ComposableCameraLookAtNode.h>
```

> **Inherits:** [`UComposableCameraCameraNodeBase`](../uobjects-other/UComposableCameraCameraNodeBase.md#ucomposablecameracameranodebase)

Node for looking at some target position.

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `EComposableCameraLookAtType` | [`LookAtType`](#lookattype)  |  |
| `FVector` | [`LookAtPosition`](#lookatposition)  |  |
| `TObjectPtr< AActor >` | [`LookAtActor`](#lookatactor)  |  |
| `FName` | [`LookAtSocket`](#lookatsocket)  |  |
| `EComposableCameraLookAtConstraintType` | [`LookAtConstraintType`](#lookatconstrainttype)  |  |
| `float` | [`SoftLookAtRange`](#softlookatrange)  |  |
| `float` | [`SoftLookAtWeight`](#softlookatweight)  |  |
| `UComposableCameraInterpolatorBase *` | [`SoftLookAtInterpolator`](#softlookatinterpolator)  |  |

---

#### LookAtType { #lookattype }

```cpp
EComposableCameraLookAtType LookAtType
```

---

#### LookAtPosition { #lookatposition }

```cpp
FVector LookAtPosition
```

---

#### LookAtActor { #lookatactor }

```cpp
TObjectPtr< AActor > LookAtActor
```

---

#### LookAtSocket { #lookatsocket }

```cpp
FName LookAtSocket
```

---

#### LookAtConstraintType { #lookatconstrainttype }

```cpp
EComposableCameraLookAtConstraintType LookAtConstraintType
```

---

#### SoftLookAtRange { #softlookatrange }

```cpp
float SoftLookAtRange { 20.f }
```

---

#### SoftLookAtWeight { #softlookatweight }

```cpp
float SoftLookAtWeight { 0.2f }
```

---

#### SoftLookAtInterpolator { #softlookatinterpolator }

```cpp
UComposableCameraInterpolatorBase * SoftLookAtInterpolator { nullptr }
```

### Public Methods

| Return | Name | Description |
|--------|------|-------------|
|  | [`UComposableCameraLookAtNode`](#ucomposablecameralookatnode-1) `inline` |  |
| `void` | [`OnInitialize_Implementation`](#oninitialize_implementation) `virtual` |  |
| `void` | [`OnTickNode_Implementation`](#onticknode_implementation-1) `virtual` |  |
| `void` | [`GetPinDeclarations_Implementation`](#getpindeclarations_implementation-1) `virtual` `const` |  |
| `void` | [`DrawNodeDebug`](#drawnodedebug) `virtual` `const` | Called each frame when the `CCS.Debug.Viewport` CVar is enabled, for every node on the currently running camera. Override to draw world-space debug gizmos via `DrawDebugHelpers` (DrawDebugSphere, DrawDebugLine, etc.) that visualise this node's runtime state — e.g. a pivot sphere for PivotOffsetNode, a look-at line for LookAtNode, the collision trace for CollisionPushNode, a sampled spline path for SplineNode. |

---

#### UComposableCameraLookAtNode { #ucomposablecameralookatnode-1 }

`inline`

```cpp
inline UComposableCameraLookAtNode()
```

---

#### OnInitialize_Implementation { #oninitialize_implementation }

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

---

#### DrawNodeDebug { #drawnodedebug }

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
| `USkeletalMeshComponent *` | [`SkeletalMeshComponentForLookAtActor`](#skeletalmeshcomponentforlookatactor)  |  |
| `TUniquePtr< TCameraInterpolator< TValueTypeWrapper< FRotator > > >` | [`Interpolator_T`](#interpolator_t)  |  |

---

#### SkeletalMeshComponentForLookAtActor { #skeletalmeshcomponentforlookatactor }

```cpp
USkeletalMeshComponent * SkeletalMeshComponentForLookAtActor { nullptr }
```

---

#### Interpolator_T { #interpolator_t }

```cpp
TUniquePtr< TCameraInterpolator< TValueTypeWrapper< FRotator > > > Interpolator_T
```
