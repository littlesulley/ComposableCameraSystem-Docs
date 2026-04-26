
# FComposableCameraContextSnapshot { #fcomposablecameracontextsnapshot }

```cpp
#include <ComposableCameraDebugPanelData.h>
```

One context entry in the stack snapshot. Produced by [UComposableCameraDirector::BuildDebugSnapshot](../core/UComposableCameraDirector.md#builddebugsnapshot) (via the stack).

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `FName` | [`ContextName`](#contextname-1)  | Name of this context (from project settings). |
| `bool` | [`bIsActive`](#bisactive-1)  | True if this is the active (top-of-stack) context. |
| `bool` | [`bIsBase`](#bisbase)  | True if this is the base (index 0) context. |
| `bool` | [`bIsPendingDestroy`](#bispendingdestroy)  | True if this entry is in PendingDestroyEntries (popped but still evaluating as a reference leaf during a transition). |
| `TArray< FComposableCameraTreeNodeSnapshot >` | [`TreeNodes`](#treenodes)  | DFS pre-order flattened tree nodes for this context's Director. |
| `TArray< FComposableCameraPatchSnapshot >` | [`Patches`](#patches-1)  | Active patches on this context's Director, in Apply iteration order. |
| `FString` | [`RunningCameraDisplay`](#runningcameradisplay)  | Display name of the director's RunningCamera ("(none)" if null). |
| `FComposableCameraPose` | [`LastPose`](#lastpose-1)  | Last evaluated pose from this director (for Director::LastEvaluatedPose). |

---

#### ContextName { #contextname-1 }

```cpp
FName ContextName = NAME_None
```

Name of this context (from project settings).

---

#### bIsActive { #bisactive-1 }

```cpp
bool bIsActive = false
```

True if this is the active (top-of-stack) context.

---

#### bIsBase { #bisbase }

```cpp
bool bIsBase = false
```

True if this is the base (index 0) context.

---

#### bIsPendingDestroy { #bispendingdestroy }

```cpp
bool bIsPendingDestroy = false
```

True if this entry is in PendingDestroyEntries (popped but still evaluating as a reference leaf during a transition).

---

#### TreeNodes { #treenodes }

```cpp
TArray< FComposableCameraTreeNodeSnapshot > TreeNodes
```

DFS pre-order flattened tree nodes for this context's Director.

---

#### Patches { #patches-1 }

```cpp
TArray< FComposableCameraPatchSnapshot > Patches
```

Active patches on this context's Director, in Apply iteration order.

---

#### RunningCameraDisplay { #runningcameradisplay }

```cpp
FString RunningCameraDisplay
```

Display name of the director's RunningCamera ("(none)" if null).

---

#### LastPose { #lastpose-1 }

```cpp
FComposableCameraPose LastPose
```

Last evaluated pose from this director (for Director::LastEvaluatedPose).
