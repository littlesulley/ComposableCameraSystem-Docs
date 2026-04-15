
# UAsyncVectorCurveEvaluator { #uasyncvectorcurveevaluator }

```cpp
#include <AsyncVectorCurveEvaluator.h>
```

> **Inherits:** `UBlueprintAsyncActionBase`, `FTickableGameObject`

An async action evaluating a given vector curve lasting for a given duration.

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `FOnTickVectorCurve` | [`OnTick`](#ontick-1)  |  |
| `FOnCompleteVectorCurve` | [`OnComplete`](#oncomplete-1)  |  |

---

#### OnTick { #ontick-1 }

```cpp
FOnTickVectorCurve OnTick
```

---

#### OnComplete { #oncomplete-1 }

```cpp
FOnCompleteVectorCurve OnComplete
```

### Public Methods

| Return | Name | Description |
|--------|------|-------------|
| `void` | [`Tick`](#tick-1) `virtual` |  |
| `TStatId` | [`GetStatId`](#getstatid-1) `virtual` `const` |  |
| `bool` | [`IsTickable`](#istickable-1) `virtual` `const` |  |

---

#### Tick { #tick-1 }

`virtual`

```cpp
virtual void Tick(float DeltaTime)
```

---

#### GetStatId { #getstatid-1 }

`virtual` `const`

```cpp
virtual TStatId GetStatId() const
```

---

#### IsTickable { #istickable-1 }

`virtual` `const`

```cpp
virtual bool IsTickable() const
```

### Public Static Methods

| Return | Name | Description |
|--------|------|-------------|
| `UAsyncVectorCurveEvaluator *` | [`AsyncVectorCurveEvaluator`](#asyncvectorcurveevaluator) `static` |  |

---

#### AsyncVectorCurveEvaluator { #asyncvectorcurveevaluator }

`static`

```cpp
static UAsyncVectorCurveEvaluator * AsyncVectorCurveEvaluator(UObject * WorldContextObject, UCurveVector * Curve, float Duration)
```

### Protected Attributes

| Return | Name | Description |
|--------|------|-------------|
| `UCurveVector *` | [`Curve`](#curve-1)  |  |
| `float` | [`Duration`](#duration-1)  |  |
| `float` | [`ElapsedTime`](#elapsedtime-1)  |  |
| `bool` | [`bShouldTick`](#bshouldtick-1)  |  |

---

#### Curve { #curve-1 }

```cpp
UCurveVector * Curve { nullptr }
```

---

#### Duration { #duration-1 }

```cpp
float Duration { 0.f }
```

---

#### ElapsedTime { #elapsedtime-1 }

```cpp
float ElapsedTime { 0.f }
```

---

#### bShouldTick { #bshouldtick-1 }

```cpp
bool bShouldTick { true }
```
