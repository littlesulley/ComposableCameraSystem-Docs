
# FComposableCameraViewportDebug { #fcomposablecameraviewportdebug }

```cpp
#include <ComposableCameraViewportDebug.h>
```

Runtime 3D viewport debug draw for the Composable Camera System.

Two-tier gating:

* `CCS.Debug.Viewport 0|1` is the master switch. When 0, nothing draws. When 1, the camera's FRUSTUM is drawn (with the F8 gate below) and each node is given a chance to paint its own per-node gizmo.

* Per-node gizmos are controlled by PER-NODE CVars of the form `CCS.Debug.Viewport.<NodeName>` (e.g. `.PivotOffset`, `.LookAt`, `.CollisionPush`, `.Spline`, `.PivotDamping`). Each defaults to 0 — users opt in per node. These gizmos are visible in BOTH possessed play and F8 eject, because they rarely occlude the viewpoint.

Frustum auto-hide. The frustum is the one exception — drawing it at the near plane while the player is viewing through the camera just occludes the scene. The frustum therefore only fires while `GEditor->bIsSimulatingInEditor` is true (F8 eject / Simulate mode). Non-editor builds always show it when the master CVar is on. `CCS.Debug.Viewport.AlwaysShow 1` forces frustum rendering even while possessing — useful for multi-viewport setups.

Rendering pathway: the draw runs from an `FTSTicker::GetCoreTicker()` delegate, not from `UDebugDrawService`. The ticker fires every frame regardless of which viewport is active, and `DrawDebugCamera` routes through the world's LineBatcher, which is rendered by every viewport that draws that world — so the draw is visible both in the game viewport (standalone / possessed play) and in the editor viewport (during F8 eject). An earlier attempt used `UDebugDrawService::Register("Game", ...)` but that hook does NOT fire from the editor viewport during F8 eject, which was the exact time we most wanted draws to appear.

Adding a new per-node gizmo is a localised ~15-line job:

1. Override `UComposableCameraCameraNodeBase::DrawNodeDebug(UWorld*, bool)` in the concrete node, guarded `#if !UE_BUILD_SHIPPING`. The second parameter is `bViewerIsOutsideCamera` — use it to gate any gizmo that sits AT the camera's own position (see `CollisionPushNode`'s self- collision sphere); most nodes ignore it.

1. Declare a static `TAutoConsoleVariable<int32>` in the node's .cpp under `CCS.Debug.Viewport.<NodeName>`, default 0.

1. Early-out on that CVar at the top of `DrawNodeDebug`.

1. Call `DrawDebug*` via `DrawDebugHelpers.h` with the node's resolved runtime state.

This is distinct from `[FComposableCameraDebugPanel](FComposableCameraDebugPanel.md#fcomposablecameradebugpanel)` (2D HUD overlay, `CCS.Debug.Panel` CVar) — they are independent and can be enabled in any combination.

All cost is guarded `#if !UE_BUILD_SHIPPING` — the ticker's body compiles to nothing in shipping builds.

