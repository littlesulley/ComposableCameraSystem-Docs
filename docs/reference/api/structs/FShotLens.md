
# FShotLens { #fshotlens }

```cpp
#include <ComposableCameraShot.h>
```

Lens layer — decides FOV + Aperture. See spec §4.5.

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `EShotFOVMode` | [`FOVMode`](#fovmode)  |  |
| `float` | [`ManualFOV`](#manualfov)  |  |
| `float` | [`DesiredViewportFillRatio`](#desiredviewportfillratio)  | Used iff FOVMode == SolvedFromBoundsFit. The perceptual-union-box's longest axis should occupy this fraction of the viewport. 0.5 = half the viewport's longest axis. |
| `FFloatInterval` | [`FOVClamp`](#fovclamp)  | Hard clamp on the solved FOV. |
| `float` | [`Aperture`](#aperture)  | Lens aperture (f-stops). No auto mode — purely artistic. |
| `float` | [`FOVSpeed`](#fovspeed)  | IIR damping speed for the solved FOV (`FMath::FInterpTo` Speed semantics). `0` = no damping → camera snaps to the authored / solved FOV every frame (V1 default). Positive = damped — when the designer drags `ManualFOV` or `SolvedFromBoundsFit`'s solved FOV jumps (target-set composition change), the lens glides toward the new value over time. Independent of Placement.DistanceSpeed (which damps depth). Requires `PriorPose != nullptr` like the other V2.2 stateful damping; first-frame seed snaps to authored. |

---

#### FOVMode { #fovmode }

```cpp
EShotFOVMode FOVMode = 
```

---

#### ManualFOV { #manualfov }

```cpp
float ManualFOV = 79.f
```

---

#### DesiredViewportFillRatio { #desiredviewportfillratio }

```cpp
float DesiredViewportFillRatio = 0.5f
```

Used iff FOVMode == SolvedFromBoundsFit. The perceptual-union-box's longest axis should occupy this fraction of the viewport. 0.5 = half the viewport's longest axis.

---

#### FOVClamp { #fovclamp }

```cpp
FFloatInterval FOVClamp { 12.f, 100.f }
```

Hard clamp on the solved FOV.

---

#### Aperture { #aperture }

```cpp
float Aperture = 2.8f
```

Lens aperture (f-stops). No auto mode — purely artistic.

---

#### FOVSpeed { #fovspeed }

```cpp
float FOVSpeed = 0.f
```

IIR damping speed for the solved FOV (`FMath::FInterpTo` Speed semantics). `0` = no damping → camera snaps to the authored / solved FOV every frame (V1 default). Positive = damped — when the designer drags `ManualFOV` or `SolvedFromBoundsFit`'s solved FOV jumps (target-set composition change), the lens glides toward the new value over time. Independent of Placement.DistanceSpeed (which damps depth). Requires `PriorPose != nullptr` like the other V2.2 stateful damping; first-frame seed snaps to authored.
