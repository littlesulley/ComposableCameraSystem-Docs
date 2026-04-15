
# FComposableCameraContextEntry { #fcomposablecameracontextentry }

```cpp
#include <ComposableCameraContextStack.h>
```

A single entry in the camera context stack. Each context owns its own Director (and thus its own EvaluationTree), representing an independent camera "mode" (e.g., gameplay, level sequence, UI).

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `TObjectPtr< UComposableCameraDirector >` | [`Director`](#director)  | The Director that manages cameras and transitions within this context. |
| `FName` | [`ContextName`](#contextname)  | The name that identifies this context (from project settings). |
| `FComposableCameraPose` | [`LastPose`](#lastpose)  | Last evaluated pose from this context. Used for inter-context blending on pop. |

---

#### Director { #director }

```cpp
TObjectPtr< UComposableCameraDirector > Director { nullptr }
```

The Director that manages cameras and transitions within this context.

---

#### ContextName { #contextname }

```cpp
FName ContextName
```

The name that identifies this context (from project settings).

---

#### LastPose { #lastpose }

```cpp
FComposableCameraPose LastPose
```

Last evaluated pose from this context. Used for inter-context blending on pop.
