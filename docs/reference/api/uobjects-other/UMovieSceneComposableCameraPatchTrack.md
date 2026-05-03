
# UMovieSceneComposableCameraPatchTrack { #umoviescenecomposablecamerapatchtrack }

```cpp
#include <MovieSceneComposableCameraPatchTrack.h>
```

> **Inherits:** `UMovieSceneNameableTrack`

Root-level Sequencer track that drives Composable Camera Patches.

Each section on the track represents one Patch activation window (asset + params + parameter bag); when a section enters its TrueRange the runtime fires AddCameraPatch, when it exits ExpireCameraPatch fires.

Root track (no object binding) by design — Patches live on the Director resolved through PlayerIndex + ContextName on the section, mirroring the BP `AddCameraPatch` library entry. This avoids forcing designers to bind the track to the PCM (which is itself transient and hard to bind cleanly in Sequencer); the section's own properties carry the addressing info.

Multi-row support is on so designers can stack overlapping patches in the same track (different LayerIndex per section, sorted by PatchManager). Each section is independent — sections do not blend with each other; the patch compositor's LayerIndex order does. Easing on each section is enabled and fed into the patch's envelope (EnterDuration / ExitDuration overrides) by the TrackInstance.

Modeled on UMovieSceneCVarTrack: same ImportEntityImpl-via-section pattern, same per-section TrackInstance dispatch through the engine's UMovieSceneTrackInstanceSystem. Track itself stores no animation data — sections own everything.

### Public Methods

| Return | Name | Description |
|--------|------|-------------|
|  | [`UMovieSceneComposableCameraPatchTrack`](#umoviescenecomposablecamerapatchtrack-1)  |  |
| `void` | [`AddSection`](#addsection-1) `virtual` |  |
| `bool` | [`SupportsType`](#supportstype-1) `virtual` `const` |  |
| `UMovieSceneSection *` | [`CreateNewSection`](#createnewsection-1) `virtual` |  |
| `bool` | [`SupportsMultipleRows`](#supportsmultiplerows-1) `virtual` `const` `inline` |  |
| `EMovieSceneTrackEasingSupportFlags` | [`SupportsEasing`](#supportseasing-1) `virtual` `const` |  |
| `const TArray< UMovieSceneSection * > &` | [`GetAllSections`](#getallsections-1) `virtual` `const` |  |
| `bool` | [`HasSection`](#hassection-1) `virtual` `const` |  |
| `bool` | [`IsEmpty`](#isempty-1) `virtual` `const` |  |
| `void` | [`RemoveSection`](#removesection-1) `virtual` |  |
| `void` | [`RemoveSectionAt`](#removesectionat-1) `virtual` |  |
| `void` | [`RemoveAllAnimationData`](#removeallanimationdata-1) `virtual` |  |

---

#### UMovieSceneComposableCameraPatchTrack { #umoviescenecomposablecamerapatchtrack-1 }

```cpp
UMovieSceneComposableCameraPatchTrack(const FObjectInitializer & ObjectInitializer)
```

---

#### AddSection { #addsection-1 }

`virtual`

```cpp
virtual void AddSection(UMovieSceneSection & Section)
```

---

#### SupportsType { #supportstype-1 }

`virtual` `const`

```cpp
virtual bool SupportsType(TSubclassOf< UMovieSceneSection > SectionClass) const
```

---

#### CreateNewSection { #createnewsection-1 }

`virtual`

```cpp
virtual UMovieSceneSection * CreateNewSection()
```

---

#### SupportsMultipleRows { #supportsmultiplerows-1 }

`virtual` `const` `inline`

```cpp
virtual inline bool SupportsMultipleRows() const
```

---

#### SupportsEasing { #supportseasing-1 }

`virtual` `const`

```cpp
virtual EMovieSceneTrackEasingSupportFlags SupportsEasing(FMovieSceneSupportsEasingParams & Params) const
```

---

#### GetAllSections { #getallsections-1 }

`virtual` `const`

```cpp
virtual const TArray< UMovieSceneSection * > & GetAllSections() const
```

---

#### HasSection { #hassection-1 }

`virtual` `const`

```cpp
virtual bool HasSection(const UMovieSceneSection & Section) const
```

---

#### IsEmpty { #isempty-1 }

`virtual` `const`

```cpp
virtual bool IsEmpty() const
```

---

#### RemoveSection { #removesection-1 }

`virtual`

```cpp
virtual void RemoveSection(UMovieSceneSection & Section)
```

---

#### RemoveSectionAt { #removesectionat-1 }

`virtual`

```cpp
virtual void RemoveSectionAt(int32 SectionIndex)
```

---

#### RemoveAllAnimationData { #removeallanimationdata-1 }

`virtual`

```cpp
virtual void RemoveAllAnimationData()
```

### Private Attributes

| Return | Name | Description |
|--------|------|-------------|
| `TArray< TObjectPtr< UMovieSceneSection > >` | [`Sections`](#sections-1)  |  |

---

#### Sections { #sections-1 }

```cpp
TArray< TObjectPtr< UMovieSceneSection > > Sections
```
