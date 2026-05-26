# Changelog

Reverse-chronological log of documentation updates.

## 2026-05-25 - plugin `8b7fd10..21214d7`

**Plugin commits processed:** `21214d7` (`Update README.md`). Fetch/pull was attempted first for both repositories, but both were blocked by `cannot open '.git/FETCH_HEAD': Permission denied`. The plugin working tree has a pre-existing local binary asset edit in `Content/CameraPresets/Preset_Cameras/Camera_BasicThirdPerson.uasset`, which was preserved.

**C++ API reference:** no public headers changed in this range, so Doxygen/moxygen regeneration was not required and no generated API pages were touched.

**Prose updates:** added the README's YouTube tutorial link to the Getting Started resource section. The docs home page already contained the tutorial link, so it did not need a new section.

**New-feature documentation decision:** this range only adds an external tutorial resource link. It does not introduce a new code feature, node, transition, modifier, Blueprint/K2 node, editor tool, setting, console command, or asset workflow, so no new feature page was needed.

**Validation / deployment:** `python -m mkdocs build --strict` reached content generation but was blocked by the sandbox's Mermaid CDN network warning; plain `python -m mkdocs build` passed. Commit and push status is tracked by the automation run summary.

---

## 2026-05-21 - plugin `6a7fe1d..8b7fd10`

**Plugin commits processed:** `689a379` (`Add GNU General Public License v3`), `59e698c` (`Update README`), `3e8df0f` (`Update`), `a85aa01` (`Add Fab copyright headers`), `ee812b6` (`Fix Fab unity build private symbol collisions`), `1d3fc90` (`Remove deprecated StructUtils dependency`), `8e7d96c` (`Remove null bytes from camera director header`), `2e5f525` (`Fix Fab review build issues`), `72d0da2` (`Remove concepts dependency from inertializer checks`), `478b473` (`Fix Fab compile compatibility with UE 5.7`), and `8b7fd10` (`Add Fab Page link to README`). Fetch/pull was attempted first for both repositories, but both were blocked by `cannot open '.git/FETCH_HEAD': Permission denied`; Documentation also had a pre-existing local newline-only edit in `docs/getting-started/enabling-plugin.md`, which was preserved.

**C++ API reference:** public headers changed, mostly for copyright normalization, removing a stray `ComposableCameraDirector.h~`, replacing the inertializer helper's C++20 `requires` usage with type-trait static assertions, and renaming anonymous-namespace helpers to avoid Fab unity-build collisions. Formal Doxygen/moxygen regeneration could not run because `doxygen` and `moxygen` are not installed locally. No new public classes, functions, Blueprint/K2 nodes, camera nodes, transitions, modifiers, editor tools, or asset workflows were added in this range, so no generated-style API page content required a manual semantic update.

**Prose updates:** added the Fab listing to the installation/getting-started path, updated engine support wording from UE 5.6-only to UE 5.6-or-newer with UE 5.7/Fab compatibility, refreshed the demo link wording from the README, and added FAQ troubleshooting for generated `Module.*.cpp` unity-build diagnostics and anonymous-namespace helper collisions.

**New-feature documentation decision:** this range is release/distribution and build-compatibility maintenance rather than a new designer-facing feature. The new internal `Docs/FabUnityBuildTroubleshooting.md` content fits the existing FAQ/troubleshooting page instead of a standalone public guide; deleted content-browser icon files were moved under `Resources/Content`, so existing asset-icon wording remains valid.

**Validation / deployment:** `python -m mkdocs build --strict` reached content generation but was blocked by the existing Mermaid CDN network warning in this sandbox; plain `python -m mkdocs build` passed. Commit/push status is tracked by the automation run summary.

---

## 2026-05-16 - plugin `3376bb6..6a7fe1d`

**Plugin commits processed:** `b277032` (`feat: add pivot look-ahead node`), `803213e` (`docs: design lock-on aim point node`), `ddc176b` (`Add lock-on aim point node`), `0ded747` (`Fix fixed-step IIR interpolation`), and `6a7fe1d` (`Lock transition rotation blend paths`). Fetch/pull was attempted first for both repositories; the plugin fetch/pull remains blocked by `cannot open '.git/FETCH_HEAD': Permission denied`, and Documentation fetch remains blocked by unavailable GitHub network access in this sandbox.

