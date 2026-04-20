
# UComposableCameraCylindricalTransition { #ucomposablecameracylindricaltransition }

```cpp
#include <ComposableCameraCylindricalTransition.h>
```

> **Inherits:** [`UComposableCameraTransitionBase`](UComposableCameraTransitionBase.md#ucomposablecameratransitionbase)

Cylindrical transition.

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `float` | [`MinimumDistanceFromOrigin`](#minimumdistancefromorigin)  |  |
| `bool` | [`bLockToPivot`](#blocktopivot)  |  |

---

#### MinimumDistanceFromOrigin { #minimumdistancefromorigin }

```cpp
float MinimumDistanceFromOrigin { 10.f }
```

---

#### bLockToPivot { #blocktopivot }

```cpp
bool bLockToPivot { true }
```

### Public Methods

| Return | Name | Description |
|--------|------|-------------|
| `void` | [`OnBeginPlay_Implementation`](#onbeginplay_implementation-3) `virtual` |  |
| `FComposableCameraPose` | [`OnEvaluate_Implementation`](#onevaluate_implementation-8) `virtual` |  |

---

#### OnBeginPlay_Implementation { #onbeginplay_implementation-3 }

`virtual`

```cpp
virtual void OnBeginPlay_Implementation(float DeltaTime, const FComposableCameraPose & CurrentSourcePose, const FComposableCameraPose & CurrentTargetPose)
```

---

#### OnEvaluate_Implementation { #onevaluate_implementation-8 }

`virtual`

```cpp
virtual FComposableCameraPose OnEvaluate_Implementation(float DeltaTime, const FComposableCameraPose & CurrentSourcePose, const FComposableCameraPose & CurrentTargetPose)
```
