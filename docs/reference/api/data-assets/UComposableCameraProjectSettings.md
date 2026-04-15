
# UComposableCameraProjectSettings { #ucomposablecameraprojectsettings }

```cpp
#include <ComposableCameraProjectSettings.h>
```

> **Inherits:** `UDeveloperSettings`

Developer settings for composable camera system.

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `TSoftObjectPtr< UComposableCameraTransitionTableDataAsset >` | [`TransitionTable`](#transitiontable)  | Optional project-wide transition routing table. Consulted when switching between camera types to resolve the transition before falling back to per-camera-type defaults. **See also**: [UComposableCameraTransitionTableDataAsset](UComposableCameraTransitionTableDataAsset.md#ucomposablecameratransitiontabledataasset) for the resolution chain. |
| `TArray< FName >` | [`ContextNames`](#contextnames)  | Named camera contexts that can be used with ActivateCamera. Each entry is just a name (e.g., "Gameplay", "UI", "LevelSequence"). The first entry is treated as the base context — it is always present and cannot be popped. The context stack is strict LIFO: contexts push on top and pop from top. |

---

#### TransitionTable { #transitiontable }

```cpp
TSoftObjectPtr< UComposableCameraTransitionTableDataAsset > TransitionTable
```

Optional project-wide transition routing table. Consulted when switching between camera types to resolve the transition before falling back to per-camera-type defaults. **See also**: [UComposableCameraTransitionTableDataAsset](UComposableCameraTransitionTableDataAsset.md#ucomposablecameratransitiontabledataasset) for the resolution chain.

---

#### ContextNames { #contextnames }

```cpp
TArray< FName > ContextNames
```

Named camera contexts that can be used with ActivateCamera. Each entry is just a name (e.g., "Gameplay", "UI", "LevelSequence"). The first entry is treated as the base context — it is always present and cannot be popped. The context stack is strict LIFO: contexts push on top and pop from top.

### Public Methods

| Return | Name | Description |
|--------|------|-------------|
| `bool` | [`IsValidContextName`](#isvalidcontextname) `const` `inline` | Returns true if the given name is a registered context. |

---

#### IsValidContextName { #isvalidcontextname }

`const` `inline`

```cpp
inline bool IsValidContextName(FName ContextName) const
```

Returns true if the given name is a registered context.

### Public Static Methods

| Return | Name | Description |
|--------|------|-------------|
| `TArray< FName >` | [`GetContextNames`](#getcontextnames) `static` `inline` | Get all context names as a list (for dropdowns / GetOptions). |

---

#### GetContextNames { #getcontextnames }

`static` `inline`

```cpp
static inline TArray< FName > GetContextNames()
```

Get all context names as a list (for dropdowns / GetOptions).
