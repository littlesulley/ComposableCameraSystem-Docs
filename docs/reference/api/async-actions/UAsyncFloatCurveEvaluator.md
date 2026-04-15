
# UAsyncFloatCurveEvaluator { #uasyncfloatcurveevaluator }

```cpp
#include <AsyncFloatCurveEvaluator.h>
```

> **Inherits:** `UBlueprintAsyncActionBase`, `FTickableGameObject`

An async action evaluating a given float curve lasting for a given duration.

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `FOnTickFloatCurve` | [`OnTick`](#ontick)  |  |
| `FOnCompleteFloatCurve` | [`OnComplete`](#oncomplete)  |  |

---

#### OnTick { #ontick }

```cpp
FOnTickFloatCurve OnTick
```

---

#### OnComplete { #oncomplete }

```cpp
FOnCompleteFloatCurve OnComplete
```

### Public Methods

| Return | Name | Description |
|--------|------|-------------|
| `void` | [`Tick`](#tick) `virtual` |  |
| `TStatId` | [`GetStatId`](#getstatid) `virtual` `const` |  |
| `bool` | [`IsTickable`](#istickable) `virtual` `const` |  |

---

#### Tick { #tick }

`virtual`

```cpp
virtual void Tick(float DeltaTime)
```

---

#### GetStatId { #getstatid }

`virtual` `const`

```cpp
virtual TStatId GetStatId() const
```

---

#### IsTickable { #istickable }

`virtual` `const`

```cpp
virtual bool IsTickable() const
```

### Public Static Methods

| Return | Name | Description |
|--------|------|-------------|
| `UAsyncFloatCurveEvaluator *` | [`AsyncFloatCurveEvaluator`](#asyncfloatcurveevaluator) `static` |  |

---

#### AsyncFloatCurveEvaluator { #asyncfloatcurveevaluator }

`static`

```cpp
static UAsyncFloatCurveEvaluator * AsyncFloatCurveEvaluator(UObject * WorldContextObject, UCurveFloat * Curve, float Duration)
```

### Protected Attributes

| Return | Name | Description |
|--------|------|-------------|
| `UCurveFloat *` | [`Curve`](#curve)  |  |
| `float` | [`Duration`](#duration)  |  |
| `float` | [`ElapsedTime`](#elapsedtime)  |  |
| `bool` | [`bShouldTick`](#bshouldtick)  |  |

---

#### Curve { #curve }

```cpp
UCurveFloat * Curve { nullptr }
```

---

#### Duration { #duration }

```cpp
float Duration { 0.f }
```

---

#### ElapsedTime { #elapsedtime }

```cpp
float ElapsedTime { 0.f }
```

---

#### bShouldTick { #bshouldtick }

```cpp
bool bShouldTick { true }
```
