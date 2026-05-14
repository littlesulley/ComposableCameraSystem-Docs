
# UComposableCameraRotationConstraints { #ucomposablecamerarotationconstraints }

```cpp
#include <ComposableCameraRotationConstraints.h>
```

> **Inherits:** [`UComposableCameraCameraNodeBase`](UComposableCameraCameraNodeBase.md#ucomposablecameracameranodebase)

Node for constraining rotation's yaw or pitch. <br/>
 @ InputParameter bConstrainYaw: Whether to enable yaw constraint. <br/>
 @ InputParameter ConstrainYawType: Constrain yaw type, choose between WorldSpace, ActorSpace and VectorSpace. <br/>
 @ InputParameter ActorForYawConstrain: Reference actor when ActorSpace is used. Its transform will be used as the reference frame. <br/>
 @ InputParameter VectorForYawConstrain: Reference vector when VectorSpace is used. It will serve as the forward vector of the reference frame. <br/>
 @ InputParameter YawRange: Yaw range in the reference frame. Use the world space, actor space or vector space as the reference frame. <br/>
 @ InputParameter bConstrainPitch: Whether to enable pitch constraint. <br/>
 @ InputParameter ConstrainPitchType: Constrain pitch type, choose between WorldSpace, ActorSpace and VectorSpace. <br/>
 @ InputParameter ActorForPitchConstrain: Reference actor when ActorSpace is used. Its transform will be used as the reference frame. <br/>
 @ InputParameter VectorForPitchConstrain: Reference vector when VectorSpace is used. It will serve as the forward vector of the reference frame. <br/>
 @ InputParameter PitchRange: Pitch range in the reference frame. Use the world space, actor space or vector space as the reference frame.

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `bool` | [`bConstrainYaw`](#bconstrainyaw)  |  |
| `EComposableCameraRotationConstrainType` | [`ConstrainYawType`](#constrainyawtype)  |  |
| `EComposableCameraActorInputSource` | [`ActorForYawConstrainSource`](#actorforyawconstrainsource)  |  |
| `TObjectPtr< AActor >` | [`ActorForYawConstrain`](#actorforyawconstrain)  |  |
| `FVector` | [`VectorForYawConstrain`](#vectorforyawconstrain)  |  |
| `FVector2D` | [`YawRange`](#yawrange-1)  |  |
| `bool` | [`bConstrainPitch`](#bconstrainpitch)  |  |
| `EComposableCameraRotationConstrainType` | [`ConstrainPitchType`](#constrainpitchtype)  |  |
| `EComposableCameraActorInputSource` | [`ActorForPitchConstrainSource`](#actorforpitchconstrainsource)  |  |
| `TObjectPtr< AActor >` | [`ActorForPitchConstrain`](#actorforpitchconstrain)  |  |
| `FVector` | [`VectorForPitchConstrain`](#vectorforpitchconstrain)  |  |
| `FVector2D` | [`PitchRange`](#pitchrange-1)  |  |

---

#### bConstrainYaw { #bconstrainyaw }

```cpp
bool bConstrainYaw { false }
```

---

#### ConstrainYawType { #constrainyawtype }

```cpp
EComposableCameraRotationConstrainType ConstrainYawType {  }
```

---

#### ActorForYawConstrainSource { #actorforyawconstrainsource }

```cpp
EComposableCameraActorInputSource ActorForYawConstrainSource { EComposableCameraActorInputSource::ExplicitActor }
```

Selects whether yaw actor-space constraints use an explicit actor or the controller-controlled pawn owned by the camera manager.

---

#### ActorForYawConstrain { #actorforyawconstrain }

```cpp
TObjectPtr< AActor > ActorForYawConstrain { nullptr }
```

---

#### VectorForYawConstrain { #vectorforyawconstrain }

```cpp
FVector VectorForYawConstrain { FVector::ForwardVector }
```

---

#### YawRange { #yawrange-1 }

```cpp
FVector2D YawRange { FVector2D {-180., 180.} }
```

---

#### bConstrainPitch { #bconstrainpitch }

```cpp
bool bConstrainPitch { true }
```

---

#### ConstrainPitchType { #constrainpitchtype }

```cpp
EComposableCameraRotationConstrainType ConstrainPitchType {  }
```

---

#### ActorForPitchConstrainSource { #actorforpitchconstrainsource }

```cpp
EComposableCameraActorInputSource ActorForPitchConstrainSource { EComposableCameraActorInputSource::ExplicitActor }
```

Selects whether pitch actor-space constraints use an explicit actor or the controller-controlled pawn owned by the camera manager.

---

#### ActorForPitchConstrain { #actorforpitchconstrain }

```cpp
TObjectPtr< AActor > ActorForPitchConstrain { nullptr }
```

---

#### VectorForPitchConstrain { #vectorforpitchconstrain }

```cpp
FVector VectorForPitchConstrain { FVector::ForwardVector }
```

---

#### PitchRange { #pitchrange-1 }

```cpp
FVector2D PitchRange { FVector2D {-70., 70.} }
```

### Public Methods

| Return | Name | Description |
|--------|------|-------------|
|  | [`UComposableCameraRotationConstraints`](#ucomposablecamerarotationconstraints-1) `inline` |  |
| `void` | [`OnTickNode_Implementation`](#onticknode_implementation-20) `virtual` |  |
| `void` | [`GetPinDeclarations_Implementation`](#getpindeclarations_implementation-19) `virtual` `const` |  |

---

#### UComposableCameraRotationConstraints { #ucomposablecamerarotationconstraints-1 }

`inline`

```cpp
inline UComposableCameraRotationConstraints()
```

---

#### OnTickNode_Implementation { #onticknode_implementation-20 }

`virtual`

```cpp
virtual void OnTickNode_Implementation(float DeltaTime, const FComposableCameraPose & CurrentCameraPose, FComposableCameraPose & OutCameraPose)
```

---

#### GetPinDeclarations_Implementation { #getpindeclarations_implementation-19 }

`virtual` `const`

```cpp
virtual void GetPinDeclarations_Implementation(TArray< FComposableCameraNodePinDeclaration > & OutPins) const
```

### Private Methods

| Return | Name | Description |
|--------|------|-------------|
| `double` | [`FindTargetYawInRange`](#findtargetyawinrange)  |  |
| `double` | [`FindTargetPitchInRange`](#findtargetpitchinrange)  |  |

---

#### FindTargetYawInRange { #findtargetyawinrange }

```cpp
double FindTargetYawInRange(double WorldCurrentYaw, double WorldPivotYaw, const FVector2D & PivotSpaceYawRange)
```

---

#### FindTargetPitchInRange { #findtargetpitchinrange }

```cpp
double FindTargetPitchInRange(const double WorldCurrentPitch, const FVector2D & Vector2)
```
