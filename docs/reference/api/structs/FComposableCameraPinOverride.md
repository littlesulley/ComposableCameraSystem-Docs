
# FComposableCameraPinOverride { #fcomposablecamerapinoverride }

```cpp
#include <ComposableCameraNodePinTypes.h>
```

Per-asset authoring override for a single pin declared by a camera node class.

Pin declarations come from C++ (GetPinDeclarations) and define the *shape* of a node's interface — names, types, directions, required flags, C++-level default values. But the authoring experience demands two things the class-level decl can't express per-instance:

1. A **user-editable default value** for inputs that are not driven by a wire. Two instances of the same node class in the same camera type asset should be able to carry different default strengths / offsets / etc.

1. A **per-instance toggle** for whether a pin should be exposed as a wire in the graph at all. When bAsPin is false, the pin is Details-only (a constant set once, at author time) and does not appear on the graph node. When true, the pin renders on the graph node and can be wired or exposed as an ExposedParameter.

Overrides are stored per-(node-instance, pin-name). Pins that never get an override use the C++ declaration's defaults for both fields (bAsPin = true, DefaultValueString = the class-level default). Storing overrides as a sparse array indexed by PinName means adding a new pin declaration in C++ doesn't require any asset migration — the new pin simply defaults to (visible, class default).

The source of truth lives on [UComposableCameraTypeAsset::NodePinOverrides](../data-assets/UComposableCameraTypeAsset.md#nodepinoverrides) (parallel array to NodeTemplates). The editor graph node also caches the overrides in a Transient field for fast read during AllocateDefaultPins / Details customization; the round-trip is handled in the same sync/rebuild phases that handle ExposedParameters.

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `FName` | [`PinName`](#pinname-1)  | Which declared pin this override applies to. Matches [FComposableCameraNodePinDeclaration::PinName](FComposableCameraNodePinDeclaration.md#pinname-3) on the node class. |
| `bool` | [`bAsPin`](#baspin)  | Whether this pin is exposed as a wire on the graph node. When false, the pin is Details-only and does not appear on the graph — it cannot be wired, and it cannot be exposed as a camera parameter. The Details panel still shows the editable default value, which is used directly as the constant input at runtime. |
| `bool` | [`bHasDefaultOverride`](#bhasdefaultoverride)  | True when DefaultValueOverride below should be used in place of the C++ declaration's class-level default. A separate flag (rather than sniffing "DefaultValueOverride is empty") is required to distinguish "user |
| `FString` | [`DefaultValueOverride`](#defaultvalueoverride)  | Per-asset override of the pin's default value. Serialized as a string in the same format as [FComposableCameraNodePinDeclaration::DefaultValueString](FComposableCameraNodePinDeclaration.md#defaultvaluestring), so the same parser can be used at runtime. Ignored when bHasDefaultOverride is false. |

---

#### PinName { #pinname-1 }

```cpp
FName PinName
```

Which declared pin this override applies to. Matches [FComposableCameraNodePinDeclaration::PinName](FComposableCameraNodePinDeclaration.md#pinname-3) on the node class.

---

#### bAsPin { #baspin }

```cpp
bool bAsPin = true
```

Whether this pin is exposed as a wire on the graph node. When false, the pin is Details-only and does not appear on the graph — it cannot be wired, and it cannot be exposed as a camera parameter. The Details panel still shows the editable default value, which is used directly as the constant input at runtime.

Invariant: toggling bAsPin from true to false on a pin that is currently wired must break the wire (transactional / undoable), and on a pin that is currently exposed as a camera parameter must also auto-unexpose it. See ExposePinAsParameter / UnexposePinParameter for the exposure side.

---

#### bHasDefaultOverride { #bhasdefaultoverride }

```cpp
bool bHasDefaultOverride = false
```

True when DefaultValueOverride below should be used in place of the C++ declaration's class-level default. A separate flag (rather than sniffing "DefaultValueOverride is empty") is required to distinguish "user
deliberately set an empty string" from "user never touched this pin".

---

#### DefaultValueOverride { #defaultvalueoverride }

```cpp
FString DefaultValueOverride
```

Per-asset override of the pin's default value. Serialized as a string in the same format as [FComposableCameraNodePinDeclaration::DefaultValueString](FComposableCameraNodePinDeclaration.md#defaultvaluestring), so the same parser can be used at runtime. Ignored when bHasDefaultOverride is false.
