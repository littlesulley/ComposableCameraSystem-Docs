# UMovieSceneComposableCameraShotSection { #umoviescenecomposablecamerashotsection }

```cpp
#include <MovieSceneComposableCameraShotSection.h>
```

> **Inherits:** `UMovieSceneSection`, `IMovieSceneEntityProvider`

One section on a [`UMovieSceneComposableCameraShotTrack`](UMovieSceneComposableCameraShotTrack.md#umoviescenecomposablecamerashottrack). It defines when a Shot is active, which bound `AComposableCameraLevelSequenceActor` receives it, and which Shot data is pushed into the Level Sequence component.

Per frame, the Shot track instance resolves the parent binding to the Level Sequence actor, calls [`BuildEffectiveShot()`](#buildeffectiveshot), and pushes `(Section, Shot, RowIndex)` to `UComposableCameraLevelSequenceComponent::SetSequencerShotOverride`.

Inline sections store their editable Shot in [`InlineShot`](#inlineshot). Asset-backed sections store a soft reference in [`ShotAssetRef`](#shotassetref), but the editable runtime data is the section-local [`ShotOverrides`](#shotoverrides) snapshot seeded from that asset. Later Sequencer edits mutate only the section copy; the shared Shot Asset remains the template for new sections.

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `EComposableCameraShotSource` | [`Source`](#source-2) | Source mode picker: `Inline` or `AssetReference`. |
| `FComposableCameraShot` | [`InlineShot`](#inlineshot) | Used iff `Source == Inline`; edited by the Shot Editor or Details panel. |
| `TSoftObjectPtr< UComposableCameraShotAsset >` | [`ShotAssetRef`](#shotassetref) | Used iff `Source == AssetReference`; picking/changing the asset seeds `ShotOverrides`. |
| `TArray< FComposableCameraShotTargetActorOverride >` | [`TargetActorOverrides`](#targetactoroverrides) | Per-target Sequencer actor binding overrides. |
| `FComposableCameraShot` | [`ShotOverrides`](#shotoverrides) | AssetReference-only editable section copy seeded from `ShotAssetRef`. |
| `bool` | [`bShotOverridesInitialized`](#bshotoverridesinitialized) | Migration guard so saved section-local edits are not re-copied from the asset every load. |
| `TSoftObjectPtr< UComposableCameraTransitionDataAsset >` | [`EnterTransition`](#entertransition-5) | Transition asset used when the playhead enters this section from an overlapping previous Shot section. |

---

#### Source { #source-2 }

```cpp
EComposableCameraShotSource Source = EComposableCameraShotSource::Inline
```

Source mode picker. `Inline` stores Shot data directly in the section. `AssetReference` stores a Shot Asset reference plus a section-local editable snapshot.

---

#### InlineShot { #inlineshot }

```cpp
FComposableCameraShot InlineShot
```

Used iff `Source == Inline`. The Shot Editor edits this value when an inline section is selected.

---

#### ShotAssetRef { #shotassetref }

```cpp
TSoftObjectPtr< UComposableCameraShotAsset > ShotAssetRef
```

Used iff `Source == AssetReference`. Changing this reference calls [`RefreshShotOverridesFromSource()`](#refreshshotoverridesfromsource), copying the asset's `Shot` into [`ShotOverrides`](#shotoverrides).

---

#### TargetActorOverrides { #targetactoroverrides }

```cpp
TArray< FComposableCameraShotTargetActorOverride > TargetActorOverrides
```

Each entry maps a target index in the effective Shot to a Sequencer binding. At evaluation time the binding resolves to an Actor and replaces `Targets[TargetIndex].Target.Actor` in the working Shot copy. This supports Spawnables, reusable Shot Assets, and sequences that reuse one framing preset with different actors.

---

#### ShotOverrides { #shotoverrides }

```cpp
FComposableCameraShot ShotOverrides
```

AssetReference-only editable copy shown by the Shot Editor. Runtime consumes this section-local value directly and never writes back to the shared Shot Asset.

---

#### bShotOverridesInitialized { #bshotoverridesinitialized }

```cpp
bool bShotOverridesInitialized = false
```

Migration/init guard for AssetReference snapshots. Existing sections created before `ShotOverrides` existed initialize once from the Shot Asset on `PostLoad`; saved section-local edits are not re-copied every load.

---

#### EnterTransition { #entertransition-5 }

```cpp
TSoftObjectPtr< UComposableCameraTransitionDataAsset > EnterTransition
```

Transition asset used when the playhead enters this section from a previous overlapping section on the same Shot Track. The overlap window controls duration; the transition asset contributes blend behavior. Null means a hard cut.

### Public Methods

| Return | Name | Description |
|--------|------|-------------|
|  | [`UMovieSceneComposableCameraShotSection`](#umoviescenecomposablecamerashotsection-1) | Constructor. |
| `void` | [`ImportEntityImpl`](#importentityimpl) `virtual` | Emits a per-section track instance dispatch. |
| `const FComposableCameraShot *` | [`ResolveActiveShot`](#resolveactiveshot) `const` | Resolves the active section Shot pointer. |
| `FComposableCameraShot *` | [`ResolveActiveShot`](#resolveactiveshot-1) | Mutable overload. |
| `FComposableCameraShot *` | [`ResolveShotEditorShot`](#resolveshoteditorshot) | Shot data the Shot Editor should edit for this section. |
| `UObject *` | [`ResolveShotEditorHost`](#resolveshoteditorhost) `const` | Host UObject for Shot Editor transactions. |
| `bool` | [`BuildEffectiveShotWithoutBindings`](#buildeffectiveshotwithoutbindings) `const` | Builds the base effective Shot before target binding overrides. |
| `void` | [`RefreshShotOverridesFromSource`](#refreshshotoverridesfromsource) | Copies Shot Asset defaults into `ShotOverrides`. |
| `bool` | [`BuildEffectiveShot`](#buildeffectiveshot) `const` | Builds the final effective Shot for evaluation. |
| `UComposableCameraShotAsset *` | [`ResolveCachedShotAsset`](#resolvecachedshotasset) `const` | Resolves the cached Shot Asset pointer without blocking the eval path. |
| `UComposableCameraTransitionDataAsset *` | [`ResolveCachedEnterTransition`](#resolvecachedentertransition) `const` | Resolves the cached transition pointer without blocking the eval path. |
| `void` | [`PostLoad`](#postload) `virtual` | Refreshes caches and initializes legacy AssetReference snapshots. |

---

#### UMovieSceneComposableCameraShotSection { #umoviescenecomposablecamerashotsection-1 }

```cpp
UMovieSceneComposableCameraShotSection(const FObjectInitializer& ObjectInitializer)
```

---

#### ImportEntityImpl { #importentityimpl }

`virtual`

```cpp
virtual void ImportEntityImpl(UMovieSceneEntitySystemLinker* EntityLinker, const UE::MovieScene::FEntityImportParams& ImportParams, UE::MovieScene::FImportedEntity* OutImportedEntity)
```

---

#### ResolveActiveShot { #resolveactiveshot }

`const`

```cpp
const FComposableCameraShot* ResolveActiveShot() const
```

Returns `&InlineShot` for inline sections. Returns `&ShotOverrides` for AssetReference sections when `ShotAssetRef` is assigned; returns null when no asset is assigned. Callers should not cache the pointer beyond the section lifetime.

---

#### ResolveActiveShot { #resolveactiveshot-1 }

```cpp
FComposableCameraShot* ResolveActiveShot()
```

Mutable overload of [`ResolveActiveShot()`](#resolveactiveshot). AssetReference authoring should prefer [`ResolveShotEditorShot()`](#resolveshoteditorshot) so edits explicitly land on the section-local override copy.

---

#### ResolveShotEditorShot { #resolveshoteditorshot }

```cpp
FComposableCameraShot* ResolveShotEditorShot()
```

Returns the Shot data the Shot Editor should mutate: `InlineShot` for inline sections, `ShotOverrides` for AssetReference sections, or null when an AssetReference section has no asset assigned.

---

#### ResolveShotEditorHost { #resolveshoteditorhost }

`const`

```cpp
UObject* ResolveShotEditorHost() const
```

Returns the section itself in both source modes so Shot Editor transactions and dirtying apply to the Level Sequence section, not the shared Shot Asset.

---

#### BuildEffectiveShotWithoutBindings { #buildeffectiveshotwithoutbindings }

`const`

```cpp
bool BuildEffectiveShotWithoutBindings(FComposableCameraShot& OutShot) const
```

Copies `InlineShot` or `ShotOverrides` into `OutShot` before Sequencer actor-binding overrides are applied. Returns false when an AssetReference section has no assigned `ShotAssetRef`.

---

#### RefreshShotOverridesFromSource { #refreshshotoverridesfromsource }

```cpp
void RefreshShotOverridesFromSource()
```

Copies the current Shot Asset defaults into `ShotOverrides`. Called when the user changes `Source` or `ShotAssetRef`, and once during legacy section migration; normal evaluation and editor refresh do not re-copy the asset.

---

#### BuildEffectiveShot { #buildeffectiveshot }

`const`

```cpp
bool BuildEffectiveShot(const UE::MovieScene::FSequenceInstance& Instance, FComposableCameraShot& OutShot) const
```

Starts from [`BuildEffectiveShotWithoutBindings()`](#buildeffectiveshotwithoutbindings), then walks `TargetActorOverrides` and substitutes each indexed `Targets[i].Target.Actor` with the actor resolved from the running Sequencer binding. Stale target indices or unresolved bindings are skipped without mutating source data.

---

#### ResolveCachedShotAsset { #resolvecachedshotasset }

`const`

```cpp
UComposableCameraShotAsset* ResolveCachedShotAsset() const
```

Resolves the cached `ShotAssetRef` pointer. The cache is refreshed off the evaluation path; AssetReference evaluation reads `ShotOverrides`, not the asset's `Shot` field.

---

#### ResolveCachedEnterTransition { #resolvecachedentertransition }

`const`

```cpp
UComposableCameraTransitionDataAsset* ResolveCachedEnterTransition() const
```

Resolves the cached `EnterTransition` pointer. An unloaded transition degrades to a hard cut instead of blocking evaluation.

---

#### PostLoad { #postload }

`virtual`

```cpp
virtual void PostLoad()
```

Refreshes cached assets and initializes `ShotOverrides` once for legacy AssetReference sections that do not yet have a saved snapshot.

### Private Attributes

| Return | Name | Description |
|--------|------|-------------|
| `TObjectPtr< UComposableCameraShotAsset >` | [`CachedShotAsset`](#cachedshotasset) | Cached resolved shot asset used for off-path snapshot refresh. |
| `TObjectPtr< UComposableCameraTransitionDataAsset >` | [`CachedEnterTransition`](#cachedentertransition) | Cached resolved transition asset. |

---

#### CachedShotAsset { #cachedshotasset }

```cpp
TObjectPtr< UComposableCameraShotAsset > CachedShotAsset
```

Cached resolved shot asset used when seeding `ShotOverrides`.

---

#### CachedEnterTransition { #cachedentertransition }

```cpp
TObjectPtr< UComposableCameraTransitionDataAsset > CachedEnterTransition
```

### Private Methods

| Return | Name | Description |
|--------|------|-------------|
| `void` | [`RefreshCachedAssets`](#refreshcachedassets) | Off-hot-path refresh for cached Shot Asset and transition pointers. |

---

#### RefreshCachedAssets { #refreshcachedassets }

```cpp
void RefreshCachedAssets()
```

Refreshes cached soft-reference targets outside the evaluation path.
