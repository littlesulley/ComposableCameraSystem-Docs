---
title: Tutorials
---

# Tutorials

End-to-end walkthroughs that take a realistic goal and build it from an empty project slot. Each tutorial picks one concrete outcome, names the nodes or classes involved, and shows the full wiring — graph, Blueprint calls, and any C++ when required. The intent is to connect the vocabulary from the [Concepts](../user-guide/concepts/index.md) tour and the cataloged behavior from [Reference](../reference/index.md) into something that *runs*.

## Prerequisites

All four tutorials assume you've finished [Getting Started](../getting-started/index.md) — that is:

- The plugin is installed and compiled into a C++ project.
- `AComposableCameraPlayerCameraManager` is your `GameMode`'s PCM class (or your `PlayerController`'s override).
- `showdebug camera` prints the in-game overlay during PIE.

You do not need to have read the full User Guide. Each tutorial links back to the concepts it leans on so you can drill down as needed.

## The four walkthroughs

### [Follow Camera](follow-camera.md)

Build a classic third-person follow camera — pivot on the player, camera offset behind, stick-driven orbit, soft collision pushback. The output is a single camera type asset that you can drop onto any character and activate from Blueprint.

*Concepts covered:* pivot vs camera, reflection-driven parameters, `ControlRotateNode` input binding, `CollisionPushNode` tuning, activation from a K2 node.

*Time to complete:* 15–25 minutes.

### [Cutscene Context](cutscene-context.md)

Push a cutscene context during a scripted sequence, hand control to a cinematic camera, and blend cleanly back to gameplay on pop — with the gameplay camera *live* under the cutscene the whole time, so the blend back is seamless.

*Concepts covered:* [Context Stack](../user-guide/concepts/context-stack.md), [reference-based inter-context blending](../user-guide/concepts/evaluation-tree.md), transition resolution across a context pop, `Activate Camera` with a Context Name (implicit push), `TerminateCurrentCamera` / `PopCameraContext`.

*Time to complete:* 20–30 minutes.

### [ADS / Aim Camera](ads-aim-camera.md)

Push an aim-down-sights context on right-click, blend into a tighter camera with lower FOV and slower sensitivity, pop back to the gameplay camera on release. A practical use of context pushing driven by held input rather than a trigger overlap.

*Concepts covered:* [Context Stack](../user-guide/concepts/context-stack.md), context push via held input, inertialized transition tuning, per-weapon modifier layering via camera tags.

*Time to complete:* 15–25 minutes.

### [Level Sequence Wrapper Camera](level-sequence-camera.md)

Wrap a ULevelSequence (Sequencer-authored camera animation) as a composable camera type using `KeyframeSequenceNode`. The sequence drives position, rotation, and optionally FOV, while the composable pipeline handles context pushing, transitions, and the return blend to gameplay.

*Concepts covered:* `KeyframeSequenceNode`, relative-to-actor playback, `StayAtLastFrameTime`, transient camera lifetime, post-sequence node chaining.

*Time to complete:* 20–30 minutes.

---

## What's *not* a tutorial

Tutorials focus on realistic end-to-end flows. A few things that might *sound* like tutorials but live elsewhere:

- **Authoring custom nodes, transitions, modifiers, and actions.** Those are extension recipes — see [Extending](../extending/index.md).
- **A walkthrough of the graph editor UI.** That's [The Graph Editor](../user-guide/graph-editor.md) in the User Guide — a UI tour rather than a build-this-thing recipe.
- **Reference for every node's parameters.** That's the [Node Catalog](../reference/nodes.md) plus the per-class [C++ API Reference](../reference/api/index.md).
- **A deep dive on the Context Stack's implementation.** That's [Concepts → Context Stack](../user-guide/concepts/context-stack.md).

If a procedural question doesn't fit a tutorial or a concept page, it probably belongs in the [FAQ](../faq/index.md).
