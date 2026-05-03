
# UMovieSceneComposableCameraShotSection { #umoviescenecomposablecamerashotsection }

```cpp
#include <MovieSceneComposableCameraShotSection.h>
```

> **Inherits:** `UMovieSceneSection`, `IMovieSceneEntityProvider`

One section on a `[UMovieSceneComposableCameraShotTrack](UMovieSceneComposableCameraShotTrack.md#umoviescenecomposablecamerashottrack)` — represents a single Shot activation window in the timeline.

The section IS the addressing artifact:

* WHEN the shot is active → the section's TrueRange.

* WHO it applies to → the bound `[AComposableCameraLevelSequenceActor](../actors/AComposableCameraLevelSequenceActor.md#acomposablecameralevelsequenceactor)` resolved through the parent binding row (no per-section `TargetActorBinding` — unlike the Patch section which is root-level).

* WHAT shot data it carries → Inline `[FComposableCameraShot](../structs/FComposableCameraShot.md#fcomposablecamerashot)` value OR soft-ref to a `[UComposableCameraShotAsset](UComposableCameraShotAsset.md#ucomposablecamerashotasset)`.

Per-frame the `UMovieSceneComposableCameraShotTrackInstance::OnAnimate`:

1. Resolves the parent binding → bound LS Actor → its `[UComposableCameraLevelSequenceComponent](UComposableCameraLevelSequenceComponent.md#ucomposablecameralevelsequencecomponent)`.

1. Calls `[ResolveActiveShot()](#resolveactiveshot-1)` to get the active Shot data (Inline or AssetReference deref).

1. Pushes (Section, Shot, RowIndex) to the LS Component via `SetSequencerShotOverride`.

The LS Component's `TickComponent` then picks the top-row override (`MinByRowIndex`) and writes its Shot into the first found `[UComposableCameraCompositionFramingNode::Shot](../nodes/UComposableCameraCompositionFramingNode.md#shot-2)` UPROPERTY on the internal camera before `TickCamera` runs — so the framing solver evaluates with the new data on the same frame.

Phase F (inter-Shot transitions) will replace the top-row picker with a blender; the multi-entry override map already supports this.

