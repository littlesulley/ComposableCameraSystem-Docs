
# FComposableCameraPatchSnapshot { #fcomposablecamerapatchsnapshot }

```cpp
#include <ComposableCameraDebugPanelData.h>
```

One active Camera Patch surfaced for the Debug Panel / dump commands. Produced by either `[UComposableCameraPatchManager::BuildDebugSnapshot](../uobjects-other/UComposableCameraPatchManager.md#builddebugsnapshot-2)` (BP path, one snapshot per active director) or `[UComposableCameraLevelSequenceComponent::BuildSequencerPatchSnapshot](../uobjects-other/UComposableCameraLevelSequenceComponent.md#buildsequencerpatchsnapshot)` (Sequencer path, one snapshot per LS Component overlay). The two are merged into a single list in `BuildPatchesLines`; `Source` distinguishes them in the row label.

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `FString` | [`AssetName`](#assetname)  | Patch asset display name; "(missing)" if the weak ptr resolved null. |
| `int32` | [`LayerIndex`](#layerindex-1)  | Effective layer index (resolved from asset default + AddPatch override). |
| `int8` | [`Phase`](#phase-1)  | Lifecycle phase (0 = Entering, 1 = Active, 2 = Exiting, 3 = Expired). Stored as int8 to keep the snapshot decoupled from the runtime enum. For Sequencer-source entries this is always Active (1) since the envelope is stateless and alpha alone carries phase semantics. |
| `float` | [`Alpha`](#alpha)  | Current effect alpha — drives BlendBy(InputPose, Evaluated, alpha). |
| `float` | [`ElapsedInPhase`](#elapsedinphase-1)  | Time spent in the current Phase (resets on every transition). 0 for Sequencer-source entries (no stateful phase tracking). |
| `float` | [`ElapsedTimeActive`](#elapsedtimeactive-1)  | Time spent in Active phase total (drives the Duration channel). 0 for Sequencer-source entries. |
| `float` | [`EnterDuration`](#enterduration-1)  | Authored EnterDuration / ExitDuration (in seconds) for ramp progress display. |
| `float` | [`ExitDuration`](#exitduration-1)  |  |
| `float` | [`Duration`](#duration-6)  | Active-phase Duration cap (0 if Duration channel is not enabled). For Sequencer-source entries this is the section's range converted to seconds. |
| `uint8` | [`ExpirationType`](#expirationtype-2)  | Bitmask of EComposableCameraPatchExpirationType — what channels can fire. For Sequencer-source entries this is always 0 (section's TrueRange is the lifetime; no per-channel expiration semantics). |
| `bool` | [`bExpireOnCameraChange`](#bexpireoncamerachange-1)  | Auxiliary "expire when running camera changes" flag. False for Sequencer-source entries. |
| `EComposableCameraPatchSource` | [`Source`](#source)  | Where this entry came from. Drives the Debug Panel row's source-tag prefix ("[BP]" vs "[Seq]") so designers can tell which path is producing each visible patch. |
| `FString` | [`HostActorName`](#hostactorname)  | For Sequencer-source entries, the bound LS Actor's display name — empty for BP-source entries. Lets the panel show "[Seq] Asset on Actor" when there are multiple LS Actors with overlapping patches. |

---

#### AssetName { #assetname }

```cpp
FString AssetName
```

Patch asset display name; "(missing)" if the weak ptr resolved null.

---

#### LayerIndex { #layerindex-1 }

```cpp
int32 LayerIndex = 0
```

Effective layer index (resolved from asset default + AddPatch override).

---

#### Phase { #phase-1 }

```cpp
int8 Phase = 0
```

Lifecycle phase (0 = Entering, 1 = Active, 2 = Exiting, 3 = Expired). Stored as int8 to keep the snapshot decoupled from the runtime enum. For Sequencer-source entries this is always Active (1) since the envelope is stateless and alpha alone carries phase semantics.

---

#### Alpha { #alpha }

```cpp
float Alpha = 0.f
```

Current effect alpha — drives BlendBy(InputPose, Evaluated, alpha).

---

#### ElapsedInPhase { #elapsedinphase-1 }

```cpp
float ElapsedInPhase = 0.f
```

Time spent in the current Phase (resets on every transition). 0 for Sequencer-source entries (no stateful phase tracking).

---

#### ElapsedTimeActive { #elapsedtimeactive-1 }

```cpp
float ElapsedTimeActive = 0.f
```

Time spent in Active phase total (drives the Duration channel). 0 for Sequencer-source entries.

---

#### EnterDuration { #enterduration-1 }

```cpp
float EnterDuration = 0.f
```

Authored EnterDuration / ExitDuration (in seconds) for ramp progress display.

---

#### ExitDuration { #exitduration-1 }

```cpp
float ExitDuration = 0.f
```

---

#### Duration { #duration-6 }

```cpp
float Duration = 0.f
```

Active-phase Duration cap (0 if Duration channel is not enabled). For Sequencer-source entries this is the section's range converted to seconds.

---

#### ExpirationType { #expirationtype-2 }

```cpp
uint8 ExpirationType = 0
```

Bitmask of EComposableCameraPatchExpirationType — what channels can fire. For Sequencer-source entries this is always 0 (section's TrueRange is the lifetime; no per-channel expiration semantics).

---

#### bExpireOnCameraChange { #bexpireoncamerachange-1 }

```cpp
bool bExpireOnCameraChange = false
```

Auxiliary "expire when running camera changes" flag. False for Sequencer-source entries.

---

#### Source { #source }

```cpp
EComposableCameraPatchSource Source = 
```

Where this entry came from. Drives the Debug Panel row's source-tag prefix ("[BP]" vs "[Seq]") so designers can tell which path is producing each visible patch.

---

#### HostActorName { #hostactorname }

```cpp
FString HostActorName
```

For Sequencer-source entries, the bound LS Actor's display name — empty for BP-source entries. Lets the panel show "[Seq] Asset on Actor" when there are multiple LS Actors with overlapping patches.
