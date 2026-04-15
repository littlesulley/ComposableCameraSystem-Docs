# User Guide

The concepts section covered how the runtime thinks about cameras. This section is about how you actually get work done in the plugin day-to-day: authoring camera types, driving them from Blueprint, picking transitions, and working inside the graph editor.

A reasonable reading order:

1. **[Concepts](concepts/index.md)** — if you haven't read it yet, start here. Everything below assumes you know what a context, director, evaluation tree, and modifier are.
2. **[Authoring Camera Types](authoring-camera-types.md)** — creating type assets, placing nodes, wiring pins, exposing parameters, declaring variables.
3. **[The Graph Editor](graph-editor.md)** — the UI tour. Palette, pin colors, exec chains, Details panel, build pane, undo/redo.
4. **[Blueprint API](blueprint-api.md)** — activating cameras from BP, adding and removing modifiers, DataTable-driven activation.
5. **[Transitions & Blending](transitions-and-blending.md)** — picking the right transition, the five-tier resolution chain in practice, authoring the transition table.

None of the pages require Blueprint or C++ expertise beyond what any UE 5 project would expect — if you can place and wire a Blueprint node, you can author a camera. The C++ side is relevant mainly if you plan to ship [custom nodes](../extending/custom-nodes.md) or [custom transitions](../extending/custom-transitions.md) of your own.
