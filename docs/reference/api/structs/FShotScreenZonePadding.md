
# FShotScreenZonePadding { #fshotscreenzonepadding }

```cpp
#include <ComposableCameraShot.h>
```

One side's padding for a `[FShotScreenZones](FShotScreenZones.md#fshotscreenzones)` rectangle. Each padding value is the **distance from the authored `ScreenPosition` center to that edge**, expressed in normalized screen fractions. Half-extents are independent per side so framing zones can be asymmetric — e.g. a tracking shot can carry a wide right-side soft zone (lead room) and a tight left-side dead zone. Designer drags one edge to mutate exactly one of these four floats.

Range `[0, 0.5]` covers half the viewport per side; the maximum realistic asymmetric zone is the full screen (0.5 + 0.5 across an axis).

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `float` | [`Left`](#left)  |  |
| `float` | [`Right`](#right)  |  |
| `float` | [`Top`](#top)  | "Top" = +Y in the solver's normalized screen convention (= upward on screen). Maps to the SMALLER pixel-Y in viewport coords. |
| `float` | [`Bottom`](#bottom)  |  |

---

#### Left { #left }

```cpp
float Left = 0.1f
```

---

#### Right { #right }

```cpp
float Right = 0.1f
```

---

#### Top { #top }

```cpp
float Top = 0.1f
```

"Top" = +Y in the solver's normalized screen convention (= upward on screen). Maps to the SMALLER pixel-Y in viewport coords.

---

#### Bottom { #bottom }

```cpp
float Bottom = 0.1f
```
