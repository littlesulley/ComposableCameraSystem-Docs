# UComposableCameraPatchManager { #ucomposablecamerapatchmanager }

```cpp
#include <ComposableCameraPatchManager.h>
```

> **Inherits:** `UObject`

Director-scoped owner of active Camera Patches.

Constructed by [UComposableCameraDirector](../core/UComposableCameraDirector.md#ucomposablecameradirector) and destroyed with it. `Apply` runs after the director evaluation tree, advances patch envelopes, checks expiration, ticks each patch evaluator with the current upstream pose, and blends outputs in layer order.

### Public Methods

| Return | Name | Description |
|--------|------|-------------|
|  | [`UComposableCameraPatchManager`](#ucomposablecamerapatchmanager-1) | |
| `UComposableCameraPatchHandle *` | [`AddPatch`](#addpatch) | Add a Patch on this Director. |
| `void` | [`ExpirePatch`](#expirepatch) | Manually retire a Patch. |
| `FComposableCameraPose` | [`Apply`](#apply) | Per-frame application pass. |
| `void` | [`DestroyAll`](#destroyall) | Synchronous teardown of every active Patch. |
| `void` | [`ExpireAll`](#expireall) | Soft-expire every active Patch through the normal envelope ramp. |
| `void` | [`ApplyParameterBlockToActivePatch`](#applyparameterblocktoactivepatch) | Mid-life parameter mutation for an active patch evaluator. |
| `int32` | [`GetActivePatchCount`](#getactivepatchcount) `const` `inline` | |
| `const TArray< TObjectPtr< UComposableCameraPatchInstance > > &` | [`GetActivePatches`](#getactivepatches) `const` `inline` | |
| `void` | [`BuildDebugSnapshot`](#builddebugsnapshot-2) `const` | Capture the active patch list for debug HUD and dump commands. |

---

#### UComposableCameraPatchManager { #ucomposablecamerapatchmanager-1 }

```cpp
UComposableCameraPatchManager()
```

---

#### AddPatch { #addpatch }

```cpp
UComposableCameraPatchHandle * AddPatch(UComposableCameraPatchTypeAsset * PatchAsset, const FComposableCameraPatchActivateParams & Params, const FComposableCameraParameterBlock & ParameterBlock)
```

Add a Patch on this Director.

Rejects null assets and Duration-enabled patches whose resolved Duration is `<= 0`. Logs a warning and returns `nullptr` on rejection.

On success, spawns the evaluator camera, builds it from the patch asset, sorted-inserts the instance into `ActivePatches` by `(LayerIndex ascending, PushSequence ascending)`, and returns a handle.

**Parameters**

* `ParameterBlock` Caller-supplied exposed-parameter / exposed-variable values for the Patch evaluator. Same shape and keyspace as the block accepted by `ActivateNewCameraFromTypeAsset`; routed through the Patch evaluator's construction path and cached on the runtime instance for later re-application.

---

#### ExpirePatch { #expirepatch }

```cpp
void ExpirePatch(UComposableCameraPatchHandle * Handle, float ExitDurationOverride)
```

Manually retire a Patch.

Live patches flip to `Exiting` and are removed by `Apply` after the exit envelope reaches `Expired`.

**Parameters**

* `ExitDurationOverride` `< 0` uses the Patch's own exit duration; `0` cuts immediately.

---

#### Apply { #apply }

```cpp
FComposableCameraPose Apply(float DeltaTime, const FComposableCameraPose & InputPose)
```

Per-frame application pass.

Iterates sorted `ActivePatches`. Each non-expired patch sees the pose produced by the tree plus all lower-layer patches, then blends its evaluator output by `CurrentAlpha`.

---

#### DestroyAll { #destroyall }

```cpp
void DestroyAll()
```

Synchronous teardown of every active Patch. Called when the owning context is popped immediately or the Director is being destroyed. Patches in flight do not get an exit blend through this path.

---

#### ExpireAll { #expireall }

```cpp
void ExpireAll(float ExitDurationOverride)
```

Soft-expire every active Patch through the normal envelope ramp. Patches mid-Entering fade out from their current alpha; Active-phase patches fade from 1. Already-Exiting / Expired entries are left alone. Removal happens in the next `Apply` pass end-of-frame sweep.

**Parameters**

* `ExitDurationOverride` `< 0` keeps each patch's own exit duration; `>= 0` replaces every patch's exit duration.

---

#### ApplyParameterBlockToActivePatch { #applyparameterblocktoactivepatch }

```cpp
void ApplyParameterBlockToActivePatch(UComposableCameraPatchHandle * Handle, const FComposableCameraParameterBlock & Parameters)
```

Mid-life parameter mutation. Re-applies a parameter block onto the Patch evaluator's runtime data block via the source asset's `ApplyParameterBlock` path.

The Sequencer patch track uses this every frame for keyed parameter values. No-op if the handle is null, stale, exiting, expired, or if the evaluator has no runtime data block yet.

---

#### GetActivePatchCount { #getactivepatchcount }

`const` `inline`

```cpp
inline int32 GetActivePatchCount() const
```

---

#### GetActivePatches { #getactivepatches }

`const` `inline`

```cpp
inline const TArray< TObjectPtr< UComposableCameraPatchInstance > > & GetActivePatches() const
```

---

#### BuildDebugSnapshot { #builddebugsnapshot-2 }

`const`

```cpp
void BuildDebugSnapshot(TArray< struct FComposableCameraPatchSnapshot > & OutPatches) const
```

Capture the current `ActivePatches` array as a value-type snapshot consumed by debug HUD and dump commands. Walks patches in the same sorted order `Apply` uses.

### Private Attributes

| Return | Name | Description |
|--------|------|-------------|
| `TArray< TObjectPtr< UComposableCameraPatchInstance > >` | [`ActivePatches`](#activepatches) | Sorted by `(LayerIndex ascending, PushSequence ascending)`. |
| `int32` | [`NextPushSequence`](#nextpushsequence) | Monotonic counter assigned to each new instance on insert. |

---

#### ActivePatches { #activepatches }

```cpp
TArray< TObjectPtr< UComposableCameraPatchInstance > > ActivePatches
```

Sorted by `(LayerIndex ascending, PushSequence ascending)`.

---

#### NextPushSequence { #nextpushsequence }

```cpp
int32 NextPushSequence = 0
```

Monotonic counter assigned to each new instance on insert.
