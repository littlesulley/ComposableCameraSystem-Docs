# FComposableCameraViewportDebug { #fcomposablecameraviewportdebug }

```cpp
#include <ComposableCameraViewportDebug.h>
```

Runtime 3D viewport debug draw for the Composable Camera System.

`CCS.Debug.Viewport 0|1` is the live viewport master switch. Per-node and per-transition CVars remain opt-in for live drawing, while Rewind trace capture can force all 3D gizmos through its draw sink so playback has complete historical debug primitives even when live CVars were disabled.

Adding a new per-node gizmo:

1. Override `UComposableCameraCameraNodeBase::DrawNodeDebug(FComposableCameraDebugDrawSink&, bool)` in the concrete node, guarded `#if !UE_BUILD_SHIPPING`.
2. Declare a static `TAutoConsoleVariable<int32>` under `CCS.Debug.Viewport.<NodeName>`, default 0.
3. Early-out when the per-node CVar, `ShouldShowAllNodeGizmos()`, and `Draw.ShouldForceDrawAllNodeGizmos()` are all false.
4. Emit primitives through `FComposableCameraDebugDrawSink` and use `FComposableCameraViewportDebugColors` for shared legend colors.

All cost is guarded `#if !UE_BUILD_SHIPPING`. The ticker's body compiles to nothing in shipping builds.

### Public Static Methods

| Return | Name | Description |
|--------|------|-------------|
| `void` | [`Initialize`](#initialize-2) `static` | Register the FTSTicker delegate. Idempotent. |
| `void` | [`Shutdown`](#shutdown-1) `static` | Unregister the FTSTicker delegate. Idempotent. |
| `bool` | [`ShouldShowAllNodeGizmos`](#shouldshowallnodegizmos) `static` | True when `CCS.Debug.Viewport.Nodes.All` is non-zero. Rewind capture may additionally force all node gizmos through its draw sink. |
| `bool` | [`ShouldShowAllTransitionGizmos`](#shouldshowalltransitiongizmos) `static` | True when `CCS.Debug.Viewport.Transitions.All` is non-zero. Rewind capture may additionally force all transition gizmos through its draw sink. |
| `TConstArrayView< FComposableCameraViewportDebugLegendEntry >` | [`GetLegendEntries`](#getlegendentries) `static` | Shared legend metadata. Used by the panel and tests so swatches come from the same color constants as 3D gizmos. |
| `float` | [`GetSphereLabelDurationSeconds`](#getspherelabeldurationseconds) `static` | Lifetime used for per-frame sphere labels. Zero prevents stale HUD text. |
| `void` | [`DrawSolidDebugSphere`](#drawsoliddebugsphere) `static` | Draw a translucent-wireframe debug sphere, optionally with a short per-frame label. |

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

True when `CCS.Debug.Viewport.Nodes.All` is non-zero. Live draw callsites combine this with their per-node CVar. Rewind capture sinks can separately force all node gizmos.

---

#### ShouldShowAllTransitionGizmos { #shouldshowalltransitiongizmos }

`static`

```cpp
static bool ShouldShowAllTransitionGizmos()
```

True when `CCS.Debug.Viewport.Transitions.All` is non-zero. Live draw callsites combine this with their per-transition CVar. Rewind capture sinks can separately force all transition gizmos.

---

#### GetLegendEntries { #getlegendentries }

`static`

```cpp
static TConstArrayView< FComposableCameraViewportDebugLegendEntry > GetLegendEntries()
```

Shared legend metadata. Used by the panel and tests so swatches come from the same color constants as 3D gizmos.

---

#### GetSphereLabelDurationSeconds { #getspherelabeldurationseconds }

`static`

```cpp
static float GetSphereLabelDurationSeconds()
```

Lifetime used for per-frame sphere labels. Zero prevents stale HUD text.

---

#### DrawSolidDebugSphere { #drawsoliddebugsphere }

`static`

```cpp
static void DrawSolidDebugSphere(class UWorld * World, const FVector & Center, float Radius, const FColor & Color, uint8 Alpha, int32 Segments, uint8 DepthPriority, const TCHAR * Label)
```

Draw a translucent-wireframe debug sphere. The `Alpha` parameter overrides `Color.A`; `Segments` is clamped to `[4, 32]`; `DepthPriority` follows the SDPG group where `1` means foreground. `Label` is optional short world-space text drawn above the sphere with a one-frame lifetime.
