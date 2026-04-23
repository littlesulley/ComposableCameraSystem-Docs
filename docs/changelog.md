# Changelog

## 2026-04-23 — plugin `195b398..e9af064`

**Plugin commits** ([compare](https://github.com/littlesulley/ComposableCameraSystem/compare/195b3986d82aa849e03aac1a096b93ba4016f3dd...e9af064c76c180dbce61109529001b7659f843fd))

- `e9af064` Improve editor UX: inline node validation badges, details-rebuild coalescing, CCS.Editor.Dump.Graph, palette cleanup.
- `4fc9d16` Fix LS gate + pose-blend edge cases; expand Debug Panel Current Pose.

**C++ API pages regenerated:** 138 pages (full regen — 3 modified public headers: `ComposableCameraTypeAsset.h`, `ComposableCameraNodeGraph.h`, `SComposableCameraGraphNode.h`).

**Prose drafts added:** none (no new node/transition/modifier catalog entries).

**Flagged for review:**

- `ComposableCameraTypeAsset.h` changed — verify the [Data Assets](reference/api/data-assets/UComposableCameraTypeAsset.md) API page reflects any new fields or methods.
- Editor UX improvements (node validation badges, `CCS.Editor.Dump.Graph` command, palette cleanup) are not yet documented. Consider adding a section to [The Graph Editor](user-guide/graph-editor.md).

---


## 2026-04-23 — plugin `716769c..195b398`

**Plugin commits** ([compare](https://github.com/littlesulley/ComposableCameraSystem/compare/716769c2e4c709e9dec4677b877eebba8a8ae92c...195b3986d82aa849e03aac1a096b93ba4016f3dd))

- `195b398` Add runtime debug & observability subsystem.

**C++ API pages regenerated:** 138 pages (full regen — 5 new Debug headers added, 33 public headers modified across nodes, transitions, and core).

**New public headers (Debug subsystem — changelog mention only):**

- `FComposableCameraDebugPanel` — in-viewport HUD overlay showing pose, context stack, evaluation tree, actions, and modifiers. Toggled via `CCS.Debug.Panel 0|1`.
- `FComposableCameraDebugPanelData` — runtime snapshot structs (`FComposableCameraTreeNodeSnapshot`, `EComposableCameraTreeNodeKind`, etc.) consumed by the debug panel. Distinct from the editor-only `FComposableCameraDebugSnapshot`.
- `FComposableCameraLogCapture` — `FOutputDevice` ring-buffer capturing Warning/Error lines from all `LogComposableCamera*` categories for display in the debug panel's Warnings region.
- `FComposableCameraPoseHistoryEntry` — per-frame pose snapshot (position, rotation, FOV, game time, context name) used for the debug panel's sparklines and scrub tooltip. ~48 bytes × 120-entry ring buffer per PCM.
- `FComposableCameraViewportDebug` — 3D viewport debug draws (frustum, per-node gizmos). Master gate: `CCS.Debug.Viewport 0|1`; per-node CVars `CCS.Debug.Viewport.<NodeName>`.

**Prose drafts added:** none (new headers are Debug subsystem internals, not node/transition/modifier catalog entries).

**Flagged for review:**

- The [ShowDebug](reference/showdebug.md) reference page predates this subsystem — consider adding a section documenting `CCS.Debug.Panel`, `CCS.Debug.Viewport`, and the per-node viewport CVar pattern.

---

## 2026-04-21 — plugin `62ebee2..${SHORT_NEW}`

**Plugin commits** ([compare](https://github.com/littlesulley/ComposableCameraSystem/compare/62ebee2245d253eab08cf193b39be1f8f6d1041c...716769c2e4c709e9dec4677b877eebba8a8ae92c))

- `716769c` Implement PreNodeTick / PostNodeTick camera actions.

**C++ API pages regenerated:** 2 classes modified:

- `UComposableCameraActionBase` — `PreNodeTick` and `PostNodeTick` execution types are now fully implemented (removing the `@TODO` stubs). New `TargetNodeClass` field (`TSubclassOf<UComposableCameraCameraNodeBase>`) added; only shown in the Details panel when `ExecutionType` is `PreNodeTick` or `PostNodeTick`.
- `AComposableCameraCameraBase` — new `PreNodeTickActions` / `PostNodeTickActions` arrays (non-UPROPERTY hot-path cache) and `RegisterNodeAction` / `UnregisterNodeAction` methods for PCM-side bookkeeping.

**Prose drafts added:** none.

**Flagged for review:**

- The [Camera Actions](user-guide/camera-actions.md) User Guide page likely still describes `PreNodeTick` / `PostNodeTick` as "not yet implemented" — update that page to document `TargetNodeClass` usage and the exact-class-match semantics.

---

## 2026-04-20 — plugin `b3d3e0a..${SHORT_NEW}`

**Plugin commits** ([compare](https://github.com/littlesulley/ComposableCameraSystem/compare/b3d3e0a28d7fbf4e35f46d29919b1de34aff5a14...62ebee2245d253eab08cf193b39be1f8f6d1041c))

- `62ebee2` LS Phase G: ECS gate instantiator for cut/blend-only LS component tick

**C++ API pages regenerated:** 1 class modified (`UComposableCameraLevelSequenceComponent` — `OnUnregister` added, `SetEvaluationEnabled` gate semantics inverted: default is now ON; the ECS gate instantiator closes it for idle entities rather than opening it for active ones).

**Prose drafts added:** none.

**Flagged for review:**

- `SetEvaluationEnabled` gate semantics changed. The tutorial page `docs/tutorials/level-sequence-authoring.md` describes the gate as "default false / auto-enabled from OnRegister" — update that sentence to reflect the new default-ON / ECS-closes behavior.

---

## 2026-04-20 — plugin `b4521a0..b3d3e0a`

**Plugin commits** ([compare](https://github.com/littlesulley/ComposableCameraSystem/compare/b4521a02219cfc47eefe292ff3f638a6a7507ff0...b3d3e0a28d7fbf4e35f46d29919b1de34aff5a14))

- `b3d3e0a` Add Level Sequence authoring path for composable cameras.
- `9d841b1` Update README.md
- `1cecf3c` Update Level Sequence wrapper.

**C++ API pages regenerated:** 129 classes (actors +1 `AComposableCameraLevelSequenceActor`, nodes +2 `PostProcessNode`/`ViewTargetProxyNode`, transitions +1 `ViewTargetTransition`, other UObjects +2 `AsyncPlayCutsceneSequence`/`LevelSequenceComponent`, structs +1 `FComposableCameraTypeAssetReference`; deleted: `ComposableCameraKeyframeSequenceNode`)

**Prose drafts added:**

- `docs/reference/nodes.md` — entry for `UComposableCameraPostProcessNode` (please review)
- `docs/reference/nodes.md` — entry for `UComposableCameraViewTargetProxyNode` (please review)
- `docs/reference/transitions.md` — entry for `UComposableCameraViewTargetTransition` (please review)

**Other new public API:** `AsyncPlayCutsceneSequence`, `ComposableCameraTypeAssetInstantiator`, `LevelSequence/` subsystem (4 headers: actor, component, pin-type utils, type-asset reference), `ComposableCameraViewportUtils` — changelog mention only; no catalog entry added.

**Flagged for review:**

- `UComposableCameraViewTargetProxyNode` and `UComposableCameraViewTargetTransition` are marked `Hidden`/`NotBlueprintable` — internal PCM bridge classes, not designer-facing.
- `LevelSequence` subsystem adds a new public module folder; consider adding a dedicated User Guide page for the LS authoring path.

---

Reverse-chronological log of documentation updates. Each entry corresponds to a batch of plugin changes that the auto-updater skill (`ccs-docs-updater`) processed.

Entries are written automatically; feel free to edit them if you want to reword or add context.

## 2026-04-18 — plugin `92c6051..b4521a0`

**Plugin commits** ([compare](https://github.com/littlesulley/ComposableCameraSystem/compare/92c605191bfa3856cf4f1f3f96a30bb5fb7c866c...b4521a02219cfc47eefe292ff3f638a6a7507ff0))

- `b4521a0` Optimize editor, support profiling.

**C++ API pages regenerated:** 3 classes modified (0 added, 3 modified, 0 removed).

- Modified: `UComposableCameraScreenSpaceConstraintsNode`, `UComposableCameraScreenSpacePivotNode`, `UComposableCameraSplineTransition`.
- The `docs/reference/api/index.md` template intro was also refreshed by `split_api.py` (no class content change there).
- Note: the upstream commit additionally touched the public headers `ComposableCameraCameraNodeBase.h` and `ComposableCameraPivotOffsetNode.h`, but those edits did not alter any doxygen-extracted symbols, so no API pages were regenerated for them.

**Prose drafts added:** none — no new public node, transition, or modifier headers were added in this commit range, so the catalog pages (`docs/reference/nodes.md`, `transitions.md`, `modifiers.md`) were left untouched.

**Flagged for review:**

- The commit message mentions profiling support. Skim the regenerated pages for any new profiling/timing members on `ScreenSpaceConstraintsNode`, `ScreenSpacePivotNode`, and `SplineTransition`; if the project exposes a user-facing profiler toggle, consider a short note in `docs/user-guide/debugging.md` (or equivalent) — this auto-updater does not infer user-guide prose.
- No internal design docs (`Docs/DesignDoc.md`, `Docs/EditorDesignDoc.md`, `Docs/ExecutionFlowExamples.md`) changed this run, so `docs/user-guide/concepts/*.md` does not need a concepts review.

---

## 2026-04-17 — plugin `2810fd5..92c6051`

**Plugin commits** ([compare](https://github.com/littlesulley/ComposableCameraSystem/compare/2810fd5eac84f7ca98d8adb0bd05de0a7a18445d...92c605191bfa3856cf4f1f3f96a30bb5fb7c866c))

- `92c6051` Add OverridePin for ActivateCameraFromDataTable.

**C++ API pages regenerated:** 14 classes modified (0 added, 14 modified, 0 removed).

- Modified: `UComposableCameraBlueprintLibrary`, `UComposableCameraEvaluationTree`, `UComposableCameraTypeAsset`, `UComposableCameraPathGuidedTransition`, `UComposableCameraSplineTransition`, `FComposableCameraActivateParams`, `FComposableCameraEvaluationTreeLeafNodeWrapper`, `FComposableCameraEvaluationTreeReferenceLeafNodeWrapper`, `FComposableCameraExposedParameter`, `FComposableCameraNodePinDeclaration`, `FComposableCameraParameterBlock`, `FComposableCameraPose`, and the shared `Enumerations` and free-`Functions` pages.

**Prose drafts added:** none — no new public node, transition, or modifier headers were added in this commit range, so the catalog pages (`docs/reference/nodes.md`, `transitions.md`, `modifiers.md`) were left untouched.

**Flagged for review:**

- The `ActivateComposableCameraFromDataTable` K2 node gained an **override-pin** mechanism this commit (the public runtime struct `FComposableCameraActivateParams` and the `UComposableCameraBlueprintLibrary` activation helpers were updated alongside the K2 node). `docs/reference/activate-camera-from-data-table.md` was already hand-edited for this in the previous docs commit (`31e8165`), so cross-check that the documented signature still matches the regenerated `FComposableCameraActivateParams` API page.
- No internal design docs (`Docs/DesignDoc.md`, `Docs/EditorDesignDoc.md`, `Docs/ExecutionFlowExamples.md`) changed this run, so `docs/user-guide/concepts/*.md` does not need a concepts review.

---

## 2026-04-16 — plugin `775fc66..2810fd5`

**Plugin commits** ([compare](https://github.com/littlesulley/ComposableCameraSystem/compare/775fc660c1a132c4549daa774d137f631926c4be...2810fd5eac84f7ca98d8adb0bd05de0a7a18445d))

- `2810fd5` Optimize pins; add more nodes; support complex camera pose parameters; add FName and Enum pin support.

**C++ API pages regenerated:** 39 classes changed (5 added, 32 modified, 2 removed).

- Added: `UComposableCameraFilmbackNode`, `UComposableCameraLensNode`, `UComposableCameraOrthographicNode`, `FComposableCameraNodePinBinding`, `FComposableCameraNodePinBindingTable`.
- Removed: `UComposableCameraComputeRandomOffsetNode`, `UComposableCameraFixedPoseNode` (headers deleted upstream).

**Prose drafts added:** none — `docs/reference/nodes.md` already contains hand-authored entries for all three new nodes (`LensNode`, `FilmbackNode`, `OrthographicNode`), so no auto-drafted stubs were appended.

**Flagged for review:**

- `docs/reference/nodes.md` still contains prose sections for `FixedPoseNode` (line 16) and `ComputeRandomOffsetNode` (line 177) whose underlying headers were deleted in this commit range. Either confirm the nodes still exist under a different name or remove/update those prose entries.
- New `FComposableCameraNodePinBinding` / `FComposableCameraNodePinBindingTable` structs appeared alongside the "FName and Enum pin support" commit. Consider whether pin-binding authoring deserves a short section in `docs/user-guide/authoring-camera-types.md`.

---

## 2026-04-15 — initial baseline at plugin `775fc66`

Documentation site and auto-update pipeline established. The C++ API reference under `reference/api/` reflects plugin `dev-v1` at commit `775fc66` ("Refactor everything with AI."). Subsequent changes will appear above this entry.
