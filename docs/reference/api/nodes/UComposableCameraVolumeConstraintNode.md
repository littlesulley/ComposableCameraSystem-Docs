
# UComposableCameraVolumeConstraintNode { #ucomposablecameravolumeconstraintnode }

```cpp
#include <ComposableCameraVolumeConstraintNode.h>
```

> **Inherits:** [`UComposableCameraCameraNodeBase`](../uobjects-other/UComposableCameraCameraNodeBase.md#ucomposablecameracameranodebase)

Constrains the camera to stay inside a single world-space volume. When the upstream camera position is outside the volume, it is projected to the nearest point on the volume's boundary. When it is inside, the node is a no-op and passes the pose through untouched.

Single volume only (MVP) — multiple-volume setups with priority / blend radius (PostProcessVolume-style) are not supported; swap cameras via transitions to change the active volume. Only the "keep inside" semantic is implemented; "keep outside" (forbidden region) is not.

The clamp is a hard projection by default. An optional ClampInterpolator adds per-axis temporal smoothing so three discontinuity modes stop reading as visible snaps:

1. **Release snap** — upstream crosses from outside to inside in one frame. Without smoothing the output jumps from the boundary point back to the freely-moving upstream position.

1. **Corner face switch** — upstream orbits past a corner where the nearest-point face flips (e.g. +X face → corner → +Y face). Position is still Lipschitz continuous but the tangent direction can change abruptly, reading as a crease.

1. **Teleport / warp** — any scripted camera jump across the boundary.

When ClampInterpolator is null, the node is fully stateless and the pose is deterministic given the upstream input. When it is set, per-axis smoothing introduces controllable lag.

Position formula each tick: let Volume = Resolve(VolumeSource)
if IsInside(OutPose.Position, Volume):
    OutPose.Position unchanged
else:
    OutPose.Position = NearestPointInsideVolume(OutPose.Position, Volume)
 For a Box volume (OBB), "nearest point" is computed in the volume's local space by per-axis clamping against the half-extents, then transformed back to world. For a Sphere, it is `Center + (Pos - Center).SafeNormal * Radius`.

Chain placement: runs on the camera's position, so put it after `CameraOffsetNode` / `LookAtNode` / any position-writing node that produces the "desired" position, and before `CollisionPushNode` so the collision push operates on the already-clamped input.

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `EComposableCameraVolumeSource` | [`VolumeSource`](#volumesource)  | Where the volume geometry comes from. |
| `TObjectPtr< AActor >` | [`VolumeActor`](#volumeactor)  | Actor with a `UShapeComponent` (UBoxComponent / USphereComponent) whose transform and scaled extents define the volume. The first shape component found via `GetComponents<UShapeComponent>` wins — multiple shape components on one actor are not supported; use Inline mode or a dedicated actor with a single shape when precise control is needed. |
| `EComposableCameraVolumeShape` | [`Shape`](#shape)  | Inline-mode shape selector. Ignored in FromActor mode (the shape comes from the component's class). |
| `FVector` | [`VolumeCenter`](#volumecenter)  | Inline-mode volume center in world space. |
| `FRotator` | [`VolumeRotation`](#volumerotation)  | Inline-mode volume rotation (world space). Only affects the Box shape — an OBB is the difference from an AABB. Ignored for Sphere. |
| `FVector` | [`BoxExtents`](#boxextents)  | Inline-mode box half-extents in the volume's local space (pre-rotation). |
| `float` | [`SphereRadius`](#sphereradius)  | Inline-mode sphere radius in world units. |
| `TObjectPtr< UComposableCameraInterpolatorBase >` | [`ClampInterpolator`](#clampinterpolator)  | Optional interpolator applied per axis to the output position. When set, the node keeps a private `LastSmoothedPosition` and each tick smooths it toward the (clamp or pass-through) target using THREE independent 1D interpolator instances (one per world-space axis), preserving the filter's dynamics per axis. When null, the node is stateless and the output is a hard projection / pass-through. |

---

#### VolumeSource { #volumesource }

```cpp
EComposableCameraVolumeSource VolumeSource {  }
```

Where the volume geometry comes from.

---

#### VolumeActor { #volumeactor }

```cpp
TObjectPtr< AActor > VolumeActor { nullptr }
```

Actor with a `UShapeComponent` (UBoxComponent / USphereComponent) whose transform and scaled extents define the volume. The first shape component found via `GetComponents<UShapeComponent>` wins — multiple shape components on one actor are not supported; use Inline mode or a dedicated actor with a single shape when precise control is needed.

---

#### Shape { #shape }

```cpp
EComposableCameraVolumeShape Shape {  }
```

Inline-mode shape selector. Ignored in FromActor mode (the shape comes from the component's class).

---

#### VolumeCenter { #volumecenter }

```cpp
FVector VolumeCenter { FVector::ZeroVector }
```

Inline-mode volume center in world space.

---

#### VolumeRotation { #volumerotation }

```cpp
FRotator VolumeRotation { FRotator::ZeroRotator }
```

Inline-mode volume rotation (world space). Only affects the Box shape — an OBB is the difference from an AABB. Ignored for Sphere.

---

#### BoxExtents { #boxextents }

```cpp
FVector BoxExtents { FVector(500.f, 500.f, 300.f) }
```

Inline-mode box half-extents in the volume's local space (pre-rotation).

---

#### SphereRadius { #sphereradius }

```cpp
float SphereRadius { 500.f }
```

Inline-mode sphere radius in world units.

---

#### ClampInterpolator { #clampinterpolator }

```cpp
TObjectPtr< UComposableCameraInterpolatorBase > ClampInterpolator
```

Optional interpolator applied per axis to the output position. When set, the node keeps a private `LastSmoothedPosition` and each tick smooths it toward the (clamp or pass-through) target using THREE independent 1D interpolator instances (one per world-space axis), preserving the filter's dynamics per axis. When null, the node is stateless and the output is a hard projection / pass-through.

Picks the same UInterpolatorBase instanced subobject pattern that CollisionPush / PivotDamping use — users choose between SpringDamper, IIR, SimpleSpring, etc.

### Public Methods

| Return | Name | Description |
|--------|------|-------------|
| `void` | [`OnInitialize_Implementation`](#oninitialize_implementation-14) `virtual` |  |
| `void` | [`OnTickNode_Implementation`](#onticknode_implementation-22) `virtual` |  |
| `void` | [`GetPinDeclarations_Implementation`](#getpindeclarations_implementation-20) `virtual` `const` |  |
| `void` | [`DrawNodeDebug`](#drawnodedebug-11) `virtual` `const` | Called each frame when the `CCS.Debug.Viewport` CVar is enabled, for every node on the currently running camera. Override to draw world-space debug gizmos via `DrawDebugHelpers` (DrawDebugSphere, DrawDebugLine, etc.) that visualise this node's runtime state — e.g. a pivot sphere for PivotOffsetNode, a look-at line for LookAtNode, the collision trace for CollisionPushNode, a sampled spline path for SplineNode. |

---

#### OnInitialize_Implementation { #oninitialize_implementation-14 }

`virtual`

```cpp
virtual void OnInitialize_Implementation()
```

---

#### OnTickNode_Implementation { #onticknode_implementation-22 }

`virtual`

```cpp
virtual void OnTickNode_Implementation(float DeltaTime, const FComposableCameraPose & CurrentCameraPose, FComposableCameraPose & OutCameraPose)
```

---

#### GetPinDeclarations_Implementation { #getpindeclarations_implementation-20 }

`virtual` `const`

```cpp
virtual void GetPinDeclarations_Implementation(TArray< FComposableCameraNodePinDeclaration > & OutPins) const
```

---

#### DrawNodeDebug { #drawnodedebug-11 }

`virtual` `const`

```cpp
virtual void DrawNodeDebug(UWorld * World, bool bViewerIsOutsideCamera) const
```

Called each frame when the `CCS.Debug.Viewport` CVar is enabled, for every node on the currently running camera. Override to draw world-space debug gizmos via `DrawDebugHelpers` (DrawDebugSphere, DrawDebugLine, etc.) that visualise this node's runtime state — e.g. a pivot sphere for PivotOffsetNode, a look-at line for LookAtNode, the collision trace for CollisionPushNode, a sampled spline path for SplineNode.

Access the owning camera via `OwningCamera` and current-frame pin values via the usual `GetInputPinValue<T>()` / member-read path — this hook fires AFTER TickNode, so pin-backed UPROPERTYs still hold the resolved values from the most recent evaluation.

`bViewerIsOutsideCamera` mirrors the ticker's frustum-draw flag: true when the viewer is observing the camera from outside (F8 eject, SIE, or `CCS.Debug.Viewport.AlwaysShow`), false when the player is looking through the camera. Most gizmos (pivot spheres at distant characters, lines to look-at targets, spline polylines far in the world) can ignore this and draw unconditionally. Gizmos that sit AT the camera's own position (e.g. `CollisionPushNode`'s self-collision sphere) should gate on this bool so they don't hermetically seal the player inside the wireframe during live gameplay.

Default implementation does nothing. Compiled out in shipping builds.

### Private Attributes

| Return | Name | Description |
|--------|------|-------------|
| `TUniquePtr< TCameraInterpolator< TValueTypeWrapper< double > > >` | [`ClampInterpolatorX_T`](#clampinterpolatorx_t)  | Per-axis 1D interpolator instances built from ClampInterpolator in OnInitialize. Three independent filter states let the X/Y/Z smoothing dynamics stay decoupled — a spring overshoot on X shouldn't bleed into Y / Z. |
| `TUniquePtr< TCameraInterpolator< TValueTypeWrapper< double > > >` | [`ClampInterpolatorY_T`](#clampinterpolatory_t)  |  |
| `TUniquePtr< TCameraInterpolator< TValueTypeWrapper< double > > >` | [`ClampInterpolatorZ_T`](#clampinterpolatorz_t)  |  |
| `FVector` | [`LastSmoothedPosition`](#lastsmoothedposition)  | Persistent smoothed output. Seeded on the first tick from the upstream position so the first frame isn't a snap from origin. |
| `bool` | [`bHasSeededSmoothing`](#bhasseededsmoothing-1)  | Cleared in OnInitialize; set to true the first time OnTickNode runs so the seed happens against the live upstream pose. Re-activation resets this via OnInitialize. |
| `FResolvedVolume` | [`DebugResolvedVolume`](#debugresolvedvolume)  |  |
| `bool` | [`DebugHasResolvedVolume`](#debughasresolvedvolume)  |  |
| `bool` | [`DebugIsClamping`](#debugisclamping)  |  |
| `FVector` | [`DebugClampedPosition`](#debugclampedposition)  |  |
| `FVector` | [`DebugUpstreamPosition`](#debugupstreamposition)  |  |

---

#### ClampInterpolatorX_T { #clampinterpolatorx_t }

```cpp
TUniquePtr< TCameraInterpolator< TValueTypeWrapper< double > > > ClampInterpolatorX_T
```

Per-axis 1D interpolator instances built from ClampInterpolator in OnInitialize. Three independent filter states let the X/Y/Z smoothing dynamics stay decoupled — a spring overshoot on X shouldn't bleed into Y / Z.

---

#### ClampInterpolatorY_T { #clampinterpolatory_t }

```cpp
TUniquePtr< TCameraInterpolator< TValueTypeWrapper< double > > > ClampInterpolatorY_T
```

---

#### ClampInterpolatorZ_T { #clampinterpolatorz_t }

```cpp
TUniquePtr< TCameraInterpolator< TValueTypeWrapper< double > > > ClampInterpolatorZ_T
```

---

#### LastSmoothedPosition { #lastsmoothedposition }

```cpp
FVector LastSmoothedPosition { FVector::ZeroVector }
```

Persistent smoothed output. Seeded on the first tick from the upstream position so the first frame isn't a snap from origin.

---

#### bHasSeededSmoothing { #bhasseededsmoothing-1 }

```cpp
bool bHasSeededSmoothing { false }
```

Cleared in OnInitialize; set to true the first time OnTickNode runs so the seed happens against the live upstream pose. Re-activation resets this via OnInitialize.

---

#### DebugResolvedVolume { #debugresolvedvolume }

```cpp
FResolvedVolume DebugResolvedVolume
```

---

#### DebugHasResolvedVolume { #debughasresolvedvolume }

```cpp
bool DebugHasResolvedVolume { false }
```

---

#### DebugIsClamping { #debugisclamping }

```cpp
bool DebugIsClamping { false }
```

---

#### DebugClampedPosition { #debugclampedposition }

```cpp
FVector DebugClampedPosition { FVector::ZeroVector }
```

---

#### DebugUpstreamPosition { #debugupstreamposition }

```cpp
FVector DebugUpstreamPosition { FVector::ZeroVector }
```

### Private Methods

| Return | Name | Description |
|--------|------|-------------|
| `bool` | [`ResolveVolume`](#resolvevolume) `const` | Fill OutVolume from the current VolumeSource / VolumeActor / Inline properties. Returns false when the source can't provide a usable volume (e.g. FromActor with null actor, or no supported shape component). Logs the specific reason. |

---

#### ResolveVolume { #resolvevolume }

`const`

```cpp
bool ResolveVolume(FResolvedVolume & OutVolume) const
```

Fill OutVolume from the current VolumeSource / VolumeActor / Inline properties. Returns false when the source can't provide a usable volume (e.g. FromActor with null actor, or no supported shape component). Logs the specific reason.

### Private Static Methods

| Return | Name | Description |
|--------|------|-------------|
| `FVector` | [`NearestPointInVolume`](#nearestpointinvolume) `static` | Return the nearest point inside the volume to WorldPos. `OutIsAlreadyInside` is set to true when WorldPos was already inside (the returned point equals WorldPos in that case). |

---

#### NearestPointInVolume { #nearestpointinvolume }

`static`

```cpp
static FVector NearestPointInVolume(const FResolvedVolume & Volume, const FVector & WorldPos, bool & OutIsAlreadyInside)
```

Return the nearest point inside the volume to WorldPos. `OutIsAlreadyInside` is set to true when WorldPos was already inside (the returned point equals WorldPos in that case).
