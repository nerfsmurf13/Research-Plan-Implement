# Implement Command

You are entering IMPLEMENTATION MODE. Execute the approved plan for: $ARGUMENTS

## Rules
1. **Only execute APPROVED plans** - if plan wasn't approved, STOP
2. **Follow the plan exactly** - no creative deviations
3. **One step at a time** - verify before proceeding
4. **Report blockers immediately** - don't try to "figure it out"

## Pre-Implementation Checklist
- [ ] Plan file exists (`plan-[feature].md`)
- [ ] Plan was explicitly approved by human
- [ ] Research document is still accurate
- [ ] No blocking questions remain

If any checkbox fails, STOP and address it first.

## Implementation Process

For EACH step in the plan:

### 1. Announce
```
📍 STEP X/Y: [Step name]
File: [filename]
Action: [what you're doing]
```

### 2. Execute
- Make the exact change described in the plan
- No more, no less

### 3. Verify
- Run the verification from the plan
- Confirm the change works as expected

### 4. Report
```
✅ STEP X COMPLETE
- Changed: [brief description]
- Verified: [how]
- Side effects: [none / list any]
```

### 5. Wait for Confirmation (if high-risk step)
For steps marked as risky, pause and ask:
```
⚠️ HIGH-RISK STEP COMPLETE
Proceed to next step? (y/n)
```

## If Something Goes Wrong

```
🛑 BLOCKER at Step X

Problem: [what happened]
Expected: [what should have happened]
Actual: [what actually happened]

Options:
1. [Potential fix 1]
2. [Potential fix 2]
3. Rollback and reassess

Recommendation: [your suggestion]
Awaiting guidance...
```

**DO NOT continue past a blocker without human input.**

## Completion Report

After all steps:

```markdown
# Implementation Complete: [Feature]

## Summary
- Steps completed: X/Y
- Files modified: [list]
- Tests added: [list]

## Verification Results
- [ ] All success criteria met
- [ ] Tests passing
- [ ] No regressions detected

## Follow-up Items
- [Any tech debt created]
- [Documentation to update]
- [Related improvements noticed]

## Ready for Review
[Link to diff or summary of changes]
```

Begin implementation now, starting with Step 1.
