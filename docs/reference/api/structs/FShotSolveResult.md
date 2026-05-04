
# FShotSolveResult { #fshotsolveresult }

```cpp
#include <ComposableCameraShotSolver.h>
```

Solver output. `bValid == false` when an essential anchor cannot be resolved (placement / aim) — caller should preserve upstream pose for the frame.

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `bool` | [`bValid`](#bvalid)  |  |
| `FVector` | [`CameraPosition`](#cameraposition)  |  |
| `FRotator` | [`CameraRotation`](#camerarotation)  |  |
| `float` | [`FieldOfView`](#fieldofview-2)  |  |
| `float` | [`FocusDistance`](#focusdistance-2)  |  |
| `float` | [`Aperture`](#aperture-3)  |  |
| `float` | [`EffectiveDistance`](#effectivedistance)  | Effective `Placement.Distance` actually used by the solve this frame — = `FInterpTo(prior.LastDistance, Shot.Placement.Distance, dt, Shot.Placement.DistanceSpeed)` clamped `>= 1cm`, or simply `max(Shot.Placement.Distance, 1)` when no prior pose was supplied / DistanceSpeed is 0 / DeltaTime is 0. |

---

#### bValid { #bvalid }

```cpp
bool bValid = false
```

---

#### CameraPosition { #cameraposition }

```cpp
FVector CameraPosition = FVector::ZeroVector
```

---

#### CameraRotation { #camerarotation }

```cpp
FRotator CameraRotation = FRotator::ZeroRotator
```

---

#### FieldOfView { #fieldofview-2 }

```cpp
float FieldOfView = 79.f
```

---

#### FocusDistance { #focusdistance-2 }

```cpp
float FocusDistance = 200.f
```

---

#### Aperture { #aperture-3 }

```cpp
float Aperture = 2.8f
```

---

#### EffectiveDistance { #effectivedistance }

```cpp
float EffectiveDistance = -1.f
```

Effective `Placement.Distance` actually used by the solve this frame — = `FInterpTo(prior.LastDistance, Shot.Placement.Distance, dt, Shot.Placement.DistanceSpeed)` clamped `>= 1cm`, or simply `max(Shot.Placement.Distance, 1)` when no prior pose was supplied / DistanceSpeed is 0 / DeltaTime is 0.

Caller should feed this back into `[FShotPriorPose::LastDistance](FShotPriorPose.md#lastdistance)` on the next tick to keep the IIR seeded. `< 0` ⇒ Distance was irrelevant for this solve (e.g. `FixedWorldPosition` mode).

# ExposedBag { #exposedbag }

### Functions

| Return | Name | Description |
|--------|------|-------------|
| `bool` | [`AddDescIfSupported`](#adddescifsupported)  | Build a single FPropertyBagPropertyDesc and, if the pin type is representable in a property bag, append it to OutDescs. Returns false for types we intentionally skip (currently just Delegate). |
| `void` | [`CopyBagValueIntoBlock`](#copybagvalueintoblock)  | Copy a single bag value (keyed by Name) into OutBlock via the matching [FComposableCameraParameterBlock](FComposableCameraParameterBlock.md#fcomposablecameraparameterblock) typed setter. If the bag has no value for Name, the block is left untouched and the camera will fall back to the node's authored default during ApplyParameterBlock. |

---

#### AddDescIfSupported { #adddescifsupported }

```cpp
bool AddDescIfSupported(FName Name, EComposableCameraPinType PinType, const UScriptStruct * StructType, const UEnum * EnumType, TArray< FPropertyBagPropertyDesc > & OutDescs)
```

Build a single FPropertyBagPropertyDesc and, if the pin type is representable in a property bag, append it to OutDescs. Returns false for types we intentionally skip (currently just Delegate).

The descriptor's PropertyFlags include CPF_Edit | CPF_Interp. CPF_Interp is what Sequencer's FindPropertySetter checks to decide whether the leaf is keyable — without it CanKeyProperty returns false on every leaf and any track-editor parameter menu collapses. The flag propagates onto the dynamic FProperty that UPropertyBag::GetOrCreateFromDescs creates.

Centralised here so both the LS Component ([FComposableCameraTypeAssetReference](FComposableCameraTypeAssetReference.md#fcomposablecameratypeassetreference)) and the Patch Section ([UMovieSceneComposableCameraPatchSection](../uobjects-other/UMovieSceneComposableCameraPatchSection.md#umoviescenecomposablecamerapatchsection)) use the exact same descriptor shape — divergence there would mean only one of the two surfaces is keyable in Sequencer.

---

#### CopyBagValueIntoBlock { #copybagvalueintoblock }

```cpp
void CopyBagValueIntoBlock(const FInstancedPropertyBag & Bag, FName Name, EComposableCameraPinType PinType, const UScriptStruct * StructType, const UEnum * EnumType, FComposableCameraParameterBlock & OutBlock)
```

Copy a single bag value (keyed by Name) into OutBlock via the matching [FComposableCameraParameterBlock](FComposableCameraParameterBlock.md#fcomposablecameraparameterblock) typed setter. If the bag has no value for Name, the block is left untouched and the camera will fall back to the node's authored default during ApplyParameterBlock.

Centralised for the same reason as AddDescIfSupported above — keeping one canonical shape for "bag → parameter block" guarantees any future pin-type addition flows uniformly through every consumer.

# PatchEnvelope { #patchenvelope }

### Functions

| Return | Name | Description |
|--------|------|-------------|
| `float` | [`ApplyEase`](#applyease)  | Apply the 5-curve enum ease shape to a normalized time t ∈ [0, 1]. Returns f(t) ∈ [0, 1]. |
| `float` | [`ComputeStatelessAlpha`](#computestatelessalpha)  | Stateless envelope alpha at a given frame, computed purely from time + section bounds + ease parameters — no Phase / ElapsedInPhase / ExitStartAlpha fields, no per-call mutation. |

---

#### ApplyEase { #applyease }

```cpp
float ApplyEase(EComposableCameraPatchEase Ease, float t)
```

Apply the 5-curve enum ease shape to a normalized time t ∈ [0, 1]. Returns f(t) ∈ [0, 1].

Pulled out of UComposableCameraPatchManager.cpp's anonymous namespace so the runtime stateful envelope (`AdvancePatchEnvelope` in PatchManager.cpp) and the editor-preview stateless envelope (`ComputeStatelessAlpha` below) agree on the curve shape to a single canonical implementation. Adding a new ease type means editing one switch instead of two.

---

#### ComputeStatelessAlpha { #computestatelessalpha }

```cpp
float ComputeStatelessAlpha(FFrameNumber CurrentFrame, FFrameNumber SectionStart, FFrameNumber SectionEnd, float EnterDurationSeconds, float ExitDurationSeconds, EComposableCameraPatchEase Ease, FFrameRate TickRate)
```

Stateless envelope alpha at a given frame, computed purely from time + section bounds + ease parameters — no Phase / ElapsedInPhase / ExitStartAlpha fields, no per-call mutation.

Used by the Sequencer **editor preview** path (LS Component's TickComponent applies the result onto its InternalCamera's pose before projecting to the CineCamera). The runtime PIE path keeps the stateful machine on [UComposableCameraPatchInstance](../uobjects-other/UComposableCameraPatchInstance.md#ucomposablecamerapatchinstance) because it needs to handle real-time Manual / Condition / OnCameraChange channels — Sequencer editor scrub doesn't have those. Computing alpha as a pure function of time also makes scrub-backwards correct: dragging the playhead to the section's exit window shows the fade-out, no matter how the user got there.

Curve shape: playhead < SectionStart → 0 playhead in [Start, Start + EnterDuration] → ease(t) // ramp up playhead in [Start + Enter, End - Exit] → 1 playhead in [End - ExitDuration, End] → 1 - ease(t) // ramp down playhead >= SectionEnd → 0

EnterDuration / ExitDuration ≤ 0 short-circuit (no ramp on that side).

**Parameters**

* `CurrentFrame` Playhead in tick units (the section / movie scene's tick resolution). 

* `SectionStart` Section's inclusive lower bound. 

* `SectionEnd` Section's exclusive upper bound. 

* `EnterDurationSeconds` Resolved enter duration (asset default OR overridden by Params; section easing is folded in upstream by the caller). 

* `ExitDurationSeconds` Same shape as EnterDurationSeconds. 

* `Ease` Patch asset's authored ease type. 

* `TickRate` Owning movie scene's tick resolution; used to convert enter/exit seconds → tick counts for the in-tick-space comparison.
