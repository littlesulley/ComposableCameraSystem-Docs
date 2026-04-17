# Profiling & Performance

Camera evaluation runs every frame on the game thread, so even small inefficiencies compound quickly — especially on mobile or when blending multiple cameras simultaneously. This page covers how to measure camera cost, where to look for bottlenecks, and how to keep the system within budget.

## The budget

A useful starting point: the entire camera pipeline (context stack evaluation → tree walk → node chain → transition blend → action ticks → modifier resolution) should complete in **under 50 µs** on your target platform for a single active camera. Blending two cameras roughly doubles that. Three simultaneous transitions (rapid-fire activations during gameplay) roughly triple it.

These numbers are a guideline, not a hard limit — your project's overall frame budget determines what you can afford.

## Quick checks before profiling

Before reaching for heavyweight tools, try these:

### `showdebug camera`

The in-game overlay (see [showdebug reference](../reference/showdebug.md)) shows the active camera's node chain, context stack, and modifier state in real time. It won't give you timing numbers, but it will immediately answer:

- How many nodes are in the active camera's chain? More nodes = more per-frame cost.
- Is a transition still running? Active transitions evaluate *both* source and target trees — double the node count.
- Are there stuck reference leaves? A `pending destroy` context that didn't collapse means an extra director is evaluating every frame.
- How many actions are active? Each action ticks once per frame.

### `stat game`

Unreal's built-in `stat game` shows the game thread's per-frame breakdown. Look for the `CameraSystem` or `PlayerCameraManager` rows — these capture the PCM's `DoUpdateCamera` cost. If the camera row is a small fraction of the total frame, you probably don't have a camera performance problem.

## Unreal Insights

For detailed per-function timing, Unreal Insights is the tool. The plugin's evaluation path is instrumented with standard UE trace markers, so it shows up in Insights without any plugin-side setup.

### Recording a trace

1. Launch PIE with `-trace=default,cpu` on the command line, or enable tracing from **Session Frontend → Profiler → Trace**.
2. Play through the scenario you want to profile (camera activation, transition, rapid-fire switches).
3. Stop tracing and open the `.utrace` file in **Unreal Insights** (standalone app shipped with the engine).

![[assets/images/Pasted image 20260417085705.png]]

### What to look for

In the **Timing Insights** view, filter by `ComposableCamera` or `PlayerCameraManager` to isolate camera-related scopes:

- **`AComposableCameraPlayerCameraManager::DoUpdateCamera`** — the top-level scope. Everything else nests inside it.
- **`UComposableCameraContextStack::Evaluate`** — Tier 1. Should be near-zero unless a context is being pushed/popped this frame.
- **`UComposableCameraDirector::Evaluate`** → **`UComposableCameraEvaluationTree::Evaluate`** — Tier 2. The recursive tree walk.
- **`AComposableCameraCameraBase::TickCamera`** — per-camera node chain evaluation. This is usually the dominant cost.
- Individual node ticks (**`OnTickNode`**) — visible as child scopes under `TickCamera`. The most expensive shipped node is typically `CollisionPushNode` (line/sphere traces) followed by `PivotDampingNode` (spring math).
- **Transition `Evaluate`** — visible during active blends. Cost depends on the transition type; inertialized transitions are cheap (polynomial math), spline transitions are moderate (spline eval + possibly traces).

![[assets/images/PixPin_2026-04-17_08-59-07.png]]
### Reading the timeline

During steady-state gameplay (one camera, no transitions), you should see a thin, consistent `DoUpdateCamera` bar each frame. During a transition, the bar doubles in width because both source and target cameras evaluate. After `CollapseFinishedTransitions` fires, the bar should return to single-camera width.

If the bar stays wide after a transition should have finished, a transition is stuck or a reference leaf isn't collapsing — check `showdebug camera` for a `pending destroy` entry that didn't clean up.

![[assets/images/PixPin_2026-04-17_09-03-57.png]]

## Common bottlenecks

### Collision nodes