**C++ API reference:** public headers changed. Formal Doxygen/moxygen regeneration could not run because `doxygen` and `moxygen` are not installed locally, so affected pages were updated manually. Added generated-style API pages for `UComposableCameraLockOnAimPointNode` and `FComposableCameraLockOnAimPointState`, linked them from the API index/nav, added `EComposableCameraLockOnAimPointSource`, documented `ComposableCameraSystem::ComputeLockOnAimPoint`, refreshed `UComposableCameraTransitionBase` for locked rotation-path helpers/state, and clarified `UComposableCameraIIRInterpolator::bUseFixedStep`.

**Prose updates:** expanded the Node Catalog with `LockOnAimPointNode`, updated Actor Input Sources for the node's follow/aim actor selectors, added `CCS.Debug.Viewport.LockOnAimPoint` to debugging references, documented built-in transition rotation path locking in the transition concept, user guide, catalog, and custom-transition extension recipe, and refreshed the Camera Presets catalog so all shipped camera type presets are listed, including `Camera_BasicLockOn`.

**New-feature documentation decision:** `LockOnAimPointNode` is a designer-facing Pivot node and fits the existing Node Catalog, Actor Input Sources reference, Debugging guide, and API reference rather than a standalone tutorial. Transition rotation-path locking and the fixed-step IIR correction are behavior refinements to existing systems, so they were documented in transition/interpolator references instead of new pages.

**Validation / deployment:** `python -m mkdocs build --strict` reached content generation but was blocked by the existing Mermaid CDN network warning in this sandbox; plain `python -m mkdocs build` passed. Push/remote freshness follow-up remains required because the sandbox cannot reach GitHub and the plugin repo cannot update `FETCH_HEAD`.

---

## 2026-05-15 - plugin `3376bb6` + local workspace changes

**Plugin changes processed:** `.last-documented-sha` already matched local plugin HEAD `3376bb6`, but the working tree contains an uncommitted public-header/source addition for `UComposableCameraPivotLookAheadNode` plus local internal-doc edits and a camera preset asset. Fetch/pull was attempted first for both repositories; the plugin fetch was blocked by `cannot open '.git/FETCH_HEAD': Permission denied`, and Documentation fetch was blocked by unavailable GitHub network access in this sandbox.

**C++ API reference:** public headers changed in the workspace. Formal Doxygen/moxygen regeneration could not run because `doxygen` and `moxygen` are not installed locally, so the affected API page was added manually: `UComposableCameraPivotLookAheadNode` now documents its velocity actor source, explicit velocity actor, look-ahead timing, velocity damping, output pivot, and debug draw hook. The API index/nav now link the page, and `ResolveActorInput` was refreshed for its optional world-context fallback parameter.

**Prose updates:** expanded the Node Catalog with `PivotLookAheadNode`, updated Actor Input Sources for `VelocityActorSource`, and added `CCS.Debug.Viewport.PivotLookAhead` to both the user-facing debugging guide and the debug reference CVar table.

**New-feature documentation decision:** Pivot look-ahead is a designer-facing Pivot node and fits the existing Node Catalog, Actor Input Sources reference, Debugging guide, and generated-style API reference. It does not need a standalone tutorial until the feature lands in a committed preset or broader camera recipe.

**Validation / deployment:** `python -m mkdocs build --strict` reached content generation but was blocked by the existing Mermaid CDN network warning in this sandbox; plain `python -m mkdocs build` passed. A local Documentation commit was created after elevated Git access allowed staging; push requires explicit approval for the configured `origin` remote.

---

## 2026-05-14 - plugin `8907715..3376bb6`

**Plugin commits processed:** `3376bb6` (`Fix composable camera graph rotation and compute routing`) on the local `dev-v1` branch. Fetch/pull was attempted first for both the plugin and Documentation repositories, but both were blocked by `cannot open '.git/FETCH_HEAD': Permission denied`; the run used the existing clean local checkouts.

**C++ API reference:** public headers changed. Formal Doxygen/moxygen regeneration could not run because `doxygen` and `moxygen` are not installed locally, so affected API pages were updated manually. Added `UComposableCameraSetRotationNode` and `UComposableCameraBeginPlaySetRotationNode`, linked them from the API index/nav, added `EComposableCameraSetRotationSource`, refreshed compute-node base prose, and updated changed API fields for rotation constraints, pivot offset actor references, build-message chain targeting, and variable-node connection chain ownership.

