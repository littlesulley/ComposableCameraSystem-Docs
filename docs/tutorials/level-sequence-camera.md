# Tutorial: Level Sequence Wrapper Camera

Use a `KeyframeSequenceNode` to drive camera motion from a ULevelSequence — wrapping Sequencer-authored animation into the composable pipeline so it blends cleanly with gameplay cameras, respects context pushes, and participates in transitions like any other camera type.

This tutorial assumes you have a gameplay camera running (the [Follow Camera](follow-camera.md) tutorial produces one) and a basic ULevelSequence authored in Sequencer with a CineCameraActor binding. If you haven't used Sequencer before, the Unreal documentation covers creating a level sequence and adding a camera cut track.

## 0. What we're actually building

From the player's perspective: they step into a trigger, the camera smoothly blends from their third-person view into a pre-authored cinematic shot (a dolly move, a crane sweep, a close-up pan — whatever the sequence contains), holds for the duration of the sequence, then blends back to gameplay.

From the system's perspective:

1. A camera type asset wraps a `KeyframeSequenceNode` as its sole node — the level sequence drives position, rotation, and optionally FOV.
2. The sequence plays relative to a reference transform (world origin, or relative to an actor/socket) so the same shot can work in different locations.
3. Activation pushes a `Cutscene` context, and the gameplay camera continues evaluating live underneath (reference leaf), so the return blend is seamless.
4. On sequence completion, gameplay code pops the context and the stack returns to the gameplay camera.

## 1. Author the level sequence

If you already have a suitable level sequence, skip to step 2. Otherwise:

1. Content Browser → right-click → **Cinematics → Level Sequence**. Name it `LS_HeroIntro`.
2. Open it in Sequencer. Click the **camera icon** ("Create a new camera and set it as the current cut") — this creates a `CineCameraActor` binding with transform and camera component tracks.
3. Keyframe the camera's transform over your desired duration. For this tutorial, a simple 3-second dolly from left to right works fine. Add FOV keyframes on the `CameraComponent` track if you want the FOV to change during the shot.
4. Save and close Sequencer.

!!! note "What the node reads from the sequence"
    `KeyframeSequenceNode` extracts **transform** (from the CineCameraActor binding) and optionally **FOV** (from the CameraComponent binding). Other properties bound in the sequence — post-process settings, depth of field, bloom — are ignored. If you need those, author them as additional nodes after the `KeyframeSequenceNode` in the chain.

## 2. Author the camera type asset

Content Browser → right-click → **Composable Camera System → Camera Type Asset**. Name it `CT_HeroIntro`.

### The node chain

This is the simplest possible camera composition — a single node:

```
KeyframeSequenceNode    plays the level sequence as camera motion
```

Drop a **KeyframeSequenceNode** onto the canvas and wire it between Start and Output.

### Configure the node

Select the `KeyframeSequenceNode` and set its properties:

| Property | Value | Why |
|---|---|---|
| `CameraSequence` | `LS_HeroIntro` | The level sequence asset to play |
| `Method` | `RelativeToActor` | The sequence plays relative to an actor's transform — use `WorldOrigin` if the shot is level-locked |
| `StayAtLastFrameTime` | `0.5` | After the sequence ends, hold the last frame for 0.5s before the camera is eligible for transition-out |

### Expose parameters

Expose `RelativeActor` as a camera parameter named `AnchorActor`. Mark it as **Required** — callers must specify which actor the shot plays relative to. This lets the same camera type asset work at different locations in the level.

If you also want per-activation FOV control, add a `FieldOfViewNode` after the `KeyframeSequenceNode`:

```
KeyframeSequenceNode → FieldOfViewNode
```

Expose the `FieldOfView` pin as `OverrideFOV` and leave it **non-required** — when omitted, the sequence's own FOV keyframes drive the value. When provided, the `FieldOfViewNode` overrides it.

### Set the enter transition

In the type asset's Details panel:

- `EnterTransition` = a new `InertializedTransition` instance, `TransitionDuration = 0.6`. Inertialized preserves the gameplay camera's velocity at the blend start, avoiding a visible kink.
- `ExitTransition` = (optional) another `InertializedTransition`, `TransitionDuration = 0.5`, for the blend back to gameplay.

### Tag the camera

Set `CameraTag` to `Cinematic` — this keeps gameplay modifiers (sprint FOV, weapon zoom) from accidentally applying to cinematic shots.

Save the asset.

## 3. Trigger the activation from Blueprint

This follows the same pattern as the [Cutscene Context](cutscene-context.md) tutorial — a trigger overlap pushes the context, and a timer or event pops it.

**Activation (trigger enter):**

```
On Trigger Overlap Begin
  └─> Activate Camera
        Player Index:        0
        Camera Type:         CT_HeroIntro
        Context Name:        Cutscene
        Transition Override:  None
        Anchor Actor:        (the actor the shot is relative to)
```

Because `Cutscene` wasn't on the stack, activation auto-pushes it. The gameplay camera suspends but keeps evaluating live.

**Pop (sequence complete):**

You have two options for knowing when the sequence ends:

**Option A — Duration-based timer.** If you know the sequence is 3 seconds long:

