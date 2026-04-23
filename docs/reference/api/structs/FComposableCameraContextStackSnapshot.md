
# FComposableCameraContextStackSnapshot { #fcomposablecameracontextstacksnapshot }

```cpp
#include <ComposableCameraDebugPanelData.h>
```

Top-level context stack + tree snapshot consumed by the debug panel. Produced by [UComposableCameraContextStack::BuildDebugSnapshot](../core/UComposableCameraContextStack.md#builddebugsnapshot-1).

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `TArray< FComposableCameraContextSnapshot >` | [`Contexts`](#contexts)  | All contexts — live entries first (LIFO, index 0 = base), then pending-destroy entries. The UI walks this as a single flat list. |
| `int32` | [`LiveStackDepth`](#livestackdepth)  | Total number of live (non-pending-destroy) entries. |
| `int32` | [`PendingDestroyCount`](#pendingdestroycount)  | Number of pending-destroy entries. |

---

#### Contexts { #contexts }

```cpp
TArray< FComposableCameraContextSnapshot > Contexts
```

All contexts — live entries first (LIFO, index 0 = base), then pending-destroy entries. The UI walks this as a single flat list.

---

#### LiveStackDepth { #livestackdepth }

```cpp
int32 LiveStackDepth = 0
```

Total number of live (non-pending-destroy) entries.

---

#### PendingDestroyCount { #pendingdestroycount }

```cpp
int32 PendingDestroyCount = 0
```

Number of pending-destroy entries.
