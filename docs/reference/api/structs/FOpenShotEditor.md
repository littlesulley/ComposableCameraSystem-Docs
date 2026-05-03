
# FOpenShotEditor { #fopenshoteditor }

```cpp
#include <EditorHooks.h>
```

### Public Static Attributes

| Return | Name | Description |
|--------|------|-------------|
| `FOpenShotEditorRequest` | [`OpenShotEditorDelegate`](#openshoteditordelegate) `static` | Bound by the editor module; a no-op in cooked / non-editor builds. |

---

#### OpenShotEditorDelegate { #openshoteditordelegate }

`static`

```cpp
FOpenShotEditorRequest OpenShotEditorDelegate
```

Bound by the editor module; a no-op in cooked / non-editor builds.

### Public Static Methods

| Return | Name | Description |
|--------|------|-------------|
| `void` | [`Open`](#open) `static` `inline` | Runtime-side helper. Routes through the delegate iff bound and we're in an editor build; silently no-ops otherwise. Safe to call from any WITH_EDITOR-conditional UFUNCTION body. |

---

#### Open { #open }

`static` `inline`

```cpp
static inline void Open(FComposableCameraShot * Shot, UObject * HostObject)
```

Runtime-side helper. Routes through the delegate iff bound and we're in an editor build; silently no-ops otherwise. Safe to call from any WITH_EDITOR-conditional UFUNCTION body.
