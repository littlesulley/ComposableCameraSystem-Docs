
# UComposableCameraControlRotateNode { #ucomposablecameracontrolrotatenode }

```cpp
#include <ComposableCameraControlRotateNode.h>
```

> **Inherits:** [`UComposableCameraCameraNodeBase`](../uobjects-other/UComposableCameraCameraNodeBase.md#ucomposablecameracameranodebase)

Node for receiving user input and applying it to camera rotation. <br/>
@InputParameter RotateAction: Input action controlling camera rotation. You must use the Enhanced Input Component. <br/>
@InputParameter HorizontalSpeed: Camera horizontal rotation speed. <br/>
@InputParameter VerticalSpeed: Camera vertical rotation speed. <br/>
@InputParameter HorizontalDamping: Acceleration and deceleration time when changing yaw. First element is acceleration, second is deceleration. <br/>
@InputParameter VerticalDamping: Acceleration and deceleration time when changing pitch. First element is acceleration, second is deceleration. <br/>
@InputParameter InvertPitch: Whether to invert pitch. <br/>

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `class UInputAction *` | [`RotateAction`](#rotateaction-2)  |  |
| `float` | [`HorizontalSpeed`](#horizontalspeed)  |  |
| `float` | [`VerticalSpeed`](#verticalspeed)  |  |
| `FVector2f` | [`HorizontalDamping`](#horizontaldamping)  |  |
| `FVector2f` | [`VerticalDamping`](#verticaldamping)  |  |
| `bool` | [`bInvertPitch`](#binvertpitch)  |  |

---

#### RotateAction { #rotateaction-2 }

```cpp
class UInputAction * RotateAction
```

---

#### HorizontalSpeed { #horizontalspeed }

```cpp
float HorizontalSpeed { 1.f }
```

---

#### VerticalSpeed { #verticalspeed }

```cpp
float VerticalSpeed { 1.f }
```

---

#### HorizontalDamping { #horizontaldamping }

```cpp
FVector2f HorizontalDamping { .5f }
```

---

#### VerticalDamping { #verticaldamping }

```cpp
FVector2f VerticalDamping { .5f }
```

---

#### bInvertPitch { #binvertpitch }

```cpp
bool bInvertPitch { true }
```

### Public Methods

| Return | Name | Description |
|--------|------|-------------|
| `void` | [`OnInitialize_Implementation`](#oninitialize_implementation-8) `virtual` |  |
| `void` | [`OnTickNode_Implementation`](#onticknode_implementation-11) `virtual` |  |
| `void` | [`GetPinDeclarations_Implementation`](#getpindeclarations_implementation-11) `virtual` `const` |  |

---

#### OnInitialize_Implementation { #oninitialize_implementation-8 }

`virtual`

```cpp
virtual void OnInitialize_Implementation()
```

---

#### OnTickNode_Implementation { #onticknode_implementation-11 }

`virtual`

```cpp
virtual void OnTickNode_Implementation(float DeltaTime, const FComposableCameraPose & CurrentCameraPose, FComposableCameraPose & OutCameraPose)
```

---

#### GetPinDeclarations_Implementation { #getpindeclarations_implementation-11 }

`virtual` `const`

```cpp
virtual void GetPinDeclarations_Implementation(TArray< FComposableCameraNodePinDeclaration > & OutPins) const
```

### Private Attributes

| Return | Name | Description |
|--------|------|-------------|
| `UEnhancedInputComponent *` | [`InputComponent`](#inputcomponent)  |  |
| `FEnhancedInputActionValueBinding *` | [`InputBinding`](#inputbinding)  |  |
| `FVector2D` | [`LastFrameCameraRotationInput`](#lastframecamerarotationinput)  |  |

---

#### InputComponent { #inputcomponent }

```cpp
UEnhancedInputComponent * InputComponent
```

---

#### InputBinding { #inputbinding }

```cpp
FEnhancedInputActionValueBinding * InputBinding
```

---

#### LastFrameCameraRotationInput { #lastframecamerarotationinput }

```cpp
FVector2D LastFrameCameraRotationInput
```

### Private Methods

| Return | Name | Description |
|--------|------|-------------|
| `void` | [`ApplyAcceleration`](#applyacceleration)  |  |

---

#### ApplyAcceleration { #applyacceleration }

```cpp
void ApplyAcceleration(float DeltaTime, FVector2f Damping, double & ThisFrameRotationInput, const double & LastFrameRotationInput)
```
