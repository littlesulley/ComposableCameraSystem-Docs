# UComposableCameraDirectionalMoveNode { #ucomposablecameradirectionalmovenode }

```cpp
#include <ComposableCameraDirectionalMoveNode.h>
```

> **Inherits:** `UComposableCameraCameraNodeBase`

Moves the camera continuously from `InitialTransform` along a camera-space direction at a fixed speed.

The node resets its internal elapsed time on initialization. Each tick it normalizes `Direction`, transforms it by `InitialTransform`'s rotation, writes `InitialTransform.Location + WorldDirection * Speed * ElapsedTime` to the pose, and writes `InitialTransform`'s rotation to the pose.

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `FVector` | [`Direction`](#direction) | Direction in camera-local space. X is forward, Y is right, Z is up. The value is normalized at runtime. |
| `FTransform` | [`InitialTransform`](#initialtransform) | Starting transform. Its rotation converts `Direction` from camera space to world space. |
| `float` | [`Speed`](#speed) | Movement speed in centimeters per second. |

---

#### Direction { #direction }

```cpp
FVector Direction { FVector::ForwardVector }
```

Direction in camera-local space. X is forward, Y is right, Z is up. The value is normalized at runtime.

---

#### InitialTransform { #initialtransform }

```cpp
FTransform InitialTransform { FTransform::Identity }
```

Starting transform for the continuous move.

---

#### Speed { #speed }

```cpp
float Speed { 100.f }
```

Movement speed in centimeters per second.

### Public Methods

| Return | Name | Description |
|--------|------|-------------|
|  | [`UComposableCameraDirectionalMoveNode`](#ucomposablecameradirectionalmovenode-1) | Sets the palette category to `Position`. |
| `void` | [`OnInitialize_Implementation`](#oninitialize_implementation) `virtual` | Resets elapsed time. |
| `void` | [`OnTickNode_Implementation`](#onticknode_implementation) `virtual` | Applies the continuous move to the camera pose. |
| `void` | [`GetPinDeclarations_Implementation`](#getpindeclarations_implementation) `virtual` | Declares input pins for Direction, Initial Transform, and Speed. |
| `EComposableCameraNodePatchCompatibility` | [`GetPatchCompatibility_Implementation`](#getpatchcompatibility_implementation) `virtual` | Returns `Incompatible`. |

---

#### UComposableCameraDirectionalMoveNode { #ucomposablecameradirectionalmovenode-1 }

```cpp
UComposableCameraDirectionalMoveNode()
```

---

#### OnInitialize_Implementation { #oninitialize_implementation }

`virtual`

```cpp
void OnInitialize_Implementation()
```

---

#### OnTickNode_Implementation { #onticknode_implementation }

`virtual`

```cpp
void OnTickNode_Implementation(float DeltaTime, const FComposableCameraPose& CurrentCameraPose, FComposableCameraPose& OutCameraPose)
```

---

#### GetPinDeclarations_Implementation { #getpindeclarations_implementation }

`virtual`

```cpp
void GetPinDeclarations_Implementation(TArray<FComposableCameraNodePinDeclaration>& OutPins) const
```

---

#### GetPatchCompatibility_Implementation { #getpatchcompatibility_implementation }

`virtual`

```cpp
EComposableCameraNodePatchCompatibility GetPatchCompatibility_Implementation() const
```

