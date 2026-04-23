# Debug Panel & Dump Commands

Technical reference for the CCS debug tools introduced alongside `showdebug camera`. See [User Guide → Debugging](../../user-guide/debugging.md) for a workflow-oriented introduction.

---

## Debug Panel (`FComposableCameraDebugPanel`)

### Activation

```
CCS.Debug.Panel 1      ← enable
CCS.Debug.Panel 0      ← disable (default)
```

Implemented by `FComposableCameraDebugPanel`. Renders via `UDebugDrawService`'s `"Game"` channel as a static delegate registered at module startup (`FComposableCameraSystemModule::StartupModule`). While disabled the draw function reads the CVar and early-outs immediately — no meaningful cost.

Available in Debug, Development, and Test builds. Stripped entirely in Shipping (`#if !UE_BUILD_SHIPPING`).

### Regions

The panel paints five regions top-to-bottom. All data comes from `BuildDebugSnapshot` calls on the context stack and director — the same pipeline that backs `showdebug camera` and the dump commands.

![[assets/images/Pasted image 20260423101255.png]]

#### Current Pose

The PCM's final output this frame.

| Field | Source |
|---|---|
| Position | `FComposableCameraPose::Position` |
| Rotation | `FComposableCameraPose::Rotation` (Pitch / Yaw / Roll) |
| FOV | `FComposableCameraPose::GetEffectiveFieldOfView()` |
| Aspect | `CurrentPOV.AspectRatio` |

Below the numeric fields: a pose-history sparkline backed by `FComposableCameraPoseHistoryEntry` ring buffer (120 entries, ~48 B each, ~6 KB total per PCM). The ring buffer records `GameTime` from `UWorld::GetTimeSeconds`, so it pauses with the game during Time Dilation / pause — the timeline stays coherent when scrubbing history during a paused PIE session. Context-switch markers are vertical lines drawn wherever `ContextName` changes between adjacent entries.

#### Context Stack & Evaluation Tree

A live tree rendered from `FComposableCameraContextStackSnapshot`. Contexts appear in stack order (base at bottom, active at top). Each context expands its director's evaluation tree, flattened DFS pre-order via `FComposableCameraTreeNodeSnapshot`.

Tree-node fields used by the renderer:

| Field | Purpose |
|---|---|
| `Kind` | Selects label prefix: `[Leaf]`, `[RefLeaf]`, `[Transition]` |
| `Depth` | Controls indent (2 spaces per level) |
| `bIsLastSibling` | Drives connector glyph: `└─` (last) vs `├─` (middle) |
| `AncestorLastFlagsBitmask` | Drives whether a vertical stem `│` is drawn at each ancestor column |
| `bIsDominantLeaf` | Highlighted leaf — the one that remains when all transitions collapse |
| `bInReferencedSubtree` | Dimmer color — this node belongs to a referenced source director's tree |
| `TransitionProgress` | Progress bar and percentage label on transition rows |
| `BlendCurveSamples` | 25-sample sparkline of `GetBlendWeightAt(i/24)` — shows the curve shape and how far the blend has advanced |

Reference leaves (`ReferenceLeaf` kind) inline their referenced director's subtree. The root of that subtree has `bIsReferencedRoot = true`, which suppresses the `[from]/[to]` role prefix that would otherwise appear at that boundary (the `RefLeaf` is a leaf in the outer tree, not a transition parent, so the usual depth-based role inference does not apply).

#### Running Camera

The active context's `Director::RunningCamera`, if any.

| Sub-section | Contents |
|---|---|
| Header | Camera class name and tag (`CameraTag`). Transient cameras show `(transient, X.Xs / Y.Ys)`. |
| Nodes | Every node in `FullExecChain` order. Each row shows the node class name and, for each output pin in the runtime data block, the pin name and its current value formatted via `ComposableCameraDebug::AppendTypedValue`. |
| Parameters | Every entry in `ExposedParameterOffsets`. `(unresolved)` if the offset is missing — indicates a sync bug between the type asset and the runtime data block. |
| Variables | Every entry in `InternalVariableOffsets`, with type looked up from the type asset's combined internal + exposed variable declarations. |
| Data Block | Memory summary: total bytes, output-pin count, exposed-parameter count, internal-variable count, default-value count. |

#### Camera Actions

Flat list from `PCM::ActiveActions`. Each row: class name + `(camera-scoped)` or `(persistent)` based on `bOnlyForCurrentCamera`.

#### Modifiers

