
# FGetActiveEditorViewport { #fgetactiveeditorviewport }

```cpp
#include <EditorHooks.h>
```

### Public Static Attributes

| Return | Name | Description |
|--------|------|-------------|
| `FGetActiveEditorViewportSize` | [`GetSizeDelegate`](#getsizedelegate) `static` |  |

---

#### GetSizeDelegate { #getsizedelegate }

`static`

```cpp
FGetActiveEditorViewportSize GetSizeDelegate
```

### Public Static Methods

| Return | Name | Description |
|--------|------|-------------|
| `bool` | [`TryGetSize`](#trygetsize) `static` `inline` | Runtime-side helper. Routes through the delegate iff bound and we're in an editor build; silently returns false otherwise. |

---

#### TryGetSize { #trygetsize }

`static` `inline`

```cpp
static inline bool TryGetSize(FIntPoint & OutSize)
```

Runtime-side helper. Routes through the delegate iff bound and we're in an editor build; silently returns false otherwise.
