
# TIIRInterpolatorTraits { #tiirinterpolatortraits }

```cpp
#include <ComposableCameraIIRInterpolator.h>
```

## TIIRInterpolatorTraits< FQuat > { #tiirinterpolatortraitsfquat }

```cpp
#include <ComposableCameraIIRInterpolator.h>
```

### Public Static Methods

| Return | Name | Description |
|--------|------|-------------|
| `FQuat` | [`InterpTo`](#interpto) `static` `inline` |  |

---

#### InterpTo { #interpto }

`static` `inline`

```cpp
static inline FQuat InterpTo(const FQuat & CurrentValue, const FQuat & TargetValue, float DeltaTime, double Speed)
```

## TIIRInterpolatorTraits< double > { #tiirinterpolatortraitsdouble }

```cpp
#include <ComposableCameraIIRInterpolator.h>
```

### Public Static Methods

| Return | Name | Description |
|--------|------|-------------|
| `double` | [`InterpTo`](#interpto-1) `static` `inline` |  |

---

#### InterpTo { #interpto-1 }

`static` `inline`

```cpp
static inline double InterpTo(double CurrentValue, double TargetValue, float DeltaTime, double Speed)
```

## TIIRInterpolatorTraits< FRotator > { #tiirinterpolatortraitsfrotator }

```cpp
#include <ComposableCameraIIRInterpolator.h>
```

### Public Static Methods

| Return | Name | Description |
|--------|------|-------------|
| `FRotator` | [`InterpTo`](#interpto-2) `static` `inline` |  |

---

#### InterpTo { #interpto-2 }

`static` `inline`

```cpp
static inline FRotator InterpTo(const FRotator & CurrentValue, const FRotator & TargetValue, float DeltaTime, double Speed)
```

## TIIRInterpolatorTraits< FVector2d > { #tiirinterpolatortraitsfvector2d }

```cpp
#include <ComposableCameraIIRInterpolator.h>
```

### Public Static Methods

| Return | Name | Description |
|--------|------|-------------|
| `FVector2d` | [`InterpTo`](#interpto-3) `static` `inline` |  |

---

#### InterpTo { #interpto-3 }

`static` `inline`

```cpp
static inline FVector2d InterpTo(const FVector2d & CurrentValue, const FVector2d & TargetValue, float DeltaTime, double Speed)
```

## TIIRInterpolatorTraits< FVector3d > { #tiirinterpolatortraitsfvector3d }

```cpp
#include <ComposableCameraIIRInterpolator.h>
```

### Public Static Methods

| Return | Name | Description |
|--------|------|-------------|
| `FVector3d` | [`InterpTo`](#interpto-4) `static` `inline` |  |

---

#### InterpTo { #interpto-4 }

`static` `inline`

```cpp
static inline FVector3d InterpTo(const FVector3d & CurrentValue, const FVector3d & TargetValue, float DeltaTime, double Speed)
```
