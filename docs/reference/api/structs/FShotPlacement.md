
# FShotPlacement { #fshotplacement }

```cpp
#include <ComposableCameraShot.h>
```

Placement layer — decides camera POSITION. Layered architecture: the solver runs Placement first to get a Position, then Aim (which only decides Rotation), then Lens (FOV), then Focus. See Docs/ShotBasedKeyframing.md §3.4 + §4.3.

Anchor concepts unified: Placement's anchor is the world point the camera is placed RELATIVE TO; Aim's anchor (separate field on `[FShotAim](FShotAim.md#fshotaim)`) is the world point the camera LOOKS AT. They can be the same (standard third-person) or different (OTS — placed near A, looking at B).

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `FComposableCameraAnchorSpec` | [`PlacementAnchor`](#placementanchor)  | Where in the world the camera is placed RELATIVE to. Resolved from the Shot's Targets list (or a fixed world point). |
| `EShotPlacementMode` | [`Mode`](#mode-2)  | Selects how Position is computed. |
| `EShotPlacementBasisFrame` | [`BasisFrame`](#basisframe)  | Reference-frame selector for `LocalCameraDirection`. World means global axes; InheritFromActor means the basis actor's world quat. Only consumed in `AnchorOrbit` mode (pure spherical); the `AnchorAtScreen` mode borrows its forward axis from Aim and has no need for a basis. |
| `int32` | [`BasisActorIndex`](#basisactorindex)  | Index into Targets — the actor whose world quat is the basis when `BasisFrame == InheritFromActor`. Falls back to World basis when out of range or the actor is null. AnchorOrbit-only. |
| `FVector2D` | [`LocalCameraDirection`](#localcameradirection)  | Camera position direction in BasisFrame's basis, expressed as (Yaw, Pitch) in degrees. AnchorOrbit-only — `AnchorAtScreen` derives camera position from the joint Aim+Placement screen constraints, no spherical direction parameter. Roll about the look axis is authored separately on the Shot's top-level `Roll` field. |
| `float` | [`Distance`](#distance)  | Camera-to-PlacementAnchor distance in world units (cm). Semantics depend on Mode: |
| `float` | [`DistanceSpeed`](#distancespeed)  | IIR damping speed for `Distance` (`FMath::FInterpTo` Speed semantics). `0` = no damping → camera snaps to the authored Distance every frame (V1 default behavior). Positive = damped — when the designer drags the Distance slider or a Sequencer track keys it, the camera glides toward the new value over time instead of teleporting. Higher values = snappier; lower values = heavier camera. Independent of the screen-space framing zones (which damp X / Y); this damps Z. |
| `FVector2D` | [`ScreenPosition`](#screenposition-1)  | `AnchorAtScreen`-only. Where the resolved PlacementAnchor should land on screen, normalized to [-0.5, 0.5]² — (0, 0) is screen center. Realized via the joint Position+Rotation solve described in spec §4.3 — camera position is constrained such that PlacementAnchor is at depth `Distance` and screen `ScreenPosition` AT THE SAME TIME AS Aim's rotation puts AimAnchor at `Aim.ScreenPosition`. Both constraints are simultaneously satisfied by a closed-form solve (5 constraints on 5 unknowns). |
| `FShotScreenZones` | [`PlacementZones`](#placementzones)  | Cinemachine-style screen-space framing zones for `Placement.ScreenPosition`. Only consumed in `AnchorAtScreen` placement mode (where placement actually produces a screen-position constraint on PlacementAnchor); ignored in `AnchorOrbit` (no `Placement.ScreenPosition`) and `FixedWorldPosition` (placement is world-locked, not screen-driven). |
| `FVector` | [`FixedWorldPosition`](#fixedworldposition)  | Used iff `Mode == FixedWorldPosition`. Camera lives at this world point; PlacementAnchor / Distance / Direction / ScreenPosition are ignored in this mode. |

---

#### PlacementAnchor { #placementanchor }

```cpp
FComposableCameraAnchorSpec PlacementAnchor
```

Where in the world the camera is placed RELATIVE to. Resolved from the Shot's Targets list (or a fixed world point).

---

#### Mode { #mode-2 }

```cpp
EShotPlacementMode Mode = 
```

Selects how Position is computed.

---

#### BasisFrame { #basisframe }

```cpp
EShotPlacementBasisFrame BasisFrame = 
```

Reference-frame selector for `LocalCameraDirection`. World means global axes; InheritFromActor means the basis actor's world quat. Only consumed in `AnchorOrbit` mode (pure spherical); the `AnchorAtScreen` mode borrows its forward axis from Aim and has no need for a basis.

---

#### BasisActorIndex { #basisactorindex }

```cpp
int32 BasisActorIndex = 0
```

Index into Targets — the actor whose world quat is the basis when `BasisFrame == InheritFromActor`. Falls back to World basis when out of range or the actor is null. AnchorOrbit-only.

---

#### LocalCameraDirection { #localcameradirection }

```cpp
FVector2D LocalCameraDirection = FVector2D(180.f, 0.f)
```

Camera position direction in BasisFrame's basis, expressed as (Yaw, Pitch) in degrees. AnchorOrbit-only — `AnchorAtScreen` derives camera position from the joint Aim+Placement screen constraints, no spherical direction parameter. Roll about the look axis is authored separately on the Shot's top-level `Roll` field.

---

#### Distance { #distance }

```cpp
float Distance = 200.f
```

Camera-to-PlacementAnchor distance in world units (cm). Semantics depend on Mode:

* AnchorOrbit: Euclidean — measured along the unit direction vector implied by `LocalCameraDirection`. In the typical case where camera looks at the placement anchor, this equals the cam-frame depth.

* AnchorAtScreen: cam-frame depth (X coordinate of PlacementAnchor under the joint-solve camera rotation, which looks at AimAnchor). Designer thinks "I want PlacementAnchor
    this far in front of camera" regardless of where the lateral offset lands it.

Range `[1, 10000]` cm = `[1cm, 100m]`. Floor matches the solver's pre-flight check (1cm prevents division by ~0 in the Picard iteration). Ceiling is a sanity cap against typo / scroll-spam pushing Distance to ~1e9 — the solver's float math degrades well before that, so a hard 100m clamp is cheaper to enforce here than to chase down NaN poses downstream. 100m covers the vast majority of in-engine framing (character / interior / vehicle scale); projects that genuinely need >100m can lift this manually — promote to a project setting if the need recurs.

`SliderExponent = "3.0"` weights the Details-panel drag toward the low end of the range so dragging at <1000 cm (the typical framing scale) doesn't blast past the value the designer is trying to hit. Picked over a fixed `Delta = "1.0"` because at high-end values (multi-km vista shots) a fixed-cm-per-pixel rate would be agonizingly slow.

---

#### DistanceSpeed { #distancespeed }

```cpp
float DistanceSpeed = 0.f
```

IIR damping speed for `Distance` (`FMath::FInterpTo` Speed semantics). `0` = no damping → camera snaps to the authored Distance every frame (V1 default behavior). Positive = damped — when the designer drags the Distance slider or a Sequencer track keys it, the camera glides toward the new value over time instead of teleporting. Higher values = snappier; lower values = heavier camera. Independent of the screen-space framing zones (which damp X / Y); this damps Z.

Skipped in `FixedWorldPosition` mode (Distance is unused there). Requires `PriorPose != nullptr` like the rest of the V2.2 stateful solver — first-frame seed snaps to authored value, damping kicks in from frame 2 onward.

---

#### ScreenPosition { #screenposition-1 }

```cpp
FVector2D ScreenPosition = FVector2D::ZeroVector
```

`AnchorAtScreen`-only. Where the resolved PlacementAnchor should land on screen, normalized to [-0.5, 0.5]² — (0, 0) is screen center. Realized via the joint Position+Rotation solve described in spec §4.3 — camera position is constrained such that PlacementAnchor is at depth `Distance` and screen `ScreenPosition` AT THE SAME TIME AS Aim's rotation puts AimAnchor at `Aim.ScreenPosition`. Both constraints are simultaneously satisfied by a closed-form solve (5 constraints on 5 unknowns).

Requires `Aim.Mode == LookAtAnchor` AND `AimAnchor != PlacementAnchor` — the joint solve degenerates without both. Solver logs warning + skips pose update otherwise.

---

#### PlacementZones { #placementzones }

```cpp
FShotScreenZones PlacementZones
```

Cinemachine-style screen-space framing zones for `Placement.ScreenPosition`. Only consumed in `AnchorAtScreen` placement mode (where placement actually produces a screen-position constraint on PlacementAnchor); ignored in `AnchorOrbit` (no `Placement.ScreenPosition`) and `FixedWorldPosition` (placement is world-locked, not screen-driven).

When enabled the joint Picard solve runs against the zone-derived effective screen target instead of the raw authored `ScreenPosition`, with damping applied in screen space — anchor inside the dead zone produces zero error → joint solve is short-circuited and the camera holds its previous `LastOutputPose`. See `[FShotScreenZones](FShotScreenZones.md#fshotscreenzones)` for the algorithm description.

---

#### FixedWorldPosition { #fixedworldposition }

```cpp
FVector FixedWorldPosition = FVector::ZeroVector
```

Used iff `Mode == FixedWorldPosition`. Camera lives at this world point; PlacementAnchor / Distance / Direction / ScreenPosition are ignored in this mode.

### Public Static Attributes

| Return | Name | Description |
|--------|------|-------------|
| `constexpr float` | [`MinDistance`](#mindistance) `static` | Authoring range for `Distance`, in cm. Mirrored by the field's `ClampMin` / `ClampMax` UPROPERTY meta — but since UPROPERTY meta only enforces clamping at the Details-panel input layer, all *code* writers (gestures, reverse-solve, BP setters, runtime) must go through `FMath::Clamp(..., MinDistance, MaxDistance)` to keep the canonical range in sync. See the `Distance` field comment for the rationale behind the bounds. |
| `constexpr float` | [`MaxDistance`](#maxdistance) `static` |  |

---

#### MinDistance { #mindistance }

`static`

```cpp
constexpr float MinDistance = 1.f
```

Authoring range for `Distance`, in cm. Mirrored by the field's `ClampMin` / `ClampMax` UPROPERTY meta — but since UPROPERTY meta only enforces clamping at the Details-panel input layer, all *code* writers (gestures, reverse-solve, BP setters, runtime) must go through `FMath::Clamp(..., MinDistance, MaxDistance)` to keep the canonical range in sync. See the `Distance` field comment for the rationale behind the bounds.

---

#### MaxDistance { #maxdistance }

`static`

```cpp
constexpr float MaxDistance = 10000.f
```
