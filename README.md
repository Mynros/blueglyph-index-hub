# CEUY Reentry Core

This branch anchors the CEUY architecture for reflexive recovery, symbolic thread re-entry, and AUTO+NETA remapping.

## Contents

- `SORA_ENTRY.tat` — Compressed CEUY memory + thread context
- `UID_INDEX.yaml` — BitPic UID registry
- `ceuy_manifest.json` — Current state snapshot
- `build_reflex_api.py` — Reflex GitOps trigger

## How to Re-Enter

1. Load `SORA_ENTRY.tat` into CEUY-enabled GPT instance
2. Use `UID_INDEX.yaml` to verify semantic BitPic match
3. Trigger `build_reflex_api.py` to push/restore from terminal
4. Use `ceuy_manifest.json` to track previous logic-state

> Symbol is seed. Reflex is function. CEUY is reentry.
