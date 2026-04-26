
# UComposableCameraAutoRotateNode { #ucomposablecameraautorotatenode }

```cpp
#include <ComposableCameraAutoRotateNode.h>
```

> **Inherits:** [`UComposableCameraCameraNodeBase`](../uobjects-other/UComposableCameraCameraNodeBase.md#ucomposablecameracameranodebase)

Node for auto-rotating around a given "main direction." The main direction is supplied either as an explicit direction vector or by reading an actor's forward vector each frame, selected via DirectionMode. Both inputs are pins so they can be wired from upstream compute nodes or context parameters.

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `EComposableCameraAutoRotateDirectionMode` | [`DirectionMode`](#directionmode)  |  |
| `FVector` | [`MainDirection`](#maindirection)  |  |
| `TObjectPtr< AActor >` | [`PrimaryActor`](#primaryactor)  |  |
| `bool` | [`bInterruptOnUserInput`](#binterruptonuserinput)  |  |
| `FVector2D` | [`CameraRotationInput`](#camerarotationinput)  |  |
| `FVector2D` | [`YawRange`](#yawrange)  |  |
| `FVector2D` | [`PitchRange`](#pitchrange)  |  |
| `bool` | [`bYawOnly`](#byawonly)  |  |
| `float` | [`BeyondValidRangeCooldown`](#beyondvalidrangecooldown)  |  |
| `float` | [`InputInterruptCooldown`](#inputinterruptcooldown)  |  |
| `int32` | [`MaxCountAfterInputInterrupt`](#maxcountafterinputinterrupt)  |  |
| `TObjectPtr< UComposableCameraInterpolatorBase >` | [`RotateInterpolator`](#rotateinterpolator)  |  |

---

#### DirectionMode { #directionmode }

```cpp
EComposableCameraAutoRotateDirectionMode DirectionMode {  }
```

---

#### MainDirection { #maindirection }

```cpp
FVector MainDirection { FVector::ForwardVector }
```

---

#### PrimaryActor { #primaryactor }

```cpp
TObjectPtr< AActor > PrimaryActor
```

---

#### bInterruptOnUserInput { #binterruptonuserinput }

```cpp
bool bInterruptOnUserInput { true }
```

---

#### CameraRotationInput { #camerarotationinput }

```cpp
FVector2D CameraRotationInput { 0.f, 0.f }
```

---

#### YawRange { #yawrange }

```cpp
FVector2D YawRange { 0.f, 0.f }
```

---

#### PitchRange { #pitchrange }

```cpp
FVector2D PitchRange { 0.f, 0.f }
```

---

#### bYawOnly { #byawonly }

```cpp
bool bYawOnly { true }
```

---

#### BeyondValidRangeCooldown { #beyondvalidrangecooldown }

```cpp
float BeyondValidRangeCooldown { 0.f }
```

---

#### InputInterruptCooldown { #inputinterruptcooldown }

```cpp
float InputInterruptCooldown { 0.f }
```

---

#### MaxCountAfterInputInterrupt { #maxcountafterinputinterrupt }

```cpp
int32 MaxCountAfterInputInterrupt { -1 }
```

---

#### RotateInterpolator { #rotateinterpolator }

```cpp
TObjectPtr< UComposableCameraInterpolatorBase > RotateInterpolator
```

### Public Methods

| Return | Name | Description |
|--------|------|-------------|
|  | [`UComposableCameraAutoRotateNode`](#ucomposablecameraautorotatenode-1) `inline` |  |
| `void` | [`OnInitialize_Implementation`](#oninitialize_implementation-4) `virtual` |  |
| `void` | [`OnTickNode_Implementation`](#onticknode_implementation-6) `virtual` |  |
| `void` | [`GetPinDeclarations_Implementation`](#getpindeclarations_implementation-6) `virtual` `const` |  |

---

#### UComposableCameraAutoRotateNode { #ucomposablecameraautorotatenode-1 }

`inline`

```cpp
inline UComposableCameraAutoRotateNode()
```

---

#### OnInitialize_Implementation { #oninitialize_implementation-4 }

`virtual`

```cpp
virtual void OnInitialize_Implementation()
```

---

#### OnTickNode_Implementation { #onticknode_implementation-6 }

`virtual`

```cpp
virtual void OnTickNode_Implementation(float DeltaTime, const FComposableCameraPose & CurrentCameraPose, FComposableCameraPose & OutCameraPose)
```

---

#### GetPinDeclarations_Implementation { #getpindeclarations_implementation-6 }

`virtual` `const`

```cpp
virtual void GetPinDeclarations_Implementation(TArray< FComposableCameraNodePinDeclaration > & OutPins) const
```

### Private Attributes

| Return | Name | Description |
|--------|------|-------------|
| `TUniquePtr< TCameraInterpolator< TValueTypeWrapper< FRotator > > >` | [`Interpolator_T`](#interpolator_t-1)  |  |
| `bool` | [`bInAutoRotate`](#binautorotate)  |  |
| `float` | [`BeyondValidRangeCooldownRemaining`](#beyondvalidrangecooldownremaining)  |  |
| `float` | [`InputInterruptCooldownRemaining`](#inputinterruptcooldownremaining)  |  |
| `int32` | [`UsedCountAfterInputInterrupt`](#usedcountafterinputinterrupt)  |  |

---

#### Interpolator_T { #interpolator_t-1 }

```cpp
TUniquePtr< TCameraInterpolator< TValueTypeWrapper< FRotator > > > Interpolator_T
```

---

#### bInAutoRotate { #binautorotate }

```cpp
bool bInAutoRotate { false }
```

---

#### BeyondValidRangeCooldownRemaining { #beyondvalidrangecooldownremaining }

```cpp
float BeyondValidRangeCooldownRemaining { 0.f }
```

---

#### InputInterruptCooldownRemaining { #inputinterruptcooldownremaining }

```cpp
float InputInterruptCooldownRemaining { 0.f }
```

---

#### UsedCountAfterInputInterrupt { #usedcountafterinputinterrupt }

```cpp
int32 UsedCountAfterInputInterrupt { 0 }
```

### Private Methods

| Return | Name | Description |
|--------|------|-------------|
| `std::pair< bool, bool >` | [`CheckIfInValidRange`](#checkifinvalidrange)  |  |

---

#### CheckIfInValidRange { #checkifinvalidrange }

```cpp
std::pair< bool, bool > CheckIfInValidRange(const FVector2D & ValidRangeYaw, const FVector2D & ValidRangePitch, const FRotator & Rotation)
```
