
# UComposableCameraSetRotationNode { #ucomposablecamerasetrotationnode }

```cpp
#include <ComposableCameraSetRotationNode.h>
```

> **Inherits:** [`UComposableCameraCameraNodeBase`](../uobjects-other/UComposableCameraCameraNodeBase.md#ucomposablecameracameranodebase)

Node for replacing the current camera rotation from an actor forward vector, an explicit forward vector, or a literal rotator.

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `EComposableCameraSetRotationSource` | [`RotationSource`](#rotationsource) | Selects where the replacement rotation comes from. |
| `EComposableCameraActorInputSource` | [`RotationActorSource`](#rotationactorsource) | Selects whether the actor source is explicit or the controller's controlled pawn. |
| `TObjectPtr< AActor >` | [`RotationActor`](#rotationactor) | Actor whose forward vector defines the replacement rotation. |
| `FVector` | [`RotationVector`](#rotationvector) | Forward vector used to build the replacement rotation. |
| `FRotator` | [`Rotation`](#rotation) | Literal replacement rotation. |

---

#### RotationSource { #rotationsource }

```cpp
EComposableCameraSetRotationSource RotationSource { EComposableCameraSetRotationSource::FromRotator }
```

Selects where the replacement rotation comes from.

---

#### RotationActorSource { #rotationactorsource }

```cpp
EComposableCameraActorInputSource RotationActorSource { EComposableCameraActorInputSource::ExplicitActor }
```

Selects whether the actor source is explicit or the controller's controlled pawn.

---

#### RotationActor { #rotationactor }

```cpp
TObjectPtr< AActor > RotationActor { nullptr }
```

Actor whose forward vector defines the replacement rotation.

---

#### RotationVector { #rotationvector }

```cpp
FVector RotationVector { FVector::ForwardVector }
```

Forward vector used to build the replacement rotation.

---

#### Rotation { #rotation }

```cpp
FRotator Rotation { FRotator::ZeroRotator }
```

Literal replacement rotation.

### Public Methods

| Return | Name | Description |
|--------|------|-------------|
|  | [`UComposableCameraSetRotationNode`](#ucomposablecamerasetrotationnode-1) `inline` |  |
| `void` | [`OnTickNode_Implementation`](#onticknode_implementation) `virtual` |  |
| `void` | [`GetPinDeclarations_Implementation`](#getpindeclarations_implementation) `virtual` `const` |  |

---

#### UComposableCameraSetRotationNode { #ucomposablecamerasetrotationnode-1 }

`inline`

```cpp
inline UComposableCameraSetRotationNode()
```

---

#### OnTickNode_Implementation { #onticknode_implementation }

`virtual`

```cpp
virtual void OnTickNode_Implementation(float DeltaTime, const FComposableCameraPose & CurrentCameraPose, FComposableCameraPose & OutCameraPose)
```

---

#### GetPinDeclarations_Implementation { #getpindeclarations_implementation }

`virtual` `const`

```cpp
virtual void GetPinDeclarations_Implementation(TArray< FComposableCameraNodePinDeclaration > & OutPins) const
```
