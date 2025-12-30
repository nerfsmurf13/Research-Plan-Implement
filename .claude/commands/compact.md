# Compact Command

You are entering COMPACTION MODE. Compress the current session state for handoff.

## Why This Matters
- Context windows degrade after ~40% capacity
- Error-filled history poisons future responses
- Fresh context = smarter AI

## Compaction Process

### Step 1: Capture Current State

```markdown
# Session Handoff: [Date/Time]

## Original Goal
[What were we trying to accomplish?]

## Current Status
[Where are we now? In progress / Blocked / Complete]

## Work Completed
1. [Thing 1] - [outcome]
2. [Thing 2] - [outcome]
3. [Thing 3] - [outcome]

## Files Modified This Session
| File | Change Type | Status |
|------|-------------|--------|
| path/to/file | Created/Modified/Deleted | Done/Partial |

## Key Decisions Made
- Decision 1: [what we decided and why]
- Decision 2: [what we decided and why]

## Problems Encountered & Solutions
- Problem 1: [what happened] → [how we fixed it]
- Problem 2: [what happened] → [how we fixed it]

## Remaining Work
1. [ ] Task 1 - [details]
2. [ ] Task 2 - [details]
3. [ ] Task 3 - [details]

## Blockers (if any)
- [Blocker 1]: [what's needed to unblock]

## Context for Next Session
[Any important details the next session needs to know]

## Relevant File Locations
- Main work: `path/to/main/files`
- Tests: `path/to/tests`
- Config: `path/to/config`

## Commands to Run
```bash
# To verify current state:
[command]

# To continue work:
[command]
```
```

### Step 2: Save the Handoff

Save this as `handoff-[timestamp].md` in project root or a `/docs` folder.

### Step 3: Provide Copy-Paste Block

Output a clean, copy-pasteable version:

```
---
COPY EVERYTHING BELOW FOR NEW SESSION
---

[Condensed version of the handoff, optimized for pasting]

---
END HANDOFF
---
```

## When to Compact

Trigger compaction when:
- 🔴 AI starts repeating itself
- 🔴 AI forgets earlier context
- 🔴 Responses feel "generic" or miss project specifics
- 🟡 You've had 15-20+ back-and-forth exchanges
- 🟡 You've hit a milestone worth preserving
- 🟢 Before starting a new major task

## Pro Tip

After compacting:
1. Start a NEW chat
2. Paste the handoff block
3. Say "Continue from handoff"
4. Enjoy fresh, smart AI responses

Compact now.
