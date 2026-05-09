
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
| `UComposableCameraInterpolatorBase *` | [`Interpolator`](#interpolator-3)  |  |
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

#### Interpolator { #interpolator-3 }

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
| `TWeakObjectPtr< class UEnhancedInputLocalPlayerSubsystem >` | [`CachedSubsystem`](#cachedsubsystem-1)  | Weak — `UEnhancedInputLocalPlayerSubsystem` is owned by the LocalPlayer, which is destroyed on PIE stop, controller swap, level-streaming-out, or kick. |
| `TWeakObjectPtr< class ULocalPlayer >` | [`CachedLocalPlayer`](#cachedlocalplayer-1)  | Identity of the LocalPlayer the cached subsystem belongs to. Used by `ResolveInputSubsystem` to detect controller-swap-without- destruction and invalidate the subsystem cache before reading from the wrong player's input source. |
| `TUniquePtr< TCameraInterpolator< TValueTypeWrapper< double > > >` | [`Interp_T`](#interp_t-1)  |  |

---

#### CachedSubsystem { #cachedsubsystem-1 }

```cpp
TWeakObjectPtr< class UEnhancedInputLocalPlayerSubsystem > CachedSubsystem
```

Weak — `UEnhancedInputLocalPlayerSubsystem` is owned by the LocalPlayer, which is destroyed on PIE stop, controller swap, level-streaming-out, or kick.

---

#### CachedLocalPlayer { #cachedlocalplayer-1 }

```cpp
TWeakObjectPtr< class ULocalPlayer > CachedLocalPlayer
```

Identity of the LocalPlayer the cached subsystem belongs to. Used by `ResolveInputSubsystem` to detect controller-swap-without- destruction and invalidate the subsystem cache before reading from the wrong player's input source.

---

#### Interp_T { #interp_t-1 }

```cpp
TUniquePtr< TCameraInterpolator< TValueTypeWrapper< double > > > Interp_T
```

### Private Methods

| Return | Name | Description |
|--------|------|-------------|
| `class UEnhancedInputLocalPlayerSubsystem *` | [`ResolveInputSubsystem`](#resolveinputsubsystem-1)  | Walk PCM → OwningPC → LocalPlayer with per-link `IsValid`, then reuse the cached subsystem only if its owning LocalPlayer matches the chain's current LocalPlayer. Returns nullptr on any chain null OR mismatch (after invalidating the stale cache). |

---

#### ResolveInputSubsystem { #resolveinputsubsystem-1 }

```cpp
class UEnhancedInputLocalPlayerSubsystem * ResolveInputSubsystem()
```

Walk PCM → OwningPC → LocalPlayer with per-link `IsValid`, then reuse the cached subsystem only if its owning LocalPlayer matches the chain's current LocalPlayer. Returns nullptr on any chain null OR mismatch (after invalidating the stale cache).

Caching just the subsystem isn't enough: `OwningPlayerController` can be re-pointed (re-possess, AI takeover, splitscreen reshuffle) to a DIFFERENT `LocalPlayer` whose subsystem is a different live object. The previous LocalPlayer can stay alive (its subsystem still valid in isolation) — so a `IsValid(CachedSubsystem)` test alone passes against a stale-player cache and we'd keep reading the previous player's input source. The LocalPlayer comparison fixes that.
