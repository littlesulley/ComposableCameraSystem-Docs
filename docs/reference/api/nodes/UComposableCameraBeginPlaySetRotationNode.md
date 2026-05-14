
# UComposableCameraBeginPlaySetRotationNode { #ucomposablecamerabeginplaysetrotationnode }

```cpp
#include <ComposableCameraSetRotationNode.h>
```

> **Inherits:** [`UComposableCameraComputeNodeBase`](../uobjects-other/UComposableCameraComputeNodeBase.md#ucomposablecameracomputenodebase)

Compute node that sets the initial camera rotation from an actor forward vector, an explicit forward vector, or a literal rotator during BeginPlay.

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `EComposableCameraSetRotationSource` | [`RotationSource`](#rotationsource-1) | Selects where the replacement rotation comes from. |
| `EComposableCameraActorInputSource` | [`RotationActorSource`](#rotationactorsource-1) | Selects whether the actor source is explicit or the controller's controlled pawn. |
| `TObjectPtr< AActor >` | [`RotationActor`](#rotationactor-1) | Actor whose forward vector defines the replacement rotation. |
| `FVector` | [`RotationVector`](#rotationvector-1) | Forward vector used to build the replacement rotation. |
| `FRotator` | [`Rotation`](#rotation-1) | Literal replacement rotation. |

---

#### RotationSource { #rotationsource-1 }

```cpp
EComposableCameraSetRotationSource RotationSource { EComposableCameraSetRotationSource::FromRotator }
```

Selects where the replacement rotation comes from.

---

#### RotationActorSource { #rotationactorsource-1 }

```cpp
EComposableCameraActorInputSource RotationActorSource { EComposableCameraActorInputSource::ExplicitActor }
```

Selects whether the actor source is explicit or the controller's controlled pawn.

---

#### RotationActor { #rotationactor-1 }

```cpp
TObjectPtr< AActor > RotationActor { nullptr }
```

Actor whose forward vector defines the replacement rotation.

---

#### RotationVector { #rotationvector-1 }

```cpp
FVector RotationVector { FVector::ForwardVector }
```

Forward vector used to build the replacement rotation.

---

#### Rotation { #rotation-1 }

```cpp
FRotator Rotation { FRotator::ZeroRotator }
```

Literal replacement rotation.

### Public Methods

| Return | Name | Description |
|--------|------|-------------|
|  | [`UComposableCameraBeginPlaySetRotationNode`](#ucomposablecamerabeginplaysetrotationnode-1) `inline` |  |
| `void` | [`ExecuteBeginPlay`](#executebeginplay-2) `virtual` | Execute this compute node's one-shot work. |
| `void` | [`GetPinDeclarations_Implementation`](#getpindeclarations_implementation-1) `virtual` `const` |  |

---

#### UComposableCameraBeginPlaySetRotationNode { #ucomposablecamerabeginplaysetrotationnode-1 }

`inline`

```cpp
inline UComposableCameraBeginPlaySetRotationNode()
```

---

#### ExecuteBeginPlay { #executebeginplay-2 }

`virtual`

```cpp
virtual void ExecuteBeginPlay()
```

Execute this compute node's one-shot work.

This node resolves the requested rotation source, then writes the owning camera's `CameraPose.Rotation` and `LastFrameCameraPose.Rotation` before the first `TickCamera`.

---

#### GetPinDeclarations_Implementation { #getpindeclarations_implementation-1 }

`virtual` `const`

```cpp
virtual void GetPinDeclarations_Implementation(TArray< FComposableCameraNodePinDeclaration > & OutPins) const
```
