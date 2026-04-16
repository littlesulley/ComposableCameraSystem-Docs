# Actions

Actions are lightweight, fire-and-forget behaviors that hook into the camera's per-frame tick. Unlike [nodes](../../reference/nodes.md), actions don't live inside the camera's permanent chain — they run alongside it, and unlike [modifiers](modifiers.md), they execute their own per-frame logic rather than overriding an existing node's parameters.

Use an action when you need a temporary, self-contained behavior that operates on the camera pose and expires on its own: a smooth one-shot move, a timed rotation, a pitch reset after a cutscene, or any gameplay-triggered impulse that shouldn't outlive its moment.

## The three tools compared

| | Node | Modifier | Action |
|---|---|---|---|
| **Runs its own per-frame logic** | Yes | No (overrides parameters) | Yes |
| **Part of the permanent chain** | Yes | No (targets a node class) | No |
| **Added / removed at runtime** | No | Yes | Yes |
| **Has built-in expiration** | No | No | Yes |

If your behavior is permanent and produces or transforms a pose, it's a **node**. If it conditionally tweaks how an existing node behaves, it's a **modifier**. If it's temporary, self-contained, and should auto-expire, it's an **action**.

## How actions work

Every action is a `UComposableCameraActionBase` subclass with two overridable hooks:

- **`CanExecute(DeltaTime, CurrentPose)`** — a predicate, called each frame when the action uses condition-based expiration. Return `false` to expire.
- **`OnExecute(DeltaTime, CurrentPose, OutPose)`** — the main logic. Reads the current pose, does its work, and writes the modified pose back.

Actions declare **when** they run relative to the camera tick (`PreCameraTick` or `PostCameraTick`) and **how** they expire:

- `Instant` — one frame, then done.
- `Duration` — runs for a fixed number of seconds.
- `Manual` — runs until you call `ExpireAction()`.
- `Condition` — runs until `CanExecute()` returns `false`.

These flags combine as a bitmask — `Duration | Condition` means "whichever limit is hit first".

## Camera-scoped vs. persistent

The `bOnlyForCurrentCamera` flag controls whether the action survives a camera switch:

- **Camera-scoped** (default) — the action auto-expires when the running camera changes. A "smooth rotate to target" action won't linger after a transition blends to a different camera.
- **Persistent** — the action survives camera switches. Use this for effects that should span an entire gameplay session or context.

Camera-scoped actions are the common case and the safer default. Prefer them unless you have a specific reason for the effect to outlive the current camera.

## Shipped actions

The plugin ships three ready-to-use actions:

| Action | What it does |
|---|---|
| `MoveToAction` | Smoothly moves the camera to a target world position over the action's duration |
| `RotateToAction` | Smoothly rotates the camera to a target rotation over the action's duration |
| `ResetPitchAction` | Smoothly resets the camera's pitch to zero over the action's duration |

All three default to `PostCameraTick` — they layer on top of whatever the node chain produces.

## Adding and removing actions

From Blueprint, use `Add Action` and `Expire Action` on `UComposableCameraBlueprintLibrary` (see [Blueprint API](../blueprint-api.md#actions)). From C++, call the same library or go through the PCM directly.

Only one instance of a given action class can be active at a time — adding a second `MoveToAction` replaces the first.

## In summary

- Actions are temporary, self-contained per-frame behaviors that run alongside the node chain.
- They expire automatically via duration, condition, or manual removal — no cleanup code required for the common case.
- Camera-scoped actions auto-expire on camera switch; persistent ones survive.
- Use them for one-shot effects that don't belong in the permanent node composition.

For the full authoring guide (including how to write custom actions), see [Camera Actions](../camera-actions.md). For the C++ class interface, see [`UComposableCameraActionBase`](../../reference/api/actions/UComposableCameraActionBase.md).
