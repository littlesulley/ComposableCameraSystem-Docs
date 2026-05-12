# FGetEditorSequencerPlaybackDeltaTime { #fgeteditorsequencerplaybackdeltatime }

```cpp
#include <EditorHooks.h>
```

Runtime-side hook used by `UComposableCameraLevelSequenceComponent` to query editor Sequencer playback delta without linking the runtime module against editor-only Sequencer APIs.

Runtime Level Sequence playback can resolve a `UMovieSceneSequencePlayer` directly. Pure editor preview is driven by `ISequencer`, which lives in the editor module. The editor module binds this delegate and scales world delta by Sequencer playback speed, or returns zero when the editor Sequencer is not playing.

### Public Static Attributes

| Return | Name | Description |
|--------|------|-------------|
| `FGetEditorSequencerPlaybackDelta` | [`GetDeltaTimeDelegate`](#getdeltatimedelegate) `static` | Editor-module callback. Unbound in cooked/non-editor builds. |

---

#### GetDeltaTimeDelegate { #getdeltatimedelegate }

```cpp
FGetEditorSequencerPlaybackDelta GetDeltaTimeDelegate
```

Editor-module callback. The runtime module calls it only through `TryGetDeltaTime`.

### Public Static Methods

| Return | Name | Description |
|--------|------|-------------|
| `bool` | [`TryGetDeltaTime`](#trygetdeltatime) `static` `inline` | Runtime helper. Returns true and fills `OutDeltaTime` only when the editor delegate is bound and recognizes the spawned actor. |

---

#### TryGetDeltaTime { #trygetdeltatime }

`static` `inline`

```cpp
static bool TryGetDeltaTime(const AActor * SpawnedActor, float WorldDeltaTime, float & OutDeltaTime)
```

Runtime helper. Routes through the delegate iff bound and in an editor build; silently returns false otherwise.
