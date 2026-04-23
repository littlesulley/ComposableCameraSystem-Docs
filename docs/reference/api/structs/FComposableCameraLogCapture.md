
# FComposableCameraLogCapture { #fcomposablecameralogcapture }

```cpp
#include <ComposableCameraLogCapture.h>
```

> **Inherits:** `FOutputDevice`

Output device that watches `GLog` for warnings and errors emitted on any `LogComposableCamera*` log category and keeps the most recent N in a ring buffer for the debug panel's Warnings region to display.

Why this is needed: several non-fatal error paths in the runtime (running-camera null, referenced-director destroyed mid-blend, spline transition missing its rail actor, etc.) emit `UE_LOG(..., Error, ...)` but are only visible in Output Log. Users running PIE without Output Log open would miss them entirely. Mirroring them into the panel surfaces the signal in the same place the rest of the debug state lives.

Thread safety: `Serialize` is called from whichever thread did the `UE_LOG`. The ring buffer is guarded by a CriticalSection, so the panel's game-thread read and any worker-thread write serialize cleanly. Capacity is small (16) so the critical section is never held long enough to matter.

Compiled out in shipping builds — both Install/Uninstall and the accessor are `#if !UE_BUILD_SHIPPING`, so shipping games pay zero cost (no output device registered, no ring buffer memory, no lock).

### Public Methods

| Return | Name | Description |
|--------|------|-------------|
| `void` | [`Serialize`](#serialize) `virtual` |  |
| `bool` | [`CanBeUsedOnAnyThread`](#canbeusedonanythread) `virtual` `const` `inline` |  |
| `bool` | [`CanBeUsedOnMultipleThreads`](#canbeusedonmultiplethreads) `virtual` `const` `inline` |  |

---

#### Serialize { #serialize }

`virtual`

```cpp
virtual void Serialize(const TCHAR * V, ELogVerbosity::Type Verbosity, const FName & Category)
```

---

#### CanBeUsedOnAnyThread { #canbeusedonanythread }

`virtual` `const` `inline`

```cpp
virtual inline bool CanBeUsedOnAnyThread() const
```

---

#### CanBeUsedOnMultipleThreads { #canbeusedonmultiplethreads }

`virtual` `const` `inline`

```cpp
virtual inline bool CanBeUsedOnMultipleThreads() const
```

### Public Static Attributes

| Return | Name | Description |
|--------|------|-------------|
| `constexpr int32` | [`MaxCapturedEntries`](#maxcapturedentries) `static` | Max entries the ring buffer keeps. Older entries overflow off the front. Exposed so the panel's height pass can reserve rows up front. |

---

#### MaxCapturedEntries { #maxcapturedentries }

`static`

```cpp
constexpr int32 MaxCapturedEntries = 16
```

Max entries the ring buffer keeps. Older entries overflow off the front. Exposed so the panel's height pass can reserve rows up front.

### Public Static Methods

| Return | Name | Description |
|--------|------|-------------|
| `void` | [`Install`](#install) `static` | Register with `GLog`. Idempotent — calling twice is a no-op. |
| `void` | [`Uninstall`](#uninstall) `static` | Unregister from `GLog` and clear the ring buffer. Idempotent. |
| `void` | [`GetRecentEntries`](#getrecententries) `static` | Copy the current ring-buffer contents into `OutEntries`, oldest first. Safe to call from any thread; blocks briefly on the ring-buffer critical section but never for more than a few μs. |

---

#### Install { #install }

`static`

```cpp
static void Install()
```

Register with `GLog`. Idempotent — calling twice is a no-op.

---

#### Uninstall { #uninstall }

`static`

```cpp
static void Uninstall()
```

Unregister from `GLog` and clear the ring buffer. Idempotent.

---

#### GetRecentEntries { #getrecententries }

`static`

```cpp
static void GetRecentEntries(TArray< FComposableCameraLogEntry > & OutEntries)
```

Copy the current ring-buffer contents into `OutEntries`, oldest first. Safe to call from any thread; blocks briefly on the ring-buffer critical section but never for more than a few μs.

### Private Attributes

| Return | Name | Description |
|--------|------|-------------|
| `TArray< FComposableCameraLogEntry >` | [`RingBuffer`](#ringbuffer)  |  |
| `FCriticalSection` | [`BufferCS`](#buffercs)  |  |
| `bool` | [`bInstalled`](#binstalled)  |  |

---

#### RingBuffer { #ringbuffer }

```cpp
TArray< FComposableCameraLogEntry > RingBuffer
```

---

#### BufferCS { #buffercs }

```cpp
FCriticalSection BufferCS
```

---

#### bInstalled { #binstalled }

```cpp
bool bInstalled = false
```

### Private Static Methods

| Return | Name | Description |
|--------|------|-------------|
| `FComposableCameraLogCapture &` | [`Get`](#get) `static` | Returns the shared singleton instance — keyed off static local so the first call installs and lifetime ends with module shutdown. Not exposed publicly: everything users want goes through the static Install / Uninstall / GetRecentEntries surface above. |

---

#### Get { #get }

`static`

```cpp
static FComposableCameraLogCapture & Get()
```

Returns the shared singleton instance — keyed off static local so the first call installs and lifetime ends with module shutdown. Not exposed publicly: everything users want goes through the static Install / Uninstall / GetRecentEntries surface above.
