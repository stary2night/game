# Recovery Baseline From Conversation History

This document captures the intended game state we had already converged on before the file corruption incident.
It is the source of truth for recovery work.

## 1. Visual Direction

- World tone: cartoon combat, not dark realism.
- Camera: lightly tilted top-down, close to a `Brawl Stars` readability style.
- Proportions: chibi / super-deformed hero and enemies.
- Map story:
  - Left side is a higher sanctuary mountain zone.
  - Middle is a downhill transition / ecological decay band.
  - Right side is a lower industrial pollution zone.
- Visual contrast:
  - Left side: lush green trees, flowers, life.
  - Middle: fading grass, exposed soil, narrowing river, bridge conflict point.
  - Right side: polluted factory terrain, drains, smoke, industrial corruption.
- Background target asset:
  - `assets/images/map_background_concept_c_v1.png`
- Victory replacement target:
  - `assets/images/factory_clean_v1.png`

## 2. Front-Facing Asset Direction

- Pure Core should align with the altar/core already visible in the background.
- Trees must use art assets matching the background, not procedural geometry.
- Enemies must use art assets matching the environment, not geometry placeholders.
- Hero must use full-body weapon-bound sprites, not hero + weapon runtime stitching.

## 3. Hero Presentation

- Hero uses complete sprite sets per weapon state.
- Movement should use multi-frame running animation, not sliding.
- Hero should feel grounded:
  - proper foot anchor
  - shadow under feet
  - no floating drift
- Hero starts on the left highland and moves downhill toward the central/plain area.
- Current keybind design to preserve:
  - `F`: plant tree
  - `J`: small combat skill / normal active attack
  - `K`: ultimate
  - `B`: shop / armory
  - `M`: mute

## 4. Combat Baseline

- Player should not auto-attack by proximity.
- Attack should only happen via the action key (`J`).
- Small skill:
  - current weapon attack behavior
  - always usable if cooldown is ready
- Ultimate:
  - triggered by `K`
  - requires minimum HP threshold
  - larger range and stronger audiovisual presentation
- Desired feedback chain:
  - real attack motion
  - slash or projectile readability
  - hit flash
  - hit impact burst
  - knockback / hit reaction
  - light screen shake
  - short hit stop

## 5. Enemy Presentation

- Enemies should emerge from factory outlets / drains, not arbitrary split lines.
- Factory zone should feel alive:
  - smoke
  - polluted drains
  - industrial activity
- Mini boss and big boss should be visibly larger than regular enemies.
- Both miniboss and boss should use multi-frame locomotion instead of static translation.
- They should face / advance in the correct direction.
- Goat should not regain unrealistic speed after entering uphill terrain.

## 6. Wave Structure

- Final agreed wave count: `3` waves.
- `Wave 2` introduces miniboss.
- Final wave includes boss.
- Inter-wave pacing should allow planting / preparation.

## 7. Ecology / Planting

- Tree planting should not be wave-break-only.
- Planting is a default hero skill available through `F`.
- Player can plant on both sanctuary and enemy-side terrain.
- Enemy-side planted trees gradually purify terrain and visually reclaim land.
- Enemies should target trees first to damage the ecosystem before the core.

## 8. Player Survival System

- Hero has explicit HP.
- Hero can be damaged by enemies.
- Hero has 3 total lives.
- Respawn delay exists.
- If the core is destroyed while the hero is down, the run still fails.

## 9. End States

- Failure:
  - stable readable text
  - no flashing unreadable prompt box
- Victory:
  - should not cut instantly
  - should pause for about 3 seconds
  - show a large artistic `Victory`
  - polluted factory side should gradually purify
  - right-side zone transitions toward `factory_clean_v1.png`
- `Play Again` must work reliably on both fail and victory screens.

## 10. Audio

- Music and SFX are enabled.
- BGM direction:
  - lighter
  - faster
  - more playful / rhythmic
- Victory sting:
  - uplifting
  - celebratory

## 11. UI / Language

- All player-facing text should be English.
- Start screen should be redesigned as:
  - hero vs boss composition
  - short concise English mission brief
- HUD should include:
  - hero HP
  - lives
  - core HP
  - wave
  - coins
  - weapon
  - `CO2 Absorbed`
  - `Toxin Cleared`
- End summary should include:
  - environmental totals
  - eco-oriented stats / summary

## 12. Recovery Priority

Recover in this order:

1. Runtime stability
2. Correct map composition and layering
3. Correct scale / anchor / shadow rules
4. Hero movement and combat readability
5. Enemy presentation and wave pacing
6. Ecology / planting / purification systems
7. End screens, UI polish, and progression details
