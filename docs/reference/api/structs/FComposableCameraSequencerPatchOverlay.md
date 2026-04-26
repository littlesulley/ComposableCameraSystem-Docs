
# FComposableCameraSequencerPatchOverlay { #fcomposablecamerasequencerpatchoverlay }

```cpp
#include <ComposableCameraLevelSequenceComponent.h>
```

Per-section editor-preview overlay state owned by UComposableCameraLevelSequenceComponent::SequencerPatchOverlays.

Top-level USTRUCT (not nested) because UHT rejects USTRUCT-inside-UCLASS. One entry per active patch section; map key is the section pointer.

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `TObjectPtr< AComposableCameraCameraBase >` | [`Evaluator`](#evaluator-1)  | Lazy-spawned evaluator actor for this section. Created on first SetSequencerPatchOverlay; destroyed on RemoveSequencerPatchOverlay or when the owning component is unregistered. |
| `FComposableCameraParameterBlock` | [`LatestParameters`](#latestparameters)  | Latest parameter block sampled from the section's channels at the current playhead frame; re-pushed every frame the section is in-range so per-tick application sees animated values. |
| `float` | [`Alpha`](#alpha-1)  | Envelope alpha at the current frame, computed by the caller via PatchEnvelope::ComputeStatelessAlpha. 0 = no contribution, 1 = full. |

---

#### Evaluator { #evaluator-1 }

```cpp
TObjectPtr< AComposableCameraCameraBase > Evaluator
```

Lazy-spawned evaluator actor for this section. Created on first SetSequencerPatchOverlay; destroyed on RemoveSequencerPatchOverlay or when the owning component is unregistered.

---

#### LatestParameters { #latestparameters }

```cpp
FComposableCameraParameterBlock LatestParameters
```

Latest parameter block sampled from the section's channels at the current playhead frame; re-pushed every frame the section is in-range so per-tick application sees animated values.

---

#### Alpha { #alpha-1 }

```cpp
float Alpha = 0.f
```

Envelope alpha at the current frame, computed by the caller via PatchEnvelope::ComputeStatelessAlpha. 0 = no contribution, 1 = full.
