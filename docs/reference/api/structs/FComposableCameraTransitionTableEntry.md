
# FComposableCameraTransitionTableEntry { #fcomposablecameratransitiontableentry }

```cpp
#include <ComposableCameraTransitionTableDataAsset.h>
```

One entry in the transition routing table.

Defines which transition to use when switching from a camera built from SourceTypeAsset to one built from TargetTypeAsset. Both fields are required — the table performs exact-match lookups only. Wildcard / fallback behavior is handled by per-camera ExitTransition and EnterTransition fields on [UComposableCameraTypeAsset](../data-assets/UComposableCameraTypeAsset.md#ucomposablecameratypeasset), which sit below the table in the resolution chain.

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `TSoftObjectPtr< UComposableCameraTypeAsset >` | [`SourceTypeAsset`](#sourcetypeasset-1)  | Source camera type asset (required). |
| `TSoftObjectPtr< UComposableCameraTypeAsset >` | [`TargetTypeAsset`](#targettypeasset)  | Target camera type asset (required). |
| `TObjectPtr< UComposableCameraTransitionBase >` | [`Transition`](#transition-1)  | Transition to use for this (Source → Target) pair. |
| `FString` | [`DisplayTitle`](#displaytitle)  | Computed display string for the array header (e.g. "ThirdPerson → FirstPerson"). |

---

#### SourceTypeAsset { #sourcetypeasset-1 }

```cpp
TSoftObjectPtr< UComposableCameraTypeAsset > SourceTypeAsset
```

Source camera type asset (required).

---

#### TargetTypeAsset { #targettypeasset }

```cpp
TSoftObjectPtr< UComposableCameraTypeAsset > TargetTypeAsset
```

Target camera type asset (required).

---

#### Transition { #transition-1 }

```cpp
TObjectPtr< UComposableCameraTransitionBase > Transition
```

Transition to use for this (Source → Target) pair.

---

#### DisplayTitle { #displaytitle }

```cpp
FString DisplayTitle
```

Computed display string for the array header (e.g. "ThirdPerson → FirstPerson").

### Public Methods

| Return | Name | Description |
|--------|------|-------------|
| `void` | [`UpdateDisplayTitle`](#updatedisplaytitle)  | Rebuild DisplayTitle from current Source/Target. |

---

#### UpdateDisplayTitle { #updatedisplaytitle }

```cpp
void UpdateDisplayTitle()
```

Rebuild DisplayTitle from current Source/Target.
