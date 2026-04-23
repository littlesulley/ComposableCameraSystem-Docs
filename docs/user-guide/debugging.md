# Debugging

CCS ships four distinct debug surfaces that complement each other rather than duplicate. Understanding what each one covers helps you reach for the right tool instead of hunting through them all.

| Tool | How to activate | Best for |
|---|---|---|
| [`showdebug camera`](../reference/debugging/showdebug.md) | Console: `showdebug camera` | Quick pose check; color-coded HUD that fires everywhere `DisplayDebug` runs |
| [Debug Panel](#debug-panel-ccsdebugpanel) | Console: `CCS.Debug.Panel 1` | Always-on live readout — sparklines, tree glyph rendering, inline warnings |
| [Viewport Debug](#viewport-debug-ccsdebugviewport) | Console: `CCS.Debug.Viewport 1` | 3D in-world gizmos — frustum, per-node overlays visible during F8 eject |
| [Dump Commands](#dump-commands-ccsdump) | Console: `CCS.Dump.Stack` / `.Tree` / `.Camera` | One-shot text snapshots to Output Log + clipboard; ideal for bug reports and diffing |
![[assets/images/Pasted image 20260423100456.png]]

All four surfaces read from the same runtime state — snapshots produced by `BuildDebugSnapshot` on the context stack, director, and evaluation tree. They stay in lockstep automatically.

None of this costs anything in Shipping builds. The Debug Panel, Viewport Debug, and Dump Commands are all gated `#if !UE_BUILD_SHIPPING`. `showdebug camera` routes through `DisplayDebug`, which Unreal strips in Shipping by default.

## Debug Panel (`CCS.Debug.Panel`)

```
CCS.Debug.Panel 1      ← enable
CCS.Debug.Panel 0      ← disable
```

The Debug Panel is a 2D HUD overlay rendered via `UDebugDrawService`'s `"Game"` channel. It updates every frame and can be toggled without leaving PIE — it persists across camera transitions and context switches so you can watch the tree evolve in real time.

![[assets/images/Pasted image 20260423100516.png]]

The panel is organized into five regions, top to bottom.

**Current Pose** — the PCM's final output this frame: world position, rotation, FOV, and aspect ratio. Below the numbers, a pose-history sparkline covers the last two seconds of frames. Context-switch moments appear as vertical lines wherever the active context changed. In editor builds, hovering over the sparkline shows a tooltip with the exact values at that history point.

**Context Stack & Evaluation Tree** — a live tree rendering of the entire context stack. Each director's evaluation tree is expanded inline using box-drawing glyphs (`└─`, `├─`, `│`). Tree nodes are labeled by kind — `[Leaf]`, `[RefLeaf]`, `[Transition]` — with the camera or transition class name. For in-progress transitions, the row also shows a percentage and elapsed/total seconds, plus a small blend-weight sparkline with 25 samples so you can see whether the curve is linear, eased, or something more complex. The dominant leaf (the one that would remain if all transitions collapsed immediately) is visually distinguished. Reference leaves inline their referenced subtree in a dimmer color, so you can see both sides of a cross-context blend without switching screens.

**Running Camera** — the active context's running camera in full: class name, camera tag, transient lifetime if applicable, every node in execution order with its resolved output-pin values, every exposed parameter's runtime value, every internal variable's value, and a data-block memory summary (bytes, pin count, parameter count, variable count). This is the richest single-screen view of what a camera is actually computing this frame.

**Camera Actions** — a flat list of currently active actions on the PCM, showing each action's class name and scope (`camera-scoped` vs `persistent`).

**Modifiers** — a count summary of active modifiers. The full per-modifier listing with priority resolution lives in `showdebug camera`'s **All Modifiers** and **Effective Modifiers** sections.

**Warnings** — any `Warning` or `Error` emitted by `LogComposableCameraSystem` or `LogComposableCameraSystemEditor` appears here in amber or red, with an elapsed-time label ("2s ago") and a repeat badge ("×4") when the same message fires multiple times. This surfaces silent runtime errors — a spline transition missing its rail actor, a referenced director destroyed mid-blend — that would otherwise require an open Output Log window to notice. The ring buffer holds the 16 most recent distinct entries; older entries are evicted from the front.

There is also a `CCS.Debug.Panel.PoseHistory` command to preview camera pose history. This only includes camera rotation and position. This can be quite useful if you want to detect when and where the camera pops or jitters.

![[assets/images/Pasted image 20260423100926.png]]

Use `CCS.Debug.Panel.PoseHistory.Freeze` to freeze the history panel, and then press F8 or Shift+F1 to display the mouse the hover above graph. It will show you the concrete information of the camera pose at that timestamp.

![[assets/images/Pasted image 20260423101130.png]]
## Viewport Debug (`CCS.Debug.Viewport`)

```
CCS.Debug.Viewport 1                      ← master switch
CCS.Debug.Viewport 0                      ← off
CCS.Debug.Viewport.AlwaysShow 1           ← force frustum even while possessing
CCS.Debug.Viewport.Nodes.All 1           ← enable all node gizmos at once
CCS.Debug.Viewport.Transitions.All 1     ← enable all transition gizmos at once
```

![[assets/images/Pasted image 20260423100715.png]]

The Viewport Debug draws into the world's line batcher via an `FTSTicker` delegate rather than `UDebugDrawService`. This matters: `UDebugDrawService`'s `"Game"` hook does not fire from the editor viewport during F8 eject, which is typically when 3D camera debug is most useful. The line batcher's output is rendered by every viewport that draws that world, so the gizmos appear both in the game viewport during possessed play and in the editor viewport during F8 eject or Simulate mode.

The master switch (`CCS.Debug.Viewport 1`) enables **frustum drawing**. The frustum auto-hides while you are possessing the camera, because the near-plane frustum occludes the scene from the camera's own viewpoint. It only fires when `bIsSimulatingInEditor` is true, i.e. during F8 eject or Simulate mode. `CCS.Debug.Viewport.AlwaysShow 1` overrides this — useful in multi-viewport setups where a secondary viewport shows the camera from outside while you possess it.

![[assets/images/Pasted image 20260423100734.png]]

Per-node gizmos are controlled individually:

| CVar | Node | What it draws |
|---|---|---|
| `CCS.Debug.Viewport.PivotOffset 1` | `PivotOffsetNode` | Pivot point and offset arm from pivot to camera |
| `CCS.Debug.Viewport.LookAt 1` | `LookAtNode` | Look-at target position and direction ray |
| `CCS.Debug.Viewport.CollisionPush 1` | `CollisionPushNode` | Trace rays and the pushed camera position |
| `CCS.Debug.Viewport.Spline 1` | `SplineNode` | The resolved spline path drawn in world space |
| `CCS.Debug.Viewport.PivotDamping 1` | `PivotDampingNode` | Raw (undamped) and damped pivot positions side by side |

Each per-node CVar defaults to 0 so a camera with multiple active nodes doesn't turn into an unreadable tangle. Enable them one at a time to isolate the node you're investigating. `CCS.Debug.Viewport.Nodes.All 1` enables all node gizmos at once — a good first overview.

All gizmos use `SDPG_Foreground` depth priority and translucent-wireframe spheres, so they render in front of scene geometry and remain readable even when the camera is embedded inside a character mesh.

If you are writing a [custom node](../extending/custom-nodes.md) and want to add your own gizmo, the implementation is about 15 lines: override `DrawNodeDebug(UWorld*, bool)` on your node class (guarded `#if !UE_BUILD_SHIPPING`), declare a static `TAutoConsoleVariable<int32>` under `CCS.Debug.Viewport.<YourNodeName>`, early-out on it, and call `DrawDebug*` helpers directly. See the Viewport Debug header for the full recipe.

## Dump Commands (`CCS.Dump`)

Dump commands produce a formatted plain-text snapshot. The text goes simultaneously to `LogComposableCameraSystem` at `Display` verbosity (so it appears in Output Log without raising the log verbosity) and to the system clipboard. They capture state at a single point in time — ideal for bug reports and for diffing before/after states when fixing a regression.

### `CCS.Dump.Stack`

Dumps the full context stack: live depth, each context's name, its running camera name, its last evaluated pose (position, rotation, FOV), and the flattened evaluation tree. Pending-destroy contexts appear at the end, labelled `[pending]`. This is the same information the Debug Panel's "Context Stack & Evaluation Tree" region shows, formatted as indented plain text.

### `CCS.Dump.Tree`

Dumps the **active context's** evaluation tree only — the running camera, the last pose, and each flattened tree node with its transition progress and elapsed/total time. Useful when only the active context matters and the full-stack output from `CCS.Dump.Stack` would add noise.

### `CCS.Dump.Camera [tag]`

Without an argument, dumps the **active context's running camera** in full: class name, camera tag, pose, transient lifetime if applicable, every node in execution order with each output pin's resolved runtime value, every exposed parameter and internal variable with its value, and a data-block memory summary (bytes, pin count, parameter count, variable count).

With a tag argument, scans every live context's running camera for a case-insensitive match on `CameraTag` and dumps the first match:

```
CCS.Dump.Camera Gameplay.ThirdPerson.Follow
```

This lets you dump a suspended source camera that is currently the source side of a blend — you can ask for it by tag without making it the active context's running camera first.

Both forms copy the result to the clipboard. Paste directly into a bug report or a diff tool.

## Choosing the right tool

The surfaces are designed to be used together — there is no wrong answer. A typical debugging session might start with the **Debug Panel** (leave it on in your dev build; it costs nothing when the CVar is 0) to notice something is wrong, switch to **Viewport Debug** to see the spatial geometry of the problem, and finish with **`CCS.Dump.Camera`** to copy a precise snapshot into a bug report.

`showdebug camera` remains the right choice fo