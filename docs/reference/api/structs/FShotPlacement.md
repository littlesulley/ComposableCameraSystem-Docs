# FShotPlacement { #fshotplacement }

```cpp
#include <ComposableCameraShot.h>
```

Placement layer for Shot solving. It decides camera position before Aim solves rotation, Lens solves FOV, Focus solves focus distance, and Shot roll is composed onto the final rotation.

Placement's anchor is the world point the camera is placed relative to. Aim's anchor is the world point the camera looks at. They can be the same for standard follow/orbit shots, or different for over-the-shoulder and two-shot compositions.

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `FComposableCameraAnchorSpec` | [`PlacementAnchor`](#placementanchor) | World point the camera is placed relative to. |
| `EShotPlacementMode` | [`Mode`](#mode-2) | Selects how position is computed. |
| `EShotPlacementBasisFrame` | [`BasisFrame`](#basisframe) | Basis selector for `LocalCameraDirection` in `AnchorOrbit`. |
| `int32` | [`BasisActorIndex`](#basisactorindex) | Target index used as the inherited basis actor when `BasisFrame == InheritFromActor`. |
| `FVector2D` | [`LocalCameraDirection`](#localcameradirection) | Camera direction in basis space, expressed as yaw/pitch degrees. `AnchorOrbit` only. |
| `float` | [`Distance`](#distance) | Camera-to-placement-anchor distance in centimeters. |
| `float` | [`DistanceSpeed`](#distancespeed) | IIR damping speed for `Distance`. |
| `FVector2D` | [`ScreenPosition`](#screenposition-1) | `AnchorAtScreen` target screen position for the placement anchor. |
| `FShotScreenZones` | [`PlacementZones`](#placementzones) | Dead/soft zones for `Placement.ScreenPosition`; consumed by `AnchorAtScreen`. |
| `FVector` | [`FixedWorldPosition`](#fixedworldposition) | Explicit camera world position for `FixedWorldPosition` mode. |

---

#### PlacementAnchor { #placementanchor }

```cpp
FComposableCameraAnchorSpec PlacementAnchor
```

World point the camera is placed relative to. It resolves from the Shot's target list or from a fixed world point depending on the anchor spec.

---

#### Mode { #mode-2 }

```cpp
EShotPlacementMode Mode
```

Selects the position solve:

* `AnchorOrbit`: spherical placement around `PlacementAnchor`.
* `AnchorAtScreen`: places the anchor at an authored screen position while Aim solves rotation.
* `FixedWorldPosition`: uses `FixedWorldPosition` directly.

---

#### BasisFrame { #basisframe }

```cpp
EShotPlacementBasisFrame BasisFrame
```

Reference-frame selector for `LocalCameraDirection`. `World` uses global axes. `InheritFromActor` uses the basis quaternion from `Targets[BasisActorIndex]`. Only consumed by `AnchorOrbit`.

---

#### BasisActorIndex { #basisactorindex }

```cpp
int32 BasisActorIndex = 0
```

Index into `Targets` for the actor basis when `BasisFrame == InheritFromActor`. Falls back to world basis if the index or actor cannot resolve.

---

#### LocalCameraDirection { #localcameradirection }

```cpp
FVector2D LocalCameraDirection = FVector2D(180.f, 0.f)
```

Camera position direction in basis space, expressed as yaw/pitch degrees. Only consumed by `AnchorOrbit`.

---

#### Distance { #distance }

```cpp
float Distance = 200.f
```

Camera-to-placement-anchor distance in centimeters. In `AnchorOrbit`, this is the Euclidean distance along `LocalCameraDirection`. In `AnchorAtScreen`, this is the camera-frame depth used by the screen-position solve.

The authored range is `[1, 10000]` cm.

---

#### DistanceSpeed { #distancespeed }

```cpp
float DistanceSpeed = 0.f
```

IIR damping speed for `Distance` using `FMath::FInterpTo` semantics. `0` means the solver snaps to the authored distance. Positive values glide toward changes. Damping is skipped in `FixedWorldPosition` mode and starts once a prior pose exists.

---

#### ScreenPosition { #screenposition-1 }

```cpp
FVector2D ScreenPosition = FVector2D::ZeroVector
```

`AnchorAtScreen`-only target for where the resolved placement anchor should land on screen, normalized to `[-0.5, 0.5]` on each axis; `(0, 0)` is screen center.

On a first-frame hard seed with `Aim.Mode == LookAtAnchor`, the solver runs a bounded joint Position+Rotation iteration so `Placement.ScreenPosition` and `Aim.ScreenPosition` start from a coherent pose. Once a prior pose exists, the hot path uses the cheaper decoupled Position-then-Aim solve and relies on zones/damping for steady-state behavior.

Requires `Aim.Mode == LookAtAnchor` and a distinct Aim anchor. If `PlacementAnchor == AimAnchor`, the solver logs a warning and skips the pose update; use `AnchorOrbit` for single-anchor framing.

---

#### PlacementZones { #placementzones }

```cpp
FShotScreenZones PlacementZones
```

Cinemachine-style screen-space framing zones for `Placement.ScreenPosition`. Only consumed in `AnchorAtScreen`. `AnchorOrbit` and `FixedWorldPosition` ignore this field.

---

#### FixedWorldPosition { #fixedworldposition }

```cpp
FVector FixedWorldPosition = FVector::ZeroVector
```

Explicit camera world position used iff `Mode == FixedWorldPosition`.

### Public Static Attributes

| Return | Name | Description |
|--------|------|-------------|
| `constexpr float` | [`MinDistance`](#mindistance) `static` | Minimum authored `Distance`, in centimeters. |
| `constexpr float` | [`MaxDistance`](#maxdistance) `static` | Maximum authored `Distance`, in centimeters. |

---

#### MinDistance { #mindistance }

`static`

```cpp
constexpr float MinDistance = 1.f
```

Minimum authored `Distance`, in centimeters.

---

#### MaxDistance { #maxdistance }

`static`

```cpp
constexpr float MaxDistance = 10000.f
```

Maximum authored `Distance`, in centimeters.
