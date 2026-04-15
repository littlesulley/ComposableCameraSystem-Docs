
# FComposableCameraPinConnection { #fcomposablecamerapinconnection }

```cpp
#include <ComposableCameraNodePinTypes.h>
```

Describes a data-pin connection between two nodes in a camera type asset.

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `int32` | [`SourceNodeIndex`](#sourcenodeindex)  | Index of the source node in the camera type's NodeTemplates array. |
| `FName` | [`SourcePinName`](#sourcepinname-1)  | Name of the output pin on the source node. |
| `int32` | [`TargetNodeIndex`](#targetnodeindex)  | Index of the target node in the camera type's NodeTemplates array. |
| `FName` | [`TargetPinName`](#targetpinname)  | Name of the input pin on the target node. |

---

#### SourceNodeIndex { #sourcenodeindex }

```cpp
int32 SourceNodeIndex = INDEX_NONE
```

Index of the source node in the camera type's NodeTemplates array.

---

#### SourcePinName { #sourcepinname-1 }

```cpp
FName SourcePinName
```

Name of the output pin on the source node.

---

#### TargetNodeIndex { #targetnodeindex }

```cpp
int32 TargetNodeIndex = INDEX_NONE
```

Index of the target node in the camera type's NodeTemplates array.

---

#### TargetPinName { #targetpinname }

```cpp
FName TargetPinName
```

Name of the input pin on the target node.