`CollisionPushNode` runs line traces and/or sphere sweeps every frame. On complex geometry, each trace can cost 2–10 µs. Two things to try:

- **Reduce trace complexity.** Use `Sphere` trace type with a small radius rather than complex sweep shapes. Set `TraceChannel` to `Camera` (which you can configure to ignore small props).
- **Reduce trace frequency.** If the camera is relatively stable (e.g. no player input), skip traces when the delta from the last frame is below a threshold. This requires a custom node — the shipped `CollisionPushNode` traces every frame unconditionally.

### Damping interpolators

`PivotDampingNode` and other damping nodes run spring-damper math each frame. The cost per instance is small (~1 µs), but cameras with multiple damping stages (pivot damping + rotation damping + offset damping) add up. Keep damping nodes to what's perceptually necessary.

### Transition pile-ups

Rapid-fire camera activations during gameplay (e.g. quick weapon switching, rapid context pushes) create a chain of inner nodes in the evaluation tree. Each in-progress transition evaluates both its children. Three concurrent transitions mean six leaf evaluations per frame instead of one.

The system collapses finished transitions on the next frame, so this is self-healing — but during the pile-up, the cost spikes. If your gameplay triggers very frequent activations, consider whether a hard cut (no transition) is acceptable for rapid switches, reserving smooth transitions for deliberate camera changes.

### Blueprint nodes on the hot path

`BlueprintCameraNode` ticks through the Blueprint VM, which is several times slower than an equivalent C++ node. For prototyping a single camera, it's fine. For shipping production code that runs on many cameras, port to C++. The [Custom Nodes](../extending/custom-nodes.md) recipe is the cheapest migration path.

### Allocations in the hot path

The [hot-path rule](../extending/custom-nodes.md#the-hot-path-rule-repeated-because-it-matters) prohibits allocations inside per-frame evaluation. Common offenders:

- `FString::Printf` inside `OnTickNode` — even for logging.
- `TArray::Add` on a result buffer every frame — preallocate with `SetNumUninitialized()`.
- `NewObject` inside tick — cache the subobject in `OnInitialize`.
- Implicit `FString` construction from `UE_LOG` at `Verbose` level — gate behind `if (UE_LOG_ACTIVE(LogComposableCameraSystem, Verbose))`.

To detect allocations, run Unreal Insights with the `memory` trace channel enabled and look for allocation events inside `TickCamera` scopes.

## `stat` commands reference

These engine-level stat commands are useful alongside the plugin's own diagnostics:

| Command | What it shows |
|---|---|
| `stat game` | Per-frame game thread breakdown — find the camera row |
| `stat slow` | Anything over 1 ms — useful for spotting camera spikes during transitions |
| `stat unit` | Frame, game, draw, GPU times — confirms whether you're game-thread bound |
| `stat scenerendering` | Rendering cost — rules out GPU as the bottleneck |

## Performance checklist

A quick list to run through before shipping:

1. **One camera, no transitions** — `DoUpdateCamera` under 50 µs on target hardware.
2. **During a transition** — cost roughly doubles (two cameras evaluating). Confirm it returns to baseline after collapse.
3. **Rapid-fire activations** — pile-up cost spikes but self-heals within a few frames. No stuck transitions in `showdebug`.
4. **No allocations in tick** — verify with Insights memory trace.
5. **No Blueprint nodes on the hot path** in shipping builds — all prototyping `BlueprintCameraNode`s ported to C++.
6. **CollisionPushNode trace channel** set to something cheaper than `Visibility` if scene complexity is high.
7. **Mobile budget** — re-profile on device; desktop numbers are not representative. Consider disabling self-collision or reducing trace frequency for mobile.

## See also

- [`showdebug camera`](../reference/showdebug.md) — the in-game overlay for live state inspection
- [Custom Nodes → Hot-Path Rule](../extending/custom-nodes.md#the-hot-path-rule-repeated-because-it-matters) — the allocation constraint and how to comply
- [FAQ → Performance](../faq/index.md#performance) — common performance questions and answers
