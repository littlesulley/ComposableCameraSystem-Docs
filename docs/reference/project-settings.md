# Project Settings

`UComposableCameraProjectSettings` is the plugin's **project-wide configuration**. It lives under **Project Settings → Plugins → Composable Camera System** in the editor and is persisted into `DefaultGame.ini` in your project's `Config/` folder.

The class derives from `UDeveloperSettings` with `Config = Game, DefaultConfig` and ships with just two fields — but both are load-bearing: they drive transition resolution and the context name dropdown that appears throughout the system.

## Fields

| Field | Type | Purpose |
|---|---|---|
| `TransitionTable` | `TSoftObjectPtr<UComposableCameraTransitionTableDataAsset>` | Project-wide routing table consulted during transition resolution. |
| `ContextNames` | `TArray<FName>` | Declared context names that can be pushed on the [Context Stack](../user-guide/concepts/context-stack.md). **First entry is the base context.** |

Both fields are `Config, EditAnywhere, BlueprintReadOnly` — they can be edited in the details panel, they persist to `DefaultGame.ini`, and gameplay Blueprint can read them at runtime (but not write them).

## `TransitionTable` — the project-wide routing layer

The transition table is **tier 2** in the [five-tier resolution chain](../user-guide/transitions-and-blending.md#five-tier-resolution-chain-in-practice) — it sits between the target camera's defaults and any caller-supplied override. When a camera activation triggers a transition, the PCM consults the table (if set) for an entry matching the `(SourceTypeAsset, TargetTypeAsset)` pair before falling back to the target camera's `EnterTransition`.

Leaving `TransitionTable` unset is fine — the tier simply no-ops and resolution cascades to the target camera's per-field defaults. Most projects start without a table and introduce one later, once recurring `(Source, Target)` patterns emerge that would be tedious to override at every call site.

Because the field is a `TSoftObjectPtr`, the table asset is only loaded on first use, not at engine startup. That keeps the cost of having the field populated close to zero.

!!! note "One table per project"
    Only one transition table is consulted, and it's the one named here. If you need per-feature or per-map tables, you'll need to swap the asset out and back through a custom mechanism — the plugin does not support multiple simultaneously-active tables.

## `ContextNames` — declaring what can be pushed

The [Context Stack](../user-guide/concepts/context-stack.md) rejects any name that isn't in this list. This is a deliberate guardrail: context names are typed via `FName` and a typo at a call site would otherwise silently push a brand-new context nobody else knows about.

```
ContextNames:
  - Gameplay       ← first entry: the base context, always present
  - UI
  - Cutscene
  - LevelSequence
```

The list has two constraints:

1. **The first entry is the base context.** It is initialized automatically before any actor's `BeginPlay`, and it cannot be popped. By convention this is `Gameplay`, but the name itself is not special — whatever sits at index 0 is treated as the base.
2. **All names must be unique.** Duplicate entries are ignored silently; prefer to validate in the editor.

The static helper `GetContextNames()` exposes this list for editor UI — specifically, the `Context Name` pin on the `Activate Camera` node uses `meta=(GetOptions=...)` to show a dropdown sourced from this array, preventing typos at the Blueprint authoring site.

!!! warning "Changing context names is a schema change"
    Renaming an entry in `ContextNames` does **not** rename references in Blueprint graphs or C++ call sites. If you rename `Gameplay` → `World`, every BP node that activated into `Gameplay` will fail its runtime lookup until you update the pin value. Treat this list like an enum declaration: add freely, but rename with care.

### How context names are used at runtime

At runtime, the PCM's context stack does three things with this list:

- **At startup**, it creates the base context entry using `ContextNames[0]` and gives it a fresh [Director](../user-guide/concepts/evaluation-tree.md).
- **On `ActivateComposableCameraFromTypeAsset` with a `ContextName`**, it validates the name against `IsValidContextName` before calling `EnsureContext`. An invalid name logs a warning and the activation is rejected.
- **On `PopCameraContext(Name)`**, it similarly validates. The base context is never popped even if named explicitly.

See [Blueprint API → Context Control](../user-guide/blueprint-api.md#context-control) for the caller-side API.

## Editing the settings

In the editor:

1. **Edit → Project Settings**
2. Under **Plugins**, click **Composable Camera System**.
3. The two fields appear with inline property editors. `TransitionTable` shows a soft-object picker; `ContextNames` shows an array of `FName` text fields.
4. Changes are saved to `Config/DefaultGame.ini` under section `[/Script/ComposableCameraSystem.ComposableCameraProjectSettings]`.

You can also edit `DefaultGame.ini` directly — both fields accept the standard UE ini syntax:

```ini
[/Script/ComposableCameraSystem.ComposableCameraProjectSettings]
TransitionTable=/Game/ComposableCamera/CCS_TransitionTable.CCS_TransitionTable
+ContextNames=Gameplay
+ContextNames=UI
+ContextNames=Cutscene
+ContextNames=LevelSequence
```

The `+` syntax appends to the array. To clear it, use `!ContextNames=ClearArray` before the `+` entries.

## Access from code

From C++:

```cpp
#include "Utils/ComposableCameraProjectSettings.h"

const UComposableCameraProjectSettings* Settings =
    GetDefault<UComposableCameraProjectSettings>();

if (Settings->IsValidContextName(TEXT("Cutscene")))
{
    // Safe to push
}

const TSoftObjectPtr<UComposableCameraTransitionTableDataAsset>& TableRef =
    Settings->TransitionTable;
```

From Blueprint, the fields are `BlueprintReadOnly` — retrieve them through `Get Default Object` on `ComposableCameraProjectSettings` or expose a small helper function in your game module.

## See also

- [Context Stack](../user-guide/concepts/context-stack.md) — runtime model for context names and push/pop semantics
- [Transitions & Blending](../user-guide/transitions-and-blending.md) — where the transition table sits in the resolution chain
- [`UComposableCameraProjectSettings` C++ reference](api/data-assets/UComposableCameraProjectSettings.md) — auto-generated field docs
