
# TSimpleSpringInterpolatorTraits { #tsimplespringinterpolatortraits }

```cpp
#include <ComposableCameraSimpleSpringInterpolator.h>
```



## TSimpleSpringInterpolatorTraits< FQuat > { #tsimplespringinterpolatortraitsfquat }

```cpp
#include <ComposableCameraSimpleSpringInterpolator.h>
```

### Public Static Methods

| Return | Name | Description |
|--------|------|-------------|
| `FQuat` | [`Damp`](#damp) `static` `inline` |  |

---

#### Damp { #damp }

`static` `inline`

```cpp
static inline FQuat Damp(const FQuat & CurrentValue, const FQuat & TargetValue, float DeltaTime, float DampTime)
```



## TSimpleSpringInterpolatorTraits< double > { #tsimplespringinterpolatortraitsdouble }

```cpp
#include <ComposableCameraSimpleSpringInterpolator.h>
```

### Public Static Methods

| Return | Name | Description |
|--------|------|-------------|
| `double` | [`Damp`](#damp-1) `static` `inline` |  |

---

#### Damp { #damp-1 }

`static` `inline`

```cpp
static inline double Damp(double CurrentValue, double TargetValue, float DeltaTime, float DampTime)
```



## TSimpleSpringInterpolatorTraits< FRotator > { #tsimplespringinterpolatortraitsfrotator }

```cpp
#include <ComposableCameraSimpleSpringInterpolator.h>
```

### Public Static Methods

| Return | Name | Description |
|--------|------|-------------|
| `FRotator` | [`Damp`](#damp-2) `static` `inline` |  |

---

#### Damp { #damp-2 }

`static` `inline`

```cpp
static inline FRotator Damp(const FRotator & CurrentValue, const FRotator & TargetValue, float DeltaTime, float DampTime)
```



## TSimpleSpringInterpolatorTraits< FVector2d > { #tsimplespringinterpolatortraitsfvector2d }

```cpp
#include <ComposableCameraSimpleSpringInterpolator.h>
```

### Public Static Methods

| Return | Name | Description |
|--------|------|-------------|
| `FVector2d` | [`Damp`](#damp-3) `static` `inline` |  |

---

#### Damp { #damp-3 }

`static` `inline`

```cpp
static inline FVector2d Damp(const FVector2d & CurrentValue, const FVector2d & TargetValue, float DeltaTime, float DampTime)
```



## TSimpleSpringInterpolatorTraits< FVector3d > { #tsimplespringinterpolatortraitsfvector3d }

```cpp
#include <ComposableCameraSimpleSpringInterpolator.h>
```

### Public Static Methods

| Return | Name | Description |
|--------|------|-------------|
| `FVector3d` | [`Damp`](#damp-4) `static` `inline` |  |

---

#### Damp { #damp-4 }

`static` `inline`

```cpp
static inline FVector3d Damp(const FVector3d & CurrentValue, const FVector3d & TargetValue, float DeltaTime, float DampTime)
```
