# API Reference

Auto-generated C++ reference for the ComposableCameraSystem plugin runtime module.

!!! info "Regeneration"
    This section is regenerated from the plugin headers via Doxygen + moxygen. The source of truth is the code; this page mirrors it.

## Core Runtime

Context stack, evaluation tree, director, modifier manager.

- [`UComposableCameraContextStack`](core/UComposableCameraContextStack.md)
- [`UComposableCameraDirector`](core/UComposableCameraDirector.md)
- [`UComposableCameraEvaluationTree`](core/UComposableCameraEvaluationTree.md)

## Actors

`AActor`-derived classes shipped with the plugin.

- [`AComposableCameraCameraBase`](actors/AComposableCameraCameraBase.md)
- [`AComposableCameraGeneralThirdPersonCamera`](actors/AComposableCameraGeneralThirdPersonCamera.md)
- [`AComposableCameraImpulseBox`](actors/AComposableCameraImpulseBox.md)
- [`AComposableCameraImpulseSphere`](actors/AComposableCameraImpulseSphere.md)
- [`AComposableCameraLevelSequenceActor`](actors/AComposableCameraLevelSequenceActor.md)
- [`AComposableCameraPlayerCameraManager`](actors/AComposableCameraPlayerCameraManager.md)

## Camera Nodes

Every `UComposableCamera*Node` — the building blocks of composed cameras.

- [`UComposableCameraAutoRotateNode`](nodes/UComposableCameraAutoRotateNode.md)
- [`UComposableCameraBlueprintCameraNode`](nodes/UComposableCameraBlueprintCameraNode.md)
- [`UComposableCameraCameraOffsetNode`](nodes/UComposableCameraCameraOffsetNode.md)
- [`UComposableCameraCollisionPushNode`](nodes/UComposableCameraCollisionPushNode.md)
- [`UComposableCameraComputeDistanceToActorNode`](nodes/UComposableCameraComputeDistanceToActorNode.md)
- [`UComposableCameraControlRotateNode`](nodes/UComposableCameraControlRotateNode.md)
- [`UComposableCameraFieldOfViewNode`](nodes/UComposableCameraFieldOfViewNode.md)
- [`UComposableCameraFilmbackNode`](nodes/UComposableCameraFilmbackNode.md)
- [`UComposableCameraFocusPullNode`](nodes/UComposableCameraFocusPullNode.md)
- [`UComposableCameraHitchcockZoomNode`](nodes/UComposableCameraHitchcockZoomNode.md)
- [`UComposableCameraImpulseResolutionNode`](nodes/UComposableCameraImpulseResolutionNode.md)
- [`UComposableCameraLensNode`](nodes/UComposableCameraLensNode.md)
- [`UComposableCameraLookAtNode`](nodes/UComposableCameraLookAtNode.md)
- [`UComposableCameraMixingCameraNode`](nodes/UComposableCameraMixingCameraNode.md)
- [`UComposableCameraOcclusionFadeNode`](nodes/UComposableCameraOcclusionFadeNode.md)
- [`UComposableCameraOrthographicNode`](nodes/UComposableCameraOrthographicNode.md)
- [`UComposableCameraPivotDampingNode`](nodes/UComposableCameraPivotDampingNode.md)
- [`UComposableCameraPivotOffsetNode`](nodes/UComposableCameraPivotOffsetNode.md)
- [`UComposableCameraPostProcessNode`](nodes/UComposableCameraPostProcessNode.md)
- [`UComposableCameraReceivePivotActorNode`](nodes/UComposableCameraReceivePivotActorNode.md)
- [`UComposableCameraRelativeFixedPoseNode`](nodes/UComposableCameraRelativeFixedPoseNode.md)
- [`UComposableCameraScreenSpaceConstraintsNode`](nodes/UComposableCameraScreenSpaceConstraintsNode.md)
- [`UComposableCameraScreenSpacePivotNode`](nodes/UComposableCameraScreenSpacePivotNode.md)
- [`UComposableCameraSpiralNode`](nodes/UComposableCameraSpiralNode.md)
- [`UComposableCameraViewTargetProxyNode`](nodes/UComposableCameraViewTargetProxyNode.md)
- [`UComposableCameraVolumeConstraintNode`](nodes/UComposableCameraVolumeConstraintNode.md)

## Transitions

Pose-blending transitions (`UComposableCamera*Transition`).

