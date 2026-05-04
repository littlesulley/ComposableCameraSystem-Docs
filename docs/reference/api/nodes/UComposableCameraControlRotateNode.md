
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
| `TObjectPtr< AActor >` | [`RotationInputActor`](#rotationinputactor)  |  |
| `TObjectPtr< class UInputAction >` | [`RotateAction`](#rotateaction-2)  |  |
| `float` | [`HorizontalSpeed`](#horizontalspeed-1)  |  |
| `float` | [`VerticalSpeed`](#verticalspeed-1)  |  |
| `FVector2D` | [`HorizontalDamping`](#horizontaldamping)  |  |
| `FVector2D` | [`VerticalDamping`](#verticaldamping)  |  |
| `bool` | [`bInvertPitch`](#binvertpitch)  |  |

---

#### RotationInputActor { #rotationinputactor }

```cpp
TObjectPtr< AActor > RotationInputActor
```

---

#### RotateAction { #rotateaction-2 }

```cpp
TObjectPtr< class UInputAction > RotateAction
```

---

#### HorizontalSpeed { #horizontalspeed-1 }

```cpp
float HorizontalSpeed { 1.f }
```

---

#### VerticalSpeed { #verticalspeed-1 }

```cpp
float VerticalSpeed { 1.f }
```

---

#### HorizontalDamping { #horizontaldamping }

```cpp
FVector2D HorizontalDamping { 0.5, 0.5 }
```

---

#### VerticalDamping { #verticaldamping }

```cpp
FVector2D VerticalDamping { 0.5, 0.5 }
```

---

#### bInvertPitch { #binvertpitch }

```cpp
bool bInvertPitch { true }
```

### Public Methods

| Return | Name | Description |
|--------|------|-------------|
|  | [`UComposableCameraControlRotateNode`](#ucomposablecameracontrolrotatenode-1) `inline` |  |
| `void` | [`OnInitialize_Implementation`](#oninitialize_implementation-11) `virtual` |  |
| `void` | [`OnTickNode_Implementation`](#onticknode_implementation-17) `virtual` |  |
| `void` | [`GetPinDeclarations_Implementation`](#getpindeclarations_implementation-16) `virtual` `const` |  |

---

#### UComposableCameraControlRotateNode { #ucomposablecameracontrolrotatenode-1 }

`inline`

```cpp
inline UComposableCameraControlRotateNode()
```

---

#### OnInitialize_Implementation { #oninitialize_implementation-11 }

`virtual`

```cpp
virtual void OnInitialize_Implementation()
```

---

#### OnTickNode_Implementation { #onticknode_implementation-17 }

`virtual`

```cpp
virtual void OnTickNode_Implementation(float DeltaTime, const FComposableCameraPose & CurrentCameraPose, FComposableCameraPose & OutCameraPose)
```

---

#### GetPinDeclarations_Implementation { #getpindeclarations_implementation-16 }

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
void ApplyAcceleration(float DeltaTime, const FVector2D & Damping, double & ThisFrameRotationInput, const double & LastFrameRotationInput)
```
