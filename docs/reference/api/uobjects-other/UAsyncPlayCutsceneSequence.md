
# UAsyncPlayCutsceneSequence { #uasyncplaycutscenesequence }

```cpp
#include <AsyncPlayCutsceneSequence.h>
```

> **Inherits:** `UBlueprintAsyncActionBase`

Action that plays a level sequence as a CCS cutscene.

This is the high-level entry point for Level Sequence integration. It handles:

1. Pushing a cutscene context (inter-context transition from gameplay).

1. Starting ULevelSequencePlayer playback with user-provided settings.

1. Popping the cutscene context when the LS ends (or is manually stopped).

Camera cuts within the LS are handled by the engine's CameraCut track, which calls SetViewTarget on the PCM at each section boundary. The PCM's overridden SetViewTarget creates transient proxy cameras for each LS camera actor and activates them in the cutscene context's director with CCS transitions converted from FViewTargetTransitionParams (implicit camera activation).

Blueprint usage: The "Play Cutscene Sequence" K2 node (UK2Node_PlayCutsceneSequence) provides a "Cutscene Action" output pin and an "On Finished" exec pin. Cache the Cutscene Action to call [StopCutsceneSequence()](#stopcutscenesequence) later.

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `FOnCutsceneSequenceFinished` | [`OnFinished`](#onfinished)  | Fires when the level sequence finishes playing (not fired on infinite loop or manual stop). |

---

#### OnFinished { #onfinished }

```cpp
FOnCutsceneSequenceFinished OnFinished
```

Fires when the level sequence finishes playing (not fired on infinite loop or manual stop).

### Public Methods

| Return | Name | Description |
|--------|------|-------------|
| `void` | [`StopCutsceneSequence`](#stopcutscenesequence)  | Stop the cutscene, pop the cutscene context, and clean up all resources. Triggers an inter-context transition back to gameplay using ExitTransition. |
| `void` | [`Activate`](#activate) `virtual` |  |

---

#### StopCutsceneSequence { #stopcutscenesequence }

```cpp
void StopCutsceneSequence(UComposableCameraTransitionDataAsset * ExitTransition)
```

Stop the cutscene, pop the cutscene context, and clean up all resources. Triggers an inter-context transition back to gameplay using ExitTransition.

**Parameters**

* `ExitTransition` Optional transition for the context pop back to gameplay. If nullptr, falls back to the resume camera's default enter transition.

---

#### Activate { #activate }

`virtual`

```cpp
virtual void Activate()
```

### Public Static Methods

| Return | Name | Description |
|--------|------|-------------|
| `UAsyncPlayCutsceneSequence *` | [`Create`](#create) `static` | Create the action and register it with the game instance. Does NOT call [Activate()](#activate) — the K2 node's ExpandNode handles that after delegate binding. |

---

#### Create { #create }

`static`

```cpp
static UAsyncPlayCutsceneSequence * Create(UObject * WorldContextObject, ULevelSequence * InLevelSequence, FName ContextName, UComposableCameraTransitionDataAsset * InEnterTransition, FMovieSceneSequencePlaybackSettings PlaybackSettings)
```

Create the action and register it with the game instance. Does NOT call [Activate()](#activate) — the K2 node's ExpandNode handles that after delegate binding.

This is a plain C++ static, not a UFUNCTION. The Blueprint entry point is [UComposableCameraBlueprintLibrary::PlayCutsceneSequence](../blueprint/UComposableCameraBlueprintLibrary.md#playcutscenesequence), which the K2 node calls via ExpandNode.

### Private Attributes

| Return | Name | Description |
|--------|------|-------------|
| `TObjectPtr< ULevelSequence >` | [`LevelSequence`](#levelsequence)  |  |
| `TObjectPtr< ULevelSequencePlayer >` | [`SequencePlayer`](#sequenceplayer)  |  |
| `TObjectPtr< ALevelSequenceActor >` | [`SequenceActor`](#sequenceactor)  |  |
| `TObjectPtr< UComposableCameraTransitionDataAsset >` | [`EnterTransition`](#entertransition)  |  |
| `TWeakObjectPtr< AComposableCameraPlayerCameraManager >` | [`CachedPCM`](#cachedpcm)  |  |
| `TWeakObjectPtr< UWorld >` | [`CachedWorld`](#cachedworld)  | Cached from the WorldContextObject in the factory — GetWorld() on the base class is unreliable. |
| `FName` | [`CutsceneContextName`](#cutscenecontextname)  |  |
| `FMovieSceneSequencePlaybackSettings` | [`CachedPlaybackSettings`](#cachedplaybacksettings)  |  |
| `bool` | [`bIsActive`](#bisactive)  |  |

---

#### LevelSequence { #levelsequence }

```cpp
TObjectPtr< ULevelSequence > LevelSequence
```

---

#### SequencePlayer { #sequenceplayer }

```cpp
TObjectPtr< ULevelSequencePlayer > SequencePlayer
```

---

#### SequenceActor { #sequenceactor }

```cpp
TObjectPtr< ALevelSequenceActor > SequenceActor
```

---

#### EnterTransition { #entertransition }

```cpp
TObjectPtr< UComposableCameraTransitionDataAsset > EnterTransition
```

---

#### CachedPCM { #cachedpcm }

```cpp
TWeakObjectPtr< AComposableCameraPlayerCameraManager > CachedPCM
```

---

#### CachedWorld { #cachedworld }

```cpp
TWeakObjectPtr< UWorld > CachedWorld
```

Cached from the WorldContextObject in the factory — GetWorld() on the base class is unreliable.

---

#### CutsceneContextName { #cutscenecontextname }

```cpp
FName CutsceneContextName
```

---

#### CachedPlaybackSettings { #cachedplaybacksettings }

```cpp
FMovieSceneSequencePlaybackSettings CachedPlaybackSettings
```

---

#### bIsActive { #bisactive }

```cpp
bool bIsActive { false }
```

### Private Methods

| Return | Name | Description |
|--------|------|-------------|
| `void` | [`OnSequenceFinished`](#onsequencefinished)  | Called when the LS player reports playback finished. |
| `void` | [`CleanUp`](#cleanup)  | Internal cleanup: pop context, destroy player. |

---

#### OnSequenceFinished { #onsequencefinished }

```cpp
void OnSequenceFinished()
```

Called when the LS player reports playback finished.

---

#### CleanUp { #cleanup }

```cpp
void CleanUp(UComposableCameraTransitionDataAsset * PopTransition)
```

Internal cleanup: pop context, destroy player.
