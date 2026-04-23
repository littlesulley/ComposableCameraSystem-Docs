
# FComposableCameraDebugPanel { #fcomposablecameradebugpanel }

```cpp
#include <ComposableCameraDebugPanel.h>
```

Runtime in-viewport debug panel for the Composable Camera System.

Toggled via the `CCS.Debug.Panel 0|1` console variable. When enabled, paints a multi-region HUD overlay showing, from top to bottom:

1. Current Pose — position / rotation / FOV / aspect

1. Context Stack & Evaluation Tree

1. Running Camera — class, tag, lifetime, nodes, parameters, variables

1. Actions

1. Modifiers — count (phase 1)

Rendering goes through UDebugDrawService's "Game" channel with a static delegate registered at module startup. While disabled the draw function only performs a CVar read and early-outs, so there is no meaningful cost.

Data sources are the same public read-only accessors already used by [AComposableCameraPlayerCameraManager::DisplayDebug](../actors/AComposableCameraPlayerCameraManager.md#displaydebug) (showdebug camera). The existing showdebug path is preserved — this panel is additive.

Lifecycle is module-owned: [FComposableCameraSystemModule::StartupModule](FComposableCameraSystemModule.md#startupmodule) calls [Initialize()](#initialize-1); ShutdownModule calls [Shutdown()](#shutdown).

### Public Static Methods

| Return | Name | Description |
|--------|------|-------------|
| `void` | [`Initialize`](#initialize-1) `static` | Register the UDebugDrawService delegate. Idempotent. |
| `void` | [`Shutdown`](#shutdown) `static` | Unregister the UDebugDrawService delegate. Idempotent. |

---

#### Initialize { #initialize-1 }

`static`

```cpp
static void Initialize()
```

Register the UDebugDrawService delegate. Idempotent.

---

#### Shutdown { #shutdown }

`static`

```cpp
static void Shutdown()
```

Unregister the UDebugDrawService delegate. Idempotent.
