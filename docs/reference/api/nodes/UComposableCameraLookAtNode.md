
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
| `void` | [`OnInitialize_Implementation`](#oninitialize_implementation) `virtual` |  |
| `void` | [`OnTickNode_Implementation`](#onticknode_implementation-1) `virtual` |  |
| `void` | [`GetPinDeclarations_Implementation`](#getpindeclarations_implementation-1) `virtual` `const` |  |

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
