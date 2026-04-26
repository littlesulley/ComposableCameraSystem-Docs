
# UComposableCameraPivotRotateNode { #ucomposablecamerapivotrotatenode }

```cpp
#include <ComposableCameraPivotRotateNode.h>
```

> **Inherits:** [`UComposableCameraCameraNodeBase`](../uobjects-other/UComposableCameraCameraNodeBase.md#ucomposablecameracameranodebase)

Synchronises the camera's rotation to a pivot actor's world rotation, with an authored offset and an optional rotator interpolator for damping.

Useful for vehicle / mount / vehicle-cockpit cameras where the camera should adopt the rig's heading (and optionally pitch / roll) but with a fixed relative offset (e.g. a slight downward tilt) and a smooth catch-up rather than a hard lock.

Compose semantics: target rotation is `PivotActor.Quat * RotationOffset.Quat`, i.e. the offset is applied in the pivot's LOCAL space — equivalent to authoring a child component attached to PivotActor with that relative rotation. This avoids the gimbal artifacts a raw FRotator add produces when the pivot has non-trivial pitch / roll.

@InputParameter PivotActor Source actor whose world rotation drives the target each frame. @InputParameter RotationOffset Local-space offset added on top of the pivot rotation.

`Interpolator` is an Instanced subobject — its inner properties surface as pins automatically via the base class's subobject-pin pipeline; no manual pin declaration needed.

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `TObjectPtr< AActor >` | [`PivotActor`](#pivotactor-2)  |  |
| `FRotator` | [`RotationOffset`](#rotationoffset)  |  |
| `TObjectPtr< UComposableCameraInterpolatorBase >` | [`Interpolator`](#interpolator-2)  |  |

---

#### PivotActor { #pivotactor-2 }

```cpp
TObjectPtr< AActor > PivotActor
```

---

#### RotationOffset { #rotationoffset }

```cpp
FRotator RotationOffset { FRotator::ZeroRotator }
```

---

#### Interpolator { #interpolator-2 }

```cpp
TObjectPtr< UComposableCameraInterpolatorBase > Interpolator
```

### Public Methods

| Return | Name | Description |
|--------|------|-------------|
|  | [`UComposableCameraPivotRotateNode`](#ucomposablecamerapivotrotatenode-1) `inline` |  |
| `void` | [`OnInitialize_Implementation`](#oninitialize_implementation-7) `virtual` |  |
| `void` | [`OnTickNode_Implementation`](#onticknode_implementation-10) `virtual` |  |
| `void` | [`GetPinDeclarations_Implementation`](#getpindeclarations_implementation-10) `virtual` `const` |  |

---

#### UComposableCameraPivotRotateNode { #ucomposablecamerapivotrotatenode-1 }

`inline`

```cpp
inline UComposableCameraPivotRotateNode()
```

---

#### OnInitialize_Implementation { #oninitialize_implementation-7 }

`virtual`

```cpp
virtual void OnInitialize_Implementation()
```

---

#### OnTickNode_Implementation { #onticknode_implementation-10 }

`virtual`

```cpp
virtual void OnTickNode_Implementation(float DeltaTime, const FComposableCameraPose & CurrentCameraPose, FComposableCameraPose & OutCameraPose)
```

---

#### GetPinDeclarations_Implementation { #getpindeclarations_implementation-10 }

`virtual` `const`

```cpp
virtual void GetPinDeclarations_Implementation(TArray< FComposableCameraNodePinDeclaration > & OutPins) const
```

### Private Attributes

| Return | Name | Description |
|--------|------|-------------|
| `TUniquePtr< TCameraInterpolator< TValueTypeWrapper< FRotator > > >` | [`Interpolator_T`](#interpolator_t-2)  |  |

---

#### Interpolator_T { #interpolator_t-2 }

```cpp
TUniquePtr< TCameraInterpolator< TValueTypeWrapper< FRotator > > > Interpolator_T
```