Lifecycle is module-owned: [FComposableCameraSystemModule::StartupModule](FComposableCameraSystemModule.md#startupmodule) calls [Initialize()](#initialize-2); ShutdownModule calls [Shutdown()](#shutdown-1).

### Public Static Methods

| Return | Name | Description |
|--------|------|-------------|
| `void` | [`Initialize`](#initialize-2) `static` | Register the FTSTicker delegate. Idempotent. |
| `void` | [`Shutdown`](#shutdown-1) `static` | Unregister the FTSTicker delegate. Idempotent. |
| `bool` | [`ShouldShowAllNodeGizmos`](#shouldshowallnodegizmos) `static` | True when `CCS.Debug.Viewport.Nodes.All` is non-zero — every per-node gizmo (both 3D `DrawNodeDebug` and 2D `DrawNodeDebug2D` paths) should show regardless of its own per-node CVar. The two paths share this switch intentionally: each node's 2D / 3D pieces already share one per-node CVar, so batching them into one "All" toggle keeps the mental model consistent. |
| `bool` | [`ShouldShowAllTransitionGizmos`](#shouldshowalltransitiongizmos) `static` | True when `CCS.Debug.Viewport.Transitions.All` is non-zero — every per-transition gizmo draws regardless of its own CVar. Same OR semantics as ShouldShowAllNodeGizmos. |
| `void` | [`DrawSolidDebugSphere`](#drawsoliddebugsphere) `static` | Draw a translucent-wireframe debug sphere — the canonical sphere gizmo used by every CCS node / transition debug override. |

---

#### Initialize { #initialize-2 }

`static`

```cpp
static void Initialize()
```

Register the FTSTicker delegate. Idempotent.

---

#### Shutdown { #shutdown-1 }

`static`

```cpp
static void Shutdown()
```

Unregister the FTSTicker delegate. Idempotent.

---

#### ShouldShowAllNodeGizmos { #shouldshowallnodegizmos }

`static`

```cpp
static bool ShouldShowAllNodeGizmos()
```

True when `CCS.Debug.Viewport.Nodes.All` is non-zero — every per-node gizmo (both 3D `DrawNodeDebug` and 2D `DrawNodeDebug2D` paths) should show regardless of its own per-node CVar. The two paths share this switch intentionally: each node's 2D / 3D pieces already share one per-node CVar, so batching them into one "All" toggle keeps the mental model consistent.

Callsite idiom: if (CVarShowMyNodeGizmo.GetValueOnGameThread() == 0 &&
    !FComposableCameraViewportDebug::ShouldShowAllNodeGizmos())
{
    return;
}
 OR semantics: if either the per-node CVar OR the All CVar is on, the gizmo draws. No "except" subtraction; users wanting granularity should leave All off and enable per-node CVars individually.

---

#### ShouldShowAllTransitionGizmos { #shouldshowalltransitiongizmos }

`static`

```cpp
static bool ShouldShowAllTransitionGizmos()
```

True when `CCS.Debug.Viewport.Transitions.All` is non-zero — every per-transition gizmo draws regardless of its own CVar. Same OR semantics as ShouldShowAllNodeGizmos.

---

#### DrawSolidDebugSphere { #drawsoliddebugsphere }

`static`

```cpp
static void DrawSolidDebugSphere(class UWorld * World, const FVector & Center, float Radius, const FColor & Color, uint8 Alpha, int32 Segments, uint8 DepthPriority)
```

Draw a translucent-wireframe debug sphere — the canonical sphere gizmo used by every CCS node / transition debug override.

NOTE on the name: "Solid" is a historical artifact — an earlier iteration rendered a filled UV-mesh via `DrawDebugMesh`, but the engine's hardcoded `DebugMeshMaterial` depth-tests regardless of `DepthPriority` (a character mesh in front would clip the sphere). `SDPG_Foreground` only bypasses depth for LINE primitives, not for the mesh path, so the helper now draws only the wireframe layer — but with low segment count (8–12), Thickness=0, and an alpha-blended color to avoid the "busy wireframe" look that motivated the mesh experiment in the first place. Kept the `Solid` name for API stability.

The `Alpha` parameter is applied OVER the passed `Color.A` (i.e. overrides it) so callsites can keep using `FColor::Yellow` etc. without manually baking alpha — the default 100/255 ≈ 39 % reads as "present but not blocking the view", which is what every CCS gizmo wants. Pass higher for emphasis (progress markers) and lower for large "volume" spheres (CollisionPush self-sphere) so they stay non-occluding.

**Parameters**

* `World` World to draw into. No-op if null. 

* `Center` Sphere center in world space. 

* `Radius` Sphere radius in world units. 

* `Color` RGB from this; A is overridden by the Alpha param. 

* `Alpha` Final alpha in [0, 255]. Default 100 (≈ 39 %). 

* `Segments` Ring segment count per hemisphere. Clamped to [4, 32]. 12 = smooth silhouette; 8 reads a touch sparser and is used as the default for overlay-style callsites. 

* `DepthPriority` SDPG group. 0 = depth-tested (sphere hides behind opaque meshes); 1 (SDPG_Foreground) = draws above scene geometry via the line batcher's foreground pass. Every CCS callsite passes `SDPG_Foreground` so the marker is always visible even when embedded in a character / geometry.

Compiled out in shipping builds.
