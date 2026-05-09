
# UComposableCameraRotateToAction { #ucomposablecamerarotatetoaction }

```cpp
#include <ComposableCameraRotateToAction.h>
```

> **Inherits:** [`UComposableCameraActionBase`](UComposableCameraActionBase.md#ucomposablecameraactionbase)

Rotate camera to a given target rotation with some interpolator. If the camera rotates to the target rotation or there is user input, the action will expire.

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `FRotator` | [`TargetRotation`](#targetrotation)  |  |
| `class UInputAction *` | [`RotateAction`](#rotateaction)  |  |
| `UComposableCameraInterpolatorBase *` | [`Interpolator`](#interpolator)  |  |
| `float` | [`InterpSpeed`](#interpspeed)  |  |

---

#### TargetRotation { #targetrotation }

```cpp
FRotator TargetRotation
```

---

#### RotateAction { #rotateaction }

```cpp
class UInputAction * RotateAction { nullptr }
```

---

#### Interpolator { #interpolator }

```cpp
UComposableCameraInterpolatorBase * Interpolator { nullptr }
```

---

#### InterpSpeed { #interpspeed }

```cpp
float InterpSpeed { 1.f }
```

### Public Methods

| Return | Name | Description |
|--------|------|-------------|
|  | [`UComposableCameraRotateToAction`](#ucomposablecamerarotatetoaction-1)  |  |
| `bool` | [`CanExecute_Implementation`](#canexecute_implementation-2) `virtual` |  |
| `void` | [`OnExecute_Implementation`](#onexecute_implementation-2) `virtual` |  |

---

#### UComposableCameraRotateToAction { #ucomposablecamerarotatetoaction-1 }

```cpp
UComposableCameraRotateToAction(const FObjectInitializer & ObjectInitializer)
```

---

#### CanExecute_Implementation { #canexecute_implementation-2 }

`virtual`

```cpp
virtual bool CanExecute_Implementation(float DeltaTime, const FComposableCameraPose & CurrentCameraPose)
```

---

#### OnExecute_Implementation { #onexecute_implementation-2 }

`virtual`

```cpp
virtual void OnExecute_Implementation(float DeltaTime, const FComposableCameraPose & CurrentCameraPose, FComposableCameraPose & OutCameraPose)
```

### Private Attributes

| Return | Name | Description |
|--------|------|-------------|
| `TWeakObjectPtr< class UEnhancedInputLocalPlayerSubsystem >` | [`CachedSubsystem`](#cachedsubsystem)  | Weak subsystem cache — see ResetPitchAction. |
| `TWeakObjectPtr< class ULocalPlayer >` | [`CachedLocalPlayer`](#cachedlocalplayer)  | LocalPlayer identity guard — see ResetPitchAction. |
| `TUniquePtr< TCameraInterpolator< TValueTypeWrapper< FRotator > > >` | [`Interp_T`](#interp_t)  |  |

---

#### CachedSubsystem { #cachedsubsystem }

```cpp
TWeakObjectPtr< class UEnhancedInputLocalPlayerSubsystem > CachedSubsystem
```

Weak subsystem cache — see ResetPitchAction.

---

#### CachedLocalPlayer { #cachedlocalplayer }

```cpp
TWeakObjectPtr< class ULocalPlayer > CachedLocalPlayer
```

LocalPlayer identity guard — see ResetPitchAction.

---

#### Interp_T { #interp_t }

```cpp
TUniquePtr< TCameraInterpolator< TValueTypeWrapper< FRotator > > > Interp_T
```

### Private Methods

| Return | Name | Description |
|--------|------|-------------|
| `class UEnhancedInputLocalPlayerSubsystem *` | [`ResolveInputSubsystem`](#resolveinputsubsystem)  | Resolve (or re-resolve) the cached subsystem. Same shape as `UComposableCameraResetPitchAction::ResolveInputSubsystem` — see that header for the LocalPlayer-teardown / chain-null / controller-swap-without-destruction rationale. |

---

#### ResolveInputSubsystem { #resolveinputsubsystem }

```cpp
class UEnhancedInputLocalPlayerSubsystem * ResolveInputSubsystem()
```

Resolve (or re-resolve) the cached subsystem. Same shape as `UComposableCameraResetPitchAction::ResolveInputSubsystem` — see that header for the LocalPlayer-teardown / chain-null / controller-swap-without-destruction rationale.
