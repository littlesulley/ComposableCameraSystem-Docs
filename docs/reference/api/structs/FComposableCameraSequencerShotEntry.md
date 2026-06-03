
# FComposableCameraSequencerShotEntry { #fcomposablecamerasequencershotentry }

```cpp
#include <ComposableCameraLevelSequenceComponent.h>
```

Per-section Shot override state owned by `UComposableCameraLevelSequenceComponent::SequencerShotOverrides`.

Top-level USTRUCT (not nested) because UHT rejects USTRUCT-inside-UCLASS. One entry per active Shot Section; map key is the section weak pointer.

`RowIndex`, `EnterTransition`, and `BlendAlpha` let the LSComponent's `ApplyActiveSequencerShotOverride` blender pick the lowest two row-index entries and produce a blended camera pose using the higher-row entry's resolved transition and alpha.

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `FComposableCameraShot` | [`Shot`](#shot-1)  | Latest Shot data sampled from the section at the current playhead. Re-pushed every frame the section is in-range (cheap value copy — Shot's TArray<FShotTarget> is short and the rest is POD). |
| `int32` | [`RowIndex`](#rowindex)  | Section row index. The blender picks the lowest two active row indices and blends them. |
| `TObjectPtr< UComposableCameraTransitionDataAsset >` | [`EnterTransition`](#entertransition-3)  | Resolved EnterTransition asset for this section, loaded synchronously by the TrackInstance from the section's `EnterTransition` soft-ref each frame. Null if the section's EnterTransition is unset or fails to load — the blender treats null as a hard cut (the incoming section's pose snaps in at the boundary; no transition pose-blend pass runs). |
| `float` | [`BlendAlpha`](#blendalpha)  | Blend progress for this entry as the *incoming* (higher-row) side of an overlap with the immediately-below RowIndex in-range peer. Range [0, 1]. |

---

#### Shot { #shot-1 }

```cpp
FComposableCameraShot Shot
```

Latest Shot data sampled from the section at the current playhead. Re-pushed every frame the section is in-range (cheap value copy — Shot's TArray<FShotTarget> is short and the rest is POD).

---

#### RowIndex { #rowindex }

```cpp
int32 RowIndex = 0
```

Section row index. The blender picks the lowest two active row indices and blends them.

---

#### EnterTransition { #entertransition-3 }

```cpp
TObjectPtr< UComposableCameraTransitionDataAsset > EnterTransition
```

Resolved EnterTransition asset for this section, loaded synchronously by the TrackInstance from the section's `EnterTransition` soft-ref each frame. Null if the section's EnterTransition is unset or fails to load — the blender treats null as a hard cut (the incoming section's pose snaps in at the boundary; no transition pose-blend pass runs).

UPROPERTY-tracked TObjectPtr so the loaded asset stays referenced for the lifetime of this entry (the soft-pointer load can otherwise be GC'd between frames if no other reference exists).

---

#### BlendAlpha { #blendalpha }

```cpp
float BlendAlpha = 1.0f
```

Blend progress for this entry as the *incoming* (higher-row) side of an overlap with the immediately-below RowIndex in-range peer. Range [0, 1].

Computed each frame by the TrackInstance: overlap_start = max(this.start, peer.start) // intersection overlap_end = min(this.end, peer.end) BlendAlpha = saturate( (CurrentFrame - overlap_start) / (overlap_end - overlap_start) )

Defaults to 1.0 when the entry has no lower-row overlapping peer, so the blender treats this as standalone single-section write-through. The lower-row entry of an overlapping pair also keeps BlendAlpha = 1.0; only the *higher-row* incoming entry's BlendAlpha is read by the blender. The lower-row entry's contribution is implicitly `(1 - higher_entry.BlendAlpha)` and computed inside the blender.
