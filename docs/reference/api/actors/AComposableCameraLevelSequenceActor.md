
# AComposableCameraLevelSequenceActor { #acomposablecameralevelsequenceactor }

```cpp
#include <ComposableCameraLevelSequenceActor.h>
```

> **Inherits:** `AActor`

Actor dedicated to binding composable cameras into a Level Sequence.

Structure ───────── RootComponent = UCineCameraComponent (OutputCineCameraComponent) ← viewport terminal Sibling = [UComposableCameraLevelSequenceComponent](../uobjects-other/UComposableCameraLevelSequenceComponent.md#ucomposablecameralevelsequencecomponent) ← logic/data driver

Mirrors ACineCameraActor's shape: the CineCamera is the Actor's root component, so every native [UE](#ue) path ("find a UCameraComponent on this
actor", Camera Cut Track, viewport Pilot, Sequencer's Camera Cut target resolution) lands on it immediately. PCM::SetViewTarget's implicit- activation filter hits its root-is-camera fast path identical to how it handles CineCameraActor.

The LevelSequenceComponent is a plain UActorComponent (no transform) — it holds the TypeAssetReference bag and drives the internal CCS camera, projecting each tick's pose onto the CineCamera.

Spawnable-only ────────────── Marked NotPlaceable so it cannot be dragged into a level directly — this camera's lifetime is owned by Sequencer (the Spawnable binding spawns it on section entry, destroys it on section exit). A free-standing actor in the level has no meaning: no Sequencer means no section ⇒ no evaluation signal (see [UComposableCameraLevelSequenceComponent::SetEvaluationEnabled](../uobjects-other/UComposableCameraLevelSequenceComponent.md#setevaluationenabled)).

NotPlaceable does NOT prevent Sequencer's spawn register from instantiating the class — it only hides it from the "Place Actors" panel and editor drag operations, which is exactly what we want.

Runtime driver ────────────── All real work lives on the LevelSequenceComponent — the actor has no per-frame responsibilities of its own.

### Public Methods

| Return | Name | Description |
|--------|------|-------------|
|  | [`AComposableCameraLevelSequenceActor`](#acomposablecameralevelsequenceactor-1)  |  |

---

#### AComposableCameraLevelSequenceActor { #acomposablecameralevelsequenceactor-1 }

```cpp
AComposableCameraLevelSequenceActor(const FObjectInitializer & ObjectInitializer)
```

### Protected Attributes

| Return | Name | Description |
|--------|------|-------------|
| `TObjectPtr< UComposableCameraLevelSequenceComponent >` | [`LevelSequenceComponent`](#levelsequencecomponent)  | Logic-and-data driver ActorComponent. Holds the TypeAssetReference (TypeAsset + Parameters / Variables bags), spawns the transient internal CCS camera each tick, and projects the resulting pose onto the CineCamera root component. Not the Actor's root — the CineCamera is, so native UCameraComponent lookups resolve immediately. |

---

#### LevelSequenceComponent { #levelsequencecomponent }

```cpp
TObjectPtr< UComposableCameraLevelSequenceComponent > LevelSequenceComponent
```

Logic-and-data driver ActorComponent. Holds the TypeAssetReference (TypeAsset + Parameters / Variables bags), spawns the transient internal CCS camera each tick, and projects the resulting pose onto the CineCamera root component. Not the Actor's root — the CineCamera is, so native UCameraComponent lookups resolve immediately.

### Protected Methods

| Return | Name | Description |
|--------|------|-------------|
| `void` | [`BeginPlay`](#beginplay-1) `virtual` |  |
| `void` | [`EndPlay`](#endplay-1) `virtual` |  |

---

#### BeginPlay { #beginplay-1 }

`virtual`

```cpp
virtual void BeginPlay()
```

---

#### EndPlay { #endplay-1 }

`virtual`

```cpp
virtual void EndPlay(const EEndPlayReason::Type EndPlayReason)
```