No `UMovieSceneParameterSection` inheritance (unlike the Patch section) — Shot fields are not designed for per-frame channel keying. Designers who want a moving target should instead drive the underlying `Targets[i].Actor` via Sequencer's standard transform tracks; the framing solver re-evaluates each frame.

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `EComposableCameraShotSource` | [`Source`](#source-2)  | Source mode picker — Inline (data in Section) vs. AssetReference (data in a ShotAsset). Default Inline because the common authoring flow is one-off shots, and elevating an Inline shot to a reusable asset is trivial later (Right-click → "Save as Shot Asset"; deferred to a later polish step). |
| `FComposableCameraShot` | [`InlineShot`](#inlineshot)  | Used iff `Source == Inline`. Edited via the Shot Editor (single-click on the Section auto-swaps the editor's context — Phase E.5) or inline in the Details panel. |
| `TSoftObjectPtr< UComposableCameraShotAsset >` | [`ShotAssetRef`](#shotassetref)  | Used iff `Source == AssetReference`. Soft-ref so the section doesn't force-load the asset at section construction time / level streaming — resolution happens lazily inside `ResolveActiveShot`. |
| `TArray< FComposableCameraShotTargetActorOverride >` | [`TargetActorOverrides`](#targetactoroverrides)  | Per-target Actor binding overrides. Each entry binds a TargetIndex in the resolved Shot's Targets array to a Sequencer binding picker; the TrackInstance resolves the binding to an Actor at evaluation time and substitutes it into the working Shot copy. |
| `TSoftObjectPtr< UComposableCameraTransitionDataAsset >` | [`EnterTransition`](#entertransition-5)  | Transition asset that drives the inter-Shot blend when the playhead enters this Section from a previous overlapping Section on the same Shot Track (Phase F). |

---

#### Source { #source-2 }

```cpp
EComposableCameraShotSource Source = 
```

Source mode picker — Inline (data in Section) vs. AssetReference (data in a ShotAsset). Default Inline because the common authoring flow is one-off shots, and elevating an Inline shot to a reusable asset is trivial later (Right-click → "Save as Shot Asset"; deferred to a later polish step).

---

#### InlineShot { #inlineshot }

```cpp
FComposableCameraShot InlineShot
```

Used iff `Source == Inline`. Edited via the Shot Editor (single-click on the Section auto-swaps the editor's context — Phase E.5) or inline in the Details panel.

---

#### ShotAssetRef { #shotassetref }

```cpp
TSoftObjectPtr< UComposableCameraShotAsset > ShotAssetRef
```

Used iff `Source == AssetReference`. Soft-ref so the section doesn't force-load the asset at section construction time / level streaming — resolution happens lazily inside `ResolveActiveShot`.

---

#### TargetActorOverrides { #targetactoroverrides }

```cpp
TArray< FComposableCameraShotTargetActorOverride > TargetActorOverrides
```

Per-target Actor binding overrides. Each entry binds a TargetIndex in the resolved Shot's Targets array to a Sequencer binding picker; the TrackInstance resolves the binding to an Actor at evaluation time and substitutes it into the working Shot copy.

Primary use case: an AssetReference Section whose ShotAsset's Targets reference a generic / placeholder Actor (or a Spawnable that doesn't survive level boundaries) — the override pins the actor resolution to a binding inside this sequence. Also useful for Inline Sections when the Inline Shot's Targets reference Spawnables.

---

#### EnterTransition { #entertransition-5 }

```cpp
TSoftObjectPtr< UComposableCameraTransitionDataAsset > EnterTransition
```

Transition asset that drives the inter-Shot blend when the playhead enters this Section from a previous overlapping Section on the same Shot Track (Phase F).

* When two Sections overlap in time, the lower-row Section is the *outgoing* shot and the higher-row Section is the *incoming* shot (top-row by RowIndex). The incoming Section's `EnterTransition` selects how the two solver outputs blend together.

* The overlap window itself defines the blend duration. The Transition asset's `TransitionTime` is ignored — designers control duration via section overlap on the timeline; the transition asset contributes its ease curve / blend math only (handoff §F decision Q4).

* Null = hard cut. The incoming Section snaps in at the boundary; no blend is performed. Equivalent V1 top-row-winner behavior with no overlap region treated as a transition.

* On the *first* Section's left edge (no previous overlapping Section) `EnterTransition` is ignored — there is nothing to blend from (handoff §F decision Q2).

Soft-ref so the section doesn't force-load the transition asset at level streaming time; resolution happens lazily inside the TrackInstance per-frame.

### Public Methods

| Return | Name | Description |
|--------|------|-------------|
|  | [`UMovieSceneComposableCameraShotSection`](#umoviescenecomposablecamerashotsection-1)  |  |
| `void` | [`ImportEntityImpl`](#importentityimpl) `virtual` |  |
| `const FComposableCameraShot *` | [`ResolveActiveShot`](#resolveactiveshot) `const` | Resolves the active Shot for this section. |
| `FComposableCameraShot *` | [`ResolveActiveShot`](#resolveactiveshot-1)  |  |
| `UObject *` | [`ResolveShotEditorHost`](#resolveshoteditorhost) `const` | Resolves the host UObject for the Shot Editor when this Section is selected. Inline → the Section itself; AssetReference → the resolved ShotAsset (or null if unresolved — Shot Editor falls through to its "no shot loaded" placeholder). |
| `bool` | [`BuildEffectiveShot`](#buildeffectiveshot) `const` | Build the effective Shot for this section + the running sequence instance. Starts from `[ResolveActiveShot()](#resolveactiveshot-1)` (Inline / AssetReference), value-copies it into `OutShot`, then walks `TargetActorOverrides` and substitutes each indexed `Targets[i].Target.Actor` with the override binding's resolved actor. |

---

#### UMovieSceneComposableCameraShotSection { #umoviescenecomposablecamerashotsection-1 }

```cpp
UMovieSceneComposableCameraShotSection(const FObjectInitializer & ObjectInitializer)
```

---

#### ImportEntityImpl { #importentityimpl }

`virtual`

```cpp
virtual void ImportEntityImpl(UMovieSceneEntitySystemLinker * EntityLinker, const UE::MovieScene::FEntityImportParams & ImportParams, UE::MovieScene::FImportedEntity * OutImportedEntity)
```

---

#### ResolveActiveShot { #resolveactiveshot }

`const`

```cpp
const FComposableCameraShot * ResolveActiveShot() const
```

Resolves the active Shot for this section.

Inline → returns &InlineShot. AssetReference → loads `ShotAssetRef` (synchronous; soft-pointer `LoadSynchronous`) and returns &Asset->Shot. Returns null if the asset is null or fails to load.

Caller must NOT cache the returned pointer across frames — the AssetReference path may reload the asset, and the soft-ref target may be GC'd between calls. Treat as a per-frame snapshot.

Const overload returns a const pointer for read-only callers (the Shot Editor's Sequencer-selection-sync uses this); non-const overload allows authoring tools that mutate Shot fields directly (the Shot Editor opened in AssetReference mode hosts the mutation on the *asset*, not the Section, so the Section doesn't need to write through).

COMPOSABLECAMERASYSTEM_API: needed because UCLASS(MinimalAPI) only exports the class type info, not member functions, and the editor module's Shot Editor + track editor link against these.

---

#### ResolveActiveShot { #resolveactiveshot-1 }

```cpp
FComposableCameraShot * ResolveActiveShot()
```

---

#### ResolveShotEditorHost { #resolveshoteditorhost }

`const`

```cpp
UObject * ResolveShotEditorHost() const
```

Resolves the host UObject for the Shot Editor when this Section is selected. Inline → the Section itself; AssetReference → the resolved ShotAsset (or null if unresolved — Shot Editor falls through to its "no shot loaded" placeholder).

---

#### BuildEffectiveShot { #buildeffectiveshot }

`const`

```cpp
bool BuildEffectiveShot(const UE::MovieScene::FSequenceInstance & Instance, FComposableCameraShot & OutShot) const
```

Build the effective Shot for this section + the running sequence instance. Starts from `[ResolveActiveShot()](#resolveactiveshot-1)` (Inline / AssetReference), value-copies it into `OutShot`, then walks `TargetActorOverrides` and substitutes each indexed `Targets[i].Target.Actor` with the override binding's resolved actor.

Returns false (OutShot left unchanged) when the source Shot is unresolvable (AssetReference asset null / unloaded). Returns true with a populated OutShot otherwise — overrides whose binding doesn't resolve OR whose TargetIndex is out of range are silently dropped, so a section with stale overrides still produces a valid Shot.

The underlying ShotAsset / InlineShot data is never mutated. The returned working copy is what the TrackInstance pushes into the LS Component's per-frame override map.