- [`UComposableCameraCubicTransition`](transitions/UComposableCameraCubicTransition.md)
- [`UComposableCameraCylindricalTransition`](transitions/UComposableCameraCylindricalTransition.md)
- [`UComposableCameraDynamicDeocclusionTransition`](transitions/UComposableCameraDynamicDeocclusionTransition.md)
- [`UComposableCameraEaseTransition`](transitions/UComposableCameraEaseTransition.md)
- [`UComposableCameraInertializedTransition`](transitions/UComposableCameraInertializedTransition.md)
- [`UComposableCameraLinearTransition`](transitions/UComposableCameraLinearTransition.md)
- [`UComposableCameraPathGuidedTransition`](transitions/UComposableCameraPathGuidedTransition.md)
- [`UComposableCameraSmoothTransition`](transitions/UComposableCameraSmoothTransition.md)
- [`UComposableCameraSplineTransition`](transitions/UComposableCameraSplineTransition.md)
- [`UComposableCameraTransitionBase`](transitions/UComposableCameraTransitionBase.md)
- [`UComposableCameraViewTargetTransition`](transitions/UComposableCameraViewTargetTransition.md)

## Modifiers

Player-camera-level modifiers applied after evaluation.

- [`UComposableCameraModifierBase`](modifiers/UComposableCameraModifierBase.md)
- [`UComposableCameraModifierManager`](modifiers/UComposableCameraModifierManager.md)

## Interpolators

Spring, damper, and IIR interpolator primitives.

- [`UComposableCameraIIRInterpolator`](interpolators/UComposableCameraIIRInterpolator.md)
- [`UComposableCameraInterpolatorBase`](interpolators/UComposableCameraInterpolatorBase.md)
- [`UComposableCameraSimpleSpringInterpolator`](interpolators/UComposableCameraSimpleSpringInterpolator.md)
- [`UComposableCameraSpringDamperInterpolator`](interpolators/UComposableCameraSpringDamperInterpolator.md)

## Splines

Spline types used by spline-guided nodes and transitions.

- [`UComposableCameraBezierSpline`](splines/UComposableCameraBezierSpline.md)
- [`UComposableCameraBuiltInSpline`](splines/UComposableCameraBuiltInSpline.md)
- [`UComposableCameraCubicHermiteSpline`](splines/UComposableCameraCubicHermiteSpline.md)
- [`UComposableCameraNURBSpline`](splines/UComposableCameraNURBSpline.md)
- [`UComposableCameraSplineBase`](splines/UComposableCameraSplineBase.md)
- [`UComposableCameraSplineInterface`](splines/UComposableCameraSplineInterface.md)
- [`UComposableCameraSplineNode`](splines/UComposableCameraSplineNode.md)

## Actions

Scheduled camera actions (async / latent).

- [`UComposableCameraActionBase`](actions/UComposableCameraActionBase.md)
- [`UComposableCameraMoveToAction`](actions/UComposableCameraMoveToAction.md)
- [`UComposableCameraResetPitchAction`](actions/UComposableCameraResetPitchAction.md)
- [`UComposableCameraRotateToAction`](actions/UComposableCameraRotateToAction.md)

## Async Curve Evaluators

Async Blueprint-latent curve evaluators.

- [`UAsyncFloatCurveEvaluator`](async-actions/UAsyncFloatCurveEvaluator.md)
- [`UAsyncVectorCurveEvaluator`](async-actions/UAsyncVectorCurveEvaluator.md)

## Data Assets

Type assets, transition tables, project settings, node modifier data.

- [`UComposableCameraNodeModifierDataAsset`](data-assets/UComposableCameraNodeModifierDataAsset.md)
- [`UComposableCameraPatchTypeAsset`](data-assets/UComposableCameraPatchTypeAsset.md)
- [`UComposableCameraProjectSettings`](data-assets/UComposableCameraProjectSettings.md)
- [`UComposableCameraTransitionDataAsset`](data-assets/UComposableCameraTransitionDataAsset.md)
- [`UComposableCameraTransitionTableDataAsset`](data-assets/UComposableCameraTransitionTableDataAsset.md)
- [`UComposableCameraTypeAsset`](data-assets/UComposableCameraTypeAsset.md)

## Blueprint API

Blueprint function library and Blueprint-authorable camera node base.

- [`UComposableCameraBlueprintLibrary`](blueprint/UComposableCameraBlueprintLibrary.md)

## Interfaces

`UINTERFACE` / `IInterface` contract types.

