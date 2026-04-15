
# UComposableCameraMoveToAction { #ucomposablecameramovetoaction }

```cpp
#include <ComposableCameraMoveToAction.h>
```

> **Inherits:** [`UComposableCameraActionBase`](UComposableCameraActionBase.md#ucomposablecameraactionbase)

This action moves the camera to a given position, regardless of camera rotation.

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `FVector` | [`TargetPosition`](#targetposition)  |  |
| `float` | [`MoveSpeed`](#movespeed)  |  |

---

#### TargetPosition { #targetposition }

```cpp
FVector TargetPosition
```

---

#### MoveSpeed { #movespeed }

```cpp
float MoveSpeed { 1.f }
```

### Public Methods

| Return | Name | Description |
|--------|------|-------------|
|  | [`UComposableCameraMoveToAction`](#ucomposablecameramovetoaction-1)  |  |
| `bool` | [`CanExecute_Implementation`](#canexecute_implementation-1) `virtual` |  |
| `void` | [`OnExecute_Implementation`](#onexecute_implementation-1) `virtual` |  |

---

#### UComposableCameraMoveToAction { #ucomposablecameramovetoaction-1 }

```cpp
UComposableCameraMoveToAction(const FObjectInitializer & ObjectInitializer)
```

---

#### CanExecute_Implementation { #canexecute_implementation-1 }

`virtual`

```cpp
virtual bool CanExecute_Implementation(float DeltaTime, const FComposableCameraPose & CurrentCameraPose)
```

---

#### OnExecute_Implementation { #onexecute_implementation-1 }

`virtual`

```cpp
virtual void OnExecute_Implementation(float DeltaTime, const FComposableCameraPose & CurrentCameraPose, FComposableCameraPose & OutCameraPose)
```
