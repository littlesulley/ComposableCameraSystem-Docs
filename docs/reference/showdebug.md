# `showdebug composablecamera`

The in-game debug overlay for the plugin. In PIE (or in a packaged build launched with a development configuration), open the console and type:

```
showdebug composablecamera
```

The command toggles a multi-section overlay anchored to the top-left of the viewport. Each section covers a subsystem of the PCM — camera pose, the running camera, the context stack, active actions, and modifiers. This page documents what each section prints and how to read it.

The overlay is implemented by `AComposableCameraPlayerCameraManager::DisplayDebug`. Calling `showdebug` with any custom category routes through Unreal's `DebugDisplay` dispatch and that override is where all the output comes from — so if you're staring at unexpected text, the canonical reference is `ComposableCameraPlayerCameraManager.cpp`.

## Color schema

The overlay uses four colors to separate structure from data:

| Color | Role | Example |
|---|---|---|
| **Purple** | Section header | `Camera Pose`, `Running Camera: CCS_FollowCamera` |
| **Teal** | Sub-header | `Camera Nodes (4)`, `Exposed Parameters (3)` |
| **Orange** | Ordinary content | Positions, node names, tags |
| **Yellow** | Exposed parameter / variable values | `FOV = 85.0`, `LookAtWeight = 0.75` |

Headers use the engine's large font; content uses the default size.

## Section-by-section

### Camera Pose

The top-level header. Prints the final, PCM-output pose the viewport is using this frame.

```
Camera Pose
    Position:  X=1234.56 Y=789.01 Z=123.45
    Rotation:  P=-10.00 Y=45.00 R=0.00
    FOV:       85.0
    Aspect:    1.778
```

- **Position / Rotation** are the `FComposableCameraPose` produced by the current evaluation (after transitions, modifiers, everything).
- **FOV** is `GetEffectiveFieldOfView()` — the pose's own FOV, not the PCM cache's.
- **Aspect** comes from `CurrentPOV.AspectRatio`, i.e. the final view info after Unreal's downstream composition.

If Position is `(0, 0, 0)` and FOV is `0`, no pose has been produced yet — the PCM is still in its pre-first-tick state, or the running camera is failing to produce a valid output.

### Running Camera

The camera currently at the head of the active context's evaluation tree.

```
Running Camera: CCS_FollowCamera
    Tag:  Gameplay.ThirdPerson.Follow
    Life: 2.35 / 3.00s remaining          ← only if transient
  Camera Nodes (4)
    [ 0] Receive Pivot Actor
    [ 1] Camera Offset
    [ 2] Look At
    [ 3] Field Of View
  Compute Nodes (2)
    [ 0] Compute Distance To Actor
    [ 1] Compute Random Offset
  Exposed Parameters (3)
    FOV                      = 85.0
    OffsetDistance           = 350.0
    LookAtWeight             = 0.75
  Variables (2)
    DistanceToTarget         = 342.12
    BumpTimer                = 1.23
```

- **Header** shows the type asset's name. If there's no type asset (rare — usually transient fallback cameras), it falls back to the camera's `CameraTag`, then to `(unknown)`.
- **Tag** is the camera's `CameraTag` gameplay tag. `(none)` means the type asset didn't declare one.
- **Life** only appears for transient cameras. Format is `Remaining / Total` seconds. Watch this tick down on a cinematic intro if you want to verify the auto-pop timer.
- **Camera Nodes** is the ordered evaluation chain on the running camera. Numbers are array indices. Empty slots (null nodes) are skipped in the display but counted into the chain position — so a gap in numbering means a node was nulled out during serialization.
- **Compute Nodes** is the same idea for compute nodes (non-pose-producing). The section only appears if there's at least one compute node — cameras with none just skip it.
- **Exposed Parameters** are the type asset's external parameters, each printed with its resolved runtime value. `(unresolved)` means the parameter is declared but has no offset in the runtime data block — which is a bug worth investigating.
- **Variables** lists internal and exposed variables together. Names come from `InternalVariableOffsets`; types are looked up in the merged map of internal + exposed variable declarations.

If there's no running camera, the whole body is replaced with `(none)` in orange.

