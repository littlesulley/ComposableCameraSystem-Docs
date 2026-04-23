
# FComposableCameraPoseHistoryEntry { #fcomposablecameraposehistoryentry }

```cpp
#include <ComposableCameraPoseHistoryData.h>
```

One frame's worth of pose snapshot captured by the PCM for the debug panel's "Pose History" sparklines + scrub tooltip.

Deliberately narrower than `[FComposableCameraPose](FComposableCameraPose.md#fcomposablecamerapose)`: we only keep the fields the sparkline rows and tooltip display. Skipping `FPostProcessSettings` matters because it embeds `TObjectPtr<UTexture>` references — and the history ring buffer is NOT a `UPROPERTY`, so any UObject refs it held would escape GC tracking. Same GC-safety pattern as `[UComposableCameraTransitionBase::FTransitionDebugSnapshot](FTransitionDebugSnapshot.md#ftransitiondebugsnapshot)`.

~48 bytes per entry × 120-entry capacity = ~6 KB of ring memory per PCM. Negligible.

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `FVector` | [`Position`](#position-2)  | World position at capture. |
| `FRotator` | [`Rotation`](#rotation-2)  | Rotation at capture (Pitch / Yaw / Roll). |
| `float` | [`FOVDegrees`](#fovdegrees-1)  | Resolved FOV in degrees (via `[FComposableCameraPose::GetEffectiveFieldOfView](FComposableCameraPose.md#geteffectivefieldofview)`). |
| `float` | [`GameTime`](#gametime)  | Game-world time in seconds at capture (`UWorld::GetTimeSeconds`). Pauses with the game so the timeline doesn't drift while paused — that's the semantic users expect when scrubbing history. |
| `FName` | [`ContextName`](#contextname-2)  | Active-context name at capture. Used both for the context-switch marker strip (vertical line across sparklines whenever this changes between adjacent entries) and for the hover tooltip. |

---

#### Position { #position-2 }

```cpp
FVector Position = FVector::ZeroVector
```

World position at capture.

---

#### Rotation { #rotation-2 }

```cpp
FRotator Rotation = FRotator::ZeroRotator
```

Rotation at capture (Pitch / Yaw / Roll).

---

#### FOVDegrees { #fovdegrees-1 }

```cpp
float FOVDegrees = 90.f
```

Resolved FOV in degrees (via `[FComposableCameraPose::GetEffectiveFieldOfView](FComposableCameraPose.md#geteffectivefieldofview)`).

---

#### GameTime { #gametime }

```cpp
float GameTime = 0.f
```

Game-world time in seconds at capture (`UWorld::GetTimeSeconds`). Pauses with the game so the timeline doesn't drift while paused — that's the semantic users expect when scrubbing history.

---

#### ContextName { #contextname-2 }

```cpp
FName ContextName = NAME_None
```

Active-context name at capture. Used both for the context-switch marker strip (vertical line across sparklines whenever this changes between adjacent entries) and for the hover tooltip.
