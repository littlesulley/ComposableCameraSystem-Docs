# Editor Hooks

Most extension work does not need editor code. The runtime already handles reflection-driven pin generation, subobject pin exposure, and standard `UPROPERTY` rendering in the Details panel — which covers the overwhelming majority of cases. This page covers the remaining cases: when you genuinely need a custom Slate widget, a custom Details-panel row, or a graph-node tweak, and which hooks to use.

If you're writing your first extension, you probably don't need anything here. Skim the section titles and come back when you hit something the defaults can't express.

## When you actually need editor code

| Symptom | Solution |
|---|---|
| A node's parameter needs a richer editor than the default (a 2D curve picker, a visual range slider, a custom class picker with asset filtering) | `IPropertyTypeCustomization` for the USTRUCT, or `IDetailCustomization` for the owning class |
| A pin needs a custom inline editor widget (default value picker, constrained asset filter) | Subclass `SGraphPin` (or `SGraphPinObject` / `SGraphPinString` for typed pins) and register a factory |
| A graph node needs a per-asset slate widget in its body (a live preview, an inline button, a status indicator) | Override `SGraphNode::UpdateGraphNode` in a custom slate subclass, registered via `FGraphPanelNodeFactory` |
| A type asset needs editor-only actions (validate, reimport, migrate schema) | `UAssetDefinition` or `FAssetTypeActions_Base` with a context-menu entry |
| A Blueprint function library needs K2 node customization (dynamic pin counts, tooltip changes) | `UK2Node` subclass in the `UncookedOnly` module |

If your case isn't on this list, the reflection-driven defaults probably handle it. Try without customization first.

## Runtime ↔ editor separation — the module discipline

The plugin is three modules for a reason:

- `ComposableCameraSystem` — runtime. No editor-only includes. Ships in packaged builds.
- `ComposableCameraSystemEditor` — editor. Slate, detail customizations, asset tools, toolkits, graph nodes. Loaded as `Editor` in `.uplugin`.
- `ComposableCameraSystemUncookedOnly` — K2 nodes, editor-only helpers that must exist in PIE but not in shipping.

When adding a customization, **the customization code lives in `ComposableCameraSystemEditor`**, even if it targets a runtime class. Runtime code never `#include`s editor headers and never `DECLARE_MODULE_DEPENDENCY`s the editor module.

If a runtime class genuinely needs to expose something *to* the editor (a callback, a computed status), put the runtime side behind `#if WITH_EDITOR` and the editor-side consumer in the editor module. The plugin's `EditorHooks/` subfolder under the runtime module is the one place where these runtime-side editor hooks live.

## Detail customization — the common case

Most "I need a richer Details panel" situations resolve to one of:

**`IPropertyTypeCustomization`** — per-`USTRUCT` customization. Register in the editor module's `StartupModule`:

```cpp
FPropertyEditorModule& PropertyModule =
    FModuleManager::LoadModuleChecked<FPropertyEditorModule>("PropertyEditor");

PropertyModule.RegisterCustomPropertyTypeLayout(
    FComposableCameraRayFeeler::StaticStruct()->GetFName(),
    FOnGetPropertyTypeCustomizationInstance::CreateStatic(
        &FComposableCameraRayFeelerCustomization::MakeInstance));
```

Unregister in `ShutdownModule`. The customization implements `CustomizeHeader` (the collapsed single-row view) and `CustomizeChildren` (the expanded view).

**`IDetailCustomization`** — per-`UCLASS` customization. Use when you need to add/remove/reorder whole rows, not just tweak one property.

!!! warning "FStructureDetailsView skips root-level `IPropertyTypeCustomization`"
    The Data Table row editor uses `FStructureDetailsView`, which **does not** invoke `IPropertyTypeCustomization` at the root struct level. If your customization needs to work inside a DataTable row, wrap the struct in a sub-struct field and customize that sub-struct — or use `IDetailCustomization` on the containing UCLASS instead.

!!! warning "`IsEnabled(true)` narrows, `EditCondition(...)` overrides"
    `IDetailPropertyRow::IsEnabled(true)` only *narrows* existing edit conditions — it can't force-enable a row that inherits a disabling `meta = EditCondition`. To fully override, use `Row->EditCondition(TAttribute<bool>(true), FOnBooleanValueChanged());`

## Custom pin widgets — `SGraphPin` subclasses

The graph editor renders each pin via an `SGraphPin` widget. For typed pins (Object, String, Vector) there are specialized subclasses. To inject a custom pin widget — a class picker with asset filtering, a constrained combo box, a slider-for-scalar — subclass the appropriate one and register a factory.

