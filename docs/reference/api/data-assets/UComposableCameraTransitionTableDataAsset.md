
# UComposableCameraTransitionTableDataAsset { #ucomposablecameratransitiontabledataasset }

```cpp
#include <ComposableCameraTransitionTableDataAsset.h>
```

> **Inherits:** `UDataAsset`

Data asset holding a transition routing table.

Provides a centralized, project-level definition of which transition to use when switching between camera type pairs. Referenced from [UComposableCameraProjectSettings::TransitionTable](UComposableCameraProjectSettings.md#transitiontable).

Resolution order when switching from camera A to camera B:

1. Caller-supplied override (TransitionOverride parameter)

1. Table lookup by (A, B) pair — this asset

1. A's ExitTransition — source camera declares how to leave

1. B's EnterTransition — target camera declares how to enter

1. Hard cut (no transition)

Steps 3 and 4 are per-camera-type-asset fields; step 2 is what this table provides. Together they cover both project-wide gameplay routing and per-camera self-contained transitions (puzzle, UI, cinematic cameras).

**See also**: [UComposableCameraProjectSettings::TransitionTable](UComposableCameraProjectSettings.md#transitiontable)

**See also**: [UComposableCameraTypeAsset::EnterTransition](UComposableCameraTypeAsset.md#entertransition-1)

**See also**: [UComposableCameraTypeAsset::ExitTransition](UComposableCameraTypeAsset.md#exittransition)

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `TArray< FComposableCameraTransitionTableEntry >` | [`Entries`](#entries-1)  | The transition routing entries. Exact-match by (Source, Target) pair; first matching entry in declaration order wins. |

---

#### Entries { #entries-1 }

```cpp
TArray< FComposableCameraTransitionTableEntry > Entries
```

The transition routing entries. Exact-match by (Source, Target) pair; first matching entry in declaration order wins.

### Public Methods

| Return | Name | Description |
|--------|------|-------------|
| `void` | [`PostEditChangeProperty`](#posteditchangeproperty) `virtual` |  |
| `void` | [`PostLoad`](#postload-1) `virtual` |  |
| `EDataValidationResult` | [`IsDataValid`](#isdatavalid) `virtual` `const` |  |
| `UComposableCameraTransitionBase *` | [`FindTransition`](#findtransition) `const` | Look up the transition for an exact (Source, Target) pair. |

---

#### PostEditChangeProperty { #posteditchangeproperty }

`virtual`

```cpp
virtual void PostEditChangeProperty(FPropertyChangedEvent & PropertyChangedEvent)
```

---

#### PostLoad { #postload-1 }

`virtual`

```cpp
virtual void PostLoad()
```

---

#### IsDataValid { #isdatavalid }

`virtual` `const`

```cpp
virtual EDataValidationResult IsDataValid(FDataValidationContext & Context) const
```

---

#### FindTransition { #findtransition }

`const`

```cpp
UComposableCameraTransitionBase * FindTransition(const UComposableCameraTypeAsset * Source, const UComposableCameraTypeAsset * Target) const
```

Look up the transition for an exact (Source, Target) pair.

**Parameters**

* `Source` The currently-active camera's type asset. Returns nullptr if null. 

* `Target` The camera type asset being activated. Returns nullptr if null. 

**Returns**

The matched transition, or nullptr if no entry matches.
