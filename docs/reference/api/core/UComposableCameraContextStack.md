
# UComposableCameraContextStack { #ucomposablecameracontextstack }

```cpp
#include <ComposableCameraContextStack.h>
```

> **Inherits:** `UObject`

Camera context stack — the macro-level orchestrator.

Manages a LIFO stack of camera evaluation contexts, each owning its own Director and EvaluationTree. This is the first tier in the two-tier camera architecture:

* Tier 1 (this): Context stack for switching between camera "modes" (gameplay, UI, cinematic).

* Tier 2: Evaluation tree within each context for transitions between cameras of the same mode.

Contexts are identified by FName and defined in project settings. The stack is strict LIFO: new contexts push on top, popping removes from top (or by name).

Auto-pop: when the active context's running camera is transient and finishes, the context is automatically popped. The camera itself drives lifecycle, not the context.

Inter-context transitions use a reference leaf node in the evaluation tree: the new context's tree gets a reference leaf that evaluates the previous context's Director live, enabling smooth blending between contexts.

Popped contexts with transitions enter a "pending destruction" state: their Director stays alive and is evaluated through the reference leaf during the transition. Once the transition finishes, the pending context's cameras are destroyed and the entry is removed.

### Public Methods

| Return | Name | Description |
|--------|------|-------------|
|  | [`UComposableCameraContextStack`](#ucomposablecameracontextstack-1)  |  |
| `UComposableCameraDirector *` | [`EnsureContext`](#ensurecontext)  | Ensure a context with the given name exists on the stack. If already present, returns its Director. If not, pushes a new context on top (LIFO) and returns its Director. |
| `void` | [`PopContext`](#popcontext)  | Pop a specific context by name. If the context is the active (top) context and a transition is available, the pop is animated: the previous context resumes with a transition from the popped context's Director. If the context is not the active one, it is removed immediately. Cannot pop the base (bottom) context if it is the last one remaining. |
| `void` | [`PopActiveContext`](#popactivecontext)  | Pop the active (top) context. Used by TerminateCurrentCamera. Cannot pop the base context if it is the last one remaining. |
| `int32` | [`GetStackDepth`](#getstackdepth) `const` `inline` | Get the number of contexts on the stack. |
| `UComposableCameraDirector *` | [`GetActiveDirector`](#getactivedirector) `const` | Get the active (top) context's Director. Returns nullptr if the stack is empty. |
| `UComposableCameraDirector *` | [`GetDirectorForContext`](#getdirectorforcontext) `const` | Get the Director for a specific context by name. Returns nullptr if not on the stack. |
| `AComposableCameraCameraBase *` | [`GetRunningCamera`](#getrunningcamera-1) `const` | Get the active context's running camera. Returns nullptr if the stack is empty. |
| `FName` | [`GetActiveContextName`](#getactivecontextname) `const` | Get the active context's name. Returns NAME_None if the stack is empty. |
| `FComposableCameraPose` | [`Evaluate`](#evaluate-4)  | Evaluate the active context for this frame. Only the top context is ticked (unless a lower context is referenced by a reference leaf in the active context's tree, in which case it ticks through the reference). If the active context's running camera is transient and finished, auto-pops the context. |
| `void` | [`BuildDebugString`](#builddebugstring-1) `const` | Build a debug string showing the full context stack state. |

---

#### UComposableCameraContextStack { #ucomposablecameracontextstack-1 }

```cpp
UComposableCameraContextStack(const FObjectInitializer & ObjectInitializer)
```

---

#### EnsureContext { #ensurecontext }

```cpp
UComposableCameraDirector * EnsureContext(AComposableCameraPlayerCameraManager * PlayerCameraManager, FName ContextName)
```

Ensure a context with the given name exists on the stack. If already present, returns its Director. If not, pushes a new context on top (LIFO) and returns its Director.

**Parameters**
* `PlayerCameraManager` The owning player camera manager. 

* `ContextName` The name identifying which context to ensure (must be in project settings). 

**Returns**
The Director for the context. Returns nullptr if the name is not registered.

---

#### PopContext { #popcontext }

```cpp
void PopContext(FName ContextName, AComposableCameraPlayerCameraManager * PlayerCameraManager, UComposableCameraTransitionDataAsset * TransitionOverride, const FComposableCameraActivateParams & ActivationParams)
```

Pop a specific context by name. If the context is the active (top) context and a transition is available, the pop is animated: the previous context resumes with a transition from the popped context's Director. If the context is not the active one, it is removed immediately. Cannot pop the base (bottom) context if it is the last one remaining.

**Parameters**
* `ContextName` The name of the context to pop. 

* `PlayerCameraManager` The owning player camera manager (needed for camera creation during transition). 

* `TransitionOverride` Optional transition data asset. If nullptr, falls back to the resume camera's EnterTransition. 

* `ActivationParams` Optional activation params for the resume camera.

---

#### PopActiveContext { #popactivecontext }

```cpp
void PopActiveContext(AComposableCameraPlayerCameraManager * PlayerCameraManager, UComposableCameraTransitionDataAsset * TransitionOverride, const FComposableCameraActivateParams & ActivationParams)
```

Pop the active (top) context. Used by TerminateCurrentCamera. Cannot pop the base context if it is the last one remaining.

**Parameters**
* `PlayerCameraManager` The owning player camera manager. 

* `TransitionOverride` Optional transition data asset override. 

* `ActivationParams` Optional activation params for the resume camera.

---

#### GetStackDepth { #getstackdepth }

`const` `inline`

```cpp
inline int32 GetStackDepth() const
```

Get the number of contexts on the stack.

---

#### GetActiveDirector { #getactivedirector }

`const`

```cpp
UComposableCameraDirector * GetActiveDirector() const
```

Get the active (top) context's Director. Returns nullptr if the stack is empty.

---

#### GetDirectorForContext { #getdirectorforcontext }

`const`

```cpp
UComposableCameraDirector * GetDirectorForContext(FName ContextName) const
```

Get the Director for a specific context by name. Returns nullptr if not on the stack.

---

#### GetRunningCamera { #getrunningcamera-1 }

`const`

```cpp
AComposableCameraCameraBase * GetRunningCamera() const
```

Get the active context's running camera. Returns nullptr if the stack is empty.

---

#### GetActiveContextName { #getactivecontextname }

`const`

```cpp
FName GetActiveContextName() const
```

Get the active context's name. Returns NAME_None if the stack is empty.

---

#### Evaluate { #evaluate-4 }

```cpp
FComposableCameraPose Evaluate(float DeltaTime)
```

Evaluate the active context for this frame. Only the top context is ticked (unless a lower context is referenced by a reference leaf in the active context's tree, in which case it ticks through the reference). If the active context's running camera is transient and finished, auto-pops the context.

**Returns**
The final camera pose for this frame.

---

#### BuildDebugString { #builddebugstring-1 }

`const`

```cpp
void BuildDebugString(TStringBuilder< 1024 > & OutString) const
```

Build a debug string showing the full context stack state.

### Public Static Methods

| Return | Name | Description |
|--------|------|-------------|
| `void` | [`AddReferencedObjects`](#addreferencedobjects) `static` |  |

---

#### AddReferencedObjects { #addreferencedobjects }

`static`

```cpp
static void AddReferencedObjects(UObject * InThis, FReferenceCollector & Collector)
```

### Private Attributes

| Return | Name | Description |
|--------|------|-------------|
| `TArray< FComposableCameraContextEntry >` | [`Entries`](#entries)  | Stack entries in LIFO order (index 0 = base, Last() = active/top). |
| `TArray< FComposableCameraContextEntry >` | [`PendingDestroyEntries`](#pendingdestroyentries)  | Contexts that have been popped but are kept alive during their pop transition. Their Directors are still evaluated via reference leaves in the resume context's tree. Cleaned up when the transition finishes. |

---

#### Entries { #entries }

```cpp
TArray< FComposableCameraContextEntry > Entries
```

Stack entries in LIFO order (index 0 = base, Last() = active/top).

---

#### PendingDestroyEntries { #pendingdestroyentries }

```cpp
TArray< FComposableCameraContextEntry > PendingDestroyEntries
```

Contexts that have been popped but are kept alive during their pop transition. Their Directors are still evaluated via reference leaves in the resume context's tree. Cleaned up when the transition finishes.

### Private Methods

| Return | Name | Description |
|--------|------|-------------|
| `int32` | [`FindContextIndex`](#findcontextindex) `const` | Find the index of a context by name. Returns INDEX_NONE if not found. |
| `void` | [`PopActiveContextInternal`](#popactivecontextinternal)  | Internal: execute a pop of the active context with optional transition. Handles the transition setup, pending destruction, and cleanup. |

---

#### FindContextIndex { #findcontextindex }

`const`

```cpp
int32 FindContextIndex(FName ContextName) const
```

Find the index of a context by name. Returns INDEX_NONE if not found.

---

#### PopActiveContextInternal { #popactivecontextinternal }

```cpp
void PopActiveContextInternal(AComposableCameraPlayerCameraManager * PlayerCameraManager, UComposableCameraTransitionDataAsset * TransitionOverride, const FComposableCameraActivateParams & ActivationParams)
```

Internal: execute a pop of the active context with optional transition. Handles the transition setup, pending destruction, and cleanup.
