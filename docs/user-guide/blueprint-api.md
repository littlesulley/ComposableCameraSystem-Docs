# Blueprint API

Everything you can do at runtime — activate cameras, push and pop contexts, switch between type assets, add and remove modifiers, manage actions, set variable values from gameplay — is reachable from Blueprint. Most of it goes through either the custom **Activate Composable Camera** K2 node or through `UComposableCameraBlueprintLibrary`.

## Activate Composable Camera (K2 node)

This is the primary way gameplay code starts a camera. Right-click in any Blueprint graph and search **Activate Composable Camera** — the node is registered under *ComposableCameraSystem*.

### Pin layout

The node has a fixed set of always-visible pins:

| Pin | Type | Purpose |
|---|---|---|
| *Exec in / out* | — | Standard flow-of-control |
| **Player Index** | `int32` | Which player the camera belongs to (default `0`) |
| **Camera Type** | `UComposableCameraTypeAsset*` | The type asset to activate — asset picker |
| **Context Name** | `FName` | Which context to activate into; dropdown sourced from project settings. Leave empty for the current top context |
| **Transition Override** | `UComposableCameraTransitionDataAsset*` | Optional — wins over every other transition tier |
| **Activation Params** | `FComposableCameraActivationParams` | Struct covering pose preservation, transient-ness, lifetime |
| **Return Value** | `AComposableCameraCameraBase*` | The activated camera actor |

Below those, the node generates **dynamic pins** based on the selected Camera Type Asset.

### Dynamic pins — opt-in, not "show everything"

The dynamic-pin set works on an *opt-in* model:

- **Required exposed parameters** (`bRequired == true` on the asset) are always present. You cannot remove them — missing a required parameter is a fatal activation error.
- **Non-required parameters and exposed variables** are hidden by default. You opt in per-name via the node's right-click context menu → **Add Override Pin → {name}**. Each opted-in pin appears under an *Overrides* advanced-pin section.

This means a camera type with 15 exposed knobs doesn't spam your Blueprint graph with 15 pins. You surface only the ones you actually want to set; the rest fall back to the asset's authored default.

Opted-in pins can be removed at any time via right-click on the pin → **Remove Override Pin**. Required pins don't offer that option.

### Pin value resolution at activation

For each dynamic pin, the K2 node's compiled output reads the pin's current value (connected wire or unconnected default), writes it into the `FComposableCameraParameterBlock`, and passes the block to the runtime. The runtime then walks `ExposedParameters` → `InternalVariables` → `ExposedVariables` in order and applies each value to the right slot.

Anything the author didn't opt in and didn't override is absent from the block — the runtime sees "no value for `FieldOfView`" and falls back to the type asset's `DefaultValueString` (for exposed parameters) or `InitialValueString` (for exposed variables). Nothing extra is required on the K2 node or at the call site.

### Auto-refresh when the asset changes

If you edit the underlying type asset (add a new exposed parameter, flip one to required, rename an entry) while the Blueprint that references it is open, the K2 node reconstructs itself live — subscribing to `OnObjectPropertyChanged` keeps the node's pin set in sync with the asset without needing to reopen the Blueprint. Orphans (override names that no longer exist on the asset) are automatically removed during refresh.

## Activate from DataTable

For data-driven camera configuration — AI selection tables, preset-driven cinematic triggers, designer-tunable camera libraries without Blueprint edits — the plugin ships a second K2 node: **Activate Composable Camera From Data Table**.

Each DataTable row is a `FComposableCameraParameterTableRow` carrying:

- `CameraType` — soft reference to the type asset to activate.
- `ContextName` — which context to push into (or `NAME_None` for the current top).
- `TransitionOverride` — optional `UComposableCameraTransitionDataAsset`.
- `ActivationParams` — pose preservation, transient flag, lifetime.
- `ParameterValues` — a `TMap<FName, FString>` of serialized values covering both exposed parameters and exposed variables, using each field's own default (`DefaultValueString` / `InitialValueString`) as the row-omission fallback.

The K2 node takes a DataTable and a row name (both driven by specialized pin widgets — the DataTable picker filters to row structs of type `FComposableCameraParameterTableRow`, and the row-name pin refreshes live as you edit the selected DataTable). At compile, it calls through to `ActivateComposableCameraFromDataTable` on the library.

Designers can edit rows inline in the DataTable editor with a typed per-parameter UI — each row renders with typed value widgets for every exposed parameter *and* every exposed variable of the selected camera type, so you get numeric spinners, vector field rows, checkboxes, and struct detail views rather than a raw string map.

## Blueprint function library

`UComposableCameraBlueprintLibrary` collects the rest of the runtime API. All functions are `static` with a `WorldContextObject` parameter — callable from anywhere you have a world context (Actor, Component, GameMode, etc.).

### Context control

