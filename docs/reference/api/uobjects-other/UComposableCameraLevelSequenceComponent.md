
# UComposableCameraLevelSequenceComponent { #ucomposablecameralevelsequencecomponent }

```cpp
#include <ComposableCameraLevelSequenceComponent.h>
```

> **Inherits:** `UActorComponent`

Actor component that drives a composable camera in the Level Sequence path.

Holds a [FComposableCameraTypeAssetReference](../structs/FComposableCameraTypeAssetReference.md#fcomposablecameratypeassetreference) (TypeAsset + editable Parameters / Variables bags) and references an OutputCineCameraComponent on the same Actor. On activation, the component spawns a transient [AComposableCameraCameraBase](../actors/AComposableCameraCameraBase.md#acomposablecameracamerabase), runs its nodes each tick (without a PlayerCameraManager), and projects the resulting pose onto the CineCamera so Sequencer's Camera Cut Track and viewport Pilot both see the CCS camera natively via the standard UCameraComponent path.

Pure UActorComponent — NOT a USceneComponent. The component holds no transform of its own; it is a logic-and-data driver. The owning Actor is expected to provide a UCineCameraComponent as its RootComponent (that's what [AComposableCameraLevelSequenceActor](../actors/AComposableCameraLevelSequenceActor.md#acomposablecameralevelsequenceactor) does), and to hand us the reference via OutputCineCameraComponent during construction. If a designer adds this component to an arbitrary Actor (BlueprintSpawnableComponent), OnRegister falls back to FindComponentByClass<UCineCameraComponent>(GetOwner()) — the component will then drive whatever CineCamera is first found on the owning Actor, or be a no-op if none exists.

**Why ActorComponent not SceneComponent**

Previously this was a USceneComponent whose RootComponent role doubled as a parent for the CineCamera child. That arrangement collided with UE's DefaultSubobject semantics (a component creating its own CreateDefaultSubobject<UCineCameraComponent> registered the CineCamera as a sub-subobject of the component, invisible to the Actor's component tree and therefore invisible to USceneComponent::GetChildrenComponents and AActor::FindComponentByClass<UCameraComponent>). PCM::SetViewTarget's implicit-activation filter relies on that traversal and silently bailed, which manifested as "second camera never activates" for blended Camera Cut sections — see the diagnostic log that uncovered it.

With the CineCamera as the Actor's RootComponent and this component as a plain sibling UActorComponent, the engine's standard "find a CameraComponent
on the actor" path trivially finds the root, PCM::SetViewTarget creates the proxy, and we go down the same fast path ACineCameraActor uses. No special-case walks needed.

Compatibility & responsibilities remain unchanged:

* PCM-independent evaluation (via [UE::ComposableCameras::ConstructCameraFromTypeAsset](../free-functions/Functions.md#constructcamerafromtypeasset)).

* Per-tick bag → RuntimeDataBlock re-sync before TickCamera.

* Pose projection to OutputCineCameraComponent (position + rotation only).

* Component evaluation while the owning Level Sequence Spawnable exists, with SetEvaluationEnabled available as a local teardown switch.

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `FComposableCameraTypeAssetReference` | [`TypeAssetReference`](#typeassetreference)  | The TypeAsset reference + its per-instance parameter and variable bags. Editing TypeAsset from the Details panel rebuilds the bags on PostEditChangeProperty; editing individual parameter values rebuilds the internal camera so the new values are reflected in the pose. Not BlueprintReadWrite: the nested FInstancedPropertyBag fields are not Blueprint-supported (see the struct comment). |
| `TObjectPtr< UCineCameraComponent >` | [`OutputCineCameraComponent`](#outputcinecameracomponent-1)  | Reference to the Actor's UCineCameraComponent used as the viewport terminal. Assigned by the owning Actor's constructor (primary path) or resolved in OnRegister via FindComponentByClass (fallback for arbitrary Actor hosts). The component does not own lifetime of the CineCamera — the Actor does. |

---

#### TypeAssetReference { #typeassetreference }

```cpp
FComposableCameraTypeAssetReference TypeAssetReference
```

The TypeAsset reference + its per-instance parameter and variable bags. Editing TypeAsset from the Details panel rebuilds the bags on PostEditChangeProperty; editing individual parameter values rebuilds the internal camera so the new values are reflected in the pose. Not BlueprintReadWrite: the nested FInstancedPropertyBag fields are not Blueprint-supported (see the struct comment).

---

#### OutputCineCameraComponent { #outputcinecameracomponent-1 }

```cpp
TObjectPtr< UCineCameraComponent > OutputCineCameraComponent
```

Reference to the Actor's UCineCameraComponent used as the viewport terminal. Assigned by the owning Actor's constructor (primary path) or resolved in OnRegister via FindComponentByClass (fallback for arbitrary Actor hosts). The component does not own lifetime of the CineCamera — the Actor does.

No edit/visible specifier on purpose: `[AComposableCameraLevelSequenceActor](../actors/AComposableCameraLevelSequenceActor.md#acomposablecameralevelsequenceactor)` exposes the same `UCineCameraComponent` via its own `OutputCineCameraComponent` UPROPERTY (the surface designers actually use to author optics). Adding Visible/EditAnywhere here would create TWO UPROPERTY paths reaching the same component instance — when the Details panel walks the actor's property map, `UpdateSinglePropertyMapRecursive` follows both paths, hits the component on the second path, and recurses without cycle detection (StackOverflow inside SDetailsView::SetObjects on Track / actor selection). Plain `UPROPERTY()` keeps GC tracking + retains the value through serialization but skips Details panel walking.

### Public Methods

| Return | Name | Description |
|--------|------|-------------|
|  | [`UComposableCameraLevelSequenceComponent`](#ucomposablecameralevelsequencecomponent-1)  |  |
| `void` | [`OnRegister`](#onregister) `virtual` |  |
| `void` | [`OnUnregister`](#onunregister) `virtual` |  |
| `void` | [`BeginPlay`](#beginplay-3) `virtual` |  |
| `void` | [`EndPlay`](#endplay-2) `virtual` |  |
| `void` | [`TickComponent`](#tickcomponent) `virtual` |  |
| `void` | [`SetEvaluationEnabled`](#setevaluationenabled)  | Enable or disable component-driven evaluation. |
| `bool` | [`IsEvaluationEnabled`](#isevaluationenabled) `const` `inline` |  |
| `AComposableCameraCameraBase *` | [`GetInternalCamera`](#getinternalcamera) `const` `inline` | Access the internal camera for editor-side inspection / debugging. |
| `void` | [`NotifyTypeAssetExternallyChanged`](#notifytypeassetexternallychanged)  | External "TypeAsset was just swapped" entry for non-Details-panel paths (e.g. the Sequencer track editor's "Camera Type Asset" picker). Performs the same chain `PostEditChangeProperty` does on a TypeAsset edit: rebuild parameter / variable bag layouts from the new asset, then destroy + respawn the InternalCamera so the next tick reflects the new TypeAsset. Caller is responsible for setting `TypeAssetReference.TypeAsset` before calling this. Marks the component dirty for transaction tracking. |
| `void` | [`SetSequencerPatchOverlay`](#setsequencerpatchoverlay)  | Push (or refresh) an overlay registration for `Section`. Called every frame the section is in-range. The pre-computed `EnvelopeAlpha` (from the section's playhead position via `PatchEnvelope::ComputeStatelessAlpha`) drives the BlendBy. The component caches a transient evaluator actor per section (lazy-spawned on first use, destroyed on Remove or component teardown). Intentionally accepts the parameter block by value — caller builds it per-frame from the section's channel curves. |
| `void` | [`RemoveSequencerPatchOverlay`](#removesequencerpatchoverlay)  | Remove an overlay registration when the section leaves its range or when the TrackInstance shuts down. Destroys the cached evaluator actor. Idempotent — safe to call on a section that wasn't registered. |
| `void` | [`BuildSequencerPatchSnapshot`](#buildsequencerpatchsnapshot) `const` | Capture this LS Component's currently-registered Sequencer patch overlays as Debug Panel snapshot rows. Called by the panel's `BuildPatchesLines` (it walks every LS Component in the world and merges results with the PatchManager-side snapshot). One snapshot row per overlay, sorted by the section's resolved LayerIndex (matches the per-tick apply order so the panel rows reflect actual composition order). Each entry has `Source = [EComposableCameraPatchSource::Sequencer](#ComposableCameraDebugPanelData_8h_1aa9c73c4b40ce69b42a63367e19e90b86a0aa30ee67105bbe58a0c35001b9efe88)` and `HostActorName` populated so the renderer can prefix "[Seq]" / suffix "on Actor". |
| `void` | [`SetSequencerShotOverride`](#setsequencershotoverride)  | Push (or refresh) a Shot override for `Section`. Called every frame the section is in-range. The `InEntry` carries the resolved Shot, RowIndex, EnterTransition, and pre-computed BlendAlpha — the TrackInstance does the cross-section overlap analysis once per frame and the LSComponent blender just consumes the result. |
| `void` | [`RemoveSequencerShotOverride`](#removesequencershotoverride)  | Remove a Shot override when the section leaves its range or the TrackInstance shuts down. Idempotent. |

---

#### UComposableCameraLevelSequenceComponent { #ucomposablecameralevelsequencecomponent-1 }

```cpp
UComposableCameraLevelSequenceComponent()
```

---

#### OnRegister { #onregister }

`virtual`

```cpp
virtual void OnRegister()
```

---

#### OnUnregister { #onunregister }

`virtual`

```cpp
virtual void OnUnregister()
```

---

#### BeginPlay { #beginplay-3 }

`virtual`

```cpp
virtual void BeginPlay()
```

---

#### EndPlay { #endplay-2 }

`virtual`

```cpp
virtual void EndPlay(const EEndPlayReason::Type EndPlayReason)
```

---

#### TickComponent { #tickcomponent }

`virtual`

```cpp
virtual void TickComponent(float DeltaTime, ELevelTick TickType, FActorComponentTickFunction * ThisTickFunction)
```

---

#### SetEvaluationEnabled { #setevaluationenabled }

```cpp
void SetEvaluationEnabled(bool bEnabled)
```

Enable or disable component-driven evaluation.

Level Sequence Spawn Tracks own actor lifetime. This flag is a local component switch used by teardown and external hosts; disabling destroys the transient internal camera, and enabling evaluates lazily on the next tick.

---

#### IsEvaluationEnabled { #isevaluationenabled }

`const` `inline`

```cpp
inline bool IsEvaluationEnabled() const
```

---

#### GetInternalCamera { #getinternalcamera }

`const` `inline`

```cpp
inline AComposableCameraCameraBase * GetInternalCamera() const
```

Access the internal camera for editor-side inspection / debugging.

---

#### NotifyTypeAssetExternallyChanged { #notifytypeassetexternallychanged }

```cpp
void NotifyTypeAssetExternallyChanged()
```

External "TypeAsset was just swapped" entry for non-Details-panel paths (e.g. the Sequencer track editor's "Camera Type Asset" picker). Performs the same chain `PostEditChangeProperty` does on a TypeAsset edit: rebuild parameter / variable bag layouts from the new asset, then destroy + respawn the InternalCamera so the next tick reflects the new TypeAsset. Caller is responsible for setting `TypeAssetReference.TypeAsset` before calling this. Marks the component dirty for transaction tracking.

---

#### SetSequencerPatchOverlay { #setsequencerpatchoverlay }

```cpp
void SetSequencerPatchOverlay(UMovieSceneComposableCameraPatchSection * Section, const FComposableCameraParameterBlock & Parameters, float EnvelopeAlpha)
```

Push (or refresh) an overlay registration for `Section`. Called every frame the section is in-range. The pre-computed `EnvelopeAlpha` (from the section's playhead position via `PatchEnvelope::ComputeStatelessAlpha`) drives the BlendBy. The component caches a transient evaluator actor per section (lazy-spawned on first use, destroyed on Remove or component teardown). Intentionally accepts the parameter block by value — caller builds it per-frame from the section's channel curves.

---

#### RemoveSequencerPatchOverlay { #removesequencerpatchoverlay }

```cpp
void RemoveSequencerPatchOverlay(UMovieSceneComposableCameraPatchSection * Section)
```

Remove an overlay registration when the section leaves its range or when the TrackInstance shuts down. Destroys the cached evaluator actor. Idempotent — safe to call on a section that wasn't registered.

---

#### BuildSequencerPatchSnapshot { #buildsequencerpatchsnapshot }

`const`

```cpp
void BuildSequencerPatchSnapshot(TArray< struct FComposableCameraPatchSnapshot > & OutPatches) const
```

Capture this LS Component's currently-registered Sequencer patch overlays as Debug Panel snapshot rows. Called by the panel's `BuildPatchesLines` (it walks every LS Component in the world and merges results with the PatchManager-side snapshot). One snapshot row per overlay, sorted by the section's resolved LayerIndex (matches the per-tick apply order so the panel rows reflect actual composition order). Each entry has `Source = [EComposableCameraPatchSource::Sequencer](#ComposableCameraDebugPanelData_8h_1aa9c73c4b40ce69b42a63367e19e90b86a0aa30ee67105bbe58a0c35001b9efe88)` and `HostActorName` populated so the renderer can prefix "[Seq]" / suffix "on Actor".

---

#### SetSequencerShotOverride { #setsequencershotoverride }

```cpp
void SetSequencerShotOverride(UMovieSceneComposableCameraShotSection * Section, const FComposableCameraSequencerShotEntry & InEntry)
```

Push (or refresh) a Shot override for `Section`. Called every frame the section is in-range. The `InEntry` carries the resolved Shot, RowIndex, EnterTransition, and pre-computed BlendAlpha — the TrackInstance does the cross-section overlap analysis once per frame and the LSComponent blender just consumes the result.

---

#### RemoveSequencerShotOverride { #removesequencershotoverride }

```cpp
void RemoveSequencerShotOverride(UMovieSceneComposableCameraShotSection * Section)
```

Remove a Shot override when the section leaves its range or the TrackInstance shuts down. Idempotent.

### Public Static Methods

| Return | Name | Description |
|--------|------|-------------|
| `void` | [`AddReferencedObjects`](#addreferencedobjects-8) `static` | Walk UObject references inside the non-UPROPERTY-reflected `SequencerPatchOverlays` map. The map keys are weak (intentional — see field doc above), so the TMap itself can't be UPROPERTY-tagged; this override surfaces each overlay's `Evaluator` actor and the UObject contents of its `LatestParameters` parameter block to GC. (Same override also walks `SequencerShotOverrides` — see `LSComponent.cpp::AddReferencedObjects` for the implementation.) |

---

#### AddReferencedObjects { #addreferencedobjects-8 }

`static`

```cpp
static void AddReferencedObjects(UObject * InThis, FReferenceCollector & Collector)
```

Walk UObject references inside the non-UPROPERTY-reflected `SequencerPatchOverlays` map. The map keys are weak (intentional — see field doc above), so the TMap itself can't be UPROPERTY-tagged; this override surfaces each overlay's `Evaluator` actor and the UObject contents of its `LatestParameters` parameter block to GC. (Same override also walks `SequencerShotOverrides` — see `LSComponent.cpp::AddReferencedObjects` for the implementation.)

### Private Attributes

| Return | Name | Description |
|--------|------|-------------|
| `TObjectPtr< AComposableCameraCameraBase >` | [`InternalCamera`](#internalcamera)  | Transient internal camera — spawned lazily on first evaluation. Not added to any context stack or director; driven entirely by this component's TickComponent. |
| `bool` | [`bEvaluationEnabled`](#bevaluationenabled)  | Local evaluation switch; see SetEvaluationEnabled. |
| `bool` | [`bEvaluateNextTickWithZeroDelta`](#bevaluatenexttickwithzerodelta)  | One-shot zero-delta evaluation consumed by TickComponent after enabling. |
| `TMap< TWeakObjectPtr< UMovieSceneComposableCameraPatchSection >, FComposableCameraSequencerPatchOverlay >` | [`SequencerPatchOverlays`](#sequencerpatchoverlays)  | Active overlays keyed by section. Key is `TWeakObjectPtr` (NOT `TObjectPtr`) so a stale section that's been GC'd can actually go stale — a strong-ref key would keep every Sequencer-side patch section alive forever, defeating the prune-on-tick path in `ApplySequencerPatchOverlays` that exists precisely to clean up overlays whose source section has been destroyed (Sequencer rebuild, asset reimport, undo across the section creation, etc.). TMap with TWeakObjectPtr keys cannot be UPROPERTY-reflected, so the inner `Evaluator` / `LatestParameters` UObject references are walked manually in `AddReferencedObjects` below — without that override, the inner Evaluator actor would be GC-blind. The section pointer itself stays alive via Sequencer's own TrackInstance / SectionInterface ownership while it's a live edit target. |
| `TMap< TWeakObjectPtr< UMovieSceneComposableCameraShotSection >, FComposableCameraSequencerShotEntry >` | [`SequencerShotOverrides`](#sequencershotoverrides)  | Active Shot overrides keyed by Section. Held by `TWeakObjectPtr` to tolerate GC of the section between frames (a common case during Sequencer hot-reload / asset reimport). |
| `TWeakObjectPtr< UMovieSceneSequencePlayer >` | [`CachedOwningSequencePlayer`](#cachedowningsequenceplayer)  | Runtime player cache used for Sequencer-aware DeltaTime scaling. |
| `TWeakObjectPtr< UMovieSceneComposableCameraShotSection >` | [`LastActivePrimarySection`](#lastactiveprimarysection)  | Last frame's resolved *primary* Section (lowest RowIndex among the active overrides). `ApplyActiveSequencerShotOverride` compares this to the current frame's primary; mismatch = section transition with no overlap (cut), which the framing node must treat as a hard reseed of its V2.2 damping state to avoid bleeding the previous shot's Distance / FOV / Roll into the new one. Phase F blend exits already trigger the same reseed independently inside `SetActiveShotsFromSequencer`; this tracker is for the non-overlap cut path that the blend logic doesn't cover. |

---

#### InternalCamera { #internalcamera }

```cpp
TObjectPtr< AComposableCameraCameraBase > InternalCamera
```

Transient internal camera — spawned lazily on first evaluation. Not added to any context stack or director; driven entirely by this component's TickComponent.

---

#### bEvaluationEnabled { #bevaluationenabled }

```cpp
bool bEvaluationEnabled = false
```

Local evaluation switch; see SetEvaluationEnabled.

---

#### bEvaluateNextTickWithZeroDelta { #bevaluatenexttickwithzerodelta }

```cpp
bool bEvaluateNextTickWithZeroDelta = false
```

One-shot zero-delta evaluation consumed by TickComponent after enabling, after Sequencer property tracks have written the current bag values.

---

#### SequencerPatchOverlays { #sequencerpatchoverlays }

```cpp
TMap< TWeakObjectPtr< UMovieSceneComposableCameraPatchSection >, FComposableCameraSequencerPatchOverlay > SequencerPatchOverlays
```

Active overlays keyed by section. Key is `TWeakObjectPtr` (NOT `TObjectPtr`) so a stale section that's been GC'd can actually go stale — a strong-ref key would keep every Sequencer-side patch section alive forever, defeating the prune-on-tick path in `ApplySequencerPatchOverlays` that exists precisely to clean up overlays whose source section has been destroyed (Sequencer rebuild, asset reimport, undo across the section creation, etc.). TMap with TWeakObjectPtr keys cannot be UPROPERTY-reflected, so the inner `Evaluator` / `LatestParameters` UObject references are walked manually in `AddReferencedObjects` below — without that override, the inner Evaluator actor would be GC-blind. The section pointer itself stays alive via Sequencer's own TrackInstance / SectionInterface ownership while it's a live edit target.

---

#### SequencerShotOverrides { #sequencershotoverrides }

```cpp
TMap< TWeakObjectPtr< UMovieSceneComposableCameraShotSection >, FComposableCameraSequencerShotEntry > SequencerShotOverrides
```

Active Shot overrides keyed by Section. Held by `TWeakObjectPtr` to tolerate GC of the section between frames (a common case during Sequencer hot-reload / asset reimport).

**Not UPROPERTY** — same constraint as `SequencerPatchOverlays` above: TMap with `TWeakObjectPtr` keys cannot be UHT-reflected. The inner `[FComposableCameraSequencerShotEntry](../structs/FComposableCameraSequencerShotEntry.md#fcomposablecamerasequencershotentry)`'s UObject references (`EnterTransition` TObjectPtr; `Shot` containing FShotTarget TSoftObjectPtr / TObjectPtr resolved to actors) are walked manually in `AddReferencedObjects` via `AddPropertyReferencesWithStructARO` per entry, so reflection's blindness to the outer TMap doesn't leave the resolved transition / target actors GC-blind.

---

#### LastActivePrimarySection { #lastactiveprimarysection }

```cpp
TWeakObjectPtr< UMovieSceneComposableCameraShotSection > LastActivePrimarySection
```

Last frame's resolved *primary* Section (lowest RowIndex among the active overrides). `ApplyActiveSequencerShotOverride` compares this to the current frame's primary; mismatch = section transition with no overlap (cut), which the framing node must treat as a hard reseed of its V2.2 damping state to avoid bleeding the previous shot's Distance / FOV / Roll into the new one. Phase F blend exits already trigger the same reseed independently inside `SetActiveShotsFromSequencer`; this tracker is for the non-overlap cut path that the blend logic doesn't cover.

---

#### CachedOwningSequencePlayer { #cachedowningsequenceplayer }

```cpp
TWeakObjectPtr< UMovieSceneSequencePlayer > CachedOwningSequencePlayer
```

Runtime player cache used for Sequencer-aware DeltaTime scaling. Weak because players can disappear during Sequencer rebuild or PIE teardown.

### Private Methods

| Return | Name | Description |
|--------|------|-------------|
| `void` | [`EnsureInternalCamera`](#ensureinternalcamera)  | Spawn InternalCamera if it doesn't exist yet, then call ConstructCameraFromTypeAsset with the current bag values. Safe to call repeatedly; reuses an existing camera when the TypeAsset hasn't changed. |
| `void` | [`RebuildInternalCamera`](#rebuildinternalcamera)  | Destroy InternalCamera and spawn a fresh one. Called from PostEditChangeProperty when TypeAsset changes. |
| `void` | [`ProjectPoseToCineCamera`](#projectposetocinecamera)  | Project a pose into OutputCineCameraComponent. Position and rotation are the only fields written; physical optics stay on the CineCamera (designer or Sequencer property tracks drive them). |
| `void` | [`DestroyInternalCamera`](#destroyinternalcamera)  | Destroy the internal camera actor if one exists. |
| `void` | [`ApplySequencerPatchOverlays`](#applysequencerpatchoverlays)  | Apply every active editor-preview patch overlay (sorted by the section's resolved LayerIndex) onto `InOutPose`. Called from TickComponent in editor world only, between InternalCamera->TickCamera and ProjectPoseToCineCamera. Lazy-spawns evaluator actors as needed and prunes stale entries (section GC'd) from the overlay map. |
| `float` | [`ResolveSequencerAwareDeltaTime`](#resolvesequencerawaredeltatime)  | Resolve a DeltaTime that follows the owning Level Sequence playback speed. |
| `UMovieSceneSequencePlayer *` | [`ResolveOwningSequencePlayer`](#resolveowningsequenceplayer)  | Find the runtime sequence player whose spawn register owns this component's Actor. |
| `void` | [`ApplyActiveSequencerShotOverride`](#applyactivesequencershotoverride)  | Pick the top-row override (lowest RowIndex) and write its Shot into the first found `[UComposableCameraCompositionFramingNode](../nodes/UComposableCameraCompositionFramingNode.md#ucomposablecameracompositionframingnode)` on the InternalCamera's CameraNodes array. No-op when the map is empty (gap between sections — CompositionFramingNode keeps last-written Shot). |
| `void` | [`EvaluateOnce`](#evaluateonce)  | Run one full evaluation pass (parameter block sync -> Shot override apply -> InternalCamera TickCamera -> patch overlays -> CineCamera projection). Used by TickComponent and by the Shot override first-entry path. |

---

#### EnsureInternalCamera { #ensureinternalcamera }

```cpp
void EnsureInternalCamera()
```

Spawn InternalCamera if it doesn't exist yet, then call ConstructCameraFromTypeAsset with the current bag values. Safe to call repeatedly; reuses an existing camera when the TypeAsset hasn't changed.

---

#### RebuildInternalCamera { #rebuildinternalcamera }

```cpp
void RebuildInternalCamera()
```

Destroy InternalCamera and spawn a fresh one. Called from PostEditChangeProperty when TypeAsset changes.

---

#### ProjectPoseToCineCamera { #projectposetocinecamera }

```cpp
void ProjectPoseToCineCamera(const FComposableCameraPose & Pose)
```

Project a pose into OutputCineCameraComponent. Position and rotation are the only fields written; physical optics stay on the CineCamera (designer or Sequencer property tracks drive them).

---

#### DestroyInternalCamera { #destroyinternalcamera }

```cpp
void DestroyInternalCamera()
```

Destroy the internal camera actor if one exists.

---

#### ApplySequencerPatchOverlays { #applysequencerpatchoverlays }

```cpp
void ApplySequencerPatchOverlays(FComposableCameraPose & InOutPose, float DeltaTime)
```

Apply every active editor-preview patch overlay (sorted by the section's resolved LayerIndex) onto `InOutPose`. Called from TickComponent in editor world only, between InternalCamera->TickCamera and ProjectPoseToCineCamera. Lazy-spawns evaluator actors as needed and prunes stale entries (section GC'd) from the overlay map.

---

#### ResolveSequencerAwareDeltaTime { #resolvesequencerawaredeltatime }

```cpp
float ResolveSequencerAwareDeltaTime(float WorldDeltaTime)
```

Resolve a DeltaTime that follows the owning Level Sequence playback speed. Editor preview resolves through the editor hook; runtime playback resolves through the owning `UMovieSceneSequencePlayer`. Paused Sequencer preview returns zero so history-dependent nodes do not advance while scrubbing or stopped.

---

#### ResolveOwningSequencePlayer { #resolveowningsequenceplayer }

```cpp
UMovieSceneSequencePlayer * ResolveOwningSequencePlayer()
```

Find the runtime sequence player whose spawn register owns this component's Actor. Used for runtime Sequencer-aware DeltaTime scaling.

---

#### ApplyActiveSequencerShotOverride { #applyactivesequencershotoverride }

```cpp
void ApplyActiveSequencerShotOverride()
```

Pick the top-row override (lowest RowIndex) and write its Shot into the first found `[UComposableCameraCompositionFramingNode](../nodes/UComposableCameraCompositionFramingNode.md#ucomposablecameracompositionframingnode)` on the InternalCamera's CameraNodes array. No-op when the map is empty (gap between sections — CompositionFramingNode keeps last-written Shot).

Called from TickComponent BEFORE `InternalCamera->TickCamera` so the solver evaluates with the new Shot data on the same frame.

---

#### EvaluateOnce { #evaluateonce }

```cpp
void EvaluateOnce(float DeltaTime)
```

Run one full evaluation pass (parameter block sync -> Shot override apply -> InternalCamera TickCamera -> patch overlays -> CineCamera projection). Identical to a `TickComponent` body sans the `Super::TickComponent` / evaluation guard. Used by TickComponent and by the Shot override first-entry path, where Sequencer has already pushed the current section data and the CineCamera must be re-projected before the cut renders.

`DeltaTime <= 0` is the standard "first-frame snap" signal — downstream solvers (V2.2 IIR damping, scrub-aware nodes) treat it as "use authored values, don't damp", which matches the cut-as-cut design intent.
