
# UComposableCameraResetPitchAction { #ucomposablecameraresetpitchaction }

```cpp
#include <ComposableCameraResetPitchAction.h>
```

> **Inherits:** [`UComposableCameraActionBase`](UComposableCameraActionBase.md#ucomposablecameraactionbase)

This action smoothly resets pitch to a target value. If the camera rotates to the target rotation or there is user input, the action will expire.

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `float` | [`Pitch`](#pitch-1)  |  |
| `class UInputAction *` | [`RotateAction`](#rotateaction-1)  |  |
| `UComposableCameraInterpolatorBase *` | [`Interpolator`](#interpolator-2)  |  |
| `float` | [`InterpSpeed`](#interpspeed-1)  |  |

---

#### Pitch { #pitch-1 }

```cpp
float Pitch { 0.f }
```

---

#### RotateAction { #rotateaction-1 }

```cpp
class UInputAction * RotateAction { nullptr }
```

---

#### Interpolator { #interpolator-2 }

```cpp
UComposableCameraInterpolatorBase * Interpolator { nullptr }
```

---

#### InterpSpeed { #interpspeed-1 }

```cpp
float InterpSpeed { 1.f }
```

### Public Methods

| Return | Name | Description |
|--------|------|-------------|
|  | [`UComposableCameraResetPitchAction`](#ucomposablecameraresetpitchaction-1)  |  |
| `bool` | [`CanExecute_Implementation`](#canexecute_implementation-3) `virtual` |  |
| `void` | [`OnExecute_Implementation`](#onexecute_implementation-3) `virtual` |  |

---

#### UComposableCameraResetPitchAction { #ucomposablecameraresetpitchaction-1 }

```cpp
UComposableCameraResetPitchAction(const FObjectInitializer & ObjectInitializer)
```

---

#### CanExecute_Implementation { #canexecute_implementation-3 }

`virtual`

```cpp
virtual bool CanExecute_Implementation(float DeltaTime, const FComposableCameraPose & CurrentCameraPose)
```

---

#### OnExecute_Implementation { #onexecute_implementation-3 }

`virtual`

```cpp
virtual void OnExecute_Implementation(float DeltaTime, const FComposableCameraPose & CurrentCameraPose, FComposableCameraPose & OutCameraPose)
```

### Private Attributes

| Return | Name | Description |
|--------|------|-------------|
| `class UEnhancedInputLocalPlayerSubsystem *` | [`Subsystem`](#subsystem-1)  |  |
| `TUniquePtr< TCameraInterpolator< TValueTypeWrapper< double > > >` | [`Interp_T`](#interp_t-1)  |  |

---

#### Subsystem { #subsystem-1 }

```cpp
class UEnhancedInputLocalPlayerSubsystem * Subsystem { nullptr }
```

---

#### Interp_T { #interp_t-1 }

```cpp
TUniquePtr< TCameraInterpolator< TValueTypeWrapper< double > > > Interp_T
```
