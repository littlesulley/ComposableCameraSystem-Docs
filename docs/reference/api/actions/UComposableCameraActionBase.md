
# UComposableCameraActionBase { #ucomposablecameraactionbase }

```cpp
#include <ComposableCameraActionBase.h>
```

> **Inherits:** `UObject`
> **Subclassed by:** [`UComposableCameraMoveToAction`](UComposableCameraMoveToAction.md#ucomposablecameramovetoaction), [`UComposableCameraResetPitchAction`](UComposableCameraResetPitchAction.md#ucomposablecameraresetpitchaction), [`UComposableCameraRotateToAction`](UComposableCameraRotateToAction.md#ucomposablecamerarotatetoaction)

A camera action is a hook where you can do anything before/after a camera is evaluated, or before/after some node is evaluated.

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `EComposableCameraActionExecutionType` | [`ExecutionType`](#executiontype)  |  |
| `TSubclassOf< UComposableCameraCameraNodeBase >` | [`TargetNodeClass`](#targetnodeclass)  |  |
| `uint8` | [`ExpirationType`](#expirationtype)  |  |
| `float` | [`Duration`](#duration-2)  |  |
| `bool` | [`bOnlyForCurrentCamera`](#bonlyforcurrentcamera)  |  |
| `AComposableCameraPlayerCameraManager *` | [`PlayerCameraManager`](#playercameramanager)  |  |

---

#### ExecutionType { #executiontype }

```cpp
EComposableCameraActionExecutionType ExecutionType {  }
```

---

#### TargetNodeClass { #targetnodeclass }

```cpp
TSubclassOf< UComposableCameraCameraNodeBase > TargetNodeClass
```

---

#### ExpirationType { #expirationtype }

```cpp
uint8 ExpirationType { static_cast<uint8>( | ) }
```

---

#### Duration { #duration-2 }

```cpp
float Duration { 1.f }
```

---

#### bOnlyForCurrentCamera { #bonlyforcurrentcamera }

```cpp
bool bOnlyForCurrentCamera { true }
```

---

#### PlayerCameraManager { #playercameramanager }

```cpp
AComposableCameraPlayerCameraManager * PlayerCameraManager {}
```

### Public Methods

| Return | Name | Description |
|--------|------|-------------|
| `bool` | [`OnCanExecute`](#oncanexecute)  |  |
| `bool` | [`CanExecute`](#canexecute)  |  |
| `bool` | [`CanExecute_Implementation`](#canexecute_implementation) `virtual` `inline` |  |
| `void` | [`OnExecute`](#onexecute)  |  |
| `void` | [`OnExecute_Implementation`](#onexecute_implementation) `virtual` `inline` |  |
| `void` | [`ExpireAction`](#expireaction) `inline` |  |

---

#### OnCanExecute { #oncanexecute }

```cpp
bool OnCanExecute(float DeltaTime, const FComposableCameraPose & CurrentCameraPose)
```

---

#### CanExecute { #canexecute }

```cpp
bool CanExecute(float DeltaTime, const FComposableCameraPose & CurrentCameraPose)
```

---

#### CanExecute_Implementation { #canexecute_implementation }

`virtual` `inline`

```cpp
virtual inline bool CanExecute_Implementation(float DeltaTime, const FComposableCameraPose & CurrentCameraPose)
```

---

#### OnExecute { #onexecute }

```cpp
void OnExecute(float DeltaTime, const FComposableCameraPose & CurrentCameraPose, FComposableCameraPose & OutCameraPose)
```

---

#### OnExecute_Implementation { #onexecute_implementation }

`virtual` `inline`

```cpp
virtual inline void OnExecute_Implementation(float DeltaTime, const FComposableCameraPose & CurrentCameraPose, FComposableCameraPose & OutCameraPose)
```

---

#### ExpireAction { #expireaction }

`inline`

```cpp
inline void ExpireAction()
```

### Private Attributes

| Return | Name | Description |
|--------|------|-------------|
| `bool` | [`bCanExecuteInstant`](#bcanexecuteinstant)  |  |
| `bool` | [`bCanExecuteDuration`](#bcanexecuteduration)  |  |
| `bool` | [`bCanExecuteManual`](#bcanexecutemanual)  |  |
| `bool` | [`bCanExecuteCondition`](#bcanexecutecondition)  |  |
| `float` | [`ElapsedTime`](#elapsedtime-2)  |  |

---

#### bCanExecuteInstant { #bcanexecuteinstant }

```cpp
bool bCanExecuteInstant { true }
```

---

#### bCanExecuteDuration { #bcanexecuteduration }

```cpp
bool bCanExecuteDuration { true }
```

---

#### bCanExecuteManual { #bcanexecutemanual }

```cpp
bool bCanExecuteManual { true }
```

---

#### bCanExecuteCondition { #bcanexecutecondition }

```cpp
bool bCanExecuteCondition { true }
```

---

#### ElapsedTime { #elapsedtime-2 }

```cpp
float ElapsedTime { 0.f }
```
