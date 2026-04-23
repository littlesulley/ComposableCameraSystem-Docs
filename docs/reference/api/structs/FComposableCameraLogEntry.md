
# FComposableCameraLogEntry { #fcomposablecameralogentry }

```cpp
#include <ComposableCameraLogCapture.h>
```

A single captured warning / error log line. Produced by `[FComposableCameraLogCapture](FComposableCameraLogCapture.md#fcomposablecameralogcapture)` every time `UE_LOG` fires on a ComposableCamera log category at Warning verbosity or worse.

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `FName` | [`CategoryName`](#categoryname)  | Log category name that emitted the line. Used so the panel can distinguish runtime (`LogComposableCameraSystem`) from editor (`LogComposableCameraSystemEditor`) origins at a glance. |
| `ELogVerbosity::Type` | [`Verbosity`](#verbosity)  | Verbosity level (Warning / Error / Fatal). Filtered at capture time — Log / Display / Verbose / VeryVerbose never enter the ring buffer so the panel doesn't drown in trivia. |
| `FString` | [`Message`](#message)  | Formatted message body (after `UE_LOG`'s printf-style substitution). |
| `double` | [`Timestamp`](#timestamp)  | Wall-clock time of capture, from `FPlatformTime::Seconds()`. The panel displays `(Now - Timestamp)` as "Xs ago" so users can tell stale warnings from fresh ones. |
| `int32` | [`RepeatCount`](#repeatcount)  | Number of times the same (Category, Verbosity, Message) triple has been emitted since it first entered the ring buffer. Starts at 1 on first capture; bumped by the dedupe path in `[FComposableCameraLogCapture::Serialize](FComposableCameraLogCapture.md#serialize)` without moving the entry or allocating. Panel renders "(xN)" when N > 1 so callers see at a glance that a warning is spamming. |

---

#### CategoryName { #categoryname }

```cpp
FName CategoryName
```

Log category name that emitted the line. Used so the panel can distinguish runtime (`LogComposableCameraSystem`) from editor (`LogComposableCameraSystemEditor`) origins at a glance.

---

#### Verbosity { #verbosity }

```cpp
ELogVerbosity::Type Verbosity = ELogVerbosity::NoLogging
```

Verbosity level (Warning / Error / Fatal). Filtered at capture time — Log / Display / Verbose / VeryVerbose never enter the ring buffer so the panel doesn't drown in trivia.

---

#### Message { #message }

```cpp
FString Message
```

Formatted message body (after `UE_LOG`'s printf-style substitution).

---

#### Timestamp { #timestamp }

```cpp
double Timestamp = 0.0
```

Wall-clock time of capture, from `FPlatformTime::Seconds()`. The panel displays `(Now - Timestamp)` as "Xs ago" so users can tell stale warnings from fresh ones.

---

#### RepeatCount { #repeatcount }

```cpp
int32 RepeatCount = 1
```

Number of times the same (Category, Verbosity, Message) triple has been emitted since it first entered the ring buffer. Starts at 1 on first capture; bumped by the dedupe path in `[FComposableCameraLogCapture::Serialize](FComposableCameraLogCapture.md#serialize)` without moving the entry or allocating. Panel renders "(xN)" when N > 1 so callers see at a glance that a warning is spamming.
