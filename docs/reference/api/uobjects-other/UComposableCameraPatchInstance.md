
# UComposableCameraPatchInstance { #ucomposablecamerapatchinstance }

```cpp
#include <ComposableCameraPatchInstance.h>
```

> **Inherits:** `UObject`

Runtime per-Patch state, owned by [UComposableCameraPatchManager](UComposableCameraPatchManager.md#ucomposablecamerapatchmanager).

Holds the source asset reference, the Patch evaluator camera actor (Stage 2+), resolved layer / push-sequence for ordering, schedule fields, envelope state, cached parameter block for evaluator (re)construction, and a back-link to the user-facing handle.

Stage 1 note: Evaluator stays nullptr; PatchManager::Apply does not tick anything yet. The envelope state is populated to "Entering, alpha 0" at construction but is not advanced — Stage 3 adds AdvanceEnvelope. All bookkeeping fields are valid as soon as AddPatch returns so debug HUD / introspection work end-to-end.

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `TWeakObjectPtr< UComposableCameraPatchTypeAsset >` | [`SourcePatchAsset`](#sourcepatchasset)  | Source patch asset. Weak — the asset can outlive any single runtime instance. |
| `TObjectPtr< AComposableCameraCameraBase >` | [`Evaluator`](#evaluator)  | The Patch's own camera-actor evaluator. Stage 2+: spawned by AddPatch via [UE::ComposableCameras::ConstructCameraFromTypeAsset](../free-functions/Functions.md#constructcamerafromtypeasset). Stage 1: always nullptr. |
| `int32` | [`LayerIndex`](#layerindex)  | Effective composition order. Resolved from the asset default and the per-AddPatch override (Params.bOverrideLayerIndex true → use Params.LayerIndex). |
| `int32` | [`PushSequence`](#pushsequence)  | Monotonic insertion sequence — tiebreaker for equal LayerIndex. Older first. |
| `uint8` | [`ExpirationType`](#expirationtype-1)  | Bitmask of EComposableCameraPatchExpirationType channels that may fire. |
| `float` | [`Duration`](#duration-5)  |  |
| `bool` | [`bExpireOnCameraChange`](#bexpireoncamerachange)  |  |
| `float` | [`EnterDuration`](#enterduration)  |  |
| `float` | [`ExitDuration`](#exitduration)  |  |
| `EComposableCameraPatchEase` | [`EaseType`](#easetype)  |  |
| `EComposableCameraPatchPhase` | [`Phase`](#phase)  |  |
| `float` | [`ElapsedInPhase`](#elapsedinphase)  | Time spent in the current Phase. Reset to 0 on every phase transition. |
| `float` | [`ElapsedTimeActive`](#elapsedtimeactive)  | Cumulative time spent in the Active phase (used by the Duration channel). |
| `float` | [`CurrentAlpha`](#currentalpha)  |  |
| `float` | [`ExitStartAlpha`](#exitstartalpha)  | The CurrentAlpha at the moment Phase flipped to Exiting. The exit ramp scales the eased curve by this value so a Patch retired mid-Entering fades out from wherever it had reached, instead of popping to 1 first. Stays at 1 by default for the common case (Active → Exiting transition). |
| `FComposableCameraParameterBlock` | [`CachedParameters`](#cachedparameters)  | Cached parameter block from AddPatch. Used by Stage 2's ConstructCameraFromTypeAsset call and any future re-construction (e.g. in response to modifier changes). |
| `TWeakObjectPtr< AComposableCameraCameraBase >` | [`RunningCameraAtAdd`](#runningcameraatadd)  | RunningCamera observed on the owning Director at AddPatch time. When bExpireOnCameraChange is true, the schedule check compares this against the Director's current RunningCamera each frame and flips the Patch to Exiting if they differ (per-patch tracking — a Patch born during camera A never treats its own birth as a "change"). |
| `TWeakObjectPtr< UComposableCameraPatchHandle >` | [`Handle`](#handle)  | Back-link to the user-facing handle. Weak — the handle can be released by the caller while the instance is still alive (the instance keeps running until expiration; the caller has just opted out of further handle queries). |

---

#### SourcePatchAsset { #sourcepatchasset }

```cpp
TWeakObjectPtr< UComposableCameraPatchTypeAsset > SourcePatchAsset
```

Source patch asset. Weak — the asset can outlive any single runtime instance.

---

#### Evaluator { #evaluator }

```cpp
TObjectPtr< AComposableCameraCameraBase > Evaluator
```

The Patch's own camera-actor evaluator. Stage 2+: spawned by AddPatch via [UE::ComposableCameras::ConstructCameraFromTypeAsset](../free-functions/Functions.md#constructcamerafromtypeasset). Stage 1: always nullptr.

---

#### LayerIndex { #layerindex }

```cpp
int32 LayerIndex = 0
```

Effective composition order. Resolved from the asset default and the per-AddPatch override (Params.bOverrideLayerIndex true → use Params.LayerIndex).

---

#### PushSequence { #pushsequence }

```cpp
int32 PushSequence = 0
```

Monotonic insertion sequence — tiebreaker for equal LayerIndex. Older first.

---

#### ExpirationType { #expirationtype-1 }

```cpp
uint8 ExpirationType = 0
```

Bitmask of EComposableCameraPatchExpirationType channels that may fire.

---

#### Duration { #duration-5 }

```cpp
float Duration = 0.f
```

---

#### bExpireOnCameraChange { #bexpireoncamerachange }

```cpp
bool bExpireOnCameraChange = false
```

---

#### EnterDuration { #enterduration }

```cpp
float EnterDuration = 0.f
```

---

#### ExitDuration { #exitduration }

```cpp
float ExitDuration = 0.f
```

---

#### EaseType { #easetype }

```cpp
EComposableCameraPatchEase EaseType = 
```

---

#### Phase { #phase }

```cpp
EComposableCameraPatchPhase Phase = 
```

---

#### ElapsedInPhase { #elapsedinphase }

```cpp
float ElapsedInPhase = 0.f
```

Time spent in the current Phase. Reset to 0 on every phase transition.

---

#### ElapsedTimeActive { #elapsedtimeactive }

```cpp
float ElapsedTimeActive = 0.f
```

Cumulative time spent in the Active phase (used by the Duration channel).

---

#### CurrentAlpha { #currentalpha }

```cpp
float CurrentAlpha = 0.f
```

---

#### ExitStartAlpha { #exitstartalpha }

```cpp
float ExitStartAlpha = 1.f
```

The CurrentAlpha at the moment Phase flipped to Exiting. The exit ramp scales the eased curve by this value so a Patch retired mid-Entering fades out from wherever it had reached, instead of popping to 1 first. Stays at 1 by default for the common case (Active → Exiting transition).

---

#### CachedParameters { #cachedparameters }

```cpp
FComposableCameraParameterBlock CachedParameters
```

Cached parameter block from AddPatch. Used by Stage 2's ConstructCameraFromTypeAsset call and any future re-construction (e.g. in response to modifier changes).

---

#### RunningCameraAtAdd { #runningcameraatadd }

```cpp
TWeakObjectPtr< AComposableCameraCameraBase > RunningCameraAtAdd
```

RunningCamera observed on the owning Director at AddPatch time. When bExpireOnCameraChange is true, the schedule check compares this against the Director's current RunningCamera each frame and flips the Patch to Exiting if they differ (per-patch tracking — a Patch born during camera A never treats its own birth as a "change").

---

#### Handle { #handle }

```cpp
TWeakObjectPtr< UComposableCameraPatchHandle > Handle
```

Back-link to the user-facing handle. Weak — the handle can be released by the caller while the instance is still alive (the instance keeps running until expiration; the caller has just opted out of further handle queries).
