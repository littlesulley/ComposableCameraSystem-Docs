
# FTransitionDebugSnapshot { #ftransitiondebugsnapshot }

```cpp
#include <ComposableCameraTransitionBase.h>
```

Per-frame pose snapshot captured for debug visualization.

Deliberately narrower than `[FComposableCameraPose](FComposableCameraPose.md#fcomposablecamerapose)` — we only keep the fields `DrawStandardTransitionDebug` actually reads (position, rotation, resolved FOV in degrees). Skipping `FPostProcessSettings` matters: that struct embeds `TObjectPtr<UTexture>` / similar UObject references through its color-grading / vignette / bloom sub-structs, and our cache is NOT a UPROPERTY, so those references wouldn't be tracked by the GC. Caching only POD-like fields sidesteps the issue entirely AND shrinks each transition's per-frame debug memory from ~3× sizeof(FPostProcessSettings) to a few dozen bytes.

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `FVector` | [`Position`](#position-1)  |  |
| `FRotator` | [`Rotation`](#rotation-1)  |  |
| `float` | [`FOVDegrees`](#fovdegrees)  |  |

---

#### Position { #position-1 }

```cpp
FVector Position { FVector::ZeroVector }
```

---

#### Rotation { #rotation-1 }

```cpp
FRotator Rotation { FRotator::ZeroRotator }
```

---

#### FOVDegrees { #fovdegrees }

```cpp
float FOVDegrees { 90.f }
```

## FTransitionDebugSnapshot { #ftransitiondebugsnapshot }

```cpp
#include <ComposableCameraTransitionBase.h>
```

Per-frame pose snapshot captured for debug visualization.

Deliberately narrower than `[FComposableCameraPose](FComposableCameraPose.md#fcomposablecamerapose)` — we only keep the fields `DrawStandardTransitionDebug` actually reads (position, rotation, resolved FOV in degrees). Skipping `FPostProcessSettings` matters: that struct embeds `TObjectPtr<UTexture>` / similar UObject references through its color-grading / vignette / bloom sub-structs, and our cache is NOT a UPROPERTY, so those references wouldn't be tracked by the GC. Caching only POD-like fields sidesteps the issue entirely AND shrinks each transition's per-frame debug memory from ~3× sizeof(FPostProcessSettings) to a few dozen bytes.

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `FVector` | [`Position`](#position-1)  |  |
| `FRotator` | [`Rotation`](#rotation-1)  |  |
| `float` | [`FOVDegrees`](#fovdegrees)  |  |

---

#### Position { #position-1 }

```cpp
FVector Position { FVector::ZeroVector }
```

---

#### Rotation { #rotation-1 }

```cpp
FRotator Rotation { FRotator::ZeroRotator }
```

---

#### FOVDegrees { #fovdegrees }

```cpp
float FOVDegrees { 90.f }
```