| Function | Purpose |
|---|---|
| `TerminateCurrentCamera(WorldContextObject, PlayerIndex, TransitionOverride)` | Pops the active top context back to whatever's below it, transitioning out. The base `Gameplay` context is protected — this is a no-op if the top is already the base. |
| `PopCameraContext(WorldContextObject, PlayerIndex, ContextName)` | Immediately pops a specific named context — with no transition, since it wasn't the active one. Useful for cancelling a non-top context (e.g. "forget the Aim stack we pushed earlier"). |

### Modifiers

| Function | Purpose |
|---|---|
| `AddModifier(WorldContextObject, PlayerIndex, Modifier)` | Adds a `UComposableCameraModifierBase` instance (or `UComposableCameraNodeModifierDataAsset` wrapping one) to the PCM's modifier manager. If the running camera has a node matching the modifier's `NodeClass`, a seamless reactivation blends into the modified camera. |
| `RemoveModifier(WorldContextObject, PlayerIndex, Modifier)` | Removes a previously-added modifier. Reactivation blends back out. |

Modifiers target a node class — see [Concepts → Modifiers](concepts/modifiers.md) for the full semantics.

### Actions

| Function | Purpose |
|---|---|
| `AddAction(WorldContextObject, PlayerIndex, Action)` | Attaches a `UComposableCameraActionBase` to the PCM. Actions receive `OnPreTick` / `OnPostTick` callbacks and can drive the pose directly. |
| `ExpireAction(WorldContextObject, PlayerIndex, Action)` | Removes a persistent action. Camera-scoped actions (`bOnlyForCurrentCamera`) expire automatically on camera switch — no manual removal needed. |

Built-in actions include `MoveToAction` (smooth move to target position), `RotateToAction` (smooth rotate), and `ResetPitchAction` (snap pitch to zero).

### Variable access

| Function | Purpose |
|---|---|
| `SetComposableCameraVariableRuntimeValue(WorldContextObject, PlayerIndex, VariableName, Value)` | Writes a value into the running camera's variable slot. Uses a custom thunk so the `Value` pin is typed to match the variable. |
| `GetComposableCameraVariableRuntimeValue(WorldContextObject, PlayerIndex, VariableName)` | Reads a variable's current value, returning it as the typed output. |

Both operate on the currently-running camera. For inter-context state, reads and writes go to whichever context is currently on top.

### Context name dropdowns

Every `FName` parameter that expects a context name (`Activate Composable Camera`'s **Context Name** pin, `PopCameraContext`'s name parameter, etc.) carries `meta=(GetContextNames)` — Blueprint's dropdown is sourced live from **Project Settings → ComposableCameraSystem → Context Names**. Adding a new context in project settings makes it available in the dropdown without recompiling anything.

## Typical patterns

### Activate a gameplay camera on `BeginPlay`

```
Event BeginPlay
  └─> Activate Composable Camera
        Player Index: 0
        Camera Type:  CT_ThirdPersonFollow
        Context Name: Gameplay       (default — also the base context)
        Pivot Actor:  Self (this character)
```

Because `Gameplay` is the base context and is initialized by the PCM in `InitializeFor` (before any actor's `BeginPlay`), it's always safe to activate into it on `BeginPlay`.

### Push a cinematic

```
On Trigger Entered
  └─> Activate Composable Camera
        Camera Type:  CT_Cinematic_HeroIntro
        Context Name: Cutscene          (a declared context)
        Transition Override: None
```

Because `Cutscene` wasn't on the stack before, the PCM pushes it. The previous `Gameplay` camera is suspended but not destroyed — when the cutscene ends and you call `TerminateCurrentCamera`, the stack pops back to `Gameplay` and the previous camera resumes with whatever transition the [five-tier resolution](transitions-and-blending.md#five-tier-resolution-chain-in-practice) picks for the pop.

### Sprint FOV modifier

```
On Sprint Started
  └─> Add Modifier (Modifier: DA_SprintFOVModifier)

On Sprint Ended
  └─> Remove Modifier (Modifier: DA_SprintFOVModifier)
```

The modifier data asset wraps a `UComposableCameraModifierBase` whose `NodeClass` is `FieldOfViewNode` and whose `ApplyModifier` adds +10° to the node's `FieldOfView` parameter. Adding and removing it triggers a seamless reactivation, so the FOV change blends in and out at whatever transition the camera's `EnterTransition` specifies.

## Calling from C++

All the library functions are also usable from C++. For gameplay-facing activation, the recommended entry point is still the type-asset path:

```cpp
#include "ComposableCamera/Public/Blueprint/ComposableCameraBlueprintLibrary.h"

UComposableCameraBlueprintLibrary::AddModifier(this, /*PlayerIndex*/ 0, MyModifier);
```

For more direct access — internal subsystems like the `MixingCameraNode` that need to spawn auxiliary cameras — the PCM still exposes `CreateNewCamera` / `ActivateNewCamera` as C++-only entry points. These are **not** recommended for gameplay code; they bypass the type asset layer and the parameter block, which means you're responsible for per-node initialization yourself.

Most gameplay code should never reach below the library — the type-asset pipeline is the supported surface.
