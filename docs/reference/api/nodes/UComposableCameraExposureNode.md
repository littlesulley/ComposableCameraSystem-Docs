
# UComposableCameraExposureNode { #ucomposablecameraexposurenode }

```cpp
#include <ComposableCameraExposureNode.h>
```

> **Inherits:** [`UComposableCameraCameraNodeBase`](../uobjects-other/UComposableCameraCameraNodeBase.md#ucomposablecameracameranodebase)

Authors physical exposure inputs on the camera pose.

`LensNode` owns DoF-related physical settings. This node owns ISO, shutter speed, and exposure blend weight so exposure can be authored independently from lens aperture.

!!! warning "Requires manual exposure setup"
    CCS writes `CameraISO` and `CameraShutterSpeed` into post-process settings, but Unreal only consumes them when the resolved post-process stack has both `AutoExposureMethod = AEM_Manual` and `AutoExposureApplyPhysicalCameraExposure = true`. Set those on an unbounded Post Process Volume, a Post Process Component, or the camera component's post-process override. This node does not toggle the apply-physical flag for you.

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `float` | [`ISO`](#iso) | Sensor sensitivity. |
| `float` | [`ShutterSpeed`](#shutterspeed) | Shutter speed in 1/seconds, e.g. 60 means 1/60s. |
| `float` | [`ExposureBlendWeight`](#exposureblendweight) | Exposure contribution weight. 0 leaves exposure untouched; 1 applies ISO/Shutter fully. |

---

#### ISO { #iso }

```cpp
float ISO { 100.f }
```

Sensor sensitivity. Clamped to at least 1.

---

#### ShutterSpeed { #shutterspeed }

```cpp
float ShutterSpeed { 60.f }
```

Shutter speed in 1/seconds. `60` means `1/60s`. Clamped to at least 1.

---

#### ExposureBlendWeight { #exposureblendweight }

```cpp
float ExposureBlendWeight { 1.f }
```

Exposure contribution weight. `0` leaves ISO/Shutter untouched; `1` applies ISO/Shutter fully.

### Public Methods

| Return | Name | Description |
|--------|------|-------------|
| | [`UComposableCameraExposureNode`](#ucomposablecameraexposurenode-1) `inline` | Sets the palette category to `Optics`. |
| `void` | [`OnTickNode_Implementation`](#onticknode_implementation) `virtual` | Writes clamped ISO, shutter speed, and exposure blend weight to the output pose. |
| `void` | [`GetPinDeclarations_Implementation`](#getpindeclarations_implementation) `virtual` `const` | Declares optional float input pins for ISO, shutter speed, and exposure blend weight. |

---

#### UComposableCameraExposureNode { #ucomposablecameraexposurenode-1 }

`inline`

```cpp
inline UComposableCameraExposureNode()
```

---

#### OnTickNode_Implementation { #onticknode_implementation }

`virtual`

```cpp
virtual void OnTickNode_Implementation(float DeltaTime, const FComposableCameraPose & CurrentCameraPose, FComposableCameraPose & OutCameraPose)
```

---

#### GetPinDeclarations_Implementation { #getpindeclarations_implementation }

`virtual` `const`

```cpp
virtual void GetPinDeclarations_Implementation(TArray< FComposableCameraNodePinDeclaration > & OutPins) const
```
