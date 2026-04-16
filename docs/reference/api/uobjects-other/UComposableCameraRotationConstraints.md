
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
| `TSoftObjectPtr< AActor >` | [`ActorForYawConstrain`](#actorforyawconstrain)  |  |
| `FVector` | [`VectorForYawConstrain`](#vectorforyawconstrain)  |  |
| `FVector2D` | [`YawRange`](#yawrange-1)  |  |
| `bool` | [`bConstrainPitch`](#bconstrainpitch)  |  |
| `EComposableCameraRotationConstrainType` | [`ConstrainPitchType`](#constrainpitchtype)  |  |
| `TSoftObjectPtr< AActor >` | [`ActorForPitchConstrain`](#actorforpitchconstrain)  |  |
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

#### ActorForYawConstrain { #actorforyawconstrain }

```cpp
TSoftObjectPtr< AActor > ActorForYawConstrain { nullptr }
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

#### ActorForPitchConstrain { #actorforpitchconstrain }

```cpp
TSoftObjectPtr< AActor > ActorForPitchConstrain { nullptr }
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
| `void` | [`OnTickNode_Implementation`](#onticknode_implementation-14) `virtual` |  |
| `void` | [`GetPinDeclarations_Implementation`](#getpindeclarations_implementation-14) `virtual` `const` |  |

---

#### OnTickNode_Implementation { #onticknode_implementation-14 }

`virtual`

```cpp
virtual void OnTickNode_Implementation(float DeltaTime, const FComposableCameraPose & CurrentCameraPose, FComposableCameraPose & OutCameraPose)
```

---

#### GetPinDeclarations_Implementation { #getpindeclarations_implementation-14 }

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
double FindTargetYawInRange(const double WorldCurrentYaw, const FVector2D & Vector2)
```

---

#### FindTargetPitchInRange { #findtargetpitchinrange }

```cpp
double FindTargetPitchInRange(const double WorldCurrentPitch, const FVector2D & Vector2)
```
