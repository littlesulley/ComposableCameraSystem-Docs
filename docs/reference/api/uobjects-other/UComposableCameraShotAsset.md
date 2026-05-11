
# UComposableCameraShotAsset { #ucomposablecamerashotasset }

```cpp
#include <ComposableCameraShotAsset.h>
```

> **Inherits:** `UDataAsset`

Reusable Shot data asset — a `UDataAsset` wrapping one `[FComposableCameraShot](../structs/FComposableCameraShot.md#fcomposablecamerashot)`.

Phase E of Shot-Based Keyframing introduces two storage modes for Shot data carried by a `[UMovieSceneComposableCameraShotSection](UMovieSceneComposableCameraShotSection.md#umoviescenecomposablecamerashotsection)` (spec §3.4.1):

* **Inline**: Shot value-typed inside the Section. One-off framing for a specific moment in a sequence.

* **AssetReference**: Section soft-refs a `[UComposableCameraShotAsset](#ucomposablecamerashotasset)`. Picking the asset snapshots its Shot into the section's local `ShotOverrides`; later Sequencer edits affect that section copy, while the asset remains the reusable template for future sections.

This class is the AssetReference template. It carries no behavior of its own - it is a data envelope. The Shot Editor edits the asset directly when it is opened from the Content Browser, but Sequencer AssetReference sections edit their section-local `ShotOverrides` snapshots.

The shot asset is **not** related to `[UComposableCameraTypeAsset](../data-assets/UComposableCameraTypeAsset.md#ucomposablecameratypeasset)` / `[UComposableCameraPatchTypeAsset](../data-assets/UComposableCameraPatchTypeAsset.md#ucomposablecamerapatchtypeasset)`; those carry node graphs and are run by the camera evaluation pipeline. ShotAsset just stores a `[FComposableCameraShot](../structs/FComposableCameraShot.md#fcomposablecamerashot)` struct that the Shot Track's evaluator pushes into the runtime `[UComposableCameraCompositionFramingNode::Shot](../nodes/UComposableCameraCompositionFramingNode.md#shot-2)` UPROPERTY at the playhead.

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `FComposableCameraShot` | [`Shot`](#shot)  | Authored shot. Edited via the Shot Editor (Phase D) or the Details panel when opened directly from the Content Browser. |

---

#### Shot { #shot }

```cpp
FComposableCameraShot Shot
```

Authored shot. Edited via the Shot Editor (Phase D) or the Details panel when opened directly from the Content Browser.
