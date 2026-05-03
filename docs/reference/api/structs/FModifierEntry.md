
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
| [`FShotSolveContext`](FShotSolveContext.md#fshotsolvecontext) | Per-frame inputs the solver needs from the runtime — viewport state + the previous frame's FOV (used as the projection FOV when the Shot is in SolvedFromBoundsFit mode). |
| [`FShotSolveResult`](FShotSolveResult.md#fshotsolveresult) | Solver output. `bValid == false` when an essential anchor cannot be resolved (placement / aim) — caller should preserve upstream pose for the frame. |

### Functions

| Return | Name | Description |
|--------|------|-------------|
| `FQuat` | [`ResolvePlacementBasis`](#resolveplacementbasis) `inline` | Resolves the basis quat for the Placement layer's `LocalCameraDirection`. |
| `FVector` | [`SolveAnchorOrbitPosition`](#solveanchororbitposition) `inline` | Camera position for AnchorOrbit mode: |
| `bool` | [`ClampAuthoredScreenPosition`](#clampauthoredscreenposition) `inline` | Clamp an authored screen position to `[-0.49, +0.49]²`. Returns true iff a clamp actually fired (caller logs a warning so the designer sees that their input was modified). |
| `FVector2D` | [`PreRotateScreenForRoll`](#prerotatescreenforroll) `inline` | Pre-rotates an authored screen position by -Roll so that, after the final pose has Roll composed onto its rotation, the world point still projects to the *authored* (un-pre-rotated) screen coords. |
| `bool` | [`SolveAnchorAtScreen`](#solveanchoratscreen) `inline` | Joint Position + Rotation solve for `[EShotPlacementMode::AnchorAtScreen](#ComposableCameraShot_8h_1ad8bb9ef9d1aefe5e2b42410fc9908537a8da460d070406aab8e2caa882f9cbf2c)`. |
| `bool` | [`SolveAnchorAtScreenIdentityRot`](#solveanchoratscreenidentityrot) `inline` | Direct algebraic solve for `AnchorAtScreen` + Aim NoOp combination. |
| `bool` | [`SolvePlacement`](#solveplacement) `inline` | Computes camera Position based on the Shot's Placement layer. Returns false (CamPos unchanged) when an essential anchor can't resolve — caller handles the no-pose fallback. |
| `FRotator` | [`SolveLookAtAnchorRotation`](#solvelookatanchorrotation) `inline` | Solves camera Rotation for LookAtAnchor mode: closed-form rotation that lands AimAnchor at Aim.ScreenPosition. Uses `SolveCameraRotationForScreenTarget` from `[ComposableCameraMath.h](#composablecameramathh)`. Roll is pre-compensated so the screen constraint holds after the caller composes Roll onto the result. |
| `bool` | [`SolveAim`](#solveaim) `inline` | Computes camera Rotation based on the Shot's Aim layer + Roll. Returns false (OutRot unchanged) when AimAnchor can't resolve. |
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
 Defined here (above the first caller, `SolveAnchorAtScreen`) so the order of inline definitions in this header matches the order of use — C++ requires inline functions to be defined before use within the same translation unit.

---

#### SolveAnchorAtScreen { #solveanchoratscreen }

`inline`

```cpp
inline bool SolveAnchorAtScreen(const FVector & AimAnchorPos, const FVector & PlacementAnchorPos, FVector2D AimScreenPos, FVector2D PlacementScreenPos, float Distance, float TanHalfHOR, float AspectRatio, float RollDeg, FVector & OutCamPos, FRotator & OutCamRot)
```

Joint Position + Rotation solve for `[EShotPlacementMode::AnchorAtScreen](#ComposableCameraShot_8h_1ad8bb9ef9d1aefe5e2b42410fc9908537a8da460d070406aab8e2caa882f9cbf2c)`.

In this mode Placement borrows its forward axis from Aim — camera looks at AimAnchor with `Aim.ScreenPosition` constraint, AND PlacementAnchor must be at depth `Distance` and screen `Placement.ScreenPosition` in cam frame. That's 5 constraints (AimAnchor screen 2 + PlacementAnchor screen 2 + PlacementAnchor depth 1) on 5 unknowns (CamPos 3 + Pitch 1 + Yaw 1).

**Iterative solve** (Picard fixed-point with damping — typically converges in 3-6 iterations). Closed-form is hard because the camera's right / up axes (which determine which world direction `Placement.ScreenPosition` shifts the camera) depend on the forward direction, which depends on CamPos itself. Iterating breaks the chicken-and-egg cleanly:

1. Pre-flight (return false on hard failures, clamp soft ones):

1. `Distance < 1` → return false (caller pre-clamps via `SafeDistance`; defensive secondary clamp).

1. `dist_AP < ε` → return false (AimAnchor ≡ PlacementAnchor; the joint solve has no canonical answer — designer should switch to `AnchorOrbit` for single-anchor framing).

1. Authored screen positions outside `[-0.49, +0.49]²` are clamped (silent for valid envelope, warning when clamp fires).

1. Initial guess: place camera at `PlacementAnchor` displaced `Distance` away along the (PlacementAnchor → AimAnchor) direction (rough OTS starting point).

1. Loop (Picard with relaxation factor `α = 0.7`): a. Compute camera rotation from current CamPos via `SolveCameraRotationForScreenTarget(AimAnchor - CamPos, AimScreenPos)` — gives (Pitch, Yaw) putting AimAnchor at the authored screen position. b. Candidate CamPos = `PlacementAnchor - R · (D, ly_p, lz_p)`. c. Damped update: `CamPos ← (1-α)·CamPos + α·Candidate`. Damping (0 < α < 1) suppresses oscillation under off-center / short-distance geometries where the un-damped iteration can ping-pong instead of converging. d. Convergence on un-damped residual `||Candidate - CamPos||² < (0.01 cm)²`. Damping doesn't change the fixed point, so convergence on the raw step is the right signal.

1. Non-convergence → return false (caller preserves upstream pose for the frame). The previous behavior of "warn + return last
     estimate" silently produced wrong cameras; failing loud lets the framing-node fallback take over and the designer's HUD shows the previous-frame pose unchanged.

1. Compose `Shot.Roll` onto output rotation. Authored screen positions pre-rotated by `-Roll` (anisotropic AR transform) before the iteration so they end up at the original values under the rolled rotation — same trick as `LookAtAnchor`.

Note: `Aim.Mode == NoOp` is handled by the separate `SolveAnchorAtScreenIdentityRot` (closed-form algebraic, no Picard).

---

#### SolveAnchorAtScreenIdentityRot { #solveanchoratscreenidentityrot }

`inline`

```cpp
inline bool SolveAnchorAtScreenIdentityRot(const FVector & PlacementAnchorPos, FVector2D ScreenPos, float Distance, float TanHalfHOR, float AspectRatio, float RollDeg, FVector & OutCamPos, FRotator & OutCamRot)
```

Direct algebraic solve for `AnchorAtScreen` + Aim NoOp combination.

When Aim is NoOp the rotation is fixed at `(Pitch=0, Yaw=0, Roll=Shot.Roll)` — there's no Aim screen constraint, so the joint quadratic in `SolveAnchorAtScreen` doesn't apply. With rotation known the camera position is closed-form algebraic: cam_anchor = (D, sx · 2·TanH · D, sy · 2·TanV · D)   // cam frame
CamPos     = PlacementAnchor - R(Roll) · cam_anchor
 which makes PlacementAnchor project to `ScreenPosition` at depth `D` under the Roll-only rotation.

---

#### SolvePlacement { #solveplacement }

`inline`

```cpp
inline bool SolvePlacement(const FComposableCameraShot & Shot, float TanHalfHOR, float AspectRatio, FVector & OutCamPos)
```

Computes camera Position based on the Shot's Placement layer. Returns false (CamPos unchanged) when an essential anchor can't resolve — caller handles the no-pose fallback.

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
inline bool SolveAim(const FComposableCameraShot & Shot, const FVector & CamPos, float TanHalfHOR, float AspectRatio, FRotator & OutRot)
```

Computes camera Rotation based on the Shot's Aim layer + Roll. Returns false (OutRot unchanged) when AimAnchor can't resolve.

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
inline FShotSolveResult SolveShot(const FComposableCameraShot & Shot, const FShotSolveContext & Context)
```

Runs the full pipeline. `bValid == false` when Placement or Aim fails to resolve — caller preserves upstream pose for the frame (spec §5.3).

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