Count summary (phase 1). Full modifier listing with priority resolution is in `showdebug camera` → [All Modifiers / Effective Modifiers](showdebug.md#modifiers).

#### Warnings (`FComposableCameraLogCapture`)

Log entries captured by `FComposableCameraLogCapture`, an `FOutputDevice` registered with `GLog` at module startup.

**What is captured:** any log line emitted on `LogComposableCameraSystem` or `LogComposableCameraSystemEditor` at `Warning` verbosity or worse (`Warning`, `Error`, `Fatal`). `Log`, `Display`, `Verbose`, and `VeryVerbose` are filtered out at capture time.

**Ring buffer:** 16 entries maximum (`FComposableCameraLogCapture::MaxCapturedEntries`). Older entries are evicted when the buffer is full.

**Deduplication:** if the same `(Category, Verbosity, Message)` triple fires again before the next eviction, the existing entry's `RepeatCount` is incremented instead of inserting a duplicate. The panel renders "(×N)" when N > 1.

**Thread safety:** `Serialize` (the capture hook) can be called from any thread. The ring buffer is guarded by a `FCriticalSection`; game-thread reads and worker-thread writes serialize cleanly. The lock is held only long enough to update a small fixed-size array.

**Build gating:** `Install` / `Uninstall` / `GetRecentEntries` are all `#if !UE_BUILD_SHIPPING`. Shipping builds pay zero cost — no output device registered, no ring buffer allocated, no lock.

---

## Viewport Debug (`FComposableCameraViewportDebug`)

### Activation

```
CCS.Debug.Viewport 1                      ← master switch (frustum + per-node gizmos)
CCS.Debug.Viewport 0                      ← off (default)
CCS.Debug.Viewport.AlwaysShow 1           ← force frustum even while possessing
CCS.Debug.Viewport.Nodes.All 1           ← OR-enable all node gizmos
CCS.Debug.Viewport.Transitions.All 1     ← OR-enable all transition gizmos
```

Per-node gizmos (all default 0):

| CVar | Node |
|---|---|
| `CCS.Debug.Viewport.PivotOffset` | `PivotOffsetNode` |
| `CCS.Debug.Viewport.LookAt` | `LookAtNode` |
| `CCS.Debug.Viewport.CollisionPush` | `CollisionPushNode` |
| `CCS.Debug.Viewport.Spline` | `SplineNode` |
| `CCS.Debug.Viewport.PivotDamping` | `PivotDampingNode` |

### Rendering pathway

Implemented by `FComposableCameraViewportDebug`. Draws via `FTSTicker::GetCoreTicker()` delegate, not `UDebugDrawService`. The ticker fires every frame regardless of which viewport is active; `DrawDebug*` calls go to the world's `LineBatcher`, which is rendered by every viewport drawing that world. This is the reason gizmos appear in the editor viewport during F8 eject — `UDebugDrawService`'s `"Game"` hook does not fire from the editor viewport, which was the blocking issue that motivated the switch to the ticker + line batcher.

### Frustum auto-hide

The frustum (drawn at the near plane) occludes the scene when the player is viewing through the camera. Auto-hide logic:

- In editor builds: frustum only fires when `GEditor->bIsSimulatingInEditor` is true (F8 eject / Simulate mode).
- In non-editor builds: frustum always fires when the master CVar is on.
- `CCS.Debug.Viewport.AlwaysShow 1`: bypasses the auto-hide in editor builds.

### `ShouldShowAllNodeGizmos` / `ShouldShowAllTransitionGizmos`

`FComposableCameraViewportDebug::ShouldShowAllNodeGizmos()` returns true when `CCS.Debug.Viewport.Nodes.All` is non-zero. Node callsite idiom:

```cpp
if (CVarShowMyNodeGizmo.GetValueOnGameThread() == 0 &&
    !FComposableCameraViewportDebug::ShouldShowAllNodeGizmos())
{
    return;
}
```

OR semantics: either the per-node CVar or the All CVar enables the gizmo. No subtraction; users wanting granularity should leave All off.

### `DrawSolidDebugSphere`

Canonical sphere gizmo helper used by every CCS node and transition debug override.

```cpp
FComposableCameraViewportDebug::DrawSolidDebugSphere(
    World,
    Center,
    Radius,
    Color,          // A is overridden by Alpha param
    Alpha,          // default 100 (≈ 39 %)
    Segments,       // default 12; clamped [4, 32]
    DepthPriority); // 0 = depth-tested; 1 (SDPG_Foreground) = above geometry
```

All CCS callsites pass `SDPG_Foreground` so the marker is always visible. The "Solid" name is a historical artifact — the helper renders translucent wireframe rather than a filled mesh, because the engine's hardcoded `DebugMeshMaterial` depth-tests regardless of `DepthPriority`, which caused geometry to clip spheres in earlier iterations.

### Adding a gizmo to a new node

Four steps, ~15 lines total:

1. Override `DrawNodeDebug(UWorld*, bool bViewerIsOutsideCamera)` in the concrete node class, guarded `#if !UE_BUILD_SHIPPING`.
2. Declare `static TAutoConsoleVariable<int32> CVarShowMyGizmo(TEXT("CCS.Debug.Viewport.MyNode"), 0, ...)` in the node's `.cpp`.
3. Early-out at the top of `DrawNodeDebug` using the ShouldShowAll OR idiom above.
4. Call `DrawDebug*` helpers from `DrawDebugHelpers.h`.

The `bViewerIsOutsideCamera` parameter is true during F8 eject / Simulate, false during possessed play. Use it to gate gizmos that sit at the camera's own position — drawing a self-collision sphere at the camera origin is only meaningful when the viewer is outside the camera.

### Build gating

All viewport debug cost is `#if !UE_BUILD_SHIPPING`. The `FTSTicker` delegate body compiles to nothing in Shipping builds. `Initialize()` / `Shutdown()` and all helper functions are no-ops.

---

## Dump Commands (`CCS.Dump.*`)

Implemented in `ComposableCameraDebugDumpCommands.cpp`. All commands are registered as `FAutoConsoleCommandWithWorldAndArgs` at static init time and stripped in Shipping (`#if !UE_BUILD_SHIPPING`).

Output route: `UE_LOG(LogComposableCameraSystem, Display, ...)` + `FPlatformApplicationMisc::ClipboardCopy(...)`. The `Display` verbosity level means the dump appears in Output Log by default, regardless of `LogComposableCameraSystem`'s configured verbosity.

### PCM resolution

All three commands share the same PCM resolution order:

1. The command-context `UWorld` (the World the console was invoked from during PIE).
2. Scan `GEngine->GetWorldContexts()` for the first `PIE` or `Game` world with a CCS PCM.

If no PCM is found, the command emits a `Warning` and returns. This means invoking a dump command from the main editor console before PIE starts will warn rather than crash.

### `CCS.Dump.Stack`

No arguments. Dumps `UComposableCameraContextStack::BuildDebugSnapshot` as indented plain text.

Output structure:

```
Context Stack (depth: N, pending destroy: M)
-> [N-1] ContextName [active]
      Running Camera: CameraName
      Last Pose: pos=(X, Y, Z)  rot=(P, Y, R)  FOV: F
      Evaluation Tree:
        [Leaf] CameraName
   [N-2] ContextName
      ...
   [pending] ContextName
```

### `CCS.Dump.Tree`

No arguments. Dumps the active director's `BuildDebugSnapshot` — running camera, last pose, and the flattened evaluation tree for the active context only.

### `CCS.Dump.Camera [tag]`

| Form | Target |
|---|---|
| `CCS.Dump.Camera` | Active context's `Director::GetRunningCamera()` |
| `CCS.Dump.Camera <tag>` | First live context whose running camera's `CameraTag` matches `tag` (case-insensitive) |

Source-side cameras that are the source (Left) of a mid-transition blend are not included in the scan — they live inside evaluation-tree leaves, not on `Director::RunningCamera`. This is acceptable for the diagnostic use case; active transitions are visible in `CCS.Dump.Stack` and `CCS.Dump.Tree`.

Output structure:

```
Camera: ActorName
  Class: ClassName
  Tag:   Gameplay.ThirdPerson.Follow
  Pose:  pos=(X, Y, Z)  rot=(P, Y, R)  fov=F
  Lifetime: E / Ts          ← transient cameras only
  Nodes (N, exec order):
    [1] NodeClassName
           PinName              = value
           ...
  Parameters (N):
    ParameterName              = value
    ...
  Variables (N):
    VariableName               = value
    ...
  Data Block: B B (P pins, Q params, R vars, S defaults)
```

Pin values are formatted via `ComposableCameraDebug::AppendOutputPinValue`, the same formatter used by the Debug Panel and `showdebug camera`. `(unresolved)` means the pin has no offset in the runtime data block — a sync issue between the type asset and the runtime.

---

## See also

- [User Guide → Debugging](../../user-guide/debugging.md) — workflow guide for all four debug surfaces
- [ShowDebug reference](showdebug.md) — section-by-section breakdown of `showdebug camera`
- [Custom Nodes](../../extending/custom-nodes.md) — how to add `DrawNodeDebug` to a new node
- [Profiling & Performance](../../user-guide/profiling.md) — using debug tools alongside Unreal Insights