### Context Stack & Evaluation Tree

Prints the context stack's own debug string, indented one level for consistency with the rest of the overlay.

```
Context Stack & Evaluation Tree
    [Context] Gameplay (active)
      └─ Director:  (type asset summary)
          └─ (evaluation tree summary)
    [Context] Cutscene (pending destroy)
      └─ (reference-leaf tree)
```

The exact format is controlled by `UComposableCameraContextStack::BuildDebugString` — the PCM just forwards the lines it produces. That's where to look if you want to understand a specific line; this section does not add interpretation.

This is the section you use to diagnose **context leaks** (a UI context you thought was popped still showing up on the stack) and **stuck reference leaves** (a `pending destroy` entry that should've collapsed after a transition finished but didn't).

### Camera Actions

A flat list of currently-active actions on the PCM.

```
Camera Actions
    ComposableCameraMoveToAction (camera-scoped)
    ComposableCameraRotateToAction (persistent)
```

Each entry shows the class name and whether `bOnlyForCurrentCamera` is true:

- `(camera-scoped)` — the action will expire when the current camera transitions away.
- `(persistent)` — the action survives camera transitions and keeps running until completion or explicit cancellation.

`(none)` means the action list is empty.

See the [Blueprint API → Actions](../user-guide/blueprint-api.md#actions) section for the lifetime model behind these flags.

### Modifiers

Printed by `BuildModifierDebugString`. Has two sub-sections:

#### All Modifiers

Every modifier currently registered with the manager, grouped by camera tag → node class → individual modifier entry.

```
All Modifiers
    [Camera Tag] Gameplay.ThirdPerson:
            [Camera Node] ComposableCameraFieldOfViewNode:
                    [Modifier] BP_SprintFOVBump_C from [Asset]DA_Sprint with priority 10
                    [Modifier] BP_ZoomFOV_C from [Asset]DA_Zoom with priority 5
            [Camera Node] ComposableCameraControlRotateNode:
                    [Modifier] BP_AimRotateDamping_C from [Asset]DA_Aim with priority 20
```

This is the **raw registration view** — all modifiers the manager knows about, not just the ones currently winning their priority contest. Useful for checking that a modifier asset was actually added via `AddModifier`.

#### Effective Modifiers

The resolved set — one winning modifier per node class on the currently running camera.

```
Effective Modifiers
    [Camera Node] ComposableCameraFieldOfViewNode:
            [Modifier] BP_SprintFOVBump_C from [Asset] DA_Sprint with priority 10
    [Camera Node] ComposableCameraControlRotateNode:
            [Modifier] BP_AimRotateDamping_C from [Asset] DA_Aim with priority 20
```

Compare to **All Modifiers** above: `BP_ZoomFOV_C` is registered but loses the priority contest on `FieldOfViewNode`, so it doesn't appear here.

This is the section to check when a modifier seems registered but isn't affecting the pose — if it's in **All Modifiers** but not **Effective Modifiers**, a higher-priority modifier is shadowing it.

## Tips

- **Toggle off with the same command.** `showdebug composablecamera` is a toggle, not a switch — typing it again hides the overlay.
- **It's PIE-safe but not editor-safe.** The overlay requires a live PCM; it draws nothing in the editor viewport before PIE has started. Use it during gameplay, not asset authoring.
- **Build type matters.** `DisplayDebug` is stripped in Shipping builds. Debug, Development, and Test all print.
- **Other engine overlays still work.** You can combine `showdebug composablecamera` with `showdebug ai`, `showdebug input`, etc. The plugin's overlay stacks below whatever engine overlay is already up.
- **Don't parse this output.** The format is for humans. If you need programmatic access to the same data, go through the subsystem directly — `PCM->RunningCamera`, `PCM->ContextStack`, `PCM->ModifierManager->GetModifierData()`.

## See also

- [Blueprint API](../user-guide/blueprint-api.md) — how to query the same state programmatically
- [Context Stack](../user-guide/concepts/context-stack.md) — the model behind the stack section
- [Modifiers](../user-guide/concepts/modifiers.md) — the model behind the modifier resolution
