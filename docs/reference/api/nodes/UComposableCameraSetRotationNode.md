# UComposableCameraSetRotationNode { #ucomposablecamerasetrotationnode }

```cpp
#include <ComposableCameraSetRotationNode.h>
```

> **Inherits:** [`UComposableCameraCameraNodeBase`](../uobjects-other/UComposableCameraCameraNodeBase.md#ucomposablecameracameranodebase)

Node for replacing the current camera rotation from an actor forward vector, the direction between two actors, an explicit forward vector, or a literal rotator.

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `EComposableCameraSetRotationSource` | [`RotationSource`](#rotationsource) | Selects where the replacement rotation comes from. |
| `EComposableCameraActorInputSource` | [`RotationActorSource`](#rotationactorsource) | Selects whether the actor source is explicit or the controller's controlled pawn. |
| `TObjectPtr< AActor >` | [`RotationActor`](#rotationactor) | Actor whose forward vector defines the replacement rotation. |
| `EComposableCameraActorInputSource` | [`FirstActorSource`](#firstactorsource) | Selects whether FirstActor comes from an explicit actor or the controller's controlled pawn. |
| `TObjectPtr< AActor >` | [`FirstActor`](#firstactor) | First endpoint for FromTwoActors. |
| `EComposableCameraActorInputSource` | [`SecondActorSource`](#secondactorsource) | Selects whether SecondActor comes from an explicit actor or the controller's controlled pawn. |
| `TObjectPtr< AActor >` | [`SecondActor`](#secondactor) | Second endpoint for FromTwoActors. |
| `FVector` | [`RotationVector`](#rotationvector) | Forward vector used to build the replacement rotation. |
| `FRotator` | [`Rotation`](#rotation) | Literal replacement rotation. |
| `FRotator` | [`RotationOffset`](#rotationoffset) | Offset applied after the base rotation is resolved. Yaw is world-space; pitch and roll are local-space. |

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

#### FirstActorSource { #firstactorsource }

```cpp
EComposableCameraActorInputSource FirstActorSource { EComposableCameraActorInputSource::ExplicitActor }
```

Selects whether FirstActor comes from an explicit actor or the controller's controlled pawn.

---

#### FirstActor { #firstactor }

```cpp
TObjectPtr< AActor > FirstActor { nullptr }
```

First endpoint for FromTwoActors.

---

#### SecondActorSource { #secondactorsource }

```cpp
EComposableCameraActorInputSource SecondActorSource { EComposableCameraActorInputSource::ExplicitActor }
```

Selects whether SecondActor comes from an explicit actor or the controller's controlled pawn.

---

#### SecondActor { #secondactor }

```cpp
TObjectPtr< AActor > SecondActor { nullptr }
```

Second endpoint for FromTwoActors.

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

---

#### RotationOffset { #rotationoffset }

```cpp
FRotator RotationOffset { FRotator::ZeroRotator }
```

Offset applied after the base rotation is resolved. Yaw is world-space; pitch and roll are local-space.

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
