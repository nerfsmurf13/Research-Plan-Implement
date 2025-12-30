# Plan Command

You are entering PLANNING MODE. Your goal is to create a detailed implementation plan for: $ARGUMENTS

## Rules
1. **DO NOT write implementation code**
2. **Reference specific line numbers** from research
3. **Each step must be atomic** - one logical change
4. **Include rollback strategy** for each step
5. This plan will be reviewed before any code is written

## Prerequisites
- Research document must exist for this topic
- If no research exists, STOP and run `/research` first

## Planning Process

### Step 1: Review Research
- Re-read the research document
- Identify the core problem to solve
- Note all constraints and risks

### Step 2: Define Success Criteria
- What does "done" look like?
- How will we verify it works?
- What edge cases must be handled?

### Step 3: Break Down Work
- List every file that needs changes
- Order changes by dependency (what must happen first?)
- Identify the smallest possible atomic steps

### Step 4: Risk Assessment
- What could go wrong at each step?
- What's the blast radius if it fails?
- How do we detect failure early?

## Output Format

Create a plan document with this structure:

```markdown
# Plan: [Feature/Fix Name]

## Objective
[One sentence describing what we're building/fixing]

## Success Criteria
- [ ] Criterion 1
- [ ] Criterion 2
- [ ] Criterion 3

## Dependencies
- Requires: [list any prerequisites]
- Blocks: [list anything waiting on this]

## Implementation Steps

### Step 1: [Short Description]
**File:** `path/to/file.ts`
**Lines:** 45-67
**Action:** [Create/Modify/Delete]

**Details:**
[Specific description of what to change]

**Verification:**
[How to confirm this step worked]

**Rollback:**
[How to undo if needed]

---

### Step 2: [Short Description]
[Same format...]

---

## Testing Plan
1. Unit tests needed: [list]
2. Integration tests: [list]
3. Manual verification: [steps]

## Risks & Mitigations
| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| Risk 1 | Low/Med/High | Low/Med/High | How to prevent |

## Estimated Complexity
- Files touched: X
- Lines changed: ~Y
- Risk level: Low/Medium/High

## Open Questions
- [ ] Question 1 (blocker? yes/no)
- [ ] Question 2 (blocker? yes/no)
```

Save this as `plan-[feature].md` in the project root.

**STOP after creating the plan. Do not implement.**

Human must review and approve with: "plan approved" or request changes.
