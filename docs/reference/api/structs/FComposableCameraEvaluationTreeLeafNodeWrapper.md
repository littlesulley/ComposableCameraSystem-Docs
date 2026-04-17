
# FComposableCameraEvaluationTreeLeafNodeWrapper { #fcomposablecameraevaluationtreeleafnodewrapper }

```cpp
#include <ComposableCameraEvaluationTree.h>
```

Leaf node wrapper: wraps a single running camera.

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `TObjectPtr< AComposableCameraCameraBase >` | [`RunningCamera`](#runningcamera-3)  |  |
| `bool` | [`bFrozen`](#bfrozen)  | When true, Evaluate returns the camera's cached pose without ticking it. |

---

#### RunningCamera { #runningcamera-3 }

```cpp
TObjectPtr< AComposableCameraCameraBase > RunningCamera { nullptr }
```

---

#### bFrozen { #bfrozen }

```cpp
bool bFrozen { false }
```

When true, Evaluate returns the camera's cached pose without ticking it.

### Public Methods

| Return | Name | Description |
|--------|------|-------------|
| `FComposableCameraPose` | [`Evaluate`](#evaluate-12)  |  |

---

#### Evaluate { #evaluate-12 }

```cpp
FComposableCameraPose Evaluate(float DeltaTime)
```
