
# UComposableCameraCameraOffsetNode { #ucomposablecameracameraoffsetnode }

```cpp
#include <ComposableCameraCameraOffsetNode.h>
```

> **Inherits:** [`UComposableCameraCameraNodeBase`](../uobjects-other/UComposableCameraCameraNodeBase.md#ucomposablecameracameranodebase)

Applies a positional offset to the camera in camera-local space.

The node evaluates `CameraOffset` in camera-local axes (`X=forward`, `Y=right`, `Z=up`). When `ForwardOffsetDeltaByPitchCurve` has keys, it samples the current camera pitch in degrees and adds the curve value to `CameraOffset.X` before computing the final camera position.

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `FVector` | [`PivotPosition`](#pivotposition-2)  | Pivot position the camera offset is applied from. |
| `FVector` | [`CameraOffset`](#cameraoffset)  | Camera-local offset, where X is forward, Y is right, and Z is up. |
| `FRuntimeFloatCurve` | [`ForwardOffsetDeltaByPitchCurve`](#forwardoffsetdeltabypitchcurve)  | Inline curve that adds to the forward offset based on current pitch in degrees. |

---

#### PivotPosition { #pivotposition-2 }

```cpp
FVector PivotPosition { FVector::ZeroVector }
```

Pivot position the camera offset is applied from.

---

#### CameraOffset { #cameraoffset }

```cpp
FVector CameraOffset
```

Camera-local offset, where X is forward, Y is right, and Z is up.

---

#### ForwardOffsetDeltaByPitchCurve { #forwardoffsetdeltabypitchcurve }

```cpp
FRuntimeFloatCurve ForwardOffsetDeltaByPitchCurve
```

Additive forward offset sampled by current pitch. Curve X is pitch in degrees, and curve Y is additive `CameraOffset.X` in centimeters. The curve is stored inline on the node, so authors can edit keys without creating a separate `UCurveFloat` asset.

### Public Methods

| Return | Name | Description |
|--------|------|-------------|
|  | [`UComposableCameraCameraOffsetNode`](#ucomposablecameracameraoffsetnode-1) `inline` |  |
| `void` | [`OnTickNode_Implementation`](#onticknode_implementation-12) `virtual` |  |
| `void` | [`GetPinDeclarations_Implementation`](#getpindeclarations_implementation-11) `virtual` `const` |  |

---

#### UComposableCameraCameraOffsetNode { #ucomposablecameracameraoffsetnode-1 }

`inline`

```cpp
inline UComposableCameraCameraOffsetNode()
```

---

#### OnTickNode_Implementation { #onticknode_implementation-12 }

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
