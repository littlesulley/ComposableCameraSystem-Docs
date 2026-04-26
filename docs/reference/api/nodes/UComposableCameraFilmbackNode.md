
# UComposableCameraFilmbackNode { #ucomposablecamerafilmbacknode }

```cpp
#include <ComposableCameraFilmbackNode.h>
```

> **Inherits:** [`UComposableCameraCameraNodeBase`](../uobjects-other/UComposableCameraCameraNodeBase.md#ucomposablecameracameranodebase)

Authors filmback (sensor) and aspect-ratio parameters on the camera pose: sensor width/height, anamorphic squeeze, overscan, and aspect-ratio constraint configuration. Mirrors Epic's UFilmbackCameraNode but integrates with the CCS pose-authoritative policy rather than a dedicated filmback struct.

The sensor dimensions are consumed by [FComposableCameraPose::GetEffectiveFieldOfView()](../structs/FComposableCameraPose.md#geteffectivefieldofview) when the pose is in focal-length mode (FieldOfView <= 0), so changing the filmback while holding focal length constant naturally changes the effective FOV — exactly as on a real camera.

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `float` | [`SensorWidth`](#sensorwidth-1)  | Sensor width in mm. Super35 default (24.89 mm). Used by FOV resolution when FocalLength drives FOV. |
| `float` | [`SensorHeight`](#sensorheight-1)  | Sensor height in mm. |
| `float` | [`SqueezeFactor`](#squeezefactor-1)  | Anamorphic squeeze factor. 1.0 = spherical (no squeeze). 2.0 = classic 2x anamorphic. |
| `float` | [`Overscan`](#overscan-1)  | Sensor overscan percentage (0 = none). Used by the post-process / renderer to render a larger area than the final framing. |
| `bool` | [`bConstrainAspectRatio`](#bconstrainaspectratio)  | Whether to constrain the aspect ratio (letterbox / pillarbox) when the viewport ratio differs from the sensor ratio. |
| `bool` | [`bOverrideAspectRatioAxisConstraint`](#boverrideaspectratioaxisconstraint)  | Whether to override the project-wide default aspect-ratio axis constraint. |
| `TEnumAsByte< EAspectRatioAxisConstraint >` | [`AspectRatioAxisConstraint`](#aspectratioaxisconstraint-1)  | Axis constraint to use when bOverrideAspectRatioAxisConstraint is true. |

---

#### SensorWidth { #sensorwidth-1 }

```cpp
float SensorWidth { 24.89f }
```

Sensor width in mm. Super35 default (24.89 mm). Used by FOV resolution when FocalLength drives FOV.

---

#### SensorHeight { #sensorheight-1 }

```cpp
float SensorHeight { 18.67f }
```

Sensor height in mm.

---

#### SqueezeFactor { #squeezefactor-1 }

```cpp
float SqueezeFactor { 1.f }
```

Anamorphic squeeze factor. 1.0 = spherical (no squeeze). 2.0 = classic 2x anamorphic.

---

#### Overscan { #overscan-1 }

```cpp
float Overscan { 0.f }
```

Sensor overscan percentage (0 = none). Used by the post-process / renderer to render a larger area than the final framing.

---

#### bConstrainAspectRatio { #bconstrainaspectratio }

```cpp
bool bConstrainAspectRatio { false }
```

Whether to constrain the aspect ratio (letterbox / pillarbox) when the viewport ratio differs from the sensor ratio.

---

#### bOverrideAspectRatioAxisConstraint { #boverrideaspectratioaxisconstraint }

```cpp
bool bOverrideAspectRatioAxisConstraint { false }
```

Whether to override the project-wide default aspect-ratio axis constraint.

---

#### AspectRatioAxisConstraint { #aspectratioaxisconstraint-1 }

```cpp
TEnumAsByte< EAspectRatioAxisConstraint > AspectRatioAxisConstraint { EAspectRatioAxisConstraint::AspectRatio_MaintainYFOV }
```

Axis constraint to use when bOverrideAspectRatioAxisConstraint is true.

### Public Methods

| Return | Name | Description |
|--------|------|-------------|
|  | [`UComposableCameraFilmbackNode`](#ucomposablecamerafilmbacknode-1) `inline` |  |
| `void` | [`OnTickNode_Implementation`](#onticknode_implementation-4) `virtual` |  |
| `void` | [`GetPinDeclarations_Implementation`](#getpindeclarations_implementation-4) `virtual` `const` |  |

---

#### UComposableCameraFilmbackNode { #ucomposablecamerafilmbacknode-1 }

`inline`

```cpp
inline UComposableCameraFilmbackNode()
```

---

#### OnTickNode_Implementation { #onticknode_implementation-4 }

`virtual`

```cpp
virtual void OnTickNode_Implementation(float DeltaTime, const FComposableCameraPose & CurrentCameraPose, FComposableCameraPose & OutCameraPose)
```

---

#### GetPinDeclarations_Implementation { #getpindeclarations_implementation-4 }

`virtual` `const`

```cpp
virtual void GetPinDeclarations_Implementation(TArray< FComposableCameraNodePinDeclaration > & OutPins) const
```
