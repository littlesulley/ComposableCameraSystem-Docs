
# UComposableCameraLensNode { #ucomposablecameralensnode }

```cpp
#include <ComposableCameraLensNode.h>
```

> **Inherits:** [`UComposableCameraCameraNodeBase`](../uobjects-other/UComposableCameraCameraNodeBase.md#ucomposablecameracameranodebase)

Authors physical-lens parameters on the camera pose (focal length, aperture, focus distance, diaphragm blade count) and gates whether the pose's physical camera settings are applied to post-process.

Conceptually mirrors Epic's GameplayCameras ULensParametersCameraNode, but split between two concerns:

1. Writing focal length + aperture + focus distance + blade count onto the pose, so they are available both to the post-process blend and to any downstream node that reads the pose.

1. Toggling PhysicalCameraBlendWeight so that ApplyPhysicalCameraSettings() actually writes DoF / exposure into FPostProcessSettings.

FOV mode coupling: writing FocalLength is orthogonal to SetFieldOfViewDegrees. To put the pose in "focal length drives FOV" mode, this node clears the pose's FieldOfView sentinel (FieldOfView = -1) iff bOverrideFieldOfViewFromFocalLength is true — otherwise whatever the upstream FieldOfViewNode authored remains authoritative for FOV resolution, and FocalLength is only used as a post-process DoF input.

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `float` | [`FocalLength`](#focallength-1)  | Focal length in millimetres. Drives both physical DoF and (optionally) FOV. |
| `float` | [`Aperture`](#aperture-1)  | Lens aperture (f-stops). Smaller number = wider aperture = more DoF blur. |
| `float` | [`FocusDistance`](#focusdistance-1)  | Distance to the focus subject in world units. <= 0 leaves the pose's FocusDistance sentinel in place (no DoF override). |
| `int32` | [`DiaphragmBladeCount`](#diaphragmbladecount-1)  | Number of blades in the lens diaphragm. Affects bokeh polygon shape. |
| `float` | [`PhysicalCameraBlendWeight`](#physicalcamerablendweight-1)  | Physical camera contribution weight. 0 disables ApplyPhysicalCameraSettings entirely; 1 applies it at full strength. Default 1.0 so that merely placing this node in the chain is enough to get DoF / auto-exposure driven off the authored lens values — callers who want a per-frame fade should wire this pin explicitly. |
| `bool` | [`bOverrideFieldOfViewFromFocalLength`](#boverridefieldofviewfromfocallength)  | When true, this node also puts the pose in focal-length-drives-FOV mode by clearing FieldOfView to -1. Use this when the LensNode is the authoritative FOV source (no separate FieldOfViewNode upstream). When false, FOV is left alone — the pose keeps whatever FOV mode an upstream node wrote. |

---

#### FocalLength { #focallength-1 }

```cpp
float FocalLength { 35.f }
```

Focal length in millimetres. Drives both physical DoF and (optionally) FOV.

---

#### Aperture { #aperture-1 }

```cpp
float Aperture { 2.8f }
```

Lens aperture (f-stops). Smaller number = wider aperture = more DoF blur.

---

#### FocusDistance { #focusdistance-1 }

```cpp
float FocusDistance { -1.f }
```

Distance to the focus subject in world units. <= 0 leaves the pose's FocusDistance sentinel in place (no DoF override).

---

#### DiaphragmBladeCount { #diaphragmbladecount-1 }

```cpp
int32 DiaphragmBladeCount { 8 }
```

Number of blades in the lens diaphragm. Affects bokeh polygon shape.

---

#### PhysicalCameraBlendWeight { #physicalcamerablendweight-1 }

```cpp
float PhysicalCameraBlendWeight { 1.f }
```

Physical camera contribution weight. 0 disables ApplyPhysicalCameraSettings entirely; 1 applies it at full strength. Default 1.0 so that merely placing this node in the chain is enough to get DoF / auto-exposure driven off the authored lens values — callers who want a per-frame fade should wire this pin explicitly.

---

#### bOverrideFieldOfViewFromFocalLength { #boverridefieldofviewfromfocallength }

```cpp
bool bOverrideFieldOfViewFromFocalLength { true }
```

When true, this node also puts the pose in focal-length-drives-FOV mode by clearing FieldOfView to -1. Use this when the LensNode is the authoritative FOV source (no separate FieldOfViewNode upstream). When false, FOV is left alone — the pose keeps whatever FOV mode an upstream node wrote.

### Public Methods

| Return | Name | Description |
|--------|------|-------------|
| `void` | [`OnTickNode_Implementation`](#onticknode_implementation) `virtual` |  |
| `void` | [`GetPinDeclarations_Implementation`](#getpindeclarations_implementation) `virtual` `const` |  |

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