- [`IComposableCameraImpulseShapeInterface`](interfaces/IComposableCameraImpulseShapeInterface.md)
- [`IComposableCameraSplineInterface`](interfaces/IComposableCameraSplineInterface.md)

## Templates

Template helpers and typed interpolator wrappers.

- [`TCameraInterpolator`](templates/TCameraInterpolator.md)
- [`TIIRInterpolator`](templates/TIIRInterpolator.md)
- [`TIIRInterpolatorTraits`](templates/TIIRInterpolatorTraits.md)
- [`TSimpleSpringInterpolator`](templates/TSimpleSpringInterpolator.md)
- [`TSimpleSpringInterpolatorTraits`](templates/TSimpleSpringInterpolatorTraits.md)
- [`TSpringDamperInterpolator`](templates/TSpringDamperInterpolator.md)
- [`TSpringDamperInterpolatorTraits`](templates/TSpringDamperInterpolatorTraits.md)
- [`TValueTypeWrapper`](templates/TValueTypeWrapper.md)

## Structs

USTRUCTs — init params, pose records, parameter blocks, etc.

- [`FComposableCameraActivateParams`](structs/FComposableCameraActivateParams.md)
- [`FComposableCameraBuildMessage`](structs/FComposableCameraBuildMessage.md)
- [`FComposableCameraContextEntry`](structs/FComposableCameraContextEntry.md)
- [`FComposableCameraContextSnapshot`](structs/FComposableCameraContextSnapshot.md)
- [`FComposableCameraContextStackSnapshot`](structs/FComposableCameraContextStackSnapshot.md)
- [`FComposableCameraDebugPanel`](structs/FComposableCameraDebugPanel.md)
- [`FComposableCameraEvaluationTreeInnerNodeWrapper`](structs/FComposableCameraEvaluationTreeInnerNodeWrapper.md)
- [`FComposableCameraEvaluationTreeLeafNodeWrapper`](structs/FComposableCameraEvaluationTreeLeafNodeWrapper.md)
- [`FComposableCameraEvaluationTreeNode`](structs/FComposableCameraEvaluationTreeNode.md)
- [`FComposableCameraEvaluationTreeReferenceLeafNodeWrapper`](structs/FComposableCameraEvaluationTreeReferenceLeafNodeWrapper.md)
- [`FComposableCameraExecEntry`](structs/FComposableCameraExecEntry.md)
- [`FComposableCameraExposedParameter`](structs/FComposableCameraExposedParameter.md)
- [`FComposableCameraExposedParameterValues`](structs/FComposableCameraExposedParameterValues.md)
- [`FComposableCameraHitResult`](structs/FComposableCameraHitResult.md)
- [`FComposableCameraInternalVariable`](structs/FComposableCameraInternalVariable.md)
- [`FComposableCameraLogCapture`](structs/FComposableCameraLogCapture.md)
- [`FComposableCameraLogEntry`](structs/FComposableCameraLogEntry.md)
- [`FComposableCameraMixingCameraNodeCameraDefinition`](structs/FComposableCameraMixingCameraNodeCameraDefinition.md)
- [`FComposableCameraModifierData`](structs/FComposableCameraModifierData.md)
- [`FComposableCameraNearestPointsOnRaysResult`](structs/FComposableCameraNearestPointsOnRaysResult.md)
- [`FComposableCameraNodePinBinding`](structs/FComposableCameraNodePinBinding.md)
- [`FComposableCameraNodePinBindingTable`](structs/FComposableCameraNodePinBindingTable.md)
- [`FComposableCameraNodePinDeclaration`](structs/FComposableCameraNodePinDeclaration.md)
- [`FComposableCameraNodeTemplatePinOverrides`](structs/FComposableCameraNodeTemplatePinOverrides.md)
- [`FComposableCameraOcclusionMaterialOverride`](structs/FComposableCameraOcclusionMaterialOverride.md)
- [`FComposableCameraParameterBlock`](structs/FComposableCameraParameterBlock.md)
- [`FComposableCameraParameterTableRow`](structs/FComposableCameraParameterTableRow.md)
- [`FComposableCameraParameterValue`](structs/FComposableCameraParameterValue.md)
- [`FComposableCameraPatchActivateParams`](structs/FComposableCameraPatchActivateParams.md)
- [`FComposableCameraPatchSnapshot`](structs/FComposableCameraPatchSnapshot.md)
- [`FComposableCameraPersistentActivateParams`](structs/FComposableCameraPersistentActivateParams.md)
- [`FComposableCameraPinConnection`](structs/FComposableCameraPinConnection.md)
- [`FComposableCameraPinKey`](structs/FComposableCameraPinKey.md)
- [`FComposableCameraPinOverride`](structs/FComposableCameraPinOverride.md)
- [`FComposableCameraPose`](structs/FComposableCameraPose.md)
- [`FComposableCameraPoseHistoryEntry`](structs/FComposableCameraPoseHistoryEntry.md)
- [`FComposableCameraRayDefinition`](structs/FComposableCameraRayDefinition.md)
- [`FComposableCameraRayFeeler`](structs/FComposableCameraRayFeeler.md)
- [`FComposableCameraRuntimeDataBlock`](structs/FComposableCameraRuntimeDataBlock.md)
- [`FComposableCameraScreenSpaceRotationParams`](structs/FComposableCameraScreenSpaceRotationParams.md)
- [`FComposableCameraScreenSpaceTranslationParams`](structs/FComposableCameraScreenSpaceTranslationParams.md)
- [`FComposableCameraSequencerPatchOverlay`](structs/FComposableCameraSequencerPatchOverlay.md)
- [`FComposableCameraSystemModule`](structs/FComposableCameraSystemModule.md)
- [`FComposableCameraTransitionInitParams`](structs/FComposableCameraTransitionInitParams.md)
- [`FComposableCameraTransitionTableEntry`](structs/FComposableCameraTransitionTableEntry.md)
- [`FComposableCameraTreeNodeSnapshot`](structs/FComposableCameraTreeNodeSnapshot.md)
- [`FComposableCameraTypeAssetReference`](structs/FComposableCameraTypeAssetReference.md)
- [`FComposableCameraVariableNodeRecord`](structs/FComposableCameraVariableNodeRecord.md)
- [`FComposableCameraVariablePinConnection`](structs/FComposableCameraVariablePinConnection.md)
- [`FComposableCameraViewportDebug`](structs/FComposableCameraViewportDebug.md)
- [`FIsSimulatingInEditor`](structs/FIsSimulatingInEditor.md)
- [`FModifierEntry`](structs/FModifierEntry.md)
- [`FResolvedVolume`](structs/FResolvedVolume.md)
- [`FTransitionDebugSnapshot`](structs/FTransitionDebugSnapshot.md)

