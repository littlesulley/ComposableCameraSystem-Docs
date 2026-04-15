
# FComposableCameraTransitionInitParams { #fcomposablecameratransitioninitparams }

```cpp
#include <ComposableCameraTransitionBase.h>
```

Parameters passed when a transition is initialized. Contains the source pose data needed for transitions to set up their internal state.

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `FComposableCameraPose` | [`CurrentSourcePose`](#currentsourcepose)  | Source pose at the moment the transition starts (the blended output the player was seeing). |
| `FComposableCameraPose` | [`PreviousSourcePose`](#previoussourcepose)  | Previous frame's source pose (for velocity-based transitions like inertialization). |
| `float` | [`DeltaTime`](#deltatime)  | Delta time of the frame when the transition was created. |

---

#### CurrentSourcePose { #currentsourcepose }

```cpp
FComposableCameraPose CurrentSourcePose
```

Source pose at the moment the transition starts (the blended output the player was seeing).

---

#### PreviousSourcePose { #previoussourcepose }

```cpp
FComposableCameraPose PreviousSourcePose
```

Previous frame's source pose (for velocity-based transitions like inertialization).

---

#### DeltaTime { #deltatime }

```cpp
float DeltaTime { 0.f }
```

Delta time of the frame when the transition was created.
