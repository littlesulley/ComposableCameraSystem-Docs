---
title: Tutorials
---

# Tutorials

End-to-end walkthroughs that take a realistic goal and build it from an empty project slot. Each tutorial picks one concrete outcome, names the nodes or classes involved, and shows the full wiring — graph, Blueprint calls, and any C++ when required. The intent is to connect the vocabulary from the [Concepts](../user-guide/concepts/index.md) tour and the cataloged behavior from [Reference](../reference/index.md) into something that *runs*.

## Prerequisites

All three tutorials assume you've finished [Getting Started](../getting-started/index.md) — that is:

- The plugin is installed and compiled into a C++ project.
- `AComposableCameraPlayerCameraManager` is your `GameMode`'s PCM class (or your `PlayerController`'s override).
- `showdebug camera` prints the in-game overlay during PIE.

You do not need to have read the full User Guide. Each tutorial links back to the concepts it leans on so you can drill down as needed.

## The three walkthroughs

### [Follow Camera](follow-camera.md)

Build a classic third-person follow camera — pivot on the player, camera offset behind, stick-driven orbit, soft collision pushback. The output is a single camera type asset that you can drop onto any character and activate from Blueprint.

*Concepts covered:* pivot vs camera, reflection-driven parameters, `ControlRotateNode` input binding, `CollisionPushNode` tuning, activation from a K2 node.

*Time to complete:* 15–25 minutes.

### [Cutscene Context](cutscene-context.md)

Push a cutscene context during a scripted sequence, hand control to a cinematic camera, and blend cleanly back to gameplay on pop — with the gameplay camera *live* under the cutscene the whole time, so the blend back is seamless.

*Concepts covered:* [Context Stack](../user-guide/concepts/context-stack.md), [reference-based inter-context blending](../user-guide/concepts/evaluation-tree.md), transition resolution across a context pop, `Activate Camera` with a Context Name (implicit push), `TerminateCurrentCamera` / `PopCameraContext`.

*Time to complete:* 20–30 minutes.

### [Writing a Custom Transition](custom-transition.md)

Author a C++ transition that implements a specific blend shape (a bounce-and-settle curve), expose it to data assets, and drop it into the transition table for a specific `(Source, Target)` pair. Also covers unit-testing the transition without a PCM or a level.

*Concepts covered:* [Transitions](../user-guide/concepts/transitions.md) pose-only contract, [Custom Transitions](../extending/custom-transitions.md) authoring recipe, [five-tier resolution chain](../user-guide/concepts/transitions.md#the-five-tier-resolution-chain).

*Time to complete:* 30–45 minutes, plus IDE compile time.

---

## What's *not* a tutorial

Tutorials focus on realistic end-to-end flows. Three things that might *sound* like tutorials but live elsewhere:

- **A walkthrough of the graph editor UI.** That's [The Graph Editor](../user-guide/graph-editor.md) in the User Guide — a UI tour rather than a build-this-thing recipe.
- **Reference for every node's parameters.** That's the [Node Catalog](../reference/nodes.md) plus the per-class [C++ API Reference](../reference/api/index.md).
- **A deep dive on the Context Stack's implementation.** That's [Concepts → Context Stack](../user-guide/concepts/context-stack.md).

If a procedural question doesn't fit a tutorial or a concept page, it probably belongs in the [FAQ](../faq/index.md).
