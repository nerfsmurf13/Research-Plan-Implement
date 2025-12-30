# RPI Framework

> **Research. Plan. Implement.** A disciplined workflow for AI-assisted software development that prevents "slop" code and maximizes AI effectiveness.

[![Claude Compatible](https://img.shields.io/badge/Claude-Compatible-blueviolet?style=flat-square&logo=anthropic)](https://claude.ai)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg?style=flat-square)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

---

## The Problem

AI coding assistants are powerful, but they fail in predictable ways:

- **Context pollution** - Error-filled history poisons future responses
- **Scope creep** - AI goes off-track without clear boundaries
- **The "fix loop"** - Repeated failed attempts that never converge
- **Generic output** - Responses that ignore your codebase's patterns

**RPI solves this** with a structured workflow that keeps AI focused, informed, and operating on clean context.

---

## How It Works

```
          +---------------+          +---------------+          +---------------+
          |   /research   |   --->   |    /plan      |   --->   |  /implement   |
          |               |          |               |          |               |
          |  Map codebase |          | Get approval  |          |   Execute     |
          |  Find risks   |          | before coding |          |   with guard  |
          +---------------+          +---------------+          +---------------+
                 |                          |                          |
                 |                          |                          |
                 +------------+-------------+--------------------------+
                              |
                              v
                       +---------------+
                       |   /compact    |
                       |               |
                       | Reset context |
                       | at milestones |
                       +---------------+
```

### The Three Phases

| Phase | Command | Purpose | Output |
|-------|---------|---------|--------|
| **Research** | `/research [topic]` | Explore codebase, map dependencies, find risks | `research-[topic].md` |
| **Plan** | `/plan [feature]` | Design implementation with atomic steps | `plan-[feature].md` |
| **Implement** | `/implement` | Execute approved plan step-by-step | Working code |

---

## Key Features

### Specialized Research Agents

RPI includes stack-specific research agents that understand framework conventions:

| Agent | Best For |
|-------|----------|
| `researcher.md` | General codebases |
| `researcher-vue.md` | Vue.js + JavaScript (Composition API, Pinia, Vue Router) |
| `researcher-python.md` | Python (FastAPI, Flask, Django, SQLAlchemy) |

Each agent produces structured research documents with:
- Architecture diagrams
- Data flow maps
- Risk assessments ("landmine detection")
- Specific file:line references
- Stack-specific gotchas

### Context Health Management

```
/status          Check context health (Fresh/Warming/Compact Soon)
/compact         Compress session for handoff
/reset           Nuclear option for poisoned context
```

**Context degradation signals:**
- AI repeats rejected suggestions
- Responses feel generic
- AI forgets earlier changes
- You're "yelling" at the AI

---

## Quick Start

### 1. Add to Your Project

```bash
# Clone into your project
git clone https://github.com/yourusername/rpi-framework.git .claude

# Or copy the files
cp -r rpi-framework/.claude your-project/
```

### 2. Reference in CLAUDE.md

Create a `CLAUDE.md` in your project root:

```markdown
# Project Instructions

This project uses the RPI Framework.

Commands: /research, /plan, /implement, /compact, /status, /reset

Rules:
1. Never code without research
2. Never implement without an approved plan
3. Compact every 15-20 exchanges
```

### 3. Use the Workflow

```bash
# Starting a new feature
/research authentication flow

# Review research doc, then:
/plan user login feature

# Review plan, say "plan approved", then:
/implement

# Every 15-20 messages:
/compact
```

---

## Project Structure

```
.claude/
├── commands/
│   ├── research.md      # Activates researcher agent
│   ├── plan.md          # Planning mode instructions
│   ├── implement.md     # Implementation mode instructions
│   ├── compact.md       # Context compression protocol
│   ├── status.md        # Session health check
│   └── reset.md         # Context reset protocol
│
└── agents/
    ├── researcher.md        # General-purpose research agent
    ├── researcher-vue.md    # Vue.js specialized agent
    └── researcher-python.md # Python specialized agent
```

---

## Command Reference

### `/research [topic]`

Activates a research agent to explore your codebase. Produces a structured document with:

- **Executive Summary** - What this area does
- **Architecture Overview** - Entry points, core components, data flow
- **Key Code Locations** - Critical files with line numbers
- **Patterns & Conventions** - Naming, structure, anti-patterns
- **Risks & Landmines** - Tech debt, gotchas, warnings
- **Recommendations** - Suggested approach

### `/plan [feature]`

Creates an implementation plan with:

- **Success Criteria** - Definition of done
- **Implementation Steps** - Atomic changes with file:line targets
- **Verification** - How to confirm each step
- **Rollback Strategy** - How to undo if needed
- **Risk Assessment** - What could go wrong

**Plans require explicit approval before implementation.**

### `/implement`

Executes an approved plan with:

- Step-by-step progress reporting
- Verification after each change
- Blocker detection with options
- Completion report with summary

### `/compact`

Compresses session context into a handoff document:

- Work completed and remaining
- Key decisions made
- Problems and solutions
- Files modified
- Commands to continue

### `/status`

Quick health check:

```
Context Health: Fresh / Warming / Compact Soon
Exchanges: ~N messages
Recommendation: Keep going / Consider compacting / Reset needed
```

### `/reset`

For poisoned context (2+ failures on same task):

1. Extract what worked
2. Document the failure
3. Start fresh with clean context

---

## Philosophy

> "Do not outsource the thinking." - [Dex Horthy, "No Vibes Allowed"](https://www.youtube.com/watch?v=rmvDxxNubIg)

RPI is built on these principles:

1. **You review plans, not just code** - AI proposes, you approve
2. **AI amplifies thinking, doesn't replace it** - Stay in the driver's seat
3. **Fresh context beats polluted context** - Reset early, not late
4. **One feature per session** - Keep scope tight

---

## Extending RPI

### Adding New Agents

Create a new agent in `.claude/agents/`:

```markdown
# [Framework] Researcher Agent

Specialized research agent for [Framework] codebases.

## Mission
Investigate: $ARGUMENTS

## Stack-Specific Investigation
[Framework-specific search patterns]

## Output Format
[Customized research document template]
```

### Custom Commands

Add commands in `.claude/commands/`:

```markdown
# [Command] Command

[Instructions for the AI]

## Output Format
[Expected output structure]
```

---

## Best Practices

### Do

- Research before every new feature
- Review and approve plans before implementation
- Compact at milestones (every 15-20 exchanges)
- Reset after 2 failures on the same task
- Trust the workflow

### Don't

- Start coding without research
- Skip plan approval
- Let error history accumulate
- Fight the AI when context is poisoned
- Try to "power through" failures

---

## Why RPI?

| Without RPI | With RPI |
|-------------|----------|
| AI hallucinates file structures | Research maps actual codebase |
| Changes break unknown dependencies | Plan identifies blast radius |
| Error loops never converge | Reset protocol breaks the loop |
| Context degrades mid-session | Compact preserves progress |
| Generic, non-idiomatic code | Agents learn your patterns |

---

## Contributing

Contributions welcome! Areas of interest:

- New stack-specific research agents (Rust, Go, React, etc.)
- Additional utility commands
- Integration with CI/CD pipelines
- IDE extensions

---

## License

MIT License - Use freely in your projects.

---

## Acknowledgments

This framework is based on the concepts presented in **["No Vibes Allowed" by Dex Horthy (HumanLayer)](https://www.youtube.com/watch?v=rmvDxxNubIg)** - an excellent talk on disciplined AI-assisted development that eliminates "slop" code through structured workflows.

Key concepts from the talk:
- Research → Plan → Implement workflow
- Context health management
- The "two failures = poisoned context" rule
- Agent-based codebase exploration

If you're serious about using AI for development, watch the video first.

---

<p align="center">
  <strong>Stop fighting the AI. Start directing it.</strong>
</p>
