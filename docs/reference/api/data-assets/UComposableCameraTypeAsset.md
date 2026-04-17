
# UComposableCameraTypeAsset { #ucomposablecameratypeasset }

```cpp
#include <ComposableCameraTypeAsset.h>
```

> **Inherits:** `UPrimaryDataAsset`

Data asset defining a camera type: node composition, exposed parameters, internal variables, pin connections, and default transition.

Replaces the need to create Blueprint subclasses of [AComposableCameraCameraBase](../actors/AComposableCameraCameraBase.md#acomposablecameracamerabase) for most camera types. Designers create and configure camera types entirely within the visual node graph editor.

At runtime, Instantiate() creates an [AComposableCameraCameraBase](../actors/AComposableCameraCameraBase.md#acomposablecameracamerabase) with node instances duplicated from the templates, a wired RuntimeDataBlock, and caller-provided parameter values.

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `TArray< TObjectPtr< UComposableCameraCameraNodeBase > >` | [`NodeTemplates`](#nodetemplates)  | Flat list of node template UObjects owned by this asset. |
| `TArray< FComposableCameraNodeTemplatePinOverrides >` | [`NodePinOverrides`](#nodepinoverrides)  | Per-asset authoring overrides for the pins on each node template. |
| `TArray< TObjectPtr< UComposableCameraComputeNodeBase > >` | [`ComputeNodeTemplates`](#computenodetemplates)  | Flat list of compute node templates authored on this type asset. Hidden from Details for the same reason NodeTemplates is — the visual graph editor is the authoritative editing surface. |
| `TArray< FComposableCameraNodeTemplatePinOverrides >` | [`ComputeNodePinOverrides`](#computenodepinoverrides)  | Per-asset authoring overrides for the pins on each compute node template. Parallel array to ComputeNodeTemplates; same semantics as NodePinOverrides. Invariant: after any successful SyncToTypeAsset, ComputeNodePinOverrides.Num() == ComputeNodeTemplates.Num(). |
| `TArray< FComposableCameraPinConnection >` | [`ComputePinConnections`](#computepinconnections)  | Intra-compute-chain data wires. Same struct as PinConnections but the Source/Target node indices refer to ComputeNodeTemplates rather than NodeTemplates. Cross-chain data wires are disallowed by the schema, so this array never contains camera-node endpoints. |
| `TArray< int32 >` | [`ComputeExecutionOrder`](#computeexecutionorder)  | Ordered list of compute node indices defining the BeginPlay execution chain, filtered to compute nodes only. This is a compute-node-only projection of ComputeFullExecChain (analogous to how ExecutionOrder is a camera-node-only projection of FullExecChain). Kept for backward compat with code paths that only care about node ordering. |
| `TArray< FComposableCameraExecEntry >` | [`ComputeFullExecChain`](#computefullexecchain)  | Full BeginPlay execution chain including both compute nodes and internal-variable Set operations, in exec-wire order. Parallel to FullExecChain but for the compute chain. |
| `FGameplayTag` | [`CameraTag`](#cameratag)  | Tag for this camera type. Propagated to spawned camera instances so modifiers can distinguish different cameras at runtime. Mirrors [AComposableCameraCameraBase::CameraTag](../actors/AComposableCameraCameraBase.md#cameratag-1) — the TypeAsset carries it so designers don't need to subclass the camera in Blueprint just to set a tag. |
| `bool` | [`bDefaultPreserveCameraPose`](#bdefaultpreservecamerapose)  | Whether cameras of this type preserve the previous camera's pose when resumed from the context stack (e.g., after a transient camera pops). Propagated to spawned camera instances. Mirrors [AComposableCameraCameraBase::bDefaultPreserveCameraPose](../actors/AComposableCameraCameraBase.md#bdefaultpreservecamerapose-1). |
| `TObjectPtr< UComposableCameraTransitionBase >` | [`EnterTransition`](#entertransition)  | Optional enter transition — used when this camera type becomes active. The full resolution chain is: |
| `TObjectPtr< UComposableCameraTransitionBase >` | [`ExitTransition`](#exittransition)  | Optional exit transition — used when leaving this camera type. Checked at priority 3 in the resolution chain (after the table, before the target's EnterTransition). Useful for cameras that must always leave with a specific transition regardless of what comes next (e.g., puzzle cameras, UI overlays). |
| `TArray< FComposableCameraExposedParameter >` | [`ExposedParameters`](#exposedparameters)  | Parameters that callers provide when activating this camera type. |
| `TArray< FComposableCameraInternalVariable >` | [`InternalVariables`](#internalvariables)  | Camera-level variables not exposed to callers but readable/writable by nodes. Used for cross-node communication and cross-frame state caching. |
| `TArray< FComposableCameraInternalVariable >` | [`ExposedVariables`](#exposedvariables)  | Camera-level variables whose initial value may be overridden by the caller at activation time, but which are otherwise identical to internal variables. |
| `TArray< FComposableCameraPinConnection >` | [`PinConnections`](#pinconnections)  | Describes all data-pin connections between nodes. Each entry maps a target node's input pin to a source node's output pin. |
| `TArray< int32 >` | [`ExecutionOrder`](#executionorder)  | Ordered list of node indices defining the execution chain, filtered down to camera nodes only. |
| `TArray< FComposableCameraExecEntry >` | [`FullExecChain`](#fullexecchain)  | Full execution chain including both camera nodes and internal-variable Set operations, in exec-wire order. |
| `TArray< FComposableCameraVariableNodeRecord >` | [`VariableNodes`](#variablenodes)  | Editor-only records describing each Get/Set variable graph node in the visual editor, along with the camera-node pins each one is wired to. The runtime doesn't consume these directly; they exist so the editor can round-trip the variable-node layout and wires. |

---

#### NodeTemplates { #nodetemplates }

```cpp
TArray< TObjectPtr< UComposableCameraCameraNodeBase > > NodeTemplates
```

Flat list of node template UObjects owned by this asset.

This array is intentionally **hidden from the Details panel** — the visual node graph editor is the authoritative editing surface for camera nodes, and showing a separate "NodeTemplates" array in Details would tempt users into thinking its order has semantic meaning. It does not: execution order comes from the exec-pin wiring chain (see FullExecChain / ExecutionOrder), not from this array's order. The array exists purely as a GC anchor and serialization container for the instanced node UObjects.

UPROPERTY has no EditAnywhere / Category keywords on purpose — the field is still serialized (bare UPROPERTY) and Instanced (so subobjects round-trip), but invisible to IDetailCustomization panels. Editor code accesses this array directly through SyncToTypeAsset / RebuildFromTypeAsset.

---

#### NodePinOverrides { #nodepinoverrides }

```cpp
TArray< FComposableCameraNodeTemplatePinOverrides > NodePinOverrides
```

Per-asset authoring overrides for the pins on each node template.

Parallel array to NodeTemplates: NodePinOverrides[i] holds the sparse list of per-pin overrides for NodeTemplates[i]. Entries store the user-edited default value and the bAsPin toggle for a specific (node instance, pin name) pair; pins without an entry inherit their class-level declaration defaults (bAsPin = true, DefaultValueString).

Invariant: after any successful SyncToTypeAsset, NodePinOverrides.Num() == NodeTemplates.Num(). Legacy assets saved before this field existed start with an empty array; the first sync after load grows it to match.

Hidden from the Details panel for the same reason NodeTemplates is — the visual graph (+ its per-node Details customization) is the authoritative editing surface. Editor code accesses this array directly through the Sync/Rebuild phases and through the graph node's accessor helpers.

---

#### ComputeNodeTemplates { #computenodetemplates }

```cpp
TArray< TObjectPtr< UComposableCameraComputeNodeBase > > ComputeNodeTemplates
```

Flat list of compute node templates authored on this type asset. Hidden from Details for the same reason NodeTemplates is — the visual graph editor is the authoritative editing surface.

---

#### ComputeNodePinOverrides { #computenodepinoverrides }

```cpp
TArray< FComposableCameraNodeTemplatePinOverrides > ComputeNodePinOverrides
```

Per-asset authoring overrides for the pins on each compute node template. Parallel array to ComputeNodeTemplates; same semantics as NodePinOverrides. Invariant: after any successful SyncToTypeAsset, ComputeNodePinOverrides.Num() == ComputeNodeTemplates.Num().

---

#### ComputePinConnections { #computepinconnections }

```cpp
TArray< FComposableCameraPinConnection > ComputePinConnections
```

Intra-compute-chain data wires. Same struct as PinConnections but the Source/Target node indices refer to ComputeNodeTemplates rather than NodeTemplates. Cross-chain data wires are disallowed by the schema, so this array never contains camera-node endpoints.

---

#### ComputeExecutionOrder { #computeexecutionorder }

```cpp
TArray< int32 > ComputeExecutionOrder
```

Ordered list of compute node indices defining the BeginPlay execution chain, filtered to compute nodes only. This is a compute-node-only projection of ComputeFullExecChain (analogous to how ExecutionOrder is a camera-node-only projection of FullExecChain). Kept for backward compat with code paths that only care about node ordering.

---

#### ComputeFullExecChain { #computefullexecchain }

```cpp
TArray< FComposableCameraExecEntry > ComputeFullExecChain
```

Full BeginPlay execution chain including both compute nodes and internal-variable Set operations, in exec-wire order. Parallel to FullExecChain but for the compute chain.

The editor walks the exec pin chain starting from the BeginPlay Start sentinel's ExecOut and records each step here. For CameraNode entries, CameraNodeIndex indexes into ComputeNodeTemplates (not NodeTemplates). For SetVariable entries, CameraNodeIndex also indexes ComputeNodeTemplates — the source node is always on the same chain.

The runtime copies this to [AComposableCameraCameraBase::ComputeFullExecChain](../actors/AComposableCameraCameraBase.md#computefullexecchain-1) during OnTypeAssetCameraConstructed. BeginPlayCamera walks it to interleave compute node execution with scratch-variable writes.

---

#### CameraTag { #cameratag }

```cpp
FGameplayTag CameraTag
```

Tag for this camera type. Propagated to spawned camera instances so modifiers can distinguish different cameras at runtime. Mirrors [AComposableCameraCameraBase::CameraTag](../actors/AComposableCameraCameraBase.md#cameratag-1) — the TypeAsset carries it so designers don't need to subclass the camera in Blueprint just to set a tag.

---

#### bDefaultPreserveCameraPose { #bdefaultpreservecamerapose }

```cpp
bool bDefaultPreserveCameraPose = true
```

Whether cameras of this type preserve the previous camera's pose when resumed from the context stack (e.g., after a transient camera pops). Propagated to spawned camera instances. Mirrors [AComposableCameraCameraBase::bDefaultPreserveCameraPose](../actors/AComposableCameraCameraBase.md#bdefaultpreservecamerapose-1).

---

#### EnterTransition { #entertransition }

```cpp
TObjectPtr< UComposableCameraTransitionBase > EnterTransition
```

Optional enter transition — used when this camera type becomes active. The full resolution chain is:

1. Caller-supplied override

1. Transition table lookup (Source → Target pair)

1. Source's ExitTransition

1. Target's EnterTransition ← this field

1. Hard cut Callers can always override via the activation API.

---

#### ExitTransition { #exittransition }

```cpp
TObjectPtr< UComposableCameraTransitionBase > ExitTransition
```

Optional exit transition — used when leaving this camera type. Checked at priority 3 in the resolution chain (after the table, before the target's EnterTransition). Useful for cameras that must always leave with a specific transition regardless of what comes next (e.g., puzzle cameras, UI overlays).

---

#### ExposedParameters { #exposedparameters }

```cpp
TArray< FComposableCameraExposedParameter > ExposedParameters
```

Parameters that callers provide when activating this camera type.

Authoring model — split between graph and Details panel:

* **Structure** (which pins are exposed) is authored **exclusively** through the visual graph editor: designers right-click a node input pin and select "Expose as Camera Parameter" (or "Unexpose"). The array is `EditFixedSize`, so the Details panel does not offer Add/Remove buttons — adding a free-standing entry that doesn't map to any node pin would have no runtime meaning, and removing one from Details would silently leave the underlying pin in an "orphaned-exposed" state on the graph side.

* **Per-parameter metadata** (DisplayName, bRequired, Tooltip) IS editable on existing entries from the Details panel. The first time a pin is exposed, these fields are seeded from the C++ [FComposableCameraNodePinDeclaration](../structs/FComposableCameraNodePinDeclaration.md#fcomposablecameranodepindeclaration), but the per-asset values become the source of truth from that point on and are preserved across SyncToTypeAsset (which only rewrites TargetNodeIndex when node ordering changes; see ComposableCameraNodeGraph.cpp Step 7).

* **Identity fields** (ParameterName, PinType, StructType, TargetNodeIndex, TargetPinName) are deliberately read-only or hidden — renaming or retyping them in Details would silently break every consumer keying by name (K2 node UserOverrideNames, DataTable row Values, ParameterBlock activations, the row editor's orphan detection). To rename or retype, change it on the underlying pin and re-expose.

---

#### InternalVariables { #internalvariables }

```cpp
TArray< FComposableCameraInternalVariable > InternalVariables
```

Camera-level variables not exposed to callers but readable/writable by nodes. Used for cross-node communication and cross-frame state caching.

The struct type ([FComposableCameraInternalVariable](../structs/FComposableCameraInternalVariable.md#fcomposablecamerainternalvariable)) is shared with ExposedVariables below; the two categories differ only in whether the caller's ParameterBlock may override the initial value at activation time (ExposedVariables: yes; InternalVariables: no). At runtime both arrays feed the same InternalVariableOffsets map on the data block — Get/Set variable graph nodes treat them uniformly. Names must be unique across ExposedParameters ∪ InternalVariables ∪ ExposedVariables; see Build().

---

#### ExposedVariables { #exposedvariables }

```cpp
TArray< FComposableCameraInternalVariable > ExposedVariables
```

Camera-level variables whose initial value may be overridden by the caller at activation time, but which are otherwise identical to internal variables.

Authoring model: edited in the Details panel like InternalVariables (not via the graph's "Expose as Camera Parameter" flow, which is for input pins on camera nodes). The struct type is the same as InternalVariables.

Activation model: [ApplyParameterBlock()](#applyparameterblock) first tries to copy the caller's ParameterBlock entry keyed by VariableName into this slot; if the caller didn't supply a value, it falls back to parsing InitialValueString via [FComposableCameraParameterBlock::ApplyStringValue](../structs/FComposableCameraParameterBlock.md#applystringvalue) (the same parser the DataTable row path uses).

Runtime model: after the activation-time write, these are indistinguishable from InternalVariables. Their slots live in the same [FComposableCameraRuntimeDataBlock::InternalVariableOffsets](../structs/FComposableCameraRuntimeDataBlock.md#internalvariableoffsets) map, and the editor's variable graph nodes (Get/Set) find them via the same FindVariable() lookup path — both arrays are searched.

Name uniqueness is enforced across ExposedParameters ∪ InternalVariables ∪ ExposedVariables in Build(); see that function for the rationale.

---

#### PinConnections { #pinconnections }

```cpp
TArray< FComposableCameraPinConnection > PinConnections
```

Describes all data-pin connections between nodes. Each entry maps a target node's input pin to a source node's output pin.

---

#### ExecutionOrder { #executionorder }

```cpp
TArray< int32 > ExecutionOrder
```

Ordered list of node indices defining the execution chain, filtered down to camera nodes only.

ExecutionOrder[0] is the first camera node executed (closest to Start's exec out), ExecutionOrder[Last] is the last (closest to Output's exec in).

This is a cached projection of FullExecChain for runtime consumers that only care about camera nodes. Set-variable entries from FullExecChain are stripped out here; the runtime (once it starts honoring scratch writes) should iterate FullExecChain instead.

---

#### FullExecChain { #fullexecchain }

```cpp
TArray< FComposableCameraExecEntry > FullExecChain
```

Full execution chain including both camera nodes and internal-variable Set operations, in exec-wire order.

The editor walks the exec pin chain in the visual graph starting from the Start sentinel's ExecOut and records each step here. Set-variable entries capture the variable GUID being written plus the camera-node output pin that supplies the value; camera-node entries just capture the node index.

ExecutionOrder above is a camera-node-only projection of this array.

---

#### VariableNodes { #variablenodes }

```cpp
TArray< FComposableCameraVariableNodeRecord > VariableNodes
```

Editor-only records describing each Get/Set variable graph node in the visual editor, along with the camera-node pins each one is wired to. The runtime doesn't consume these directly; they exist so the editor can round-trip the variable-node layout and wires.

### Public Methods

| Return | Name | Description |
|--------|------|-------------|
| `const TArray< FComposableCameraExposedParameter > &` | [`GetExposedParameters`](#getexposedparameters) `const` `inline` | Get the list of exposed parameters for K2Node / DataTable introspection. |
| `FString` | [`GetExposedParameterDefaultValue`](#getexposedparameterdefaultvalue) `const` | Resolve the effective default value for an exposed parameter. |
| `FComposableCameraRuntimeDataBlock` | [`BuildRuntimeDataLayout`](#buildruntimedatalayout) `const` | Build a RuntimeDataBlock layout from this type asset's pin declarations, connections, exposed parameters, and internal variables. |
| `void` | [`ApplyParameterBlock`](#applyparameterblock) `const` | Fill a RuntimeDataBlock's exposed parameter slots from a ParameterBlock. Called after [BuildRuntimeDataLayout()](#buildruntimedatalayout) and before the camera starts ticking. |
| `void` | [`ApplyDelegateBindings`](#applydelegatebindings) `const` | Apply delegate bindings from the parameter block to the camera's node UPROPERTYs. |
| `FPrimaryAssetId` | [`GetPrimaryAssetId`](#getprimaryassetid) `virtual` `const` |  |

---

#### GetExposedParameters { #getexposedparameters }

`const` `inline`

```cpp
inline const TArray< FComposableCameraExposedParameter > & GetExposedParameters() const
```

Get the list of exposed parameters for K2Node / DataTable introspection.

---

#### GetExposedParameterDefaultValue { #getexposedparameterdefaultvalue }

`const`

```cpp
FString GetExposedParameterDefaultValue(const FComposableCameraExposedParameter & Param) const
```

Resolve the effective default value for an exposed parameter.

The default lives on the node's pin, not on the ExposedParameter struct. This helper looks up NodeTemplates[Param.TargetNodeIndex], gathers its pin declarations, finds the one matching Param.TargetPinName, then checks NodePinOverrides for a per-instance override. Returns the override if present, otherwise the class-level declaration default.

Returns an empty string if the target node/pin cannot be resolved (stale index, missing pin name, etc.).

---

#### BuildRuntimeDataLayout { #buildruntimedatalayout }

`const`

```cpp
FComposableCameraRuntimeDataBlock BuildRuntimeDataLayout() const
```

Build a RuntimeDataBlock layout from this type asset's pin declarations, connections, exposed parameters, and internal variables.

This computes all byte offsets and connection mappings. Called once per camera instantiation (or cached if the asset hasn't changed).

---

#### ApplyParameterBlock { #applyparameterblock }

`const`

```cpp
void ApplyParameterBlock(FComposableCameraRuntimeDataBlock & DataBlock, const FComposableCameraParameterBlock & Parameters) const
```

Fill a RuntimeDataBlock's exposed parameter slots from a ParameterBlock. Called after [BuildRuntimeDataLayout()](#buildruntimedatalayout) and before the camera starts ticking.

---

#### ApplyDelegateBindings { #applydelegatebindings }

`const`

```cpp
void ApplyDelegateBindings(class AComposableCameraCameraBase * Camera, const FComposableCameraParameterBlock & Parameters) const
```

Apply delegate bindings from the parameter block to the camera's node UPROPERTYs.

Called after ApplyParameterBlock. Iterates exposed parameters that are Delegate-typed and, for each one that has an entry in Parameters.DelegateValues, writes the FScriptDelegate into the target node's FDelegateProperty via reflection.

Delegates cannot go through the data block (they're not POD) so this is a separate pass that operates directly on node instances.

---

#### GetPrimaryAssetId { #getprimaryassetid }

`virtual` `const`

```cpp
virtual FPrimaryAssetId GetPrimaryAssetId() const
```