## Other UObjects

UObject-derived types that don't fit a more specific category.

- [`UAsyncPlayCutsceneSequence`](uobjects-other/UAsyncPlayCutsceneSequence.md)
- [`UComposableCameraCameraNodeBase`](uobjects-other/UComposableCameraCameraNodeBase.md)
- [`UComposableCameraComputeNodeBase`](uobjects-other/UComposableCameraComputeNodeBase.md)
- [`UComposableCameraImpulseShapeInterface`](uobjects-other/UComposableCameraImpulseShapeInterface.md)
- [`UComposableCameraLevelSequenceComponent`](uobjects-other/UComposableCameraLevelSequenceComponent.md)
- [`UComposableCameraPatchHandle`](uobjects-other/UComposableCameraPatchHandle.md)
- [`UComposableCameraPatchInstance`](uobjects-other/UComposableCameraPatchInstance.md)
- [`UComposableCameraPatchManager`](uobjects-other/UComposableCameraPatchManager.md)
- [`UComposableCameraRotationConstraints`](uobjects-other/UComposableCameraRotationConstraints.md)
- [`UMovieSceneComposableCameraPatchSection`](uobjects-other/UMovieSceneComposableCameraPatchSection.md)
- [`UMovieSceneComposableCameraPatchTrack`](uobjects-other/UMovieSceneComposableCameraPatchTrack.md)

## Helpers

Non-reflected helper classes and inertializer primitives.

- [`ComposableCameraIndependentPositionalInertializer`](helpers/ComposableCameraIndependentPositionalInertializer.md)
- [`ComposableCameraInitializer`](helpers/ComposableCameraInitializer.md)
- [`ComposableCameraPolynomial`](helpers/ComposableCameraPolynomial.md)
- [`ComposableCameraPositionalInertializer`](helpers/ComposableCameraPositionalInertializer.md)
- [`ComposableCameraRotationalInertializer`](helpers/ComposableCameraRotationalInertializer.md)

## Enumerations

All `enum class` types.

- [`Enumerations`](enumerations/Enumerations.md)

## Free Functions

Top-level macros and non-member functions.

- [`Functions`](free-functions/Functions.md)
