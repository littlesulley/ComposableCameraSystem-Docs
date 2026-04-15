# Concepts

This section explains **how ComposableCameraSystem works** — enough that you can predict what will happen when you activate a camera, push a cutscene context, add a modifier, or wire up a transition. It is not a walkthrough of the editor (that's [Authoring Camera Types](../authoring-camera-types.md)) and it is not a catalog of shipped nodes (that's [Reference](../../reference/index.md)).

## Read these pages in order

1. **[Architecture Overview](overview.md)** — the full pipeline in one picture. Start here.
2. **[Context Stack](context-stack.md)** — Tier 1. Macro-level mode switching: gameplay vs cutscene vs UI.
3. **[Evaluation Tree](evaluation-tree.md)** — Tier 2. Per-context camera blending, frame by frame.
4. **[Transitions](transitions.md)** — pose-only blenders, and the five-tier resolution chain that decides which transition runs between any two cameras.
5. **[Modifiers](modifiers.md)** — post-evaluation tweaks and runtime re-tuning of nodes.

## The two ideas to internalize

If you skim nothing else, hold onto these two:

**Composition, not inheritance.** A camera is a lightweight actor that owns an ordered list of nodes. A "third-person follow camera" is not a subclass — it's a particular composition of `ReceivePivotActorNode → PivotOffsetNode → CameraOffsetNode → ControlRotateNode → CollisionPushNode → LookAtNode → FieldOfViewNode`. New behaviors come from combining nodes, not writing new camera classes. The camera base class is deliberately marked `NotBlueprintable` to enforce this.

**Two tiers, cleanly separated.** Tier 1 (the **Context Stack**) decides *which mode we're in*. Tier 2 (the **Evaluation Tree**) decides *how two cameras inside that mode blend into one pose*. Pushing a cutscene context does not kill the gameplay camera — it suspends it. Popping the cutscene resumes gameplay. Transitions live entirely at Tier 2 and never reference cameras directly, so the same transition type works whether you're switching cameras within a context or crossing a context boundary.

Keep these two ideas in mind as you read the rest.
