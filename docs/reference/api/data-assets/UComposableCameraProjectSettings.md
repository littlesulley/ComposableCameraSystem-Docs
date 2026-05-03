
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
| `int32` | [`PicardMaxIterations`](#picardmaxiterations)  | Maximum Picard iterations before giving up. Hard fail returns `bValid=false`; caller (CompositionFramingNode / Shot Editor preview) preserves the upstream pose. Higher = more stress-geometry tolerance at a per-frame cost ceiling; lower = quicker fail-out on truly unsolvable inputs. Typical convergence is 3-6 iters; the cap matters only for stress / edge cases. |
| `float` | [`PicardConvergenceTolerance`](#picardconvergencetolerance)  | Convergence tolerance in cm. The iteration stops when the un-damped step's `\|\|Candidate - PrevCamPos\|\|` drops below this. Smaller = tighter convergence (more iters, more stable framing under solver noise); larger = looser (fewer iters, possible visible jitter on off-center geometry). 0.01 cm matches what the eye can't see at typical character scale (~200 cm). |
| `float` | [`PicardRelaxation`](#picardrelaxation)  | Damping factor α ∈ (0, 1] for the Picard step: `OutCamPos = Lerp(PrevCamPos, Candidate, α)`. 1.0 = un-damped (fastest when stable, prone to oscillation on off-center / short-Distance geometry); 0.7 = moderate damping (default, suppresses oscillation with mild iter-count cost); lower = more damping, even more oscillation suppression but slower convergence. The convergence test runs on the un-damped residual so damping doesn't affect the fixed point — only path length to it. |

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

---

#### PicardMaxIterations { #picardmaxiterations }

```cpp
int32 PicardMaxIterations = 16
```

Maximum Picard iterations before giving up. Hard fail returns `bValid=false`; caller (CompositionFramingNode / Shot Editor preview) preserves the upstream pose. Higher = more stress-geometry tolerance at a per-frame cost ceiling; lower = quicker fail-out on truly unsolvable inputs. Typical convergence is 3-6 iters; the cap matters only for stress / edge cases.

---

#### PicardConvergenceTolerance { #picardconvergencetolerance }

```cpp
float PicardConvergenceTolerance = 0.01f
```

Convergence tolerance in cm. The iteration stops when the un-damped step's `||Candidate - PrevCamPos||` drops below this. Smaller = tighter convergence (more iters, more stable framing under solver noise); larger = looser (fewer iters, possible visible jitter on off-center geometry). 0.01 cm matches what the eye can't see at typical character scale (~200 cm).

---

#### PicardRelaxation { #picardrelaxation }

```cpp
float PicardRelaxation = 0.7f
```

Damping factor α ∈ (0, 1] for the Picard step: `OutCamPos = Lerp(PrevCamPos, Candidate, α)`. 1.0 = un-damped (fastest when stable, prone to oscillation on off-center / short-Distance geometry); 0.7 = moderate damping (default, suppresses oscillation with mild iter-count cost); lower = more damping, even more oscillation suppression but slower convergence. The convergence test runs on the un-damped residual so damping doesn't affect the fixed point — only path length to it.

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
