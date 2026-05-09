
# UMovieSceneComposableCameraShotTrack { #umoviescenecomposablecamerashottrack }

```cpp
#include <MovieSceneComposableCameraShotTrack.h>
```

> **Inherits:** `UMovieSceneNameableTrack`

Sequencer track that drives Composable Camera Shots — Phase E of Shot-Based Keyframing.

Each section on the track represents one Shot activation window in the timeline. The active Shot's data (`[FComposableCameraShot](../structs/FComposableCameraShot.md#fcomposablecamerashot)`) is pushed every frame into the bound `[AComposableCameraLevelSequenceActor](../actors/AComposableCameraLevelSequenceActor.md#acomposablecameralevelsequenceactor)`'s internal `[UComposableCameraCompositionFramingNode::Shot](../nodes/UComposableCameraCompositionFramingNode.md#shot-2)` UPROPERTY by the `UMovieSceneComposableCameraShotTrackInstance` — so the runtime CCS pipeline runs unchanged (TickCamera evaluates the framing node, the solver builds a pose, the LS Component projects it to the CineCamera).

**Track binding model**

Bound under an `[AComposableCameraLevelSequenceActor](../actors/AComposableCameraLevelSequenceActor.md#acomposablecameralevelsequenceactor)` (or subclass — notably the Phase E `[AComposableCameraLevelSequenceShotActor](../actors/AComposableCameraLevelSequenceShotActor.md#acomposablecameralevelsequenceshotactor)`) binding row, NOT root-level. The track has no `TargetActorBinding` field — its parent in the outliner is the binding it drives. The track editor (Phase E.4) surfaces the menu entry only when the binding's class matches.

**Multi-row + overlap semantics**

Rows are enabled. When two sections overlap on different rows, the overlap window is treated as an inter-Shot transition zone. The lower-row section is the outgoing Shot, the higher-row section is the incoming Shot, and the incoming section's `EnterTransition` selects the transition asset used to blend the two solved poses. If `EnterTransition` is null, the overlap behaves as a hard cut.

**Transition timing**

The section overlap itself defines blend duration. The transition asset contributes its blend curve and pose blend behavior; its own `TransitionTime` is ignored on this Sequencer Shot path.

**Section exit semantics**

`CompositionFramingNode::Shot` retains the last-written value when no section is active (gap between sections / past the final section). This is intentional — the camera holds its last framing rather than snapping back to a default. Designers explicitly add a new section to change the framing.

Modeled on `[UMovieSceneComposableCameraPatchTrack](UMovieSceneComposableCameraPatchTrack.md#umoviescenecomposablecamerapatchtrack)` for layout consistency. Shot-track-specific divergences:

* Bound (under a binding row), not root.

* Inter-Shot blends are authored through section overlap plus the incoming section's `EnterTransition`.

* No `TargetActorBinding` (the bound actor IS the parent binding).

### Public Methods

| Return | Name | Description |
|--------|------|-------------|
|  | [`UMovieSceneComposableCameraShotTrack`](#umoviescenecomposablecamerashottrack-1)  |  |
| `void` | [`AddSection`](#addsection) `virtual` |  |
| `bool` | [`SupportsType`](#supportstype) `virtual` `const` |  |
| `UMovieSceneSection *` | [`CreateNewSection`](#createnewsection) `virtual` |  |
| `bool` | [`SupportsMultipleRows`](#supportsmultiplerows) `virtual` `const` `inline` |  |
| `EMovieSceneTrackEasingSupportFlags` | [`SupportsEasing`](#supportseasing) `virtual` `const` |  |
| `const TArray< UMovieSceneSection * > &` | [`GetAllSections`](#getallsections) `virtual` `const` |  |
| `bool` | [`HasSection`](#hassection) `virtual` `const` |  |
| `bool` | [`IsEmpty`](#isempty) `virtual` `const` |  |
| `void` | [`RemoveSection`](#removesection) `virtual` |  |
| `void` | [`RemoveSectionAt`](#removesectionat) `virtual` |  |
| `void` | [`RemoveAllAnimationData`](#removeallanimationdata) `virtual` |  |

---

#### UMovieSceneComposableCameraShotTrack { #umoviescenecomposablecamerashottrack-1 }

```cpp
UMovieSceneComposableCameraShotTrack(const FObjectInitializer & ObjectInitializer)
```

---

#### AddSection { #addsection }

`virtual`

```cpp
virtual void AddSection(UMovieSceneSection & Section)
```

---

#### SupportsType { #supportstype }

`virtual` `const`

```cpp
virtual bool SupportsType(TSubclassOf< UMovieSceneSection > SectionClass) const
```

---

#### CreateNewSection { #createnewsection }

`virtual`

```cpp
virtual UMovieSceneSection * CreateNewSection()
```

---

#### SupportsMultipleRows { #supportsmultiplerows }

`virtual` `const` `inline`

```cpp
virtual inline bool SupportsMultipleRows() const
```

---

#### SupportsEasing { #supportseasing }

`virtual` `const`

```cpp
virtual EMovieSceneTrackEasingSupportFlags SupportsEasing(FMovieSceneSupportsEasingParams & Params) const
```

---

#### GetAllSections { #getallsections }

`virtual` `const`

```cpp
virtual const TArray< UMovieSceneSection * > & GetAllSections() const
```

---

#### HasSection { #hassection }

`virtual` `const`

```cpp
virtual bool HasSection(const UMovieSceneSection & Section) const
```

---

#### IsEmpty { #isempty }

`virtual` `const`

```cpp
virtual bool IsEmpty() const
```

---

#### RemoveSection { #removesection }

`virtual`

```cpp
virtual void RemoveSection(UMovieSceneSection & Section)
```

---

#### RemoveSectionAt { #removesectionat }

`virtual`

```cpp
virtual void RemoveSectionAt(int32 SectionIndex)
```

---

#### RemoveAllAnimationData { #removeallanimationdata }

`virtual`

```cpp
virtual void RemoveAllAnimationData()
```

### Private Attributes

| Return | Name | Description |
|--------|------|-------------|
| `TArray< TObjectPtr< UMovieSceneSection > >` | [`Sections`](#sections)  |  |

---

#### Sections { #sections }

```cpp
TArray< TObjectPtr< UMovieSceneSection > > Sections
```
