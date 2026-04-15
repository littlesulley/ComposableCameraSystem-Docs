
# FComposableCameraEvaluationTreeLeafNodeWrapper { #fcomposablecameraevaluationtreeleafnodewrapper }

```cpp
#include <ComposableCameraEvaluationTree.h>
```

Leaf node wrapper: wraps a single running camera.

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `TObjectPtr< AComposableCameraCameraBase >` | [`RunningCamera`](#runningcamera-3)  |  |

---

#### RunningCamera { #runningcamera-3 }

```cpp
TObjectPtr< AComposableCameraCameraBase > RunningCamera { nullptr }
```

### Public Methods

| Return | Name | Description |
|--------|------|-------------|
| `FComposableCameraPose` | [`Evaluate`](#evaluate-12)  |  |

---

#### Evaluate { #evaluate-12 }

```cpp
FComposableCameraPose Evaluate(float DeltaTime)
```
