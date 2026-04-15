
# UComposableCameraBlueprintCameraNode { #ucomposablecamerablueprintcameranode }

```cpp
#include <ComposableCameraBlueprintCameraNode.h>
```

> **Inherits:** [`UComposableCameraCameraNodeBase`](../uobjects-other/UComposableCameraCameraNodeBase.md#ucomposablecameracameranodebase)

Base class for user-authored camera nodes written in Blueprint.

Subclass this in Blueprint to create custom camera nodes with:

* Custom initialization logic (override "InitializeNode")

* Custom per-frame tick logic (override "TickNode")

* Custom pin declarations (override "GetPinDeclarations")

Blueprint subclasses are automatically discovered by the camera type asset editor — they appear in the "Add Node" context menu alongside built-in C++ nodes with no manual registration required.

Pin values can be read/written from Blueprint via the type-specific accessors inherited from [UComposableCameraCameraNodeBase](../uobjects-other/UComposableCameraCameraNodeBase.md#ucomposablecameracameranodebase):

* GetInputPinValueFloat, GetInputPinValueVector, etc.

* SetOutputPinValueFloat, SetOutputPinValueVector, etc.

Any EditAnywhere + BlueprintReadWrite UPROPERTY on a Blueprint subclass that maps to a supported pin type (bool, int32, float, double, Vector2D, Vector, Vector4, Rotator, Transform, Actor, Object) is treated as an implicit pin with the UPROPERTY's default value. See the build validator for details.

This class is Abstract — users must subclass it in Blueprint; it cannot be placed directly.

### Public Methods

| Return | Name | Description |
|--------|------|-------------|
| `FVector2D` | [`GetInputPinValueVector2D`](#getinputpinvaluevector2d) `const` | Read an input pin value as Vector2D from Blueprint. (The base class exposes Float/Int32/Bool/Vector/Rotator/Transform/Actor but omits Vector2D and Double — fill the gap here.) |
| `void` | [`SetOutputPinValueVector2D`](#setoutputpinvaluevector2d)  |  |
| `FComposableCameraPose` | [`GetCurrentCameraPose`](#getcurrentcamerapose-1) `const` | Convenience: get the current camera pose from the owning PCM. Useful in OnInitialize when the node needs the pose at activation time. |

---

#### GetInputPinValueVector2D { #getinputpinvaluevector2d }

`const`

```cpp
FVector2D GetInputPinValueVector2D(FName PinName) const
```

Read an input pin value as Vector2D from Blueprint. (The base class exposes Float/Int32/Bool/Vector/Rotator/Transform/Actor but omits Vector2D and Double — fill the gap here.)

---

#### SetOutputPinValueVector2D { #setoutputpinvaluevector2d }

```cpp
void SetOutputPinValueVector2D(FName PinName, FVector2D Value)
```

---

#### GetCurrentCameraPose { #getcurrentcamerapose-1 }

`const`

```cpp
FComposableCameraPose GetCurrentCameraPose() const
```

Convenience: get the current camera pose from the owning PCM. Useful in OnInitialize when the node needs the pose at activation time.
