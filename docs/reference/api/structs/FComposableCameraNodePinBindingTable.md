
# FComposableCameraNodePinBindingTable { #fcomposablecameranodepinbindingtable }

```cpp
#include <ComposableCameraCameraNodeBase.h>
```

Class-level binding table for a camera node UClass.

Built once (lazily, on first call) per concrete UClass and cached module-locally. The node's TickNode prologue uses this to re-resolve every input pin into its matching UPROPERTY field each frame, so subclass code can just read members directly instead of calling GetInputPinValue<T>(FName).

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `TArray< FComposableCameraNodePinBinding >` | [`InputBindings`](#inputbindings)  | All input pins that have a matched top-level UPROPERTY on the node. |

---

#### InputBindings { #inputbindings }

```cpp
TArray< FComposableCameraNodePinBinding > InputBindings
```

All input pins that have a matched top-level UPROPERTY on the node.
