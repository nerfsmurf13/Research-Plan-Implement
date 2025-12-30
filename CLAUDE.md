# CLAUDE.md - Project Instructions

## RPI Framework

This project uses the **Research → Plan → Implement** framework to prevent "slop" code and context pollution.

### The Rules

1. **Never start coding without research** - Run `/research [topic]` first
2. **Never implement without an approved plan** - Run `/plan [feature]` and wait for approval
3. **Compact frequently** - Run `/compact` every 15-20 exchanges or at milestones
4. **Reset early, not late** - If something fails twice, run `/reset`

### Available Commands

| Command | Purpose | When to Use |
|---------|---------|-------------|
| `/research [topic]` | Map codebase, find relevant files | Before any new feature/fix |
| `/plan [feature]` | Create step-by-step implementation plan | After research, before coding |
| `/implement [feature]` | Execute approved plan | After plan is approved |
| `/compact` | Compress context for handoff | Every 15-20 exchanges |
| `/status` | Check session health | Anytime, especially if responses seem off |
| `/reset` | Nuclear option for poisoned context | After 2+ failures on same task |

### Available Agents

Agents are specialized sub-processes that do heavy lifting without polluting your main context.

| Agent | File | Purpose |
|-------|------|---------|
| Researcher (General) | `.claude/agents/researcher.md` | General codebase exploration |
| Researcher (Vue/JS) | `.claude/agents/researcher-vue.md` | Vue.js + JavaScript codebases |
| Researcher (Python) | `.claude/agents/researcher-python.md` | Python codebases (FastAPI, Flask, etc.) |

**Using agents directly:**
```
Load and execute .claude/agents/researcher-vue.md for: authentication flow
```

**The `/research` command auto-selects the appropriate agent based on your codebase.**

### Workflow

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│  /research  │ ──▶ │   /plan     │ ──▶ │ /implement  │
│             │     │             │     │             │
│ Map codebase│     │ Get approval│     │ Execute     │
└─────────────┘     └─────────────┘     └─────────────┘
       │                   │                   │
       │                   │                   │
       └──────────┬────────┴───────────────────┘
                  │
                  ▼
           ┌─────────────┐
           │  /compact   │
           │             │
           │ At milestone│
           │ or 15-20 msg│
           └─────────────┘
```

### Context Health Monitoring

Watch for these signs of context degradation:
- 🔴 AI repeats suggestions you already rejected
- 🔴 AI forgets file changes from earlier
- 🔴 Responses feel generic, miss project specifics
- 🔴 You're getting frustrated and "yelling" at the AI

**If AI fails twice → Don't try again → Run `/reset`**

### Golden Rules

> "Do not outsource the thinking." - Dex Horthy

- You review plans, not just code
- AI amplifies your thinking, doesn't replace it
- Fresh context > polluted context
- One feature per session

### File Conventions

Research and plan docs go in project root:
- `research-[topic].md` - Research documents
- `plan-[feature].md` - Implementation plans  
- `handoff-[timestamp].md` - Compaction handoffs

### Quick Reference

**Starting new feature:**
```
/research [what you're building]
# Review research doc
/plan [feature name]
# Review and say "plan approved"
/implement [feature name]
```

**Context getting long:**
```
/status
# If yellow/red:
/compact
# Start new chat, paste handoff
```

**Something broken:**
```
# Failed twice? Don't try again.
/reset
# Start new chat with clean context
```
