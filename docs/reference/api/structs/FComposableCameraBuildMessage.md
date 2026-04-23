
# FComposableCameraBuildMessage { #fcomposablecamerabuildmessage }

```cpp
#include <ComposableCameraTypeAsset.h>
```

A single message from the build/validation pipeline.

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `uint8` | [`Severity`](#severity)  |  |
| `FText` | [`Message`](#message-1)  |  |
| `int32` | [`NodeIndex`](#nodeindex-1)  | Which node the message relates to (-1 for asset-level). |
| `FName` | [`PinName`](#pinname-2)  | Which pin the message relates to (None for node-level). |

---

#### Severity { #severity }

```cpp
uint8 Severity = 0
```

---

#### Message { #message-1 }

```cpp
FText Message
```

---

#### NodeIndex { #nodeindex-1 }

```cpp
int32 NodeIndex = INDEX_NONE
```

Which node the message relates to (-1 for asset-level).

---

#### PinName { #pinname-2 }

```cpp
FName PinName
```

Which pin the message relates to (None for node-level).
