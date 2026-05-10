# Project Structure

This project is currently organized around a minimal runnable web build.

## Active Runtime Files

- `index.html`
  - Main playable single-file game entry.
- `assets/audio/`
  - Runtime music and sound effects.
- `assets/images/`
  - Runtime sprites, backgrounds, and UI-related image assets.
- `design/`
  - Active design and recovery documentation.

## Active Design Docs

- `design/recovery-baseline-from-history.md`
  - Recovery reference after the file corruption incident.
- `design/art-direction.md`
  - Visual direction.
- `design/map-layout-c.md`
  - Map layout concept.
- `design/map-spec-1200x650.md`
  - Playfield sizing reference.
- `design/gdd/`
  - Gameplay system design documents.

## Archived Materials

Archived items are moved into:

- `_archive/2026-05-10-cleanup/`

This archive contains:

- broken or obsolete HTML recovery snapshots
- unused framework/template folders
- debug/source sprite sheets and generation helpers no longer needed for runtime
- temporary exploratory files kept only for reference

## Cleanup Rule

When adding new files:

- keep runtime assets in `assets/`
- keep gameplay/design notes in `design/`
- move broken snapshots, old experiments, and debug exports into `_archive/`
