# Your First Camera

By the end of this page you'll have:

- a **Camera Type Asset** — the data asset that defines a camera's behavior,
- a small **graph** inside it that makes the camera follow a target and look at it, and
- a **Blueprint call** that activates the camera at runtime.

It assumes you've finished [Enabling the Plugin](enabling-plugin.md) and that `showdebug composablecamera` prints an overlay in PIE.

!!! info "Heads up"
    The screenshots and graph editor details here describe the **dev-v1** iteration of the editor. The editor is still evolving; minor UI changes may be out of sync. File an issue on GitHub if anything is drastically different from what you see.

## 1. Create a Camera Type Asset

In the Content Browser:

1. Right-click an empty area → **Composable Camera → Camera Type Asset**.
2. Name it `CT_ThirdPersonFollow` (or whatever you like — the `CT_` prefix is a suggestion, not a requirement).
3. Double-click the asset to open the **Graph Editor**.

You'll see an empty graph canvas with a single output node on the right labeled **Camera Output**. This is where the camera's final pose comes from each frame.

## 2. Add a target input

A follow camera needs to know **who** to follow. ComposableCameraSystem exposes this via **parameters** on the type asset — these become pins on the Blueprint activation node.

1. In the **Parameters** panel (usually on the right), click **+ Add Parameter**.
2. Set its **Name** to `FollowTarget`.
3. Set its **Type** to `Actor Reference`.

The parameter now appears as a named node in the graph palette; drag it onto the canvas. This will drive downstream nodes.

## 3. Wire up the minimal node chain

For a minimal follow camera we need to answer three questions every frame: *what point is the camera tracking*, *where does the camera sit relative to that point*, and *where is the camera looking*. Three shipped nodes cover those one-to-one, plus a fourth to author the lens:

| Node | Role |
|---|---|
| **ReceivePivotActor** | Reads `FollowTarget`'s world position and publishes it as the pivot. |
| **CameraOffset** | Moves the camera to a fixed offset from the pivot. |
| **LookAt** | Rotates the camera to face `FollowTarget`. |
| **FieldOfView** | Authors the final lens FOV. |

1. Drag a **ReceivePivotActor** node onto the canvas. Wire the `FollowTarget` parameter into its **Actor** input.
2. Drop a **CameraOffset** node after it. In Details, set **OffsetSpace** to **Camera Space** and **Offset** to `(-400, 0, 100)` — 4m behind the pivot, slightly above. Wire the previous node's pose output into its pose input.
3. Drop a **LookAt** node next. Set **LookAtType** to **By Actor** and wire `FollowTarget` into its **TargetActor** pin. Set **ConstraintType** to **Hard** so the camera always tracks the target. Wire the previous pose into its input.
4. Drop a **FieldOfView** node. Set **FieldOfView** to `70`. Wire the previous pose into its input, and its output into the **Camera Output** node's **Pose** pin.

Save the asset (`Ctrl+S`). The asset header should show a green checkmark; if it shows a red error, hover over it to read what's wrong — typically a missing pin connection or a parameter type mismatch.

!!! tip "This is the bare minimum — real cameras do more"
    The [Follow Camera tutorial](../tutorials/follow-camera.md) expands this into a production-grade chain with pivot damping, stick-driven orbit input, rotation clamping, and collision pushback. Come back to it after you've got this minimal version running.

## 4. Activate the camera from a Blueprint

Open your player character or player controller Blueprint and find a convenient place — for example, the `BeginPlay` event.

1. Right-click the graph, search for **Activate Composable Camera**, and place the node.
2. The node has two *static* pins:
    - **Camera Type Asset** — set this to your new `CT_ThirdPersonFollow`.
    - **Player Index** — `0` for single-player.
3. Once the type asset is set, the node **rebuilds its pins** to match the parameters you defined. You'll see a new input pin named `Follow Target` (generated from your `FollowTarget` parameter). Wire your character actor (or `Get Player Pawn`) into it.
4. Connect the execution pin from `BeginPlay` into the node.

!!! note "Custom K2 node"
    `Activate Composable Camera` is a custom K2 node (`UK2Node_ActivateComposableCamera`). It introspects the selected type asset and builds matching pins for each exposed parameter. If you change the parameters on the type asset, right-click the K2 node and pick **Refresh Node** to pull in the updated pin list.

## 5. Play

Press **Play**. Your camera should snap to the configured offset behind the target and track it as it moves. If `showdebug composablecamera` is still active from the previous page, the overlay will show:

- Context Stack: `Gameplay`
- Active Camera: `CT_ThirdPersonFollow` (or whatever you named the instance)
- Evaluation Tree: a single leaf

## Common issues

- **"No camera is active" in the debug overlay** — the Activate node never ran. Common causes: `BeginPlay` fires before your follow target spawns (wire the node to a later event), or the PlayerController class in the GameMode doesn't use `AComposableCameraPlayerCameraManager` (revisit [Enabling the Plugin](enabling-plugin.md)).
- **Camera is at world origin, not behind the target** — the `ReceivePivotActor` node's **Actor** pin isn't wired, or the actor you're passing in is `None`. Print-string the target before the activation call.
- **Camera pops to the new position with no blend** — that's expected for a first activation. Blending is driven by **transitions**, which are covered in [Transitions & Blending](../user-guide/transitions-and-blending.md) in the User Guide.

## Where next

You now have the full end-to-end loop: plugin installed, PCM swapped, type asset authored, activated from Blueprint. Recommended next reads:

- **[Concepts](../user-guide/concepts/index.md)** — understand what the Context Stack, Director, and Evaluation Tree are actually doing during that `BeginPlay` call.
- **[Authoring Camera Types](../user-guide/authoring-camera-types.md)** — the full tour of the graph editor, parameters, variables, and subgraphs.
- **[Reference → Nodes](../reference/nodes.md)** — catalog of every shipped node, so you know what building blocks are available.
