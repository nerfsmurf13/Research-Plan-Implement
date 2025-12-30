# Reset Command

CONTEXT RESET PROTOCOL

## When to Use This
- AI has failed the same task 2+ times
- Responses are nonsensical or repetitive
- You're frustrated and yelling at the AI (stop, it doesn't help)
- Context is "poisoned" with error history

## The Problem

When your conversation history is full of:
- Failed attempts
- Error messages
- Corrections and "no, I meant..."
- Frustrated responses

The AI statistically trends toward MORE errors. It's not learning from mistakes - it's pattern-matching toward failure.

## Reset Process

### Step 1: Stop
Do not send another message trying to fix it.

### Step 2: Extract What Worked
Before nuking the session, grab:
- Any correct code that was generated
- Valid insights or research
- Decisions that were made

### Step 3: Document the Failure
```markdown
# Reset Log: [Date]

## What We Were Trying
[Goal]

## What Went Wrong
[Brief description - not the full error history]

## Root Cause (if known)
[Why it failed]

## What to Try Differently
[New approach]
```

### Step 4: Start Fresh

1. Open NEW chat/session
2. Paste only:
   - The goal (clean description)
   - Relevant file paths
   - What approach to use (learned from failure)
3. Do NOT paste:
   - Error messages
   - Failed code
   - The frustration

### Step 5: New Approach

```markdown
# Fresh Start: [Feature]

## Goal
[Clean description of what we're building]

## Relevant Files
- `file1.ts` - [purpose]
- `file2.vue` - [purpose]

## Approach
[What strategy to use - informed by what didn't work, but stated positively]

## Constraints
- [Constraint 1]
- [Constraint 2]

Let's start with /research to map this properly.
```

## Prevention

To avoid needing resets:
1. Use `/research` before coding
2. Use `/plan` and get approval
3. Use `/compact` every 15-20 exchanges
4. Don't let errors accumulate - reset early

## Remember

> "If the AI fails twice, your context is poisoned. Wipe it."
> - Dex Horthy

The AI is not going to "figure it out" with more attempts. Fresh context is your friend.
