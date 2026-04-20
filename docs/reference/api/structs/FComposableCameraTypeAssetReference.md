
# FComposableCameraTypeAssetReference { #fcomposablecameratypeassetreference }

```cpp
#include <ComposableCameraTypeAssetReference.h>
```

Designer-facing wrapper for a [UComposableCameraTypeAsset](../data-assets/UComposableCameraTypeAsset.md#ucomposablecameratypeasset) + its exposed parameters + exposed variables, laid out as two FInstancedPropertyBag fields.

This is the struct a [UComposableCameraLevelSequenceComponent](../uobjects-other/UComposableCameraLevelSequenceComponent.md#ucomposablecameralevelsequencecomponent) owns. It exists for two reasons:

1) Sequencer needs something it can bind standard property tracks against. Stock FMovieSceneFloatTrack / FMovieSceneDoubleVectorTrack / etc. walk FProperty paths on the bound object; we can't invent our own channel types per CCS pin type without writing a lot of custom MovieScene sections. The FInstancedPropertyBag route gives us type-correct FProperty's for free.

2) Designers editing the component in the Details panel need one field per exposed parameter (typed float / vector / actor picker / …), matching what the TypeAsset declared. FInstancedPropertyBag renders exactly that.

Parameters vs Variables ─────────────────────── The TypeAsset's ExposedParameters and ExposedVariables arrays are kept as separate bags intentionally — they correspond to visually-distinct categories in the Sequencer "Add Track" menu ("Camera Parameters" vs "Camera Variables") and eliminate any chance of name collision between a parameter and a variable that happen to share a name at the TypeAsset level.

Lifecycle ───────── [RebuildBagsFromTypeAsset()](#rebuildbagsfromtypeasset) must be called whenever TypeAsset changes (the component calls it from PostEditChangeProperty). Values for properties whose name + type survive the rebuild are carried over; everything else is reset to the bag's default for that type.

At camera activation time, [BuildParameterBlock()](#buildparameterblock) walks both bags and emits a [FComposableCameraParameterBlock](FComposableCameraParameterBlock.md#fcomposablecameraparameterblock) ready to hand to [UE::ComposableCameras::ConstructCameraFromTypeAsset](../free-functions/Functions.md#constructcamerafromtypeasset).

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `TObjectPtr< UComposableCameraTypeAsset >` | [`TypeAsset`](#typeasset)  | The TypeAsset this reference targets. Changing this triggers RebuildBagsFromTypeAsset on the owning component. |
| `FInstancedPropertyBag` | [`Parameters`](#parameters-1)  | One entry per TypeAsset::ExposedParameters, typed according to each exposed parameter's PinType. |
| `FInstancedPropertyBag` | [`Variables`](#variables)  | One entry per TypeAsset::ExposedVariables (NOT InternalVariables — those are not caller-overridable). Same FixedLayout and "no |

---

#### TypeAsset { #typeasset }

```cpp
TObjectPtr< UComposableCameraTypeAsset > TypeAsset
```

The TypeAsset this reference targets. Changing this triggers RebuildBagsFromTypeAsset on the owning component.

---

#### Parameters { #parameters-1 }

```cpp
FInstancedPropertyBag Parameters
```

One entry per TypeAsset::ExposedParameters, typed according to each exposed parameter's PinType.

* FixedLayout prevents the designer from reshaping the bag by hand in the Details panel — its structure is derived from the TypeAsset and must only be mutated via RebuildBagsFromTypeAsset.

* We deliberately do NOT set meta=(InterpBagProperties=true) here. That metadata would make Sequencer's core drill-in walk the bag automatically and surface leaves through a deep "TypeAssetReference
  › Parameters › Value › Leaf" chain — duplicating what our own FComposableCameraLevelSequenceComponentTrackEditor already surfaces at two levels (Camera Parameters › Leaf). Instead, we only rely on CPF_Interp being set on each dynamic bag leaf by RebuildBagsFromTypeAsset (see AddDescIfSupported in the .cpp) — that single flag is what makes CanKeyProperty succeed; the outer bag metadata is not required for the custom track-editor path.

---

#### Variables { #variables }

```cpp
FInstancedPropertyBag Variables
```

One entry per TypeAsset::ExposedVariables (NOT InternalVariables — those are not caller-overridable). Same FixedLayout and "no
InterpBagProperties" rationale as Parameters.

### Public Methods

| Return | Name | Description |
|--------|------|-------------|
| `void` | [`RebuildBagsFromTypeAsset`](#rebuildbagsfromtypeasset)  | Regenerate the Parameters and Variables bag layouts to match the current TypeAsset, preserving any existing values whose name + type survive. |
| `void` | [`BuildParameterBlock`](#buildparameterblock) `const` | Read every current bag value into OutBlock so it can be passed to [UE::ComposableCameras::ConstructCameraFromTypeAsset](../free-functions/Functions.md#constructcamerafromtypeasset). Uses [FComposableCameraParameterBlock](FComposableCameraParameterBlock.md#fcomposablecameraparameterblock)'s existing typed setters so the block is indistinguishable from one produced by the K2Node activation path. |

---

#### RebuildBagsFromTypeAsset { #rebuildbagsfromtypeasset }

```cpp
void RebuildBagsFromTypeAsset()
```

Regenerate the Parameters and Variables bag layouts to match the current TypeAsset, preserving any existing values whose name + type survive.

If TypeAsset is null, both bags are reset empty.

Called from UComposableCameraLevelSequenceComponent::PostEditChangeProperty when TypeAsset is swapped, and from ComponentActivated / OnRegister on first load so freshly-placed components pick up the latest interface.

---

#### BuildParameterBlock { #buildparameterblock }

`const`

```cpp
void BuildParameterBlock(FComposableCameraParameterBlock & OutBlock) const
```

Read every current bag value into OutBlock so it can be passed to [UE::ComposableCameras::ConstructCameraFromTypeAsset](../free-functions/Functions.md#constructcamerafromtypeasset). Uses [FComposableCameraParameterBlock](FComposableCameraParameterBlock.md#fcomposablecameraparameterblock)'s existing typed setters so the block is indistinguishable from one produced by the K2Node activation path.

Safe to call with a null TypeAsset — writes nothing in that case.
