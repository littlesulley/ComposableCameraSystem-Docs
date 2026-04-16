
# UComposableCameraAutoRotateNode { #ucomposablecameraautorotatenode }

```cpp
#include <ComposableCameraAutoRotateNode.h>
```

> **Inherits:** [`UComposableCameraCameraNodeBase`](../uobjects-other/UComposableCameraCameraNodeBase.md#ucomposablecameracameranodebase)

Node for auto-rotating around a given "main direction." The main direction is supplied through the MainDirection input pin, typically wired from an upstream node (e.g. a compute node that reads character forward vector) or set as a context parameter override.

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `FVector` | [`MainDirection`](#maindirection)  |  |
| `FVector2D` | [`CameraRotationInput`](#camerarotationinput)  |  |
| `FVector2D` | [`YawRange`](#yawrange)  |  |
| `FVector2D` | [`PitchRange`](#pitchrange)  |  |
| `bool` | [`bYawOnly`](#byawonly)  |  |
| `float` | [`BeyondValidRangeCooldown`](#beyondvalidrangecooldown)  |  |
| `float` | [`InputInterruptCooldown`](#inputinterruptcooldown)  |  |
| `int32` | [`MaxCountAfterInputInterrupt`](#maxcountafterinputinterrupt)  |  |
| `TObjectPtr< UComposableCameraInterpolatorBase >` | [`RotateInterpolatorForYaw`](#rotateinterpolatorforyaw)  |  |
| `TObjectPtr< UComposableCameraInterpolatorBase >` | [`RotateInterpolatorForPitch`](#rotateinterpolatorforpitch)  |  |

---

#### MainDirection { #maindirection }

```cpp
FVector MainDirection { FVector::ForwardVector }
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

#### RotateInterpolatorForYaw { #rotateinterpolatorforyaw }

```cpp
TObjectPtr< UComposableCameraInterpolatorBase > RotateInterpolatorForYaw
```

---

#### RotateInterpolatorForPitch { #rotateinterpolatorforpitch }

```cpp
TObjectPtr< UComposableCameraInterpolatorBase > RotateInterpolatorForPitch
```

### Public Methods

| Return | Name | Description |
|--------|------|-------------|
| `void` | [`OnInitialize_Implementation`](#oninitialize_implementation-2) `virtual` |  |
| `void` | [`OnTickNode_Implementation`](#onticknode_implementation-4) `virtual` |  |
| `void` | [`GetPinDeclarations_Implementation`](#getpindeclarations_implementation-4) `virtual` `const` |  |

---

#### OnInitialize_Implementation { #oninitialize_implementation-2 }

`virtual`

```cpp
virtual void OnInitialize_Implementation()
```

---

#### OnTickNode_Implementation { #onticknode_implementation-4 }

`virtual`

```cpp
virtual void OnTickNode_Implementation(float DeltaTime, const FComposableCameraPose & CurrentCameraPose, FComposableCameraPose & OutCameraPose)
```

---

#### GetPinDeclarations_Implementation { #getpindeclarations_implementation-4 }

`virtual` `const`

```cpp
virtual void GetPinDeclarations_Implementation(TArray< FComposableCameraNodePinDeclaration > & OutPins) const
```

### Private Attributes

| Return | Name | Description |
|--------|------|-------------|
| `TUniquePtr< TCameraInterpolator< TValueTypeWrapper< double > > >` | [`InterpolatorYaw_T`](#interpolatoryaw_t)  |  |
| `TUniquePtr< TCameraInterpolator< TValueTypeWrapper< double > > >` | [`InterpolatorPitch_T`](#interpolatorpitch_t)  |  |
| `bool` | [`bInAutoRotate`](#binautorotate)  |  |
| `float` | [`BeyondValidRangeCooldownRemaining`](#beyondvalidrangecooldownremaining)  |  |
| `float` | [`InputInterruptCooldownRemaining`](#inputinterruptcooldownremaining)  |  |
| `int32` | [`UsedCountAfterInputInterrupt`](#usedcountafterinputinterrupt)  |  |

---

#### InterpolatorYaw_T { #interpolatoryaw_t }

```cpp
TUniquePtr< TCameraInterpolator< TValueTypeWrapper< double > > > InterpolatorYaw_T
```

---

#### InterpolatorPitch_T { #interpolatorpitch_t }

```cpp
TUniquePtr< TCameraInterpolator< TValueTypeWrapper< double > > > InterpolatorPitch_T
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
