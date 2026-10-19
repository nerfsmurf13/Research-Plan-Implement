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
- **Destructive mistakes** - A "quick cleanup" that drops a table or wipes production data

**RPI solves this** with a structured workflow that keeps AI focused, informed, operating on clean context, and away from your data.

---

## How It Works

```
 +-------------+      +--------------+      +-------------+      +-------------+
 |  /research  | ---> | /crosscheck  | ---> |    /plan    | ---> | /implement  |
 |             |      |  (optional)  |      |             |      |             |
 | Subagents   |      | Gemini + GPT |      | Human must  |      | Step by     |
 | map the code|      | second look  |      | approve     |      | step, with  |
 | and risks   |      | via PAL MCP  |      |             |      | checks      |
 +-------------+      +--------------+      +-------------+      +-------------+
```

| Phase | Command | Purpose | Output |
|-------|---------|---------|--------|
| **Research** | `/research [topic]` | Stack-specific subagent maps the flow, cites `file:line`, finds risks | `research-[topic].md` |
| **Crosscheck** | `/crosscheck research [topic]` | Optional review by Gemini and GPT; skipped when PAL MCP is offline | `verified-[doc].md` |
| **Plan** | `/plan [feature]` | Steps that target symbols, each with a concrete verification | `plan-[feature].md` |
| **Implement** | `/implement [feature]` | Executes the approved plan, checks off steps in the plan file | Working code |

Trivial fixes (a typo, an obvious one-line bug) skip the flow. Everything that touches several files, data access, auth, integrations, or both frontend and backend goes through it.

---

## Key Features

### Research runs in subagents

Researchers are registered Claude Code subagents. They do the heavy reading in their own context and return only the report, so the main conversation stays clean.

| Agent | Best For |
|-------|----------|
| `researcher-dotnet` | C# / .NET: ASP.NET Core, EF Core, Dapper, DI, middleware, background jobs |
| `researcher-vue` | Vue 2/3: components, reactivity, Pinia/Vuex, Vue Router, API layer, JS or TS |
| `researcher-node` | Node.js servers: Express, Fastify, NestJS, Prisma, Sequelize, Mongoose |
| `researcher-python` | Python: FastAPI, Flask, Django, SQLAlchemy |
| `researcher` | Any other stack |

`/research` picks the agent from your `CLAUDE.md` Project section or from manifest files (`*.csproj`, `package.json`, `pyproject.toml`, ...).

### Full-stack topics (e.g. ASP.NET Core + Vue)

When a topic crosses the frontend/backend boundary, `/research` runs the matching researchers **in parallel**. The Vue researcher lists the endpoints and payload shapes the UI depends on; the .NET researcher confirms or contradicts them. The index document records any contract mismatches (field names, casing, nullability), and `/plan` orders the steps so the API contract lands first.

### Serena-first, grep fallback