**Prose updates:** expanded the node catalog for `SetRotationNode` and `BeginPlaySetRotationNode`, removed the stale `ComputeRandomOffsetNode` catalog entry, corrected the compute-node base method name to `ExecuteBeginPlay`, updated the custom-node extension guide, updated the Graph Editor palette wording, and added the new rotation actor-source row to the Actor Input Sources reference.

**New-feature documentation decision:** the new rotation-setting camera/compute nodes fit the existing Node Catalog and API reference rather than requiring a standalone guide. The compute routing fixes were treated as stale-doc cleanup in the graph/editor and API pages because they refine existing variable and BeginPlay-chain behavior.

**Validation / deployment:** `python -m mkdocs build --strict` reached content generation but was blocked by the existing Mermaid CDN network warning in this sandbox; plain `python -m mkdocs build` passed. Commit and push were blocked because Git could not create `Documentation/.git/index.lock` (`Permission denied`).

---

## 2026-05-14 - plugin `b9f1885..8907715`

**Plugin commits processed:** `8907715` (`Fix SpinBox drag on node-template detail rows and sync dev-v1`). Fetch/pull for both repositories was attempted first and succeeded after sandbox escalation; both were already up to date. The plugin working tree has two already-staged camera preset assets, which were preserved untouched.

**C++ API reference:** public headers changed. Formal Doxygen/moxygen regeneration could not run because `doxygen` and `moxygen` are not installed in this sandbox, so the affected new API page was added manually: `UComposableCameraExposureNode` documents ISO, shutter speed, and exposure blend weight pins/properties, and the API nav/index now link it.

**Prose updates:** expanded the node catalog with `ExposureNode`, clarified that `LensNode` owns lens/DoF while exposure owns ISO/shutter, and documented the Manual + Apply Physical Camera Exposure level setup requirement. Updated the Graph Editor page to describe canvas-position ordering for fully unwired camera graphs and the warning behavior for orphaned nodes in non-empty exec chains.

**New-feature documentation decision:** `ExposureNode` is a user-facing Optics node and belongs in the existing Node Catalog rather than a standalone page. The SpinBox drag fix is an editor usability bug fix; no public workflow page was needed beyond avoiding stale wording around detail-row editing. The node-template canvas ordering change is documented in the Graph Editor page because it changes authoring behavior for patches and unwired camera graphs.

**Validation / deployment:** `python -m mkdocs build --strict` reached content generation but was blocked by the existing Mermaid CDN network warning in this sandbox; plain `python -m mkdocs build` passed. Commit and push succeeded so GitHub Pages can deploy from the Documentation remote.

---

## 2026-05-13 — plugin `3be0fa0..b9f1885`

