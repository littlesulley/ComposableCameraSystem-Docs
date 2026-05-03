
# FShotFocus { #fshotfocus }

```cpp
#include <ComposableCameraShot.h>
```

Focus layer — decides focus distance. Independent of Position / Rotation / FOV. See spec §4.6.

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `EShotFocusMode` | [`Mode`](#mode-1)  |  |
| `float` | [`ManualDistance`](#manualdistance)  | Used iff Mode == Manual. |
| `FComposableCameraAnchorSpec` | [`FocusAnchor`](#focusanchor)  | Used iff Mode == FollowCustomAnchor. Lets the focus point follow a third world point distinct from Placement / Aim. Resolved from the Shot's Targets list (or a fixed world point) via `[FComposableCameraAnchorSpec](FComposableCameraAnchorSpec.md#fcomposablecameraanchorspec)`. |

---

#### Mode { #mode-1 }

```cpp
EShotFocusMode Mode = 
```

---

#### ManualDistance { #manualdistance }

```cpp
float ManualDistance = 200.f
```

Used iff Mode == Manual.

---

#### FocusAnchor { #focusanchor }

```cpp
FComposableCameraAnchorSpec FocusAnchor
```

Used iff Mode == FollowCustomAnchor. Lets the focus point follow a third world point distinct from Placement / Aim. Resolved from the Shot's Targets list (or a fixed world point) via `[FComposableCameraAnchorSpec](FComposableCameraAnchorSpec.md#fcomposablecameraanchorspec)`.
