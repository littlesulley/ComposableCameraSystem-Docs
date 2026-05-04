
# FModifierEntry { #fmodifierentry }

```cpp
#include <ComposableCameraNamespaces.h>
```

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `UComposableCameraModifierBase *` | [`Modifier`](#modifier)  |  |
| `UComposableCameraNodeModifierDataAsset *` | [`Asset`](#asset)  |  |

---

#### Modifier { #modifier }

```cpp
UComposableCameraModifierBase * Modifier
```

---

#### Asset { #asset }

```cpp
UComposableCameraNodeModifierDataAsset * Asset
```

### Public Methods

| Return | Name | Description |
|--------|------|-------------|
| `bool` | [`operator==`](#operator-7) `const` `inline` |  |
| `bool` | [`operator!=`](#operator-8) `const` `inline` |  |

---

#### operator== { #operator-7 }

`const` `inline`

```cpp
inline bool operator==(const FModifierEntry & Other) const
```

---

#### operator!= { #operator-8 }

`const` `inline`

```cpp
inline bool operator!=(const FModifierEntry & Other) const
```

# ShotSolver { #shotsolver }

Composition Solver for `[FComposableCameraShot](FComposableCameraShot.md#fcomposablecamerashot)` — the heart of the Shot-Based Keyframing runtime. Three-layer pipeline (Placement → Aim → Lens) plus an independent Focus pass and a final Roll composition.

1. Placement → camera Position AnchorOrbit — spherical placement around PlacementAnchor, plus lateral shift to realize Placement.ScreenPosition. FixedWorldPosition — camera at an explicit world point.

1. Aim → camera Rotation LookAtAnchor — closed-form rotation that lands AimAnchor at Aim.ScreenPosition (pre-rotated by -Roll so the constraint holds after the final Roll composition).

1. Lens → FOV + Aperture Manual — direct passthrough. SolvedFromBoundsFit — Weight-scaled Perceptual Union Box on Targets' bounds (BlackEye-derived; spec §4.5).

1. Focus → focus distance (independent) Manual / FollowPlacementAnchor / FollowAimAnchor / FollowCustomAnchor.

1. Roll composed onto output rotation as the final operation.

Pose-time only: consumes target world transforms at the moment of evaluation, no prediction.

All step functions are public so they can be unit-tested independently. The top-level orchestrator is `[SolveShot()](#solveshot)`.

Design notes:

* Header-inline. Optimizer benefits from seeing through the call boundaries; cold-enough that we don't care about code-size duplication. Same convention as `[Math/ComposableCameraMath.h](#composablecameramathh)`.

* No Blueprint-callable surface (per spec §1.4 "no runtime BP API for
    mutating Shot data"). Solver consumers are C++ only — `[UComposableCameraCompositionFramingNode](../nodes/UComposableCameraCompositionFramingNode.md#ucomposablecameracompositionframingnode)` and the unit tests.

* Chicken-and-egg with FOV: the rotation-solve projection uses the previous frame's FOV (passed in via `[FShotSolveContext](FShotSolveContext.md#fshotsolvecontext)`). When `FOVMode == Manual`, the manual value is used instead. When SolvedFromBoundsFit is active, the solver converges in 1-2 frames after a Shot transition.

* Coupling between Placement.ScreenPosition (lateral camera shift) and Aim.ScreenPosition (rotation) is intentionally one-way: Placement determines Position with a TENTATIVE look-at-PlacementAnchor rotation; Aim then OVERRIDES rotation. So when AimAnchor != PlacementAnchor, the placement anchor's *final* projected screen position drifts from `Placement.ScreenPosition`. Document this and let designers set both equal in the typical AimAnchor==PlacementAnchor case.

### Classes

| Name | Description |
|------|-------------|
| [`FShotPriorPose`](FShotPriorPose.md#fshotpriorpose) | Optional prior camera pose handed to `SolveShot` so the zone path has a base to project anchors through. Lightweight (Pos + Rot, FOV reuses `Context.PreviousFrameFOV`) — the Solver header stays free of `[FComposableCameraPose](FComposableCameraPose.md#fcomposablecamerapose)` (which lives one module-folder away in `[Cameras/ComposableCameraCameraBase.h](#composablecameracamerabaseh)`). |
| [`FShotSolveContext`](FShotSolveContext.md#fshotsolvecontext) | Per-frame inputs the solver needs from the runtime — viewport state + the previous frame's FOV (used as the projection FOV when the Shot is in SolvedFromBoundsFit mode). |
| [`FShotSolveResult`](FShotSolveResult.md#fshotsolveresult) | Solver output. `bValid == false` when an essential anchor cannot be resolved (placement / aim) — caller should preserve upstream pose for the frame. |

### Functions

| Return | Name | Description |
|--------|------|-------------|
| `FQuat` | [`ResolvePlacementBasis`](#resolveplacementbasis) `inline` | Resolves the basis quat for the Placement layer's `LocalCameraDirection`. |
| `FVector` | [`SolveAnchorOrbitPosition`](#solveanchororbitposition) `inline` | Camera position for AnchorOrbit mode: |
| `bool` | [`ClampAuthoredScreenPosition`](#clampauthoredscreenposition) `inline` | Clamp an authored screen position to `[-0.49, +0.49]²`. Returns true iff a clamp actually fired (caller logs a warning so the designer sees that their input was modified). |
| `FVector2D` | [`PreRotateScreenForRoll`](#prerotatescreenforroll) `inline` | Pre-rotates an authored screen position by -Roll so that, after the final pose has Roll composed onto its rotation, the world point still projects to the *authored* (un-pre-rotated) screen coords. |
| `FVector2D` | [`ApplyScreenZones`](#applyscreenzones) `inline` | Compute the effective screen-space target an anchor should be solved toward this frame, given: |
| `FVector2D` | [`ResolveEffectiveScreenTarget`](#resolveeffectivescreentarget) `inline` | Resolve the effective screen-space target for a single anchor given a prior camera pose. Convenience wrapper that handles the "anchor unresolvable" failure path (returns the authored screen position so the V1 hard-constraint solver still has something sensible to chew on — caller will likely fail on anchor resolve downstream anyway). |
| `bool` | [`SolveAnchorAtScreenPos`](#solveanchoratscreenpos) `inline` | Closed-form Position pass for `[EShotPlacementMode::AnchorAtScreen](#ComposableCameraShot_8h_1ad8bb9ef9d1aefe5e2b42410fc9908537a8da460d070406aab8e2caa882f9cbf2c)`. |
| `bool` | [`SolvePlacement`](#solveplacement) `inline` | Computes camera Position based on the Shot's Placement layer. Returns false (CamPos unchanged) when an essential anchor can't resolve — caller handles the no-pose fallback. |
| `FRotator` | [`SolveLookAtAnchorRotation`](#solvelookatanchorrotation) `inline` | Solves camera Rotation for LookAtAnchor mode: closed-form rotation that lands AimAnchor at Aim.ScreenPosition. Uses `SolveCameraRotationForScreenTarget` from `[ComposableCameraMath.h](#composablecameramathh)`. Roll is pre-compensated so the screen constraint holds after the caller composes Roll onto the result. |
| `bool` | [`SolveAim`](#solveaim) `inline` | Computes camera Rotation based on the Shot's Aim layer + Roll. Returns false (OutRot unchanged) when AimAnchor can't resolve. |
| `float` | [`DampAngleDeg`](#dampangledeg) `inline` | Wrap-aware angle damping (degrees). Same `FInterpTo` Speed semantics as `FMath::FInterpTo` but operates on the *shortest* angular delta — a transition from `+175°` to `-175°` (visually `+10°`) takes the short way, not the long way. Returns the unwrapped degrees value (re-normalized into `[-180, 180]`) so caching the result keeps the authoring envelope. `Speed <= 0` or `DeltaTime <= 0` ⇒ return Target (instant snap), matching `FInterpTo`. |
| `float` | [`SolvePerceptualUnionBoxFOV`](#solveperceptualunionboxfov) `inline` | Solves FOV from per-target bounds via the Weight-scaled Perceptual Union Box algorithm. See spec §4.5 for the algorithm; ported from BlackEyeCameras' ULookAtComponent::GetTargetGroupViewportBoundingBox. |
| `float` | [`SolveLens`](#solvelens) `inline` | Computes FOV based on the Shot's Lens layer. |
| `float` | [`SolveFocus`](#solvefocus) `inline` | Focus distance based on Shot.Focus.Mode: |
| `FShotSolveResult` | [`SolveShot`](#solveshot) `inline` | Runs the full pipeline. `bValid == false` when Placement or Aim fails to resolve — caller preserves upstream pose for the frame (spec §5.3). |

---

#### ResolvePlacementBasis { #resolveplacementbasis }

`inline`

```cpp
inline FQuat ResolvePlacementBasis(const FComposableCameraShot & Shot)
```

Resolves the basis quat for the Placement layer's `LocalCameraDirection`.

* World basis → FQuat::Identity (always valid).

* InheritFromActor basis → Targets[BasisActorIndex]'s basis quat, via [FComposableCameraTargetInfo::ResolveBasisQuat](FComposableCameraTargetInfo.md#resolvebasisquat) (mesh-component quat for ACharacter-style targets when the per-target flag is set, actor quat otherwise; PIE-remap aware). Falls back to identity (with warning) when the index is out of range or the actor is unresolvable. Both warning paths dedupe so the log line fires at most once per (Shot pointer, distinct unresolvable Actor soft-path) — designers are told once when their basis assignment isn't taking effect, then the hot path stays quiet.

---

#### SolveAnchorOrbitPosition { #solveanchororbitposition }

`inline`

```cpp
inline FVector SolveAnchorOrbitPosition(const FVector & AnchorPos, const FQuat & BasisQuat, float Distance, const FVector2D & LocalCameraDirection, const FVector2D & ScreenPosition, float TanHalfHOR, float AspectRatio)
```

Camera position for AnchorOrbit mode:

CamPos = AnchorPos + Distance · BasisQuat · UnitDir(Yaw, Pitch)

* lateral shift to realize ScreenPosition

The lateral shift is along the camera's right / up axes, computed from the *tentative* look-at-anchor forward (which equals `-BasisQuat · UnitDir(Yaw, Pitch)`). This is independent of the Aim layer's eventual rotation: Position is fixed by Placement alone.

Distance is Euclidean — measured along the unit direction vector. Equals camera-frame depth in the typical case (AimAnchor == PlacementAnchor → camera looks at PlacementAnchor → depth = Euclidean distance).

**Parameters**

* `TanHalfHOR` tan(FOV_h / 2) for the lateral shift's screen-to-world conversion. Pass the projection FOV (manual or previous-frame). 

* `AspectRatio` viewport aspect (width / height).

---

#### ClampAuthoredScreenPosition { #clampauthoredscreenposition }

`inline`

```cpp
inline bool ClampAuthoredScreenPosition(FVector2D & InOutScreenPos)
```

Clamp an authored screen position to `[-0.49, +0.49]²`. Returns true iff a clamp actually fired (caller logs a warning so the designer sees that their input was modified).

---

#### PreRotateScreenForRoll { #prerotatescreenforroll }

`inline`

```cpp
inline FVector2D PreRotateScreenForRoll(const FVector2D & Authored, float CosRoll, float SinRoll, float AspectRatio)
```

Pre-rotates an authored screen position by -Roll so that, after the final pose has Roll composed onto its rotation, the world point still projects to the *authored* (un-pre-rotated) screen coords.

Math (derivation in spec §4.8): under camera Roll R about forward, a fixed world point's projected coords transform anisotropically as Sx_R = Sx_0 · cosR  -  (Sy_0 / AR) · sinR
Sy_R = AR · Sx_0 · sinR  +  Sy_0 · cosR
 To preserve post-Roll proj == authored ScreenPos, we solve the inverse: Sx_0 = Sx · cosR  +  (Sy / AR) · sinR
Sy_0 = -AR · Sx · sinR  +  Sy · cosR
 Defined here (above the first caller, `SolveLookAtAnchorRotation`) so the order of inline definitions in this header matches the order of use — C++ requires inline functions to be defined before use within the same translation unit.

---

#### ApplyScreenZones { #applyscreenzones }

`inline`

```cpp
inline FVector2D ApplyScreenZones(const FVector2D & CurrentScreen, const FVector2D & AuthoredScreenPos, const FShotScreenZones & Zones, float DeltaTime)
```

Compute the effective screen-space target an anchor should be solved toward this frame, given:

* `CurrentScreen` — the anchor's current projected screen coordinate (read off the prior pose).

* `AuthoredScreenPos` — the designer's authored target screen position (zone-rect center).

* `Zones` — the dead/soft padding + damping config.

* `DeltaTime` — frame delta seconds (for `FInterpTo`).

Algorithm (Cinemachine-style, asymmetric per-side):

err = CurrentScreen - AuthoredScreenPos

// Per-axis dead-zone subtraction. The dead zone is the rect // [-DeadLeft, +DeadRight] × [-DeadBottom, +DeadTop] around SP. // err > +Right → eff = err - Right (anchor right of dead, pull left) // err < -Left → eff = err + Left (anchor left of dead, pull right) // else → eff = 0 (anchor inside dead, hold) eff_after = FInterpTo(eff, 0, dt, Speed) // damping step = eff - eff_after new_err = err - step

// Soft-zone hard limit: clamp into the soft padding rect, no // damping on the clamp (Cinemachine's "HardLimits" semantics). new_err.x in [-SoftLeft, +SoftRight] new_err.y in [-SoftBottom, +SoftTop]

target = AuthoredScreenPos + new_err

Anchor inside the dead rect → eff = 0 → step = 0 → new_err = err → target = CurrentScreen → solver reproduces the prior pose. Damping Speed = 0 collapses eff_after to 0, i.e. step = eff, so the anchor snaps to the nearest dead-zone edge in one frame.

Soft padding is defensively `>=` dead padding per side; the drag handler enforces this on author, but the solver also clamps so an inverted authoring (Soft < Dead on a side) still yields sensible output rather than a degenerate clamp band.

---

#### ResolveEffectiveScreenTarget { #resolveeffectivescreentarget }

`inline`

```cpp
inline FVector2D ResolveEffectiveScreenTarget(const FComposableCameraAnchorSpec & Anchor, TConstArrayView< FComposableCameraShotTarget > Targets, const FVector2D & AuthoredScreenPos, const FShotScreenZones & Zones, const FShotPriorPose & PriorPose, float TanHalfHOR, float AspectRatio, float DeltaTime)
```

Resolve the effective screen-space target for a single anchor given a prior camera pose. Convenience wrapper that handles the "anchor unresolvable" failure path (returns the authored screen position so the V1 hard-constraint solver still has something sensible to chew on — caller will likely fail on anchor resolve downstream anyway).

Returns the authored ScreenPosition unchanged when:

* Zones are disabled, OR

* The anchor cannot resolve to a world point (zone math needs the projected `CurrentScreen`, which needs a world point), OR

* The prior pose's rotation is degenerate (Forward dot AnchorDir near zero in `ProjectWorldPointToScreen`).

The projection uses the same `TanHalfHOR` / `AspectRatio` the rest of the SolveShot pipeline uses for the current frame — so the effective screen target is consistent with the projection the V1 solver will subsequently invert.

---

#### SolveAnchorAtScreenPos { #solveanchoratscreenpos }

`inline`

```cpp
inline bool SolveAnchorAtScreenPos(const FVector & PlacementAnchorPos, FVector2D ScreenPos, float Distance, float TanHalfHOR, float AspectRatio, const FRotator & AssumedRot, FVector & OutCamPos)
```

Closed-form Position pass for `[EShotPlacementMode::AnchorAtScreen](#ComposableCameraShot_8h_1ad8bb9ef9d1aefe5e2b42410fc9908537a8da460d070406aab8e2caa882f9cbf2c)`.

Computes a camera position that places `PlacementAnchor` at depth `Distance` and screen `ScreenPos` IN THE CAM FRAME OF `AssumedRot`. Algebraic, no iteration: cam_anchor = (D, sx · 2·TanH · D, sy · 2·TanV · D)   // cam frame
CamPos     = PlacementAnchor - AssumedRot · cam_anchor
`AssumedRot` is sourced from:

* Aim NoOp: identity + Shot.Roll (Roll-only).

* Aim LookAtAnchor + prior: prior frame’s camera rotation. Decoupling-drift is then per-frame O(rotation delta).

* Aim LookAtAnchor + first-frame seed: rotation built from the (PlacementAnchor → AimAnchor) world direction + Shot.Roll. Matches the Aim pass’s eventual look-at-AimAnchor rotation closely enough that one frame of decoupling drift washes out inside the IIR damping window.

`ScreenPos` is consumed as-is (no `-Roll` pre-rotation): when `AssumedRot` already includes Shot.Roll, the cam-frame right/up axes are themselves rolled, so `(sx · 2·TanH · D, sy · 2·TanV · D)` lands the anchor at the authored ScreenPosition under the rolled view. Contrast with `SolveLookAtAnchorRotation` which DOES pre-rotate — it solves for the rotation, so it cannot pre-roll it.

Returns false (OutCamPos unchanged) iff `Distance < 1cm`. Authored `ScreenPos` outside `[-0.49, +0.49]²` is silently clamped to keep the cam-frame target inside the frustum-safe envelope.

---

#### SolvePlacement { #solveplacement }

`inline`

```cpp
inline bool SolvePlacement(const FComposableCameraShot & Shot, float EffectiveDistance, float TanHalfHOR, float AspectRatio, FVector & OutCamPos)
```

Computes camera Position based on the Shot's Placement layer. Returns false (CamPos unchanged) when an essential anchor can't resolve — caller handles the no-pose fallback.

`EffectiveDistance` overrides `Shot.Placement.Distance` for the `AnchorOrbit` mode — `SolveShot` injects a damped distance here (V2.2 IIR via `Shot.Placement.DistanceSpeed`); decoupled callers pass `Shot.Placement.Distance` directly to keep V1 hard behavior. `FixedWorldPosition` ignores it; the solver expects callers to still pass a sensible value for symmetry.

---

#### SolveLookAtAnchorRotation { #solvelookatanchorrotation }

`inline`

```cpp
inline FRotator SolveLookAtAnchorRotation(const FVector & CamPos, const FVector & AimAnchorPos, const FVector2D & AimScreenPosition, float RollRad, float TanHalfHOR, float AspectRatio)
```

Solves camera Rotation for LookAtAnchor mode: closed-form rotation that lands AimAnchor at Aim.ScreenPosition. Uses `SolveCameraRotationForScreenTarget` from `[ComposableCameraMath.h](#composablecameramathh)`. Roll is pre-compensated so the screen constraint holds after the caller composes Roll onto the result.

Returns FRotator with Pitch / Yaw set, Roll left at zero — caller sets Roll = Shot.Roll afterwards.

---

#### SolveAim { #solveaim }

`inline`

```cpp
inline bool SolveAim(const FComposableCameraShot & Shot, const FVector & CamPos, const FVector2D & EffectiveAimScreenPos, float EffectiveRollDeg, float TanHalfHOR, float AspectRatio, FRotator & OutRot)
```

Computes camera Rotation based on the Shot's Aim layer + Roll. Returns false (OutRot unchanged) when AimAnchor can't resolve.

`EffectiveAimScreenPos` overrides `Shot.Aim.ScreenPosition` for `LookAtAnchor` mode — this is how `SolveShot` injects a zone-derived effective screen target (Cinemachine-style damped framing). Pass `Shot.Aim.ScreenPosition` directly to keep V1 hard-constraint behavior. NoOp ignores this argument (it has no screen constraint).

`EffectiveRollDeg` is the V2.2 damped Roll (computed in `SolveShot` from `Shot.Roll`, `PriorPose->LastRoll`, and `Shot.RollSpeed`). Pass `Shot.Roll` directly to keep V1 hard-constraint behavior.

---

#### DampAngleDeg { #dampangledeg }

`inline`

```cpp
inline float DampAngleDeg(float LastDeg, float TargetDeg, float DeltaTime, float Speed)
```

Wrap-aware angle damping (degrees). Same `FInterpTo` Speed semantics as `FMath::FInterpTo` but operates on the *shortest* angular delta — a transition from `+175°` to `-175°` (visually `+10°`) takes the short way, not the long way. Returns the unwrapped degrees value (re-normalized into `[-180, 180]`) so caching the result keeps the authoring envelope. `Speed <= 0` or `DeltaTime <= 0` ⇒ return Target (instant snap), matching `FInterpTo`.

---

#### SolvePerceptualUnionBoxFOV { #solveperceptualunionboxfov }

`inline`

```cpp
inline float SolvePerceptualUnionBoxFOV(const FVector & CameraPos, const FRotator & CameraRot, TConstArrayView< FComposableCameraShotTarget > Targets, float DesiredViewportFillRatio, float CurrentFOVDeg, float AspectRatio, const FFloatInterval & FOVClamp)
```

Solves FOV from per-target bounds via the Weight-scaled Perceptual Union Box algorithm. See spec §4.5 for the algorithm; ported from BlackEyeCameras' ULookAtComponent::GetTargetGroupViewportBoundingBox.

Edge cases:

* No contributing bounds → keep CurrentFOV.

* Any vertex of a target's BB behind camera → skip that target.

**Parameters**

* `CurrentFOV` Used as projection FOV (consistent per-frame projection) AND as the basis for the closed-form atan inversion.

---

#### SolveLens { #solvelens }

`inline`

```cpp
inline float SolveLens(const FComposableCameraShot & Shot, const FVector & CamPos, const FRotator & CamRot, const FShotSolveContext & Context)
```

Computes FOV based on the Shot's Lens layer.

---

#### SolveFocus { #solvefocus }

`inline`

```cpp
inline float SolveFocus(const FComposableCameraShot & Shot, const FVector & CamPos, const FRotator & CamRot)
```

Focus distance based on Shot.Focus.Mode:

* Manual → Focus.ManualDistance.

* FollowPlacementAnchor → camera-to-PlacementAnchor depth.

* FollowAimAnchor → camera-to-AimAnchor depth.

* FollowCustomAnchor → camera-to-FocusAnchor depth.

Depth is on-axis (`(WorldPoint - CameraPos) · CameraForward`), not Euclidean — same convention as `FocusPullNode` and what `ApplyPhysicalCameraSettings` consumes downstream. Falls back to `Manual.ManualDistance` when an anchor mode can't resolve its world point.

---

#### SolveShot { #solveshot }

`inline`

```cpp
inline FShotSolveResult SolveShot(const FComposableCameraShot & Shot, const FShotSolveContext & Context, const FShotPriorPose * PriorPose, float DeltaTime)
```

Runs the full pipeline. `bValid == false` when Placement or Aim fails to resolve — caller preserves upstream pose for the frame (spec §5.3).

`PriorPose` + `DeltaTime` enable Cinemachine-style screen-space framing zones. When non-null AND `Aim.AimZones.bEnabled` / `Placement.PlacementZones.bEnabled` is set, the solver projects the corresponding anchor through `*PriorPose` and substitutes a zone-derived effective screen target for the V1 hard ScreenPosition read. When null OR zones disabled, V1 hard-constraint behavior is preserved exactly — every existing call site continues to work with default arguments.

`PlacementZones` only meaningfully fires in `AnchorAtScreen` placement (the only mode that authors a Placement.ScreenPosition); `AnchorOrbit` and `FixedWorldPosition` ignore the placement zone configuration regardless of `bEnabled`.

### Variables

| Return | Name | Description |
|--------|------|-------------|
| `constexpr float` | [`ShotSolverScreenClampLimit`](#shotsolverscreenclamplimit)  | Soft-clamp limit for authored screen positions in the joint-solve paths. The screen-coord convention is `[-0.5, +0.5]²` (= edge of frustum at the projection FOV). Authoring values *at* the edge make the iterative solver's `SolveCameraRotationForScreenTarget` saturate its `\|T\| ≤ 1` clamp, which is correct math but loses convergence margin and tends to produce contorted poses. We clamp authored inputs to a slightly inset envelope (~ 98% of frustum width / height) before they enter the iteration so the solver always has headroom. |

---

#### ShotSolverScreenClampLimit { #shotsolverscreenclamplimit }

```cpp
constexpr float ShotSolverScreenClampLimit = 0.49f
```

Soft-clamp limit for authored screen positions in the joint-solve paths. The screen-coord convention is `[-0.5, +0.5]²` (= edge of frustum at the projection FOV). Authoring values *at* the edge make the iterative solver's `SolveCameraRotationForScreenTarget` saturate its `|T| ≤ 1` clamp, which is correct math but loses convergence margin and tends to produce contorted poses. We clamp authored inputs to a slightly inset envelope (~ 98% of frustum width / height) before they enter the iteration so the solver always has headroom.

Designers authoring values outside this envelope see a one-shot warning per solve; the clamp is silent at the iteration's interior (pre-rotation by -Roll can push pre-rotated values outside the envelope, which is fine — that's an internal value, not user input).
