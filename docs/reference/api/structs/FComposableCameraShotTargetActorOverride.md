
# FComposableCameraShotTargetActorOverride { #fcomposablecamerashottargetactoroverride }

```cpp
#include <MovieSceneComposableCameraShotSection.h>
```

Per-target Actor override for a `[UMovieSceneComposableCameraShotSection](../uobjects-other/UMovieSceneComposableCameraShotSection.md#umoviescenecomposablecamerashotsection)`.

The framing data carried by a Shot (`[FComposableCameraShot::Targets](FComposableCameraShot.md#targets)[i].Target.Actor`) is a `TSoftObjectPtr<AActor>` which can only refer to actors that exist as persistent / package-scoped instances in some level. That works for Possessables in the level where the ShotAsset / Inline shot was authored, but it breaks for:

* Sequencer Spawnables (instantiated only while the section is alive),

* Possessables in a different level than where the ShotAsset was authored,

* reusable ShotAssets dragged across many sequences.

Each override entry on the Section binds a TargetIndex inside the resolved Shot's Targets array to a Sequencer FMovieSceneObjectBindingID. At evaluation time, the TrackInstance resolves the binding through the running sequence instance and substitutes the resulting actor into a value-copy of the Shot — the underlying ShotAsset / InlineShot data is never mutated, so the same ShotAsset can be reused across sections / sequences each with their own bindings.

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `int32` | [`TargetIndex`](#targetindex-2)  | Index into the resolved Shot's Targets array. Overrides for indices outside the array (stale ShotAsset edit, mismatched count) are silently dropped at evaluation time — designer's data isn't damaged by a count-drift between authoring and runtime. |
| `FMovieSceneObjectBindingID` | [`Binding`](#binding)  | Sequencer binding whose resolved Actor replaces `Targets[TargetIndex].Target.Actor`. Works with Spawnables, Possessables, and cross-sequence sub-bindings — same picker UX as Camera Cut Track's CameraBindingID. |

---

#### TargetIndex { #targetindex-2 }

```cpp
int32 TargetIndex = 0
```

Index into the resolved Shot's Targets array. Overrides for indices outside the array (stale ShotAsset edit, mismatched count) are silently dropped at evaluation time — designer's data isn't damaged by a count-drift between authoring and runtime.

---

#### Binding { #binding }

```cpp
FMovieSceneObjectBindingID Binding
```

Sequencer binding whose resolved Actor replaces `Targets[TargetIndex].Target.Actor`. Works with Spawnables, Possessables, and cross-sequence sub-bindings — same picker UX as Camera Cut Track's CameraBindingID.
