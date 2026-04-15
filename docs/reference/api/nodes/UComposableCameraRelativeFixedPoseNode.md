
# UComposableCameraRelativeFixedPoseNode { #ucomposablecamerarelativefixedposenode }

```cpp
#include <ComposableCameraRelativeFixedPoseNode.h>
```

> **Inherits:** [`UComposableCameraCameraNodeBase`](../uobjects-other/UComposableCameraCameraNodeBase.md#ucomposablecameracameranodebase)

Node for maintaining a fixed pose relative to some given transform.

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `EComposableCameraRelativeFixedPoseMethod` | [`Method`](#method-2)  |  |
| `FTransform` | [`RelativeTransform`](#relativetransform-1)  |  |
| `AActor *` | [`RelativeActor`](#relativeactor-1)  |  |
| `FName` | [`RelativeSocket`](#relativesocket-1)  |  |
| `FTransform` | [`TargetTransform`](#targettransform)  |  |

---

#### Method { #method-2 }

```cpp
EComposableCameraRelativeFixedPoseMethod Method
```

---

#### RelativeTransform { #relativetransform-1 }

```cpp
FTransform RelativeTransform
```

---

#### RelativeActor { #relativeactor-1 }

```cpp
AActor * RelativeActor
```

---

#### RelativeSocket { #relativesocket-1 }

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
| `void` | [`OnInitialize_Implementation`](#oninitialize_implementation-13) `virtual` |  |
| `void` | [`OnTickNode_Implementation`](#onticknode_implementation-17) `virtual` |  |
| `void` | [`GetPinDeclarations_Implementation`](#getpindeclarations_implementation-17) `virtual` `const` |  |

---

#### OnInitialize_Implementation { #oninitialize_implementation-13 }

`virtual`

```cpp
virtual void OnInitialize_Implementation()
```

---

#### OnTickNode_Implementation { #onticknode_implementation-17 }

`virtual`

```cpp
virtual void OnTickNode_Implementation(float DeltaTime, const FComposableCameraPose & CurrentCameraPose, FComposableCameraPose & OutCameraPose)
```

---

#### GetPinDeclarations_Implementation { #getpindeclarations_implementation-17 }

`virtual` `const`

```cpp
virtual void GetPinDeclarations_Implementation(TArray< FComposableCameraNodePinDeclaration > & OutPins) const
```

### Private Attributes

| Return | Name | Description |
|--------|------|-------------|
| `USkeletalMeshComponent *` | [`SkeletalMeshComponentForRelativeActor`](#skeletalmeshcomponentforrelativeactor-1)  |  |

---

#### SkeletalMeshComponentForRelativeActor { #skeletalmeshcomponentforrelativeactor-1 }

```cpp
USkeletalMeshComponent * SkeletalMeshComponentForRelativeActor { nullptr }
```
