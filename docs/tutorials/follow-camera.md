# Tutorial: Follow Camera

Build a standard third-person follow camera — pivot locked to a target actor, camera offset behind and slightly above, stick-driven yaw/pitch, soft collision pushback. By the end you'll have a single `UComposableCameraTypeAsset` that runs on any character and activates from a one-line Blueprint call.

The chain we're building:

```
ReceivePivotActorNode        reads FollowTarget, publishes PivotPosition
  → ControlRotateNode        right-stick yaw + pitch input
  → RotationConstraints      pitch clamp
  → PivotOffsetNode          shoulder-height lift
  → PivotDampingNode         smooths pivot snaps (optional but recommended)
  → CameraOffsetNode         pushes the camera behind the pivot
  → CollisionPushNode        trace + self-collision pushback
  → FieldOfViewNode          author FOV
```

Each of these is a shipped node documented in the [Node Catalog](../reference/nodes.md). The tutorial steps through authoring the asset, exposing parameters, wiring input, and activating it.

![[assets/images/Pasted image 20260419210534.png]]

## 1. Create the type asset

Content Browser → right-click → **Composable Camera System → Camera Type Asset**. Name it `CT_ThirdPersonFollow`. Double-click to open the graph editor.

![[assets/images/Pasted image 20260417092149.png]]

The canvas starts empty with a single **Output** node on the right — that's where the final pose ends up each frame.

![[assets/images/PixPin_2026-04-17_09-22-21.png]]

## 2. Declare a `FollowTarget` variable

A follow camera needs to know which actor to follow. We expose that as a **context variable** so callers can pass it in on activation.

1. Open the **Exposed Variables** panel (right side of the editor).
2. Click **+ Add**.
3. Set **Name** to `FollowTarget`, **Type** to `Actor Reference`.

This variable now appears as a variable node in the palette and — crucially — it will become a pin on the `Activate Camera` K2 node in Blueprint.

![[assets/images/Pasted image 20260417092546.png]]

## 3. Stick-driven orbit

Drop a **ControlRotate** node. Wire `FollowTarget` into its `RotationInputActor` pin (the actor owning the `EnhancedInputComponent`). In Details:

- `RotateAction` — your `IA_Look` asset (or whatever you use for right-stick look input). This must be an `UInputAction` with `Axis2D` value type.
- `HorizontalSpeed` / `VerticalSpeed` — `1` / `1` are reasonable starting values.
- `HorizontalDamping` = `(0.05, 0.1)` — a short acceleration, slightly longer deceleration.
- `VerticalDamping` = `(0.05, 0.1)`.
- `bInvertPitch` — toggle to taste.

!!! note "Enhanced Input dependency"
    `ControlRotateNode` reads input via the Enhanced Input system. If `EnhancedInput` isn't already in your project's module dependencies, add it to your `Build.cs` — otherwise the node compiles but reads no input at runtime.

Now drop a **RotationConstraints** node after it. Set `PitchRange` to `(-40, 40)` so the player can't look straight up or down into the floor.

![[assets/images/Pasted image 20260419210641.png]]
## 4. The pivot chain

Drop these three nodes onto the canvas, left to right:

- **ReceivePivotActor** — wire `FollowTarget` into its `Actor` input.
- **PivotOffset** — set `OffsetSpace` to **Actor Space**, `Offset` to `(0, 0, 80)` for shoulder height. Wire the receive node's `PivotPosition` output into the offset node's `PivotPosition` input.
- **PivotDamping** — add an Instanced `IIRInterpolator` in its `Interpolator` slot, `Speed = 1`, `bUseFixedStep = true`. Wire the previous node's output in.

The three nodes handle *what point the camera is tracking*. They don't touch camera position or rotation yet.

![[assets/images/Pasted image 20260419210725.png]]

## 5. Camera offset

Drop a **CameraOffset** node. Set:

- `Offset` = `(-400, 50, 20)` — 4m behind, slightly right, slightly above the pivot.

Wire the previous node's output pose into its input. The camera now sits at a fixed offset from the pivot, but still points at wherever it was pointed when the tree was built (usually world origin).

![[assets/images/Pasted image 20260419210741.png]]


## 6. Collision

Drop a **CollisionPush** node. This is the largest single node in the shipped set — it handles two collision modes simultaneously:

- **Trace collision** — a line/sphere trace from pivot to camera each frame; if something blocks it, the camera is pushed toward the pivot along the trace direction.
- **Self collision** — a sphere around the camera; if something overlaps it, the camera is pushed to the *far side* via a reverse sphere sweep from beyond the camera back toward the pivot.

Starting values:

- `TraceUseSphere = true`, `TraceSphereRadius` = `12`.
-  `SelfSphereRadius` = `12`.
- `TraceCollisionChannel` = `Camera` (or `Visibility`, depending on your project), `SelfCollisionChannel = SelfCamera` (depening on your project),
- For both modes, the push/pull interpolators default to `IIRInterpolator`. Set `PushInterpolator.Speed = 10` and `PullInterpolator.Speed = 10` — fast push on occlusion, slow return so the camera doesn't bounce.

![[assets/images/Pasted image 20260417093402.png]]

## 7. Author FOV

Finally, drop a **FieldOfView** node. Set `FieldOfView` = `70`. Wire its output into the Output node's `Pose` input.

## 8. Save and build

`Ctrl+S`. The asset header should show a green checkmark. If it's red, hover for the error — typically an unconnected exec pin or a dangling parameter reference.

The final graph looks like a straight pipeline: parameter → 8 nodes → Output.

## 9. Activate from Blueprint

Open your character Blueprint. On `BeginPlay`:

1. Right-click → search **Activate Camera**. Place the node.
2. Set **Camera Type Asset** = `CT_ThirdPersonFollow`. The node rebuilds its pins — you'll see a `Follow Target` pin appear (generated from your parameter).
3. Wire the character's `Self` into `Follow Target`, and `Player Index` = `0`.
4. Connect the exec pin from `BeginPlay`.

![[assets/images/Pasted image 20260417103122.png]]

That's the entire activation path. Compile, play, and the camera snaps to your character with stick-driven orbit and collision-aware pushback.

## Tuning notes

A few things to nudge once you see it running:

- **Camera feels "sticky" behind the character** — increase `HorizontalDamping.Y` (deceleration time) on `ControlRotateNode`, or lower `SoftLookAtWeight` on `LookAtNode`.
- **Camera snaps through thin walls** — you're relying on trace collision only. Enable self collision and increase `SelfCollisionRadius` until the camera stops poking through.
- **Pitch feels sluggish near the clamps** — `RotationConstraints` is a hard clamp; if you want softer approach, author a custom node that smoothstops near the range endpoints, or set a wider pitch range and let content design the limit.
- **Camera jitters while the character is on a moving platform** — add a second `PivotDamping` after the offset, and lower the spring damp time to `~0.08`. The source of the jitter is usually high-frequency root-bone motion during animation blends.

## Where next

- [Transitions & Blending](../user-guide/transitions-and-blending.md) — author an `EnterTransition` on `CT_ThirdPersonFollow` so activation blends in rather than snaps.
- [Modifiers](../user-guide/concepts/modifiers.md) — add a sprint-FOV-bump modifier that targets `FieldOfViewNode` on this camera's tag set.
- [Cutscene Context](cutscene-context.md) — the next tutorial, which pushes a cutscene over this camera and blends back to it cleanly.
