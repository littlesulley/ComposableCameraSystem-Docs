
# FComposableCameraPose { #fcomposablecamerapose }

```cpp
#include <ComposableCameraCameraBase.h>
```

Camera pose state produced by node evaluation and consumed by the PCM.

Field categories:

* Transform (Position, Rotation) — always lerped.

* FOV dual-mode (FieldOfView, FocalLength) — a pose expresses FOV either in degrees (FieldOfView > 0) or via physical optics (FocalLength > 0), never both. Use [GetEffectiveFieldOfView()](#geteffectivefieldofview) to resolve to degrees. [BlendBy()](#blendby) resolves both sides to degrees BEFORE lerping and emits a degrees-mode result (FocalLength = -1). See "FOV resolution invariant" in DesignDoc.

* Physical camera (SensorWidth/Height, Aperture, FocusDistance, ISO, etc.) — always lerped; only applied to post-process when PhysicalCameraBlendWeight > 0 via [ApplyPhysicalCameraSettings()](#applyphysicalcamerasettings).

* Projection & aspect (ProjectionMode, ConstrainAspectRatio, ...) — booleans and enums snap at 50% blend factor; numerics (OrthographicWidth etc.) lerp normally.

Sentinel semantics (<= 0 means "unset"):

* FieldOfView: -1 means "use FocalLength".

* FocusDistance: -1 means "no DoF override". These fields use LerpOptional semantics in [BlendBy()](#blendby): if one side is unset, the valid side's value is inherited across the blend rather than lerped through a meaningless range.

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `FVector` | [`Position`](#position)  |  |
| `FRotator` | [`Rotation`](#rotation)  |  |
| `double` | [`FieldOfView`](#fieldofview)  | Horizontal FOV in degrees. If <= 0, FocalLength is used instead. |
| `float` | [`FocalLength`](#focallength)  | Focal length in mm. If <= 0, FieldOfView (in degrees) is used instead. |
| `float` | [`SensorWidth`](#sensorwidth)  | Sensor width in mm. Super35 default. |
| `float` | [`SensorHeight`](#sensorheight)  | Sensor height in mm. |
| `float` | [`Aperture`](#aperture)  | Lens aperture in f-stops. Used for DoF when PhysicalCameraBlendWeight > 0. |
| `float` | [`FocusDistance`](#focusdistance)  | Focus distance in world units. <= 0 means "no DoF override" (sentinel). |
| `float` | [`ShutterSpeed`](#shutterspeed)  | Shutter speed in 1/seconds. Used for auto-exposure when PhysicalCameraBlendWeight > 0. |
| `float` | [`ISO`](#iso)  | Sensor sensitivity in ISO. |
| `int32` | [`DiaphragmBladeCount`](#diaphragmbladecount)  | Number of blades in the lens diaphragm (affects bokeh shape). |
| `float` | [`SqueezeFactor`](#squeezefactor)  | Anamorphic squeeze factor. 1.0 = spherical. |
| `float` | [`Overscan`](#overscan)  | Sensor overscan percentage (0 = none). |
| `float` | [`PhysicalCameraBlendWeight`](#physicalcamerablendweight)  | Blend weight for physical-camera post-process contribution. 0 = skip ApplyPhysicalCameraSettings entirely (no DoF/exposure override). 1 = apply physical settings at full strength. Naturally gates the fade-in of DoF during non-physical -> physical transitions. |
| `TEnumAsByte< ECameraProjectionMode::Type >` | [`ProjectionMode`](#projectionmode)  | Projection mode (Perspective or Orthographic). Snapped at 50% blend. |
| `bool` | [`ConstrainAspectRatio`](#constrainaspectratio)  | Whether to constrain aspect ratio (letterbox). Snapped at 50% blend. |
| `bool` | [`OverrideAspectRatioAxisConstraint`](#overrideaspectratioaxisconstraint)  | Whether to override the default aspect ratio axis constraint. Snapped at 50% blend. |
| `TEnumAsByte< EAspectRatioAxisConstraint >` | [`AspectRatioAxisConstraint`](#aspectratioaxisconstraint)  | Axis constraint (only honored when OverrideAspectRatioAxisConstraint is true). Snapped at 50% blend. |
| `float` | [`OrthographicWidth`](#orthographicwidth)  | Orthographic view width in world units (only honored when ProjectionMode = Orthographic). |
| `float` | [`OrthoNearClipPlane`](#orthonearclipplane)  | Ortho near clip plane (only honored when ProjectionMode = Orthographic). |
| `float` | [`OrthoFarClipPlane`](#orthofarclipplane)  | Ortho far clip plane (only honored when ProjectionMode = Orthographic). |

---

#### Position { #position }

```cpp
FVector Position { 0, 0, 0 }
```

---

#### Rotation { #rotation }

```cpp
FRotator Rotation { 0, 0, 0 }
```

---

#### FieldOfView { #fieldofview }

```cpp
double FieldOfView { -1.0 }
```

Horizontal FOV in degrees. If <= 0, FocalLength is used instead.

---

#### FocalLength { #focallength }

```cpp
float FocalLength { 35.f }
```

Focal length in mm. If <= 0, FieldOfView (in degrees) is used instead.

---

#### SensorWidth { #sensorwidth }

```cpp
float SensorWidth { 24.89f }
```

Sensor width in mm. Super35 default.

---

#### SensorHeight { #sensorheight }

```cpp
float SensorHeight { 18.67f }
```

Sensor height in mm.

---

#### Aperture { #aperture }

```cpp
float Aperture { 2.8f }
```

Lens aperture in f-stops. Used for DoF when PhysicalCameraBlendWeight > 0.

---

#### FocusDistance { #focusdistance }

```cpp
float FocusDistance { -1.f }
```

Focus distance in world units. <= 0 means "no DoF override" (sentinel).

---

#### ShutterSpeed { #shutterspeed }

```cpp
float ShutterSpeed { 60.f }
```

Shutter speed in 1/seconds. Used for auto-exposure when PhysicalCameraBlendWeight > 0.

---

#### ISO { #iso }

```cpp
float ISO { 100.f }
```

Sensor sensitivity in ISO.

---

#### DiaphragmBladeCount { #diaphragmbladecount }

```cpp
int32 DiaphragmBladeCount { 8 }
```

Number of blades in the lens diaphragm (affects bokeh shape).

---

#### SqueezeFactor { #squeezefactor }

```cpp
float SqueezeFactor { 1.f }
```

Anamorphic squeeze factor. 1.0 = spherical.

---

#### Overscan { #overscan }

```cpp
float Overscan { 0.f }
```

Sensor overscan percentage (0 = none).

---

#### PhysicalCameraBlendWeight { #physicalcamerablendweight }

```cpp
float PhysicalCameraBlendWeight { 0.f }
```

Blend weight for physical-camera post-process contribution. 0 = skip ApplyPhysicalCameraSettings entirely (no DoF/exposure override). 1 = apply physical settings at full strength. Naturally gates the fade-in of DoF during non-physical -> physical transitions.

---

#### ProjectionMode { #projectionmode }

```cpp
TEnumAsByte< ECameraProjectionMode::Type > ProjectionMode { ECameraProjectionMode::Perspective }
```

Projection mode (Perspective or Orthographic). Snapped at 50% blend.

---

#### ConstrainAspectRatio { #constrainaspectratio }

```cpp
bool ConstrainAspectRatio { false }
```

Whether to constrain aspect ratio (letterbox). Snapped at 50% blend.

---

#### OverrideAspectRatioAxisConstraint { #overrideaspectratioaxisconstraint }

```cpp
bool OverrideAspectRatioAxisConstraint { false }
```

Whether to override the default aspect ratio axis constraint. Snapped at 50% blend.

---

#### AspectRatioAxisConstraint { #aspectratioaxisconstraint }

```cpp
TEnumAsByte< EAspectRatioAxisConstraint > AspectRatioAxisConstraint { EAspectRatioAxisConstraint::AspectRatio_MaintainYFOV }
```

Axis constraint (only honored when OverrideAspectRatioAxisConstraint is true). Snapped at 50% blend.

---

#### OrthographicWidth { #orthographicwidth }

```cpp
float OrthographicWidth { 512.f }
```

Orthographic view width in world units (only honored when ProjectionMode = Orthographic).

---

#### OrthoNearClipPlane { #orthonearclipplane }

```cpp
float OrthoNearClipPlane { 0.f }
```

Ortho near clip plane (only honored when ProjectionMode = Orthographic).

---

#### OrthoFarClipPlane { #orthofarclipplane }

```cpp
float OrthoFarClipPlane { 10000.f }
```

Ortho far clip plane (only honored when ProjectionMode = Orthographic).

### Public Methods

| Return | Name | Description |
|--------|------|-------------|
| `double` | [`GetEffectiveFieldOfView`](#geteffectivefieldofview) `const` | Resolve the effective horizontal FOV in degrees. Uses FocalLength + SensorWidth if FocalLength > 0, otherwise uses FieldOfView directly. Falls back to a reasonable default if both are unset. |
| `void` | [`SetFieldOfViewDegrees`](#setfieldofviewdegrees)  | Set FOV in degrees, clearing the FocalLength sentinel so this pose is unambiguously in degrees mode. Nodes that produce an FOV in degrees (like FieldOfViewNode) should call this instead of assigning FieldOfView directly. |
| `bool` | [`ApplyPhysicalCameraSettings`](#applyphysicalcamerasettings) `const` | Apply physical-camera-derived settings (DoF, auto-exposure) to a post-process settings block. No-op if PhysicalCameraBlendWeight <= 0. Scales contribution by PhysicalCameraBlendWeight. Mirrors GameplayCameras' FCameraPose::ApplyPhysicalCameraSettings. |
| `void` | [`BlendBy`](#blendby)  | Blend this pose toward Other by OtherWeight in [0, 1]. Blend rules (see struct comment for categories): |

---

#### GetEffectiveFieldOfView { #geteffectivefieldofview }

`const`

```cpp
double GetEffectiveFieldOfView() const
```

Resolve the effective horizontal FOV in degrees. Uses FocalLength + SensorWidth if FocalLength > 0, otherwise uses FieldOfView directly. Falls back to a reasonable default if both are unset.

---

#### SetFieldOfViewDegrees { #setfieldofviewdegrees }

```cpp
void SetFieldOfViewDegrees(double InFieldOfViewDegrees)
```

Set FOV in degrees, clearing the FocalLength sentinel so this pose is unambiguously in degrees mode. Nodes that produce an FOV in degrees (like FieldOfViewNode) should call this instead of assigning FieldOfView directly.

---

#### ApplyPhysicalCameraSettings { #applyphysicalcamerasettings }

`const`

```cpp
bool ApplyPhysicalCameraSettings(FPostProcessSettings & PostProcessSettings, bool bOverwriteSettings) const
```

Apply physical-camera-derived settings (DoF, auto-exposure) to a post-process settings block. No-op if PhysicalCameraBlendWeight <= 0. Scales contribution by PhysicalCameraBlendWeight. Mirrors GameplayCameras' FCameraPose::ApplyPhysicalCameraSettings.

**Parameters**

* `PostProcessSettings` Target to modify. 

* `bOverwriteSettings` If true, overwrites already-set post-process entries; else only writes unset ones. 

**Returns**

true if any settings were written, false if the call was a no-op.

---

#### BlendBy { #blendby }

```cpp
void BlendBy(const FComposableCameraPose & Other, float OtherWeight)
```

Blend this pose toward Other by OtherWeight in [0, 1]. Blend rules (see struct comment for categories):

* Position: linear lerp.

* Rotation: delta-angle lerp (normalized).

* FOV: resolve both sides via [GetEffectiveFieldOfView()](#geteffectivefieldofview), lerp degrees, emit degrees-mode result (FocalLength = -1).

* Physical numerics: linear lerp.

* Sentinel fields (FocusDistance): LerpOptional — inherit valid side if the other is unset.

* Projection booleans/enums: snap at OtherWeight >= 0.5.
