
# UComposableCameraRelativeFixedPoseNode { #ucomposablecamerarelativefixedposenode }

```cpp
#include <ComposableCameraRelativeFixedPoseNode.h>
```

> **Inherits:** [`UComposableCameraCameraNodeBase`](../uobjects-other/UComposableCameraCameraNodeBase.md#ucomposablecameracameranodebase)

Node for maintaining a fixed pose relative to some given transform.

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `EComposableCameraRelativeFixedPoseMethod` | [`Method`](#method-1)  |  |
| `FTransform` | [`RelativeTransform`](#relativetransform)  |  |
| `AActor *` | [`RelativeActor`](#relativeactor)  |  |
| `FName` | [`RelativeSocket`](#relativesocket)  |  |
| `FTransform` | [`TargetTransform`](#targettransform)  |  |

---

#### Method { #method-1 }

```cpp
EComposableCameraRelativeFixedPoseMethod Method
```

---

#### RelativeTransform { #relativetransform }

```cpp
FTransform RelativeTransform
```

---

#### RelativeActor { #relativeactor }

```cpp
AActor * RelativeActor
```

---

#### RelativeSocket { #relativesocket }

```cpp
FName RelativeSocket
```

---

#### TargetTransform { #targettransform }

```cpp
FTransform TargetTransform
```

### Public Methods

| Return | Name | Description |
|--------|------|-------------|
| `void` | [`OnInitialize_Implementation`](#oninitialize_implementation-12) `virtual` |  |
| `void` | [`OnTickNode_Implementation`](#onticknode_implementation-20) `virtual` |  |
| `void` | [`GetPinDeclarations_Implementation`](#getpindeclarations_implementation-18) `virtual` `const` |  |

---

#### OnInitialize_Implementation { #oninitialize_implementation-12 }

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

#### GetPinDeclarations_Implementation { #getpindeclarations_implementation-18 }

`virtual` `const`

```cpp
virtual void GetPinDeclarations_Implementation(TArray< FComposableCameraNodePinDeclaration > & OutPins) const
```

### Private Attributes

| Return | Name | Description |
|--------|------|-------------|
| `USkeletalMeshComponent *` | [`SkeletalMeshComponentForRelativeActor`](#skeletalmeshcomponentforrelativeactor)  |  |

---

#### SkeletalMeshComponentForRelativeActor { #skeletalmeshcomponentforrelativeactor }

```cpp
USkeletalMeshComponent * SkeletalMeshComponentForRelativeActor { nullptr }
```
