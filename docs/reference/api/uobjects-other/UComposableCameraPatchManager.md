
# UComposableCameraPatchManager { #ucomposablecamerapatchmanager }

```cpp
#include <ComposableCameraPatchManager.h>
```

> **Inherits:** `UObject`

Director-scoped owner of active Camera Patches.

Constructed by [UComposableCameraDirector](../core/UComposableCameraDirector.md#ucomposablecameradirector) at director init (NewObject in the non-CDO branch of the ctor, mirroring how EvaluationTree is built). Lives for the director's lifetime and is destroyed with it.

STAGE 1 (this revision): API surface and bookkeeping in place. AddPatch / ExpirePatch construct and clean up [UComposableCameraPatchInstance](UComposableCameraPatchInstance.md#ucomposablecamerapatchinstance) entries, insert sorted into ActivePatches, and return a [UComposableCameraPatchHandle](UComposableCameraPatchHandle.md#ucomposablecamerapatchhandle). Apply is callable but is a no-op (returns the input pose unchanged) and is NOT yet wired into [UComposableCameraDirector::Evaluate](../core/UComposableCameraDirector.md#evaluate) — no evaluator is spawned and no pose mutation happens. This lets the rest of the system observe ActivePatches via debug surfaces / tests without any user-visible behavior change.

Subsequent stages (per PatchSystemProposal §19): Stage 2 — TickWithInputPose on CameraBase, evaluator spawned via ConstructCameraFromTypeAsset, real Apply at constant alpha = 1, Director::Evaluate wires the call. Stage 3 — Envelope phase machine driving CurrentAlpha. Stage 4 — Duration / Manual / Condition / OnCameraChange expiration. ...

### Public Methods

| Return | Name | Description |
|--------|------|-------------|
|  | [`UComposableCameraPatchManager`](#ucomposablecamerapatchmanager-1)  |  |
| `UComposableCameraPatchHandle *` | [`AddPatch`](#addpatch)  | Add a Patch on this Director. |
| `void` | [`ExpirePatch`](#expirepatch)  | Manually retire a Patch. |
| `FComposableCameraPose` | [`Apply`](#apply)  | Per-frame application pass. |
| `void` | [`DestroyAll`](#destroyall)  | Synchronous teardown of every active Patch. Called when the owning context is popped immediately (non-top context) or the Director itself is being destroyed. Patches in flight do NOT get an exit blend through this path — matching how EvaluationTree is dropped synchronously in the same situations. |
| `void` | [`ExpireAll`](#expireall)  | Soft "expire every active Patch" — flips each one to Exiting via the normal envelope ramp (mirroring per-handle ExpirePatch). Patches mid-Entering fade out from their current alpha; Active-phase patches fade from 1. Already-Exiting / Expired entries are left alone (idempotent). Removal happens in the next Apply pass's end-of-frame sweep, NOT inside this call. |
| `void` | [`ApplyParameterBlockToActivePatch`](#applyparameterblocktoactivepatch)  | Mid-life parameter mutation. Re-applies a parameter block onto the Patch evaluator's runtime data block via the source asset's ApplyParameterBlock — exactly the path the LS Component uses on its own per-tick re-sync (see [UComposableCameraLevelSequenceComponent::TickComponent](UComposableCameraLevelSequenceComponent.md#tickcomponent)). |
| `int32` | [`GetActivePatchCount`](#getactivepatchcount) `const` `inline` |  |
| `const TArray< TObjectPtr< UComposableCameraPatchInstance > > &` | [`GetActivePatches`](#getactivepatches) `const` `inline` |  |
| `void` | [`BuildDebugSnapshot`](#builddebugsnapshot-2) `const` | Capture the current ActivePatches array as a value-type snapshot consumed by the debug HUD / dump commands. Walks ActivePatches in iteration order (sorted by LayerIndex asc, PushSequence asc — same order Apply uses). |

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

Validation (Stage 1): rejects null asset; rejects when the Duration channel is enabled but the resolved Duration is still <= 0. Logs a warning and returns nullptr on rejection.

On success, the instance is sorted-inserted into ActivePatches by (LayerIndex ascending, PushSequence ascending). The returned handle holds a weak reference to the instance.

**Parameters**

* `ParameterBlock` Caller-supplied exposed-parameter / exposed-variable values for the Patch evaluator. Same shape and keyspace as the block accepted by ActivateNewCameraFromTypeAsset; routed through the Patch evaluator's ConstructCameraFromTypeAsset and cached on the runtime instance for later re-construction.

---

#### ExpirePatch { #expirepatch }

```cpp
void ExpirePatch(UComposableCameraPatchHandle * Handle, float ExitDurationOverride)
```

Manually retire a Patch.

Stage 1 implementation: removes the instance from ActivePatches synchronously. Stage 3 will replace this with a phase flip to Exiting + envelope-driven removal at end of Apply.

**Parameters**

* `ExitDurationOverride` < 0 → use the Patch's own ExitDuration. (Unused in Stage 1.)

---

#### Apply { #apply }

```cpp
FComposableCameraPose Apply(float DeltaTime, const FComposableCameraPose & InputPose)
```

Per-frame application pass.

Stage 1 returns InputPose unchanged. Stage 2 fills in: iterate sorted ActivePatches, tick each evaluator with the upstream pose, lerp result by CurrentAlpha. Wired into [UComposableCameraDirector::Evaluate](../core/UComposableCameraDirector.md#evaluate) by Stage 2.

---

#### DestroyAll { #destroyall }

```cpp
void DestroyAll()
```

Synchronous teardown of every active Patch. Called when the owning context is popped immediately (non-top context) or the Director itself is being destroyed. Patches in flight do NOT get an exit blend through this path — matching how EvaluationTree is dropped synchronously in the same situations.

---

#### ExpireAll { #expireall }

```cpp
void ExpireAll(float ExitDurationOverride)
```

Soft "expire every active Patch" — flips each one to Exiting via the normal envelope ramp (mirroring per-handle ExpirePatch). Patches mid-Entering fade out from their current alpha; Active-phase patches fade from 1. Already-Exiting / Expired entries are left alone (idempotent). Removal happens in the next Apply pass's end-of-frame sweep, NOT inside this call.

**Parameters**

* `ExitDurationOverride` < 0 → each patch keeps its own ExitDuration. >= 0 → that value replaces every patch's ExitDuration.

---

#### ApplyParameterBlockToActivePatch { #applyparameterblocktoactivepatch }

```cpp
void ApplyParameterBlockToActivePatch(UComposableCameraPatchHandle * Handle, const FComposableCameraParameterBlock & Parameters)
```

Mid-life parameter mutation. Re-applies a parameter block onto the Patch evaluator's runtime data block via the source asset's ApplyParameterBlock — exactly the path the LS Component uses on its own per-tick re-sync (see [UComposableCameraLevelSequenceComponent::TickComponent](UComposableCameraLevelSequenceComponent.md#tickcomponent)).

Drives Sequencer integration's per-frame parameter keying: the patch track's TrackInstance::OnAnimate rebuilds a block from the section's current bag values and pushes it through this entry once per frame for every still-active section.

Cost is O(exposed-parameter count) per call; ApplyParameterBlock copies typed values directly into the data block with no allocations on hits. Safe to call every frame on the same handle. No-op if the handle is null / stale / already in Exiting / Expired phase, or if the evaluator has no runtime data block yet.

NOTE: this is NOT the broader `SetPatchParameter(handle, name, value)` runtime mutation API — it takes a complete parameter block (every exposed value at once), which is the natural shape Sequencer keys produce. A single-key per-call API is still deferred (PatchSystemProposal §0 "Remaining deferred work") because there is no current driver for it.

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

Capture the current ActivePatches array as a value-type snapshot consumed by the debug HUD / dump commands. Walks ActivePatches in iteration order (sorted by LayerIndex asc, PushSequence asc — same order Apply uses).

### Private Attributes

| Return | Name | Description |
|--------|------|-------------|
| `TArray< TObjectPtr< UComposableCameraPatchInstance > >` | [`ActivePatches`](#activepatches)  | Sorted by (LayerIndex ascending, PushSequence ascending). |
| `int32` | [`NextPushSequence`](#nextpushsequence)  | Monotonic counter — assigned to each new instance's PushSequence on insert. |

---

#### ActivePatches { #activepatches }

```cpp
TArray< TObjectPtr< UComposableCameraPatchInstance > > ActivePatches
```

Sorted by (LayerIndex ascending, PushSequence ascending).

---

#### NextPushSequence { #nextpushsequence }

```cpp
int32 NextPushSequence = 0
```

Monotonic counter — assigned to each new instance's PushSequence on insert.
