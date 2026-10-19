---
description: Recovery protocol after the same task fails twice - salvage what works, write a handoff note, restart clean
---

# Reset Command

Recovery protocol after repeated failures (2+ attempts at the same task).

A conversation full of failed attempts, error logs and corrections biases the model toward more failure. Don't keep pushing; restart clean.

If only the last turn or two went wrong, `/rewind` (Esc Esc) to the last good point may be enough. Use the full reset when the context as a whole is poisoned.

1. **Stop.** Do not retry the failing approach.
2. **Salvage** anything correct so far: working code, valid research findings, decisions made. If a plan exists, make sure its checkboxes reflect what is actually done.
3. **Write a handoff note** to `handoff-[task].md` in the project root (gitignored): the goal, what went wrong, root cause if known, and what to try differently.
4. **Start a fresh session** (`/clear`) with only the clean goal, the handoff note, relevant file paths and the new approach. Do not carry over error messages or failed code.
5. Begin the fresh session with `/research`, or `/implement` if an approved plan is still valid and only execution went wrong.
