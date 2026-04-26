
# UComposableCameraPatchTypeAsset { #ucomposablecamerapatchtypeasset }

```cpp
#include <ComposableCameraPatchTypeAsset.h>
```

> **Inherits:** [`UComposableCameraTypeAsset`](UComposableCameraTypeAsset.md#ucomposablecameratypeasset)

Data asset describing a Camera Patch type — a small, time-bounded, additively- composable overlay that reads upstream pose, applies a node graph, writes a modified pose. Authored in the same visual editor as [UComposableCameraTypeAsset](UComposableCameraTypeAsset.md#ucomposablecameratypeasset), with no schema change (PatchSystemProposal §5 / §16.8).

Subclasses [UComposableCameraTypeAsset](UComposableCameraTypeAsset.md#ucomposablecameratypeasset) for type-safe API (AddPatch only accepts UComposableCameraPatchTypeAsset*) and a separate Content Browser factory. The graph schema, pin system, parameter / variable system, and runtime data-block layout are all inherited unchanged.

Patch-incompatible nodes (those that ignore InPose and synthesize pose from scratch — e.g. RelativeFixedPose, MixingCamera, ViewTargetProxy) will be caught by the upcoming GetPatchCompatibility() node enum + a yellow-banner editor warning. That enum is introduced in a later staging step (see PatchSystemProposal §11 / §19); until then, any node may be wired into a Patch graph without surface-level guard rails.

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `float` | [`DefaultEnterDuration`](#defaultenterduration)  | Default fade-in duration. Used when AddPatch's EnterDuration sentinel (== 0) is supplied. |
| `float` | [`DefaultExitDuration`](#defaultexitduration)  | Default fade-out duration. Used when AddPatch's ExitDuration sentinel (== 0) is supplied. |
| `EComposableCameraPatchEase` | [`DefaultEaseType`](#defaulteasetype)  | Easing curve applied symmetrically to BOTH the enter and the exit ramp. Asset-only — see EComposableCameraPatchEase doc comment for the rationale (no natural sentinel for an enum). |
| `int32` | [`DefaultLayerIndex`](#defaultlayerindex)  | Default composition order. Lower runs earlier (matches GameplayCameras' StackOrder). Per-AddPatch override available via [FComposableCameraPatchActivateParams::bOverrideLayerIndex](../structs/FComposableCameraPatchActivateParams.md#boverridelayerindex) |
| `uint8` | [`DefaultExpirationType`](#defaultexpirationtype)  | Default expiration channels. Bitmask of EComposableCameraPatchExpirationType. Per-AddPatch override always wins when non-zero (no sentinel — bitmask of 0 from the caller is treated as "use asset default"). |
| `float` | [`DefaultDuration`](#defaultduration)  | Default duration in seconds for the Duration expiration channel. Used when AddPatch's Duration sentinel (== 0) is supplied AND the Duration channel is enabled. |

---

#### DefaultEnterDuration { #defaultenterduration }

```cpp
float DefaultEnterDuration = 0.25f
```

Default fade-in duration. Used when AddPatch's EnterDuration sentinel (== 0) is supplied.

---

#### DefaultExitDuration { #defaultexitduration }

```cpp
float DefaultExitDuration = 0.25f
```

Default fade-out duration. Used when AddPatch's ExitDuration sentinel (== 0) is supplied.

---

#### DefaultEaseType { #defaulteasetype }

```cpp
EComposableCameraPatchEase DefaultEaseType = 
```

Easing curve applied symmetrically to BOTH the enter and the exit ramp. Asset-only — see EComposableCameraPatchEase doc comment for the rationale (no natural sentinel for an enum).

---

#### DefaultLayerIndex { #defaultlayerindex }

```cpp
int32 DefaultLayerIndex = 0
```

Default composition order. Lower runs earlier (matches GameplayCameras' StackOrder). Per-AddPatch override available via [FComposableCameraPatchActivateParams::bOverrideLayerIndex](../structs/FComposableCameraPatchActivateParams.md#boverridelayerindex)

* LayerIndex.

---

#### DefaultExpirationType { #defaultexpirationtype }

```cpp
uint8 DefaultExpirationType = static_cast<uint8>()
```

Default expiration channels. Bitmask of EComposableCameraPatchExpirationType. Per-AddPatch override always wins when non-zero (no sentinel — bitmask of 0 from the caller is treated as "use asset default").

---

#### DefaultDuration { #defaultduration }

```cpp
float DefaultDuration = 0.f
```

Default duration in seconds for the Duration expiration channel. Used when AddPatch's Duration sentinel (== 0) is supplied AND the Duration channel is enabled.

### Public Methods

| Return | Name | Description |
|--------|------|-------------|
| `bool` | [`CanRemain`](#canremain)  | Condition expiration hook. Override in a Blueprint subclass to decide per-frame whether the Patch may remain active. Called ONLY when the Patch is in Active phase AND the Condition bit of ExpirationType is enabled — otherwise it is not consulted. Returning false flips the Patch to Exiting via the standard envelope ramp (same path as Duration expiration and manual ExpirePatch). |
| `bool` | [`CanRemain_Implementation`](#canremain_implementation) `virtual` `inline` |  |

---

#### CanRemain { #canremain }

```cpp
bool CanRemain(float DeltaTime, const FComposableCameraPose & UpstreamPose)
```

Condition expiration hook. Override in a Blueprint subclass to decide per-frame whether the Patch may remain active. Called ONLY when the Patch is in Active phase AND the Condition bit of ExpirationType is enabled — otherwise it is not consulted. Returning false flips the Patch to Exiting via the standard envelope ramp (same path as Duration expiration and manual ExpirePatch).

Signature mirrors [UComposableCameraActionBase::CanExecute](../actions/UComposableCameraActionBase.md#canexecute) (PatchSystemProposal §16.10) — same param shape, same BlueprintNativeEvent idiom. UpstreamPose is the pose this Patch would act on (output of the tree evaluation and all lower-layer Patches this frame); inspect it to write conditions like "stop
when the player is looking below the horizon" or "stop when FOV drops below 30°".

Default implementation returns true (Patch stays) — override in BP to add real gating.

---

#### CanRemain_Implementation { #canremain_implementation }

`virtual` `inline`

```cpp
virtual inline bool CanRemain_Implementation(float DeltaTime, const FComposableCameraPose & UpstreamPose)
```
