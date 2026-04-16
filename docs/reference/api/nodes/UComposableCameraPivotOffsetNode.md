
# UComposableCameraPivotOffsetNode { #ucomposablecamerapivotoffsetnode }

```cpp
#include <ComposableCameraPivotOffsetNode.h>
```

> **Inherits:** [`UComposableCameraCameraNodeBase`](../uobjects-other/UComposableCameraCameraNodeBase.md#ucomposablecameracameranodebase)

Node for adjusting the pivot position by applying an offset in world/camera/actor local space. <br/>
If using camera space, the CurrentCameraPose parameter in the Tick function will be used. <br/>
@ InputParameter PivotOffsetType: In which space you'd like to apply offset, can be world, camera, or actor local. <br/>
@ InputParameter ActorForLocalSpace: The actor determining the local space if you choose actor local space. <br/>
@ InputParameter PivotOffset: The offset. <br/>
This node runs every tick.

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `FVector` | [`PivotPosition`](#pivotposition)  |  |
| `ECameraPivotOffset` | [`PivotOffsetType`](#pivotoffsettype)  |  |
| `TSoftObjectPtr< AActor >` | [`ActorForLocalSpace`](#actorforlocalspace)  |  |
| `FVector` | [`PivotOffset`](#pivotoffset)  |  |

---

#### PivotPosition { #pivotposition }

```cpp
FVector PivotPosition { FVector::ZeroVector }
```

---

#### PivotOffsetType { #pivotoffsettype }

```cpp
ECameraPivotOffset PivotOffsetType = 
```

---

#### ActorForLocalSpace { #actorforlocalspace }

```cpp
TSoftObjectPtr< AActor > ActorForLocalSpace = nullptr
```

---

#### PivotOffset { #pivotoffset }

```cpp
FVector PivotOffset = FVector::ZeroVector
```

### Public Methods

| Return | Name | Description |
|--------|------|-------------|
| `void` | [`OnInitialize_Implementation`](#oninitialize_implementation-4) `virtual` |  |
| `void` | [`OnTickNode_Implementation`](#onticknode_implementation-7) `virtual` |  |
| `void` | [`GetPinDeclarations_Implementation`](#getpindeclarations_implementation-7) `virtual` `const` |  |

---

#### OnInitialize_Implementation { #oninitialize_implementation-4 }

`virtual`

```cpp
virtual void OnInitialize_Implementation()
```

---

#### OnTickNode_Implementation { #onticknode_implementation-7 }

`virtual`

```cpp
virtual void OnTickNode_Implementation(float DeltaTime, const FComposableCameraPose & CurrentCameraPose, FComposableCameraPose & OutCameraPose)
```

---

#### GetPinDeclarations_Implementation { #getpindeclarations_implementation-7 }

`virtual` `const`

```cpp
virtual void GetPinDeclarations_Implementation(TArray< FComposableCameraNodePinDeclaration > & OutPins) const
```

### Private Methods

| Return | Name | Description |
|--------|------|-------------|
| `void` | [`UpdatePivotOffset`](#updatepivotoffset)  |  |

---

#### UpdatePivotOffset { #updatepivotoffset }

```cpp
void UpdatePivotOffset(const FVector & InPivot, const FComposableCameraPose & CurrentCameraPose)
```
