
# FComposableCameraPatchActivateParams { #fcomposablecamerapatchactivateparams }

```cpp
#include <ComposableCameraPatchTypes.h>
```

Caller-provided activation parameters for AddPatch.

Each "overridable" field is paired with a `bOverride*` bool tagged `InlineEditConditionToggle` and gated by `EditCondition` on the value field — the same idiom as `FPostProcessSettings::bOverride_*`.

Two surfaces, two distinct workflows:

• Details panel (asset details, struct customization): the bool collapses into an inline checkbox next to the value field. Unchecked → use asset default; checked → caller value wins. Standard.

• BP `Make [FComposableCameraPatchActivateParams](#fcomposablecamerapatchactivateparams)` node: UE's MakeStructHandler treats `InlineEditConditionToggle` bools as *implicit* override flags. The bool's runtime value is forced TRUE for every value pin whose `bShowPin` flag is true on the MakeStruct node, and FALSE for pins whose `bShowPin` is false. **Important UI subtlety**: `bShowPin` is controlled ONLY by the node's details-panel "Show Pin For …" checkboxes — NOT by the per-pin eye icon visible on the node body. The eye icon toggles a different state (advanced/visual collapse) and does NOT propagate to `bShowPin`, so clicking it leaves `bOverride*=true` even though the pin appears collapsed. Authoring rule: **to use asset defaults for a field, uncheck "Show Pin For [FieldName]" in the MakeStruct node's details panel** (selecting the node shows the list). (See `K2Node_MakeStruct.cpp:117``CanBeExposed` returning false for `InlineEditConditionToggle` properties, and `MakeStructHandler.cpp:189` where `KCST_Assignment` of `bool = true` is injected only for properties whose `PropertyEntry.bShowPin` is true.)

The paired-bool design (over float-zero sentinels) is what lets a caller legitimately request a literal `0` — e.g. `EnterDuration = 0` for "no
fade-in" — without having that confused with "fall back to asset".

Fields without an asset-side default — `bExpireOnCameraChange` is the only one — have no override toggle; the per-call value is always used.

Exposed parameter / exposed variable values are passed separately as a [FComposableCameraParameterBlock](FComposableCameraParameterBlock.md#fcomposablecameraparameterblock) argument to AddPatch — mirroring the shape of [FComposableCameraActivateParams](FComposableCameraActivateParams.md#fcomposablecameraactivateparams) + ActivateComposableCameraFromTypeAsset, and letting UK2Node_AddCameraPatch generate typed pins for each exposed name without having to set-fields-in-struct on this struct.

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `bool` | [`bOverrideEnterDuration`](#boverrideenterduration)  | When true, EnterDuration overrides the asset's DefaultEnterDuration. |
| `float` | [`EnterDuration`](#enterduration-2)  |  |
| `bool` | [`bOverrideExitDuration`](#boverrideexitduration)  | When true, ExitDuration overrides the asset's DefaultExitDuration. |
| `float` | [`ExitDuration`](#exitduration-2)  |  |
| `bool` | [`bOverrideExpirationType`](#boverrideexpirationtype)  | When true, ExpirationType overrides the asset's DefaultExpirationType. |
| `uint8` | [`ExpirationType`](#expirationtype-3)  |  |
| `bool` | [`bOverrideDuration`](#boverrideduration)  | When true, Duration overrides the asset's DefaultDuration. Only consulted when the Duration channel is enabled (either via the per-call ExpirationType override or via the asset default). |
| `float` | [`Duration`](#duration-8)  |  |
| `bool` | [`bExpireOnCameraChange`](#bexpireoncamerachange-2)  | If true, the Patch flips to Exiting when the owning Director's RunningCamera changes. Stacks additively with the ExpirationType channels. No asset-side default — always uses this per-call value. |
| `bool` | [`bOverrideLayerIndex`](#boverridelayerindex)  | When true, LayerIndex below overrides the asset's DefaultLayerIndex. |
| `int32` | [`LayerIndex`](#layerindex-2)  | Composition order. Lower runs earlier (matches GameplayCameras' StackOrder). Only consulted when bOverrideLayerIndex is true; otherwise the asset's DefaultLayerIndex wins. |

---

#### bOverrideEnterDuration { #boverrideenterduration }

```cpp
bool bOverrideEnterDuration = false
```

When true, EnterDuration overrides the asset's DefaultEnterDuration.

---

#### EnterDuration { #enterduration-2 }

```cpp
float EnterDuration = 0.f
```

---

#### bOverrideExitDuration { #boverrideexitduration }

```cpp
bool bOverrideExitDuration = false
```

When true, ExitDuration overrides the asset's DefaultExitDuration.

---

#### ExitDuration { #exitduration-2 }

```cpp
float ExitDuration = 0.f
```

---

#### bOverrideExpirationType { #boverrideexpirationtype }

```cpp
bool bOverrideExpirationType = false
```

When true, ExpirationType overrides the asset's DefaultExpirationType.

---

#### ExpirationType { #expirationtype-3 }

```cpp
uint8 ExpirationType = 0
```

---

#### bOverrideDuration { #boverrideduration }

```cpp
bool bOverrideDuration = false
```

When true, Duration overrides the asset's DefaultDuration. Only consulted when the Duration channel is enabled (either via the per-call ExpirationType override or via the asset default).

---

#### Duration { #duration-8 }

```cpp
float Duration = 0.f
```

---

#### bExpireOnCameraChange { #bexpireoncamerachange-2 }

```cpp
bool bExpireOnCameraChange = false
```

If true, the Patch flips to Exiting when the owning Director's RunningCamera changes. Stacks additively with the ExpirationType channels. No asset-side default — always uses this per-call value.

---

#### bOverrideLayerIndex { #boverridelayerindex }

```cpp
bool bOverrideLayerIndex = false
```

When true, LayerIndex below overrides the asset's DefaultLayerIndex.

---

#### LayerIndex { #layerindex-2 }

```cpp
int32 LayerIndex = 0
```

Composition order. Lower runs earlier (matches GameplayCameras' StackOrder). Only consulted when bOverrideLayerIndex is true; otherwise the asset's DefaultLayerIndex wins.
