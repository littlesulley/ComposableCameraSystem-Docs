---
title: Extending
---

# Extending the Plugin

The plugin ships with ~27 camera nodes, 9 transitions, and a modifier system, but gameplay needs are endless. When the shipped set doesn't cover your case, you extend — write your own node, transition, or modifier in C++. This section is the authoring guide.

## What to write, and when

| You want… | Write a… | Why |
|---|---|---|
| A per-frame camera operation (reads/writes the pose, consumes input, drives rotation, resolves collision) | [Custom Node](custom-nodes.md) | Nodes are the per-frame operators. If you're going to mutate the pose each frame, you want a node. |
| A new blend shape between two poses (a novel easing, a physics model, a context-aware blend) | [Custom Transition](custom-transitions.md) | Transitions are the pose-only blenders. If your feature is "how to get from pose A to pose B", it's a transition. |
| A runtime override that tweaks an existing node's parameters (gameplay-driven FOV bumps, AI aim damping, debug spectator lens changes) | [Custom Modifier](custom-modifiers.md) | Modifiers target a node class and mutate its parameters before evaluation — no new node required. |
| A temporary, self-expiring behavior that layers on top of (or underneath) the node chain (one-shot rotations, smooth moves, pitch resets) | [Custom Action](custom-actions.md) | Actions are fire-and-forget hooks with built-in lifetime management. They don't modify the node composition — they read/write the final pose. |

If you're unsure whether to write a node or a modifier, the rule of thumb is: *is this effect always part of this camera's behavior, or is it conditional?* Always-present → node. Conditional → modifier. If the effect is temporary and should expire on its own, it's probably an action.

Editor integration — authoring per-asset slate widgets, customizing the Details panel, adding K2 pins — is covered separately in [Editor Hooks](editor-hooks.md). Most extension work doesn't need it: the runtime already handles reflection-driven pin generation, subobject pin exposure, and standard property Details rendering for everything you throw at it.

## Prerequisites

You should be comfortable with:

- UE's reflection system (`UCLASS`, `USTRUCT`, `UPROPERTY`, `UFUNCTION`, their metadata specifiers).
- Instanced UObject subobjects and how `DefaultToInstanced` interacts with `EditInlineNew`.
- The plugin's three-module layout (`ComposableCameraSystem` runtime, `ComposableCameraSystemEditor`, `ComposableCameraSystemUncookedOnly`).

If you're extending the editor (slate widgets, K2 node customizations, graph schema rules), you should also be comfortable with `FAssetEditorToolkit`, `IDetailCustomization`, and UE's `UEdGraph` APIs.

## Where your code goes

Placement follows the runtime module's subfolder convention:

| Extension type | Header location | Source location |
|---|---|---|
| Custom camera node | `Source/ComposableCameraSystem/Public/Nodes/MyNode.h` | `Source/ComposableCameraSystem/Private/Nodes/MyNode.cpp` |
| Custom compute node | same folder, derives from `UComposableCameraComputeNodeBase` | same folder |
| Custom transition | `Source/ComposableCameraSystem/Public/Transitions/MyTransition.h` | `Source/ComposableCameraSystem/Private/Transitions/MyTransition.cpp` |
| Custom modifier | `Source/ComposableCameraSystem/Public/Modifiers/MyModifier.h` | `Source/ComposableCameraSystem/Private/Modifiers/MyModifier.cpp` |
| Custom action | `Source/ComposableCameraSystem/Public/Actions/MyAction.h` | `Source/ComposableCameraSystem/Private/Actions/MyAction.cpp` |

Do not scatter these into `Core/` or `Utils/`. The runtime reflection registration and the editor's palette / context menu both walk the whole `UComposableCameraCameraNodeBase` / `UComposableCameraTransitionBase` / `UComposableCameraModifierBase` hierarchies, so your new class will be picked up automatically once it's in the right folder and compiled.

## Hard rules

A few constraints carry over from the runtime architecture. Violate them at your own risk:

- **The evaluation hot path must not allocate.** Inside `OnTickNode`, `OnEvaluate`, or `ApplyModifier`, no `new`, no `TArray::Add`, no `TMap::Add`, no `FString` formatting, no `MakeShared`. Preallocate in `OnInitialize` / `OnBeginPlay`, reuse buffers.
- **`UPROPERTY`-ed object references must use `TObjectPtr<T>`.** Not raw `UObject*`.
- **Use the plugin's log categories.** `LogComposableCameraSystem` for runtime, `LogComposableCameraSystemEditor` for editor. Do not use `LogTemp`.

These rules apply to extensions exactly as they apply to shipped code.

## Reading the recipes

Each of the five recipes below is self-contained — you can jump directly to the relevant one:

- [Custom Nodes](custom-nodes.md) — the biggest recipe; covers reflection, pin schema, `OnInitialize` vs `OnTickNode`, subobject pin exposure, and node-vs-modifier decision guidance.
- [Custom Transitions](custom-transitions.md) — pose-only contract, four-phase lifecycle, velocity handling, testing in isolation, and a worked bounce-and-settle example.
- [Custom Modifiers](custom-modifiers.md) — blueprint-authored in most cases, but C++ modifiers make sense for performance-sensitive or cross-project reusable effects. Includes a sprint FOV walkthrough.
- [Custom Actions](custom-actions.md) — fire-and-forget behaviors with built-in lifetime management. Covers execution timing, expiration types, and a worked look-at-target example.
- [Editor Hooks](editor-hooks.md) — for when the default reflection-driven editor surface isn't enough.

Start with the one closest to what you want to build. The [Custom Nodes](custom-nodes.md) page is also the densest general reference — if you only read one, read that.
