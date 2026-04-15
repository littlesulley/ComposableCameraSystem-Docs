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

## 3. Drop a FollowNode and a LookAtNode

The **Nodes** palette (left side) is grouped by category. For this camera we'll use two:

| Category | Node | What it does |
|---|---|---|
| Movement | **Follow Node** | Places the camera at a configurable offset behind / around a target actor. |
| Rotation | **Look At Node** | Rotates the camera to aim at a target point. |

1. Drag a **Follow Node** onto the canvas.
2. Connect the `FollowTarget` parameter to the Follow Node's **Target** pin.
3. Configure the Follow Node in the Details panel: set **Offset** to something like `(0, -400, 200)` for a standard over-the-shoulder view.
4. Drag a **Look At Node** onto the canvas, downstream of the Follow Node.
5. Connect `FollowTarget` to its **Target** pin as well.
6. Connect the Follow Node's **Pose Out** pin to the Look At Node's **Pose In** pin.
7. Connect the Look At Node's **Pose Out** pin to the **Camera Output** node.

Save the asset (Ctrl+S). The asset header should show a green checkmark; if it shows a red error, hover over it to read what's wrong — typically a missing pin connection or a parameter type mismatch.

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
- **Camera is at world origin, not behind the target** — the Follow Node's Target pin isn't wired, or the actor you're passing in is `None`. Print-string the target before the activation call.
- **Camera pops to the new position with no blend** — that's expected for a first activation. Blending is driven by **transitions**, which are covered in [Transitions & Blending](../user-guide/transitions-and-blending.md) in the User Guide.

## Where next

You now have the full end-to-end loop: plugin installed, PCM swapped, type asset authored, activated from Blueprint. Recommended next reads:

- **[Concepts](../user-guide/concepts/index.md)** — understand what the Context Stack, Director, and Evaluation Tree are actually doing during that `BeginPlay` call.
- **[Authoring Camera Types](../user-guide/authoring-camera-types.md)** — the full tour of the graph editor, parameters, variables, and subgraphs.
- **[Reference → Nodes](../reference/nodes.md)** — catalog of every shipped node, so you know what building blocks are available.