```cpp
class FMyPinFactory : public FGraphPanelPinFactory
{
public:
    virtual TSharedPtr<SGraphPin> CreatePin(UEdGraphPin* Pin) const override
    {
        if (Pin->PinType.PinCategory == UEdGraphSchema_ComposableCamera::PC_MyType)
        {
            return SNew(SMyCustomPin, Pin);
        }
        return nullptr;
    }
};

// in StartupModule:
FEdGraphUtilities::RegisterVisualPinFactory(MakeShared<FMyPinFactory>());
```

!!! warning "`SGraphPinObject::OnShouldFilterAsset` is non-virtual"
    `SGraphPinObject` exposes `OnShouldFilterAsset` as a non-virtual bind-point, so overriding it in a subclass does not take effect. To install a custom asset filter on an object pin, override `GenerateAssetPicker` in your subclass and construct the picker with your filter hooked in — do not try to override `OnShouldFilterAsset`.

!!! warning "Default value widgets can't be rebuilt in place"
    `SGraphPin`'s default-value widget is constructed once during the pin's slate tree. If you need to swap the widget live (e.g. in response to a schema change on the connected pin), wrap it in a stable outer `SBox` container and call `SetContent` to swap — don't try to rebuild the `SGraphPin` subtree.

## Graph node customization

The plugin's camera graph uses custom `UEdGraphNode` subclasses with bespoke slate widgets. For 99% of extensions you do not touch these — the schema auto-generates pin widgets from `FComposableCameraNodePinDeclaration`. Touch them when:

- You need a preview widget in the node body (a mini 3D preview, a waveform, a color swatch).
- You need per-node actions in the header (a "reset to defaults" button, a pin-refresh button).
- You need a node-level status indicator (error state, warning, validation pass).

The pattern is `SGraphNode` subclass → `FGraphPanelNodeFactory` → register in `StartupModule`. Keep the widget focused; node bodies get dense fast.

## K2 node customization (UncookedOnly module)

If your runtime exposes a Blueprint-callable function library with *dynamic* behavior (pin count depends on an enum input, tooltip changes based on a wildcard type), write a `UK2Node` subclass in the `UncookedOnly` module. K2 nodes are editor-only at compile time but still exist during PIE, so they participate in BP compilation but not packaged builds.

The plugin does this sparingly — most BP integration uses plain `UFUNCTION(BlueprintCallable)` with good tooltips, which needs no K2 work.

## Asset actions

Custom right-click menu entries on a type asset, custom thumbnail rendering, custom factory behavior — all live in the editor module under `AssetTools/` and `Factories/`. Register in `StartupModule` via `IAssetTools::Get().RegisterAssetTypeActions(...)`. Unregister in `ShutdownModule`.

UE 5.6 offers both `FAssetTypeActions_Base` (older API) and `UAssetDefinition` (newer). For new work, prefer `UAssetDefinition` — it survives engine upgrades better.

## Undo/redo discipline

Any `UObject` you mutate in response to editor input must be `Modify()`-ed **before** the mutation, or Ctrl+Z will silently leave the object in its post-change state:

```cpp
Node->Modify();
Node->Offset = NewOffset;
// NotifyPostChange is handled by the Details panel for UPROPERTY edits.
```

This applies to custom slate widgets that mutate runtime objects directly — the Details panel handles `Modify()` for you on `UPROPERTY` edits, but custom widgets are on their own.

## Module API visibility

Out-of-line methods on `USTRUCT`s that are called across module boundaries (e.g. a helper defined in the runtime module but called from the editor module) must carry the module's `_API` macro:

```cpp
USTRUCT()
struct FComposableCameraSomething
{
    GENERATED_BODY()

    // Inline method — no API tag needed.
    int32 GetCount() const { return Count; }

    // Out-of-line method called from the editor module — API tag required.
    COMPOSABLECAMERASYSTEM_API void Recompute();
};
```

Without the tag you get `LNK2019` at link time when the editor module tries to resolve the symbol. Inline methods in the header don't need it.

## Gameplay-tags, category strings, and palette ordering

Node and transition classes are discovered via reflection walks, not via a central registry. The editor's palette groups them by `UCLASS(ClassGroup = ComposableCameraSystem)` and sub-categorizes by `meta = (Category = "Offset")` on the class or per-property. Use these consistently — a misspelled category creates a one-member group in the palette that's easy to miss.
