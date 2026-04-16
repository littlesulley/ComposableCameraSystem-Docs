# Architecture Overview

Every frame, your player sees the output of one logical camera — a single pose (position, rotation, FOV, projection, physical-lens parameters) applied to the viewport. ComposableCameraSystem produces that pose by running a layered pipeline. This page walks the layers from outermost to innermost.

## The layered picture

```mermaid
flowchart TB
    subgraph PCM["<b>AComposableCameraPlayerCameraManager</b> — replaces APlayerCameraManager"]
        direction TB
        MM[ModifierManager]
        CA["Camera Actions (TSet)"]
        subgraph CS["<b>Context Stack</b> — Tier 1 · macro mode switching"]
            direction LR
            Base["[ Base ]"] --- Cut["[ Cutscene ]"] --- Top["[ Active&nbsp;(top) ]<br/><i>evaluated</i>"]
        end
        subgraph DIR["<b>Director</b> — one per context · owns the running camera"]
            direction TB
            subgraph ET["<b>Evaluation Tree</b> — Tier 2 · per-context blending"]
                direction TB
                Inner(["Inner: Transition"])
                Inner --> LeafA["Leaf: CamA<br/>(source)"]
                Inner --> LeafB["Leaf: CamB<br/>(target / running)"]
            end
        end
        CS -.->|"each entry owns"| DIR
    end
    classDef pcm fill:#eef3ff,stroke:#4a69bb,stroke-width:1.5px;
    classDef stack fill:#fff4e6,stroke:#d97706;
    classDef tree fill:#e8f7ee,stroke:#0e9f6e;
    class PCM pcm;
    class CS stack;
    class ET tree;
```

Read it top-down:

- **Player Camera Manager (PCM)** sits where Unreal's `APlayerCameraManager` would — it's a subclass (`AComposableCameraPlayerCameraManager`) that every interested PlayerController points at via `PlayerCameraManagerClass` (see [Enabling the Plugin](../../getting-started/enabling-plugin.md)). It owns everything below it and drives the per-frame loop.
- **Context Stack** is a LIFO stack of named contexts (`Gameplay`, `Cutscene`, `UI`, …). Only the top context is evaluated each frame. Pushing a new context suspends everything below without tearing it down. Context names are registered in `UComposableCameraProjectSettings::ContextNames`; the first entry is the base context and is initialized before any actor's `BeginPlay`. See [Context Stack](context-stack.md).
- **Director** is per-context. It owns an Evaluation Tree, tracks the currently-running camera, and remembers the last two evaluated poses — which transitions use for velocity calculations. See [Evaluation Tree](evaluation-tree.md).
- **Evaluation Tree** is a binary tree of leaves (wrapping a Camera) and inner nodes (wrapping a Transition). Leaves produce poses; inner nodes blend two poses into one. See [Evaluation Tree](evaluation-tree.md).
- **Camera** is an `AComposableCameraCameraBase` actor that owns an ordered array of Camera Nodes. It's data-driven: the actor is a container, not a subclass hierarchy. See [Authoring Camera Types](../authoring-camera-types.md).
- **Camera Node** is a single-responsibility operator. It reads the input pose, applies its logic, and writes an output pose. Nodes also talk to each other through a typed pin system routed by a flat `RuntimeDataBlock`. See [Node Catalog](../../reference/nodes.md).
- **Transition** is a pose-only blender. Each frame it receives two input poses (source and target) and outputs one blended pose. It never references the source/target cameras directly. See [Transitions](transitions.md).
- **Modifier** targets a specific *node class* and overrides its parameters at runtime. Highest priority wins; changes may trigger a seamless camera reactivation. See [Modifiers](modifiers.md).
- **Action** is a lightweight, fire-and-forget behavior that hooks into the camera's pre- or post-tick. Actions don't transform the pose through the node chain — they run alongside it, with built-in expiration (instant, duration, manual, or condition-based). Camera-scoped actions auto-expire on camera switch; persistent ones survive. See [Camera Actions](../camera-actions.md).

## What happens on one frame

Once per frame, `AComposableCameraPlayerCameraManager::DoUpdateCamera(DeltaTime)` drives this sequence:

```mermaid
flowchart TB
    Start(["<b>DoUpdateCamera</b>(DeltaTime)"])
    Start --> CSE["ContextStack · Evaluate"]
    CSE --> AP{"Transient&nbsp;&amp;&nbsp;finished?"}
    AP -- yes --> Pop["Auto-pop active context"]
    AP -- no  --> DE
    Pop --> DE["ActiveDirector · Evaluate"]
    DE --> ETE["EvaluationTree · Evaluate"]
    ETE --> Walk{"Recursive walk"}
    Walk --> Leaf["<b>Leaf</b><br/>Camera.TickCamera() → pose"]
    Walk --> Ref["<b>RefLeaf</b><br/>OtherDirector.Evaluate() → pose"]
    Walk --> In["<b>Inner</b><br/>blend(left, right) → pose"]
    Leaf --> Col["CollapseFinishedTransitions"]
    Ref  --> Col
    In   --> Col
    Col --> Upd["Update Last / Previous EvaluatedPose"]
    Upd --> Post["Update actions, running camera, current context"]
    Post --> Final["Convert pose → FMinimalViewInfo → viewport"]
```

The recursive tree walk is the heart of the system. A leaf produces a pose by ticking its camera (which itself walks its ordered node list). An inner node produces a pose by blending its two children. A reference leaf produces a pose by evaluating a different Director entirely — that's how a gameplay camera keeps animating live while a cutscene is blending in on top.

After the pose comes out, `CollapseFinishedTransitions` walks the tree one more time and promotes any inner node whose transition is done, so the tree stays small.

## Where each subsystem is explained

- The LIFO, push/pop semantics, auto-pop for transient cameras, and inter-context resume → [Context Stack](context-stack.md).
- Tree shape, activation rewrites, reference leaves, the collapse rule → [Evaluation Tree](evaluation-tree.md).
- Lifecycle (`TransitionEnabled → OnBeginPlay → OnEvaluate → OnFinished`), velocity-aware inertialization, the five-tier resolution chain → [Transitions](transitions.md).
- Priority-per-node-class, reactivation with transition, the difference from UE's built-in `UCameraModifier` → [Modifiers](modifiers.md).
- Temporary per-frame behaviors with built-in expiration, camera-scoped vs. persistent → [Actions](actions.md).
