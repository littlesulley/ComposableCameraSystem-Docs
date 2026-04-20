
# UComposableCameraReceivePivotActorNode { #ucomposablecamerareceivepivotactornode }

```cpp
#include <ComposableCameraReceivePivotActorNode.h>
```

> **Inherits:** [`UComposableCameraCameraNodeBase`](../uobjects-other/UComposableCameraCameraNodeBase.md#ucomposablecameracameranodebase)

Reads a pivot actor's location and publishes it as the pivot position for downstream nodes. This node runs every tick.

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `TObjectPtr< AActor >` | [`PivotActor`](#pivotactor-2)  |  |
| `bool` | [`bUseBoneForPivot`](#buseboneforpivot)  |  |
| `FName` | [`BoneName`](#bonename-1)  |  |

---

#### PivotActor { #pivotactor-2 }

```cpp
TObjectPtr< AActor > PivotActor
```

---

#### bUseBoneForPivot { #buseboneforpivot }

```cpp
bool bUseBoneForPivot { false }
```

---

#### BoneName { #bonename-1 }

```cpp
FName BoneName
```

### Public Methods

| Return | Name | Description |
|--------|------|-------------|
| `void` | [`OnInitialize_Implementation`](#oninitialize_implementation-11) `virtual` |  |
| `void` | [`OnTickNode_Implementation`](#onticknode_implementation-19) `virtual` |  |
| `void` | [`GetPinDeclarations_Implementation`](#getpindeclarations_implementation-17) `virtual` `const` |  |

---

#### OnInitialize_Implementation { #oninitialize_implementation-11 }

`virtual`

```cpp
virtual void OnInitialize_Implementation()
```

---

#### OnTickNode_Implementation { #onticknode_implementation-19 }

`virtual`

```cpp
virtual void OnTickNode_Implementation(float DeltaTime, const FComposableCameraPose & CurrentCameraPose, FComposableCameraPose & OutCameraPose)
```

---

#### GetPinDeclarations_Implementation { #getpindeclarations_implementation-17 }

`virtual` `const`

```cpp
virtual void GetPinDeclarations_Implementation(TArray< FComposableCameraNodePinDeclaration > & OutPins) const
```

### Private Attributes

| Return | Name | Description |
|--------|------|-------------|
| `USkeletalMeshComponent *` | [`SkeletalMeshComponentForPivotActor`](#skeletalmeshcomponentforpivotactor-1)  |  |

---

#### SkeletalMeshComponentForPivotActor { #skeletalmeshcomponentforpivotactor-1 }

```cpp
USkeletalMeshComponent * SkeletalMeshComponentForPivotActor { nullptr }
```