Agents use [Serena](https://github.com/oraios/serena) (v2) symbol tools (`find_symbol`, `find_referencing_symbols`, `find_implementations`, ...) for language-server-accurate navigation, and native Grep/Glob for text and file searches. If Serena is not connected, they say so and carry on with Grep/Glob/Read.

### Data Safety

`CLAUDE.md` forbids Claude from running anything that deletes or bulk-modifies data: destructive SQL, ORM reset commands, wipe endpoints, cloud resource deletion, force pushes. Claude writes such scripts to a file and hands them to a human.

A **PreToolUse hook** (`.claude/hooks/block_destructive.py`) backs this up by denying matching Bash/PowerShell commands, including `DELETE FROM`, `DROP TABLE`, `dotnet ef database drop`, `prisma migrate reset`, `manage.py flush`, `az ... delete`, `terraform destroy` and `git push --force`. Add your project's own dangerous endpoints to `PROJECT_RULES`.

### Plans you can resume

Plans name targets by symbol (`OrderService/GetOrders`, `useCartStore`) rather than line numbers alone, scale to the size of the change, flag destructive paths for explicit approval, and use checkboxes that `/implement` ticks off, so a fresh session picks up where the last one stopped.

---

## Quick Start

### 1. Add to your project

```bash
git clone https://github.com/nerfsmurf13/Research-Plan-Implement.git rpi
cp -r rpi/.claude your-project/
cp rpi/CLAUDE.md your-project/CLAUDE.md   # or merge into your existing CLAUDE.md
```

Then in your project:

- Fill in the **Project** section at the bottom of `CLAUDE.md`: stack, which researchers to use, verification commands, and destructive endpoints.
- Delete the researcher agents you do not need.
- Add your destructive endpoints to `PROJECT_RULES` in `.claude/hooks/block_destructive.py`.
- Gitignore the working docs:

  ```gitignore
  research-*.md
  plan-*.md
  verified-*.md
  handoff-*.md
  CLAUDE.local.md
  .claude/settings.local.json
  ```

The hook needs `python` on your `PATH`.

### 2. Optional tooling

- **Serena MCP** for symbol-aware research. For Vue projects, enable the Vue (or TypeScript) language server in the Serena project config.
- **PAL MCP** for `/crosscheck` (Gemini + GPT review). Without it, `/crosscheck` skips cleanly.

### 3. Use the workflow

```bash
/research order history page          # writes research-order-history-page.md
# review it, answer blocking questions
/crosscheck research order-history-page   # optional
/plan order history filters           # writes plan-order-history-filters.md
# review it, reply "plan approved"
/implement order history filters
```

---

## Project Structure

```
CLAUDE.md                      # Rules, Data Safety, agents, and your Project section
.claude/
├── settings.json              # Wires the Data Safety hook
├── hooks/
│   └── block_destructive.py   # PreToolUse hook that denies destructive shell commands
├── commands/
│   ├── research.md            # Picks and spawns researcher subagent(s)
│   ├── crosscheck.md          # Optional Gemini + GPT review via PAL MCP
│   ├── plan.md                # Planning rules and plan template
│   ├── implement.md           # Executes an approved plan
│   └── reset.md               # Recovery protocol after repeated failures
└── agents/
    ├── researcher-dotnet.md   # C# / .NET
    ├── researcher-vue.md      # Vue.js
    ├── researcher-node.md     # Node.js servers
    ├── researcher-python.md   # Python
    ├── researcher.md          # General fallback
    └── verifier.md            # Multi-model verification for /crosscheck
```

Context health uses Claude Code's built-ins (`/context`, `/compact`, `/clear`, `/rewind`); RPI no longer ships its own `/compact` and `/status`.

---

## Command Reference

### `/research [topic]`

Spawns the stack's researcher subagent(s). Each report contains:

- **Stack** line, confirmed from the code
- **Summary** of what exists and what matters for the change
- **Flow** traced hop by hop with `file:line`
- **Key Code** table
- **Risks and Findings**, only where they apply to the traced code, including destructive paths
- **Open Questions** marked as blockers or not
- **Recommendations**, including how to verify locally

### `/crosscheck research [topic] | plan [feature] | [file].md`

Optional. Sends the document and the source files it cites to Gemini and GPT via PAL MCP, spot-checks citations, and writes `verified-[doc].md` with both verdicts side by side.

### `/plan [feature]`

Creates `plan-[feature].md` with an objective, success criteria, checkbox steps (target symbol, change, verification), verify-after-deploy checks, destructive paths, risks and open questions. **Stops for approval.**

### `/implement [feature]`

Executes the approved plan step by step, runs each step's verification, ticks the step off in the plan file, stops at blockers, and never commits unless asked.

### `/reset`

For poisoned context (2+ failures on the same task): salvage what worked, write `handoff-[task].md`, `/clear`, and restart from research or the still-valid plan.

---

## Philosophy

> "Do not outsource the thinking." - [Dex Horthy, "No Vibes Allowed"](https://www.youtube.com/watch?v=rmvDxxNubIg)

RPI is built on these principles:

1. **You review plans, not just code** - AI proposes, you approve
2. **AI amplifies thinking, doesn't replace it** - Stay in the driver's seat
3. **Fresh context beats polluted context** - Reset early, not late
4. **One feature per session** - Keep scope tight
5. **AI never touches your data destructively** - It writes the script; you run it

---

## Extending RPI

### Adding a researcher

Create `.claude/agents/researcher-[stack].md` with frontmatter so Claude Code registers it as a subagent, and follow the shape of the existing researchers:

```markdown
---
name: researcher-[stack]
description: "Research agent for [stack] codebases. Maps ... and writes research-[topic].md. Use for the Research phase of the RPI workflow."
color: green
---

# [Stack] Researcher

## Establish the stack first
## Tools: Serena first, grep fallback
## How to research
## Constraints
## Output
```

Then add its detection signal to the table in `.claude/commands/research.md`.

### Custom commands

Add commands in `.claude/commands/` with `description` (and `argument-hint`) frontmatter. Use `disable-model-invocation: true` for commands only a human should trigger.

---

## Best Practices

### Do

- Research before every non-trivial change
- Fill in the Project section of `CLAUDE.md`, especially verification commands and destructive endpoints
- Review and approve plans before implementation
- Reset after 2 failures on the same task

### Don't

- Skip plan approval
- Let error history accumulate
- Try to "power through" failures
- Ask Claude to run cleanup scripts against real data

---

## Why RPI?

| Without RPI | With RPI |
|-------------|----------|
| AI hallucinates file structures | Research maps the actual codebase with citations |
| Changes break unknown dependencies | Plan identifies blast radius |
| Frontend and backend drift apart | Full-stack research flags contract mismatches |
| Error loops never converge | Reset protocol breaks the loop |
| A "quick fix" wipes a table | Data Safety rules and a hook block destructive commands |

---

## Contributing

Contributions welcome! Areas of interest:

- New stack-specific researchers (Go, Rust, Java, React, Angular, ...)
- More destructive-command patterns for the hook
- Additional utility commands

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