**Plugin commits** ([compare](https://github.com/littlesulley/ComposableCameraSystem/compare/3be0fa0bf58f3c7dbc8aab48bdb9a05b5938cd04...b9f1885df2fd209106b85bc91bc5d36a9e740c11))

- `b9f1885` Fix shot zone overlay and blend cache handoff

**C++ API pages updated:** 2 pages revised (no new classes added)

- `docs/reference/api/nodes/UComposableCameraCompositionFramingNode.md` — `SetActiveShotsFromSequencer` signature gains `bPrimaryWasPreviousSecondary` and `bSecondaryChanged` parameters; parameter descriptions updated to reflect blend cache promotion vs. hard-cut reseed semantics.
- `docs/reference/api/uobjects-other/UComposableCameraLevelSequenceComponent.md` — new `LastActiveSecondarySection` private field documented; `LastActivePrimarySection` description updated.

**Prose drafts added:** none (no new node/transition/modifier classes)

**Flagged for review:**

- `DesignDoc.md` last updated 2026-05-06 — predates this commit (2026-05-12). Check §Blend-cache handoff / overlap-exit behaviour sections against current code.
- `EditorDesignDoc.md` last updated 2026-05-11 — also predates commit. Likely unaffected (change is runtime-only), but confirm.

---

## 2026-05-12 - plugin `55ea759..3be0fa0`

**Plugin commits processed:** `ff75cbc` (`Restore camera preset assets`) and `3be0fa0` (`Add Sequencer camera authoring tools`) on the local `dev-v1` branch. Repository synchronization was attempted first for both the plugin and Documentation repositories, but both fetch/pull operations were blocked by `cannot open .git/FETCH_HEAD: Permission denied`; this run used the existing clean local HEADs.

**C++ API reference:** public headers changed. Formal Doxygen/moxygen regeneration could not run because `doxygen` and `moxygen` are not installed in this sandbox, so affected API pages were updated manually: `UComposableCameraDirectionalMoveNode` now includes `Duration`, `UComposableCameraLevelSequenceComponent` reflects Spawn Track lifetime semantics, Sequencer-aware delta-time helpers, and removal of the no-op parameter/variable setter hooks, `UMovieSceneComposableCameraPatchSection` no longer references the removed ECS gate model, `AComposableCameraCameraBase` no longer describes gate warm-up edge cases, and new `FGetEditorSequencerPlaybackDeltaTime` API navigation was added.

**Prose updates:** expanded the CCS Camera in Sequencer and Shot-Based Keyframing tutorials with the new **Key Spawn Tracks From Camera Cuts** command, `CCS.Editor.KeySpawnTracksFromCameraCuts`, and viewport transform utilities (`Ctrl+Alt+C` copy, `Ctrl+Alt+K` key selected CCS transform tracks). Updated the node catalog for `DirectionalMoveNode.Duration`.

**New-feature documentation decision:** the new Sequencer tools were documented inside the existing Sequencer authoring tutorials rather than a new page because they are workflow accelerators for the existing Level Sequence and Shot Actor paths. The Spawn Track lifetime change was treated as stale-doc cleanup across tutorials and API prose.

**Validation / deployment:** `python -m mkdocs build --strict` reached content generation but was blocked by the existing Mermaid CDN network warning in this sandbox; plain `python -m mkdocs build` passed. Commit and push were blocked because Git cannot create `Documentation/.git/index.lock` in this sandbox; earlier fetch/pull attempts were also blocked by `.git/FETCH_HEAD` permission errors. Manual follow-up remains to rerun the Doxygen/moxygen API workflow in an environment with those tools installed.

---

## 2026-05-11 - plugin `332f3e9..55ea759`

**Plugin commits processed:** `55ea759` (`Improve shot authoring workflow and presets`) on the local `dev-v1` branch. Repository synchronization was attempted first for both the plugin and Documentation repositories, but both fetches were blocked by `cannot open .git/FETCH_HEAD: Permission denied`; this run used the existing local HEADs and preserved existing Documentation working-tree edits.

**C++ API reference:** public headers changed. Formal Doxygen/moxygen regeneration could not run because `doxygen` and `moxygen` are not installed in this sandbox, so the affected API pages were updated manually: added `UComposableCameraDirectionalMoveNode` and `UComposableCameraTwoPointMoveNode`, linked them from the API nav/index, refreshed `FComposableCameraTargetInfo` for editor preview mesh/transform fields, refreshed `UMovieSceneComposableCameraShotSection` for `ShotOverrides` and section-local authoring, updated `EComposableCameraShotSource` and `UComposableCameraShotAsset` wording, and corrected ShotSolver / `FShotPlacement` docs for the first-frame `AnchorAtScreen + LookAtAnchor` joint seed path.

**Prose updates:** expanded the Shot-Based Keyframing tutorial to document AssetReference copy-on-pick behavior, section-local `ShotOverrides`, editor-only target preview meshes/transforms, and target binding override behavior. Expanded the node catalog for `DirectionalMoveNode` and `TwoPointMoveNode`.

**New-feature documentation decision:** the two new move nodes are designer-facing Position nodes and now have node catalog entries plus API pages. Shot Asset authoring changes are documented in the Sequencer tutorial and Shot Section API page rather than a new standalone page because they refine the existing Shot-Based Keyframing workflow. The solver seed change was treated as stale-reference/API cleanup because it changes activation behavior, not the authoring surface.

**Validation / deployment:** `python -m mkdocs build --strict` reached content generation but was blocked by the existing Mermaid CDN network warning in this sandbox; plain `python -m mkdocs build` passed. Commit and push were blocked because Git cannot write `Documentation/.git/index.lock` in this sandbox; earlier fetch/pull attempts were also blocked by `.git/FETCH_HEAD` permission errors.

---

## 2026-05-10 - C++ API actor source reference follow-up

**Plugin commits processed:** `2785600..332f3e9`, covering `Add controller pawn actor source option`.

**C++ API reference:** updated generated API markdown manually because local Doxygen/moxygen tooling is unavailable. Added `EComposableCameraActorInputSource`, `ComposableCameraSystem::ResolveActorInput`, the new `*ActorSource` public attributes for affected camera nodes and rotation constraints, `LastEffectivePivotActor`, and the current `EnsureInputBinding(AActor * EffectiveRotationInputActor)` signature.

**New-feature documentation decision:** prose docs for controller-controlled-pawn actor sources already exist in `docs/reference/actor-input-sources.md`; this follow-up only brings stale C++ reference node definitions back in line with the public headers.

**Validation:** checked the public-header actor-source field list against API docs. `mkdocs build --strict` reached content generation but was blocked by the existing Mermaid CDN network warning in this sandbox; plain `mkdocs build` passed.

---

## 2026-05-09 — plugin `2785600..332f3e9`

**Plugin commits processed:** `332f3e9` (`Add controller pawn actor source option`) on the local `dev-v1` branch. Repository synchronization was attempted first, but the plugin fetch was blocked by `.git/FETCH_HEAD` permission denial and the Documentation fetch was blocked by unavailable GitHub network access in this environment.

**New-feature documentation:** added `docs/reference/actor-input-sources.md` and linked it from the Reference nav. The page documents `EComposableCameraActorInputSource`, `ExplicitActor` vs `ControllerControlledPawn`, affected nodes, Sequencer caveats, and migration guidance.

**Prose updates:** expanded `docs/reference/nodes.md`, `docs/getting-started/your-first-camera.md`, `docs/tutorials/follow-camera.md`, and `docs/user-guide/authoring-camera-types.md` so gameplay camera workflows mention the controller-controlled-pawn shortcut while preserving the explicit actor workflow for reusable, AI, cutscene, and Sequencer-driven cameras.

**C++ API pages:** public headers changed, but formal Doxygen/moxygen regeneration could not run because neither `doxygen` nor `moxygen` is installed in this sandbox. The generated API reference was left unchanged to avoid unsafe manual regeneration drift. Manual follow-up: rerun `Documentation/Doxyfile`, `tools/split_api.py`, and `tools/build_api_nav.py` in an environment with those tools, then advance `.last-documented-sha`.

---

## 2026-05-09 — MkDocs Windows URL warning fix

**Build fix:** normalized mkdocs-shadcn raw Markdown URLs to POSIX-style paths on Windows and guarded custom sidebar index links against backslash URLs. This removes the MkDocs 1.6 warning `Path ... uses OS-specific separator '\'` during local builds.

**Validation:** `python -m mkdocs build --strict` passes when the Mermaid CDN URL check is allowed to access the network.

---

## 2026-05-09 — plugin `2785600` docs follow-up

**Plugin commits processed:** no new local plugin commits since `.last-documented-sha` (`2785600721920a81b2a6914f7bea071c98988922`). Repository fetch/pull for both the plugin and Documentation repos was attempted first but blocked by `Permission denied` when Git tried to update `.git/FETCH_HEAD`; the working trees were clean and this pass used the existing local HEADs.

**C++ API pages regenerated:** not regenerated; no public-header delta was detected between `.last-documented-sha` and local plugin HEAD.

**Prose updates:**

- Added `docs/tutorials/shot-based-keyframing.md`, a new Sequencer workflow tutorial for `AComposableCameraLevelSequenceShotActor`, Composable Camera Shot Track, Shot Editor modes, Placement/Aim/Lens/Focus layers, target binding overrides, inter-Shot overlap transitions, and Shot Zone debugging.
- Added the new tutorial to `mkdocs.yml` and `docs/tutorials/index.md`.
- Expanded `docs/reference/nodes.md` for `CompositionFramingNode` and removed the auto-draft review note.
- Removed the auto-draft review note from `docs/reference/debugging/debug-panel.md`'s Shot Zone Overlay section.

**Stale-doc fixes:**

- Updated `docs/tutorials/level-sequence-authoring.md` to stop saying `AComposableCameraLevelSequenceActor` is `NotPlaceable`; it is now placeable and still supports Spawnable/Possessable Sequencer use.
- Updated Shot Track / Shot Section API reference overview prose so it describes current overlap + `EnterTransition` blending instead of treating Phase F as future work.

**Manual follow-up:** plugin header comments for `UMovieSceneComposableCameraShotTrack` still contain older Phase-F-future wording; the Documentation API overview was corrected manually, but a future plugin-source cleanup plus normal API regeneration would make that fix durable.

---

## 2026-05-09 — plugin `0021823..2785600`

**Plugin commits** ([compare](https://github.com/littlesulley/ComposableCameraSystem/compare/00218233c9d80a262ae25b0c27f0236039f482db...2785600721920a81b2a6914f7bea071c98988922))

- `2785600` Fix plugin packaging for shipping builds
- `9cbb343` Harden public-API nullptr guards across PCM, Director, and EvaluationTree
- `c3e14fd` Add typed struct storage, typed K2 setter dispatch, and full enum picker
- `51debc2` Port three-layer K2 reconstruction safety to AddCameraPatch + FromDataTable
- `791cd96` Add GC-safe Actor/Object mirrors and widen struct pins to POD-friendly auto-detection
- `7330930` Fix intermittent orphan pin on K2Node_ActivateComposableCamera cold restart
- `68ed0cd` Fix LS Shot CineCam-at-origin on PIE cut into Shot-driven LSActor
- `61534f9` Add V2.2 Shot Solver: framing zones + five-axis damping + decoupled AnchorAtScreen + LS overlay + cut hardening
- `07208d8` Add Shot-Based Keyframing system: Shot data model, Composition Solver, CompositionFramingNode runtime, LS Shot Section/Track/TrackInstance, full Shot Editor

**C++ API pages regenerated:** 182 pages (26 pages added: Shot data model classes, ShotSolver, CompositionFramingNode, ShotZoneOverlay, LevelSequenceShotActor, MovieSceneShot Section/Track, and related structs)

**Prose drafts added:**

- `docs/reference/nodes.md` — entry for `UComposableCameraCompositionFramingNode` (please review)

**Flagged for review:**

- Design docs (DesignDoc.md, EditorDesignDoc.md, TechDoc.md, ExecutionFlowExamples.md) last updated before commit date 2026-05-07 — check `docs/user-guide/concepts/*.md` and `docs/reference/` pages against the Shot-Based Keyframing system additions (Shot data model, Composition Solver pipeline, LS Shot integration, Shot Editor).
- New Shot-Based Keyframing feature is large (9 commits, ~26 new public headers) — `docs/user-guide/` may need a dedicated tutorial/guide page.

---


## 2026-04-26 — plugin `1f6fc9d..0021823`

**Plugin commits** ([compare](https://github.com/littlesulley/ComposableCameraSystem/compare/1f6fc9d29bfb15773d16c9dd47b57d5f0fc5f13b...00218233c9d80a262ae25b0c27f0236039f482db))

- `0021823` Add PivotRotate node; per-category palette nesting in camera editor.

**C++ API pages regenerated:** 156 pages (1 class added: `UComposableCameraPivotRotateNode`; all existing node headers updated with `PaletteCategory` field)

**Prose drafts added:**

- `docs/reference/nodes.md` — entry for `PivotRotateNode` (please review)

**Design docs status:** DesignDoc.md, EditorDesignDoc.md, TechDoc.md confirmed in sync (Last updated 2026-04-26 ≥ commit date 2026-04-26). ExecutionFlowExamples.md has no Last updated header — no new flow patterns detected in this commit.

---

## 2026-04-26 — plugin `145a2e9..1f6fc9d`

**Plugin commits** ([compare](https://github.com/littlesulley/ComposableCameraSystem/compare/145a2e9c9d4490517c56308367049f1d13eb1406...1f6fc9d29bfb15773d16c9dd47b57d5f0fc5f13b))

- `1f6fc9d` Add Patch Sequencer integration: track / section / track-instance, LS Component overlay, channel-keyable parameters, dilation-on-resize, debug observability, authoring polish.
- `c89d99c` Add Camera Patch system: type asset, runtime PatchManager with envelope/schedule/layer ordering, K2 node + BP API, debug HUD, per-node compatibility validation.

**C++ API pages regenerated:** 155 pages across 18 categories (includes 9 new Patch-system headers and 2 new MovieScene headers).

**Prose drafts added:**

- `docs/reference/patches.md` — new Camera Patch Catalog page (auto-drafted; covers `UComposableCameraPatchTypeAsset`, `UComposableCameraPatchManager`, `UComposableCameraPatchHandle`, lifecycle enums/structs, Sequencer track/section, and envelope math). Please review and expand with usage examples.

**Flagged for review:**

- `DesignDoc.md` last-updated date (`2026-04-25`) predates the commit date (`2026-04-26`). The Patch system is a significant runtime addition — check that `Docs/DesignDoc.md` fully covers `PatchManager` integration into the Director evaluation path, context-stack teardown semantics for patches, and the staged rollout (Stage 1 = no-op Apply; Stage 2 = Director::Evaluate wiring).
- `ExecutionFlowExamples.md` has no "Last updated" header — verify manually whether a Patch activation/expiry flow example should be added.
- Node patch-compatibility validation (`GetPatchCompatibility()` enum) is referenced in headers as a future staging step (`PatchSystemProposal §11 / §19`) but not yet implemented. Consider adding a "coming soon" note to `docs/reference/patches.md` once the enum lands.
- `UComposableCameraLevelSequenceComponent` gained a Sequencer overlay surface (`SetSequencerPatchOverlay`). If `docs/user-guide/` has a Level Sequence integration page, check it reflects the new per-frame overlay tick.

---

## 2026-04-24 — plugin `e9af064..145a2e9`

**Plugin commits** ([compare](https://github.com/littlesulley/ComposableCameraSystem/compare/e9af064c76c180dbce61109529001b7659f843fd...145a2e9c9d4490517c56308367049f1d13eb1406))

- `145a2e9` Add FocusPull, HitchcockZoom, OcclusionFade, Spiral, VolumeConstraint nodes; extend AutoRotate and K2 activation.

**C++ API pages regenerated:** 145 pages (+7 new: FocusPullNode, HitchcockZoomNode, OcclusionFadeNode, SpiralNode, VolumeConstraintNode + 2 supporting structs; 1 modified: AutoRotateNode).

**Prose drafts added:**

- `docs/reference/nodes.md` — entry for `UComposableCameraFocusPullNode` (please review)
- `docs/reference/nodes.md` — entry for `UComposableCameraHitchcockZoomNode` (please review)
- `docs/reference/nodes.md` — entry for `UComposableCameraOcclusionFadeNode` (please review)
- `docs/reference/nodes.md` — entry for `UComposableCameraSpiralNode` (please review)
- `docs/reference/nodes.md` — entry for `UComposableCameraVolumeConstraintNode` (please review)

**Design-doc sync:**

- `DesignDoc.md` — Last updated 2026-04-24 ✓ in sync
- `TechDoc.md` — Last updated 2026-04-24 ✓ in sync
- `EditorDesignDoc.md` — Last updated 2026-04-23, commit date 2026-04-24 — **flagged for review**: may not reflect graph schema changes in this commit (editor-side changes to NodeGraphSchema and EditorToolkit were included).
- `ExecutionFlowExamples.md` — No "Last updated" header found — **flagged for review**: verify it doesn't need a new flow example for the new cinematic/effects nodes.

---

## 2026-04-23 — plugin `195b398..e9af064`

**Plugin commits** ([compare](https://github.com/littlesulley/ComposableCameraSystem/compare/195b3986d82aa849e03aac1a096b93ba4016f3dd...e9af064c76c180dbce61109529001b7659f843fd))

- `e9af064` Improve editor UX: inline node validation badges, details-rebuild coalescing, CCS.Editor.Dump.Graph, palette cleanup.
- `4fc9d16` Fix LS gate + pose-blend edge cases; expand Debug Panel Current Pose.

**C++ API pages regenerated:** 138 pages (full regen — 3 modified public headers: `ComposableCameraTypeAsset.h`, `ComposableCameraNodeGraph.h`, `SComposableCameraGraphNode.h`).

**Prose drafts added:** none (no new node/transition/modifier catalog entries).

**Design-doc sync:** DesignDoc.md, EditorDesignDoc.md, and TechDoc.md all confirmed updated to 2026-04-23 — in sync with the commit date.

**Public-site updates applied in this commit:**

- `docs/reference/debugging/debug-panel.md` — Current Pose section rewritten: two-column four-group layout (Transform / Context / Projection / Physical) + Physical group CineCamera fallback path (commit `4fc9d16`).
- `docs/reference/debugging/debug-panel.md` — Modifiers section updated from placeholder to structured Effective + All view.
- `docs/reference/debugging/debug-panel.md` — Camera Actions section updated to three-line-per-action view.
- `docs/reference/debugging/debug-panel.md` — `CCS.Editor.Dump.Graph` editor dump command documented.
- `docs/user-guide/graph-editor.md` — Inline validation-badge description corrected (top-right of node title bar, not beside pins).

**Flagged for review:**

- `UComposableCameraTypeAsset` API page — header modified; verify the generated page reflects any new public fields or methods.

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
