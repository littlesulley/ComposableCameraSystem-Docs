
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

* On-demand tick gating via SetEvaluationEnabled.

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
| `void` | [`SetEvaluationEnabled`](#setevaluationenabled)  | Gate for on-demand ticking. |
| `bool` | [`IsEvaluationEnabled`](#isevaluationenabled) `const` `inline` |  |
| `void` | [`SetParameterValue`](#setparametervalue)  | Forward-compat hooks for a future ECS instantiator. The V1.4 simplified path doesn't route through these — Sequencer's stock property tracks write the bag directly and the per-tick ApplyParameterBlock picks it up. Left in place (as no-ops) so external integrations don't have to be re-wired when a proper instantiator is added later. |
| `void` | [`SetVariableValue`](#setvariablevalue)  |  |
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

Gate for on-demand ticking.

Default: ON. OnRegister unconditionally calls SetEvaluationEnabled(true) so every LS Actor ticks by default (same as pre-Phase-G behavior). The ECS gate (UMovieSceneComposableCameraGateInstantiator) does not "open" the gate — it CLOSES it for tracked entities that aren't currently the Camera Cut Track's target or a blend participant. Entities it cannot reach (pre-upgrade LS assets, UE 5.5+ custom-binding spawnables the hook doesn't see, non-Sequencer hosts) keep the default always-on behavior, which is the correct graceful degradation.

Toggling to false tears down the internal camera so the Actor can go fully idle; toggling back to true respawns it lazily on the first tick.

---

#### IsEvaluationEnabled { #isevaluationenabled }

`const` `inline`

```cpp
inline bool IsEvaluationEnabled() const
```

---

#### SetParameterValue { #setparametervalue }

```cpp
void SetParameterValue(FName Name, const void * Value, EComposableCameraPinType Type)
```

Forward-compat hooks for a future ECS instantiator. The V1.4 simplified path doesn't route through these — Sequencer's stock property tracks write the bag directly and the per-tick ApplyParameterBlock picks it up. Left in place (as no-ops) so external integrations don't have to be re-wired when a proper instantiator is added later.

---

#### SetVariableValue { #setvariablevalue }

```cpp
void SetVariableValue(FName Name, const void * Value, EComposableCameraPinType Type)
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

### Private Attributes

| Return | Name | Description |
|--------|------|-------------|
| `TObjectPtr< AComposableCameraCameraBase >` | [`InternalCamera`](#internalcamera)  | Transient internal camera — spawned lazily on first evaluation. Not added to any context stack or director; driven entirely by this component's TickComponent. |
| `bool` | [`bEvaluationEnabled`](#bevaluationenabled)  | Gate for on-demand ticking; see SetEvaluationEnabled. |
| `TMap< TObjectPtr< UMovieSceneComposableCameraPatchSection >, FComposableCameraSequencerPatchOverlay >` | [`SequencerPatchOverlays`](#sequencerpatchoverlays)  | Active overlays keyed by section. UPROPERTY so the inner TObjectPtrs inside [FComposableCameraSequencerPatchOverlay](../structs/FComposableCameraSequencerPatchOverlay.md#fcomposablecamerasequencerpatchoverlay) are GC-tracked. Pruned on RemoveSequencerPatchOverlay or when the section pointer goes stale. |
| `TMap< TWeakObjectPtr< UMovieSceneComposableCameraShotSection >, FComposableCameraSequencerShotEntry >` | [`SequencerShotOverrides`](#sequencershotoverrides)  | Active Shot overrides keyed by Section. Held by raw section pointer with `TWeakObjectPtr` to tolerate GC of the section between frames (a common case during Sequencer hot-reload / asset reimport). |

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

Gate for on-demand ticking; see SetEvaluationEnabled.

---

#### SequencerPatchOverlays { #sequencerpatchoverlays }

```cpp
TMap< TObjectPtr< UMovieSceneComposableCameraPatchSection >, FComposableCameraSequencerPatchOverlay > SequencerPatchOverlays
```

Active overlays keyed by section. UPROPERTY so the inner TObjectPtrs inside [FComposableCameraSequencerPatchOverlay](../structs/FComposableCameraSequencerPatchOverlay.md#fcomposablecamerasequencerpatchoverlay) are GC-tracked. Pruned on RemoveSequencerPatchOverlay or when the section pointer goes stale.

---

#### SequencerShotOverrides { #sequencershotoverrides }

```cpp
TMap< TWeakObjectPtr< UMovieSceneComposableCameraShotSection >, FComposableCameraSequencerShotEntry > SequencerShotOverrides
```

Active Shot overrides keyed by Section. Held by raw section pointer with `TWeakObjectPtr` to tolerate GC of the section between frames (a common case during Sequencer hot-reload / asset reimport).

### Private Methods

| Return | Name | Description |
|--------|------|-------------|
| `void` | [`EnsureInternalCamera`](#ensureinternalcamera)  | Spawn InternalCamera if it doesn't exist yet, then call ConstructCameraFromTypeAsset with the current bag values. Safe to call repeatedly; reuses an existing camera when the TypeAsset hasn't changed. |
| `void` | [`RebuildInternalCamera`](#rebuildinternalcamera)  | Destroy InternalCamera and spawn a fresh one. Called from PostEditChangeProperty when TypeAsset changes. |
| `void` | [`ProjectPoseToCineCamera`](#projectposetocinecamera)  | Project a pose into OutputCineCameraComponent. Position and rotation are the only fields written; physical optics stay on the CineCamera (designer or Sequencer property tracks drive them). |
| `void` | [`DestroyInternalCamera`](#destroyinternalcamera)  | Destroy the internal camera actor if one exists. |
| `void` | [`ApplySequencerPatchOverlays`](#applysequencerpatchoverlays)  | Apply every active editor-preview patch overlay (sorted by the section's resolved LayerIndex) onto `InOutPose`. Called from TickComponent in editor world only, between InternalCamera->TickCamera and ProjectPoseToCineCamera. Lazy-spawns evaluator actors as needed and prunes stale entries (section GC'd) from the overlay map. |
| `void` | [`ApplyActiveSequencerShotOverride`](#applyactivesequencershotoverride)  | Pick the top-row override (lowest RowIndex) and write its Shot into the first found `[UComposableCameraCompositionFramingNode](../nodes/UComposableCameraCompositionFramingNode.md#ucomposablecameracompositionframingnode)` on the InternalCamera's CameraNodes array. No-op when the map is empty (gap between sections — CompositionFramingNode keeps last-written Shot). |

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

#### ApplyActiveSequencerShotOverride { #applyactivesequencershotoverride }

```cpp
void ApplyActiveSequencerShotOverride()
```

Pick the top-row override (lowest RowIndex) and write its Shot into the first found `[UComposableCameraCompositionFramingNode](../nodes/UComposableCameraCompositionFramingNode.md#ucomposablecameracompositionframingnode)` on the InternalCamera's CameraNodes array. No-op when the map is empty (gap between sections — CompositionFramingNode keeps last-written Shot).

Called from TickComponent BEFORE `InternalCamera->TickCamera` so the solver evaluates with the new Shot data on the same frame.
