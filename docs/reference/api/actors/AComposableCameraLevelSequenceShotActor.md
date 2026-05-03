
# AComposableCameraLevelSequenceShotActor { #acomposablecameralevelsequenceshotactor }

```cpp
#include <ComposableCameraLevelSequenceShotActor.h>
```

> **Inherits:** [`AComposableCameraLevelSequenceActor`](AComposableCameraLevelSequenceActor.md#acomposablecameralevelsequenceactor)

Specialized `[AComposableCameraLevelSequenceActor](AComposableCameraLevelSequenceActor.md#acomposablecameralevelsequenceactor)` whose `LevelSequenceComponent` comes pre-wired with a system-managed default `[UComposableCameraTypeAsset](../data-assets/UComposableCameraTypeAsset.md#ucomposablecameratypeasset)` — a one-node TypeAsset whose only camera node is a `[UComposableCameraCompositionFramingNode](../nodes/UComposableCameraCompositionFramingNode.md#ucomposablecameracompositionframingnode)`.

Phase E of Shot-Based Keyframing — handoff §"Phase E Final Architecture": 1. Designer drops an AComposableCameraLevelSequenceShotActor into the LS
   as Spawnable or Possessable.
2. The Shot Actor's TypeAssetReference auto-populates with a built-in
   DefaultShotTypeAsset; designer never sees TypeAsset / graph editor /
   evaluation tree.
3. Designer adds a Composable Camera Shot Track under the actor's
   binding row. Shot Sections push framing data into the
   CompositionFramingNode each frame.
 The default TypeAsset is created **in-memory per actor instance** (not as an on-disk asset). This avoids:

* bootstrap timing races against AssetRegistry availability,

* ConstructorHelpers::FObjectFinder failures on first install,

* the user accidentally deleting the system asset.

The owning actor's lifetime carries the TypeAsset (the TypeAsset is outered to this actor and serialized inline as part of the actor's package), so duplication for Spawnable spawning auto-clones the TypeAsset along with the actor.

Power-user override path: the inherited `TypeAssetReference.TypeAsset` field on the LevelSequenceComponent is still settable from the Details panel. Setting a different TypeAsset there bypasses the default (PostInitProperties only seeds when the field is null), so a designer who wants a multi-node camera (e.g. CompositionFramingNode + a downstream shake or noise modifier) can still do so by authoring a custom TypeAsset and assigning it.

### Public Methods

| Return | Name | Description |
|--------|------|-------------|
|  | [`AComposableCameraLevelSequenceShotActor`](#acomposablecameralevelsequenceshotactor-1)  |  |
| `void` | [`EnsureDefaultShotTypeAsset`](#ensuredefaultshottypeasset)  | Construct (or refresh) the default TypeAsset and assign it to the inherited LevelSequenceComponent's TypeAssetReference. Idempotent — skips when a TypeAsset is already set, so designer-supplied custom TypeAssets aren't stomped. Called from PostInitProperties so it runs for every spawned instance, including Sequencer Spawnable duplication. |

---

#### AComposableCameraLevelSequenceShotActor { #acomposablecameralevelsequenceshotactor-1 }

```cpp
AComposableCameraLevelSequenceShotActor(const FObjectInitializer & ObjectInitializer)
```

---

#### EnsureDefaultShotTypeAsset { #ensuredefaultshottypeasset }

```cpp
void EnsureDefaultShotTypeAsset()
```

Construct (or refresh) the default TypeAsset and assign it to the inherited LevelSequenceComponent's TypeAssetReference. Idempotent — skips when a TypeAsset is already set, so designer-supplied custom TypeAssets aren't stomped. Called from PostInitProperties so it runs for every spawned instance, including Sequencer Spawnable duplication.

### Protected Methods

| Return | Name | Description |
|--------|------|-------------|
| `void` | [`PostInitProperties`](#postinitproperties) `virtual` |  |

---

#### PostInitProperties { #postinitproperties }

`virtual`

```cpp
virtual void PostInitProperties()
```

### Private Attributes

| Return | Name | Description |
|--------|------|-------------|
| `TObjectPtr< UComposableCameraTypeAsset >` | [`DefaultShotTypeAsset`](#defaultshottypeasset)  | Owned in-memory TypeAsset — outered to this actor, lifetime bound by it. Visible in the Details panel for inspection (the field shown on the ShotActor itself, NOT the same field on LevelSequenceComponent), but read-only — designers don't author it. |

---

#### DefaultShotTypeAsset { #defaultshottypeasset }

```cpp
TObjectPtr< UComposableCameraTypeAsset > DefaultShotTypeAsset
```

Owned in-memory TypeAsset — outered to this actor, lifetime bound by it. Visible in the Details panel for inspection (the field shown on the ShotActor itself, NOT the same field on LevelSequenceComponent), but read-only — designers don't author it.
