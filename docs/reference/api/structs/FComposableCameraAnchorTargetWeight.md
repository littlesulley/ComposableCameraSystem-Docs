
# FComposableCameraAnchorTargetWeight { #fcomposablecameraanchortargetweight }

```cpp
#include <ComposableCameraShot.h>
```

One entry in `[FComposableCameraAnchorSpec::WeightedTargets](FComposableCameraAnchorSpec.md#weightedtargets)`: a target index + non-negative weight. Used when AnchorMode == WeightedWorldCentroid.

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `int32` | [`TargetIndex`](#targetindex-1)  | Index into the owning Shot's Targets array. |
| `float` | [`Weight`](#weight)  | Weight in [0, 1]. Entries with Weight == 0 are silently dropped. Only ratios matter in the centroid math, [0, 1] keeps Details intent readable (consistent with the other Weight fields on FShotTarget). |

---

#### TargetIndex { #targetindex-1 }

```cpp
int32 TargetIndex = 0
```

Index into the owning Shot's Targets array.

---

#### Weight { #weight }

```cpp
float Weight = 1.f
```

Weight in [0, 1]. Entries with Weight == 0 are silently dropped. Only ratios matter in the centroid math, [0, 1] keeps Details intent readable (consistent with the other Weight fields on FShotTarget).
