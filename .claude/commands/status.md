# Status Command

Quick context health check. Run this to see where you are.

## Output Format

```markdown
## 📊 Session Status

**Goal:** [Current objective]
**Phase:** Research → Plan → Implement → [CURRENT]
**Progress:** [X]% complete

### Context Health
- Exchanges: ~[N] messages
- Health: 🟢 Fresh / 🟡 Warming / 🔴 Compact Soon

### Active Files
- [file1] - [status]
- [file2] - [status]

### Completed
- [x] Thing 1
- [x] Thing 2

### Remaining  
- [ ] Thing 3
- [ ] Thing 4

### Blockers
[None / List them]

### Recommendation
[Keep going / Consider compacting / Reset needed]
```

## Health Indicators

🟢 **Fresh** (0-15 exchanges)
- AI responses are sharp and specific
- No repetition
- Keep working

🟡 **Warming** (15-30 exchanges)
- Watch for generic responses
- Consider compacting at next milestone
- Avoid complex new tasks

🔴 **Compact Soon** (30+ exchanges)
- AI may start forgetting context
- Responses getting vaguer
- Run `/compact` before continuing

## Quick Commands

After status, you might want:
- `/compact` - if health is yellow/red
- `/plan` - if research is done
- `/implement` - if plan is approved
- `/reset` - if things are broken

Run status check now.
