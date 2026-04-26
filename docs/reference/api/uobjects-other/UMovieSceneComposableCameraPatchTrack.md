
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

#### UMovieSceneComposableCameraPatchTrack { #umoviescenecomposablecamerapatchtrack-1 }

```cpp
UMovieSceneComposableCameraPatchTrack(const FObjectInitializer & ObjectInitializer)
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