```
On Trigger Overlap Begin
  └─> Activate Camera (as above)
  └─> Delay (3.5 seconds — sequence duration + StayAtLastFrameTime)
      └─> Get Composable Camera Player Camera Manager (Index 0) ─┐
      └─> Terminate Current Camera (PCM: ↑, TransitionOverride: None)
```

**Option B — Transient camera with auto-pop.** Set the activation's `ActivationParams.bIsTransient = true` and `ActivationParams.Lifetime = 3.5`. The camera auto-expires after the lifetime and the context pops itself — no timer or manual `TerminateCurrentCamera` needed.

!!! warning "Transient cameras skip modifier resolution"
    If `bIsTransient = true`, the camera won't respond to modifiers. For most cinematic shots this is desirable — you don't want a sprint FOV modifier affecting a scripted dolly. But if you need modifiers on the cinematic camera, use Option A instead and leave `bIsTransient = false`.

## 4. Play and verify

Enter PIE. Walk into the trigger. You should see:

1. A smooth inertialized blend from the gameplay camera into the level sequence's starting position.
2. The sequence plays — the camera follows the keyframed dolly/crane/pan motion.
3. After the sequence ends and `StayAtLastFrameTime` elapses (or the lifetime expires), the context pops and the camera blends back to gameplay — which has been tracking the character the entire time.

Open `showdebug composablecamera`. During the sequence:

```
Context Stack (depth 2)
  [1] Cutscene     ← active
  [0] Gameplay

Active Camera: CT_HeroIntro
  Node Chain:
    KeyframeSequenceNode (Sequence: LS_HeroIntro, Elapsed: 1.2s / 3.0s)
```

## 5. Making it relative to different actors

The power of exposing `RelativeActor` as a parameter is reuse. The same `CT_HeroIntro` asset can play at the throne room entrance (anchor = throne actor), at the balcony overlook (anchor = balcony actor), or anywhere else — the sequence motion is applied relative to the anchor's transform.

If the anchor actor has a skeletal mesh and you want the sequence relative to a specific socket (e.g. a character's head socket for a close-up), set `RelativeSocket` on the `KeyframeSequenceNode` to the socket name. Expose it as a non-required parameter if different activation sites need different sockets.

## 6. Adding more nodes after the sequence

A single `KeyframeSequenceNode` is the minimal composition, but you can extend it:

```
KeyframeSequenceNode
  → LookAtNode          (soft constraint — nudges the authored rotation toward a target)
  → FieldOfViewNode     (override the sequence's FOV)
  → LensNode            (set filmback, aperture, focus distance)
```

Nodes after the sequence node modify the pose the sequence produced — they don't fight it, they refine it. A `LookAtNode` with `ConstraintType = Soft` and a low `Influence` (0.2) gently biases the authored rotation toward a target without overriding the sequence entirely. This is useful for "cinematic shot that loosely tracks a moving target" setups.

## 7. `Method` options

The `Method` property on `KeyframeSequenceNode` controls how the sequence's coordinate space maps to the world:

| Method | Behavior |
|---|---|
| `WorldOrigin` | Sequence plays in world space as-authored. Use for level-locked shots where the camera positions in Sequencer are final. |
| `RelativeToTransform` | Sequence plays relative to a fixed `FTransform` you author on the node (or expose as a parameter). Use for reusable shots that need manual placement. |
| `RelativeToActor` | Sequence plays relative to an actor's transform each frame. Use for shots anchored to a moving or placed actor. |

`RelativeToActor` with `RelativeSocket` is the most flexible — the sequence becomes fully location-independent.

## Common pitfalls

- **Sequence plays but camera doesn't move.** The level sequence has no CineCameraActor binding. `KeyframeSequenceNode` requires a `CineCameraActor` with transform tracks — not a generic camera actor or a camera component track alone.
- **FOV doesn't change during the sequence.** The level sequence has no `CameraComponent → FieldOfView` track. Add one in Sequencer, or add a `FieldOfViewNode` after the sequence node to set a fixed FOV.
- **Camera position looks wrong.** Check `Method` — if it's `WorldOrigin`, the sequence plays in world space. If the sequence was authored at a different world position than where the trigger is, the shot will be offset. Switch to `RelativeToActor` and anchor to a nearby actor.
- **Gameplay camera snaps on return.** The gameplay camera wasn't evaluating during the cutscene — this happens if the PCM isn't a `AComposableCameraPlayerCameraManager` (the reference leaf mechanism requires it). Verify the [plugin setup](../getting-started/enabling-plugin.md).
- **Transition pops visibly at the start.** The gameplay camera had high velocity when the sequence activated, and the transition duration is too short for inertialization to smooth it. Increase `EnterTransition.TransitionDuration` or use a longer inertialization.

## Where next

- [Cutscene Context](cutscene-context.md) — the same context-push pattern with a spline-based cinematic camera instead of a level sequence.
- [Authoring Camera Types → Cinematic keyframe camera](../user-guide/authoring-camera-types.md#typical-compositions) — the minimal single-node composition reference.
- [Concepts → Context Stack](../user-guide/concepts/context-stack.md) — full conceptual model for context pushing and inter-context blending.
- [`UComposableCameraKeyframeSequenceNode` API](../reference/api/nodes/UComposableCameraKeyframeSequenceNode.md) — full class reference.
