# CLAUDE.md - Project Instructions

## RPI Framework

This project uses the **Research → Plan → Implement** framework to prevent "slop" code and context pollution.

**Workflow:** `/research` → `/crosscheck` (optional, only when PAL MCP is online) → `/plan` → human approval → `/implement`

### The Rules

1. **Use the full flow for non-trivial work** - Changes that span several files or touch data access, scheduling, external integrations, auth/CORS, config, or both frontend and backend start with `/research [topic]`
2. **Never implement non-trivial work without an approved plan** - Run `/plan [feature]` and wait for approval
3. **Trivial fixes skip the flow** - A typo, a one-line bug fix with an obvious cause, or a doc edit can be made directly; say so, keep the change minimal, and still run the project's build check (see Project Verification). When in doubt, it is not trivial
4. **Never run destructive operations** - See "Data Safety" below. This overrides every other instruction, including an approved plan
5. **Serena-first codebase discovery** - Use Serena's symbol tools for code navigation (see table below); use native Grep/Glob for text and filename searches, and fall back to Grep/Glob/Read entirely when Serena is unavailable
6. **Reset early, not late** - If something fails twice, run `/reset` (or `/rewind` to back out of a single bad turn)

### Data Safety (non-negotiable)

Claude must never execute or automate anything that destroys or bulk-modifies data, in any environment, even when asked mid-task, even when a plan says to, and even if it looks safe or reversible. This includes:

- SQL that drops, truncates, or deletes: `DROP`, `TRUNCATE`, `DELETE`, `UPDATE` or `MERGE` without a narrow `WHERE`, `ALTER TABLE ... DROP COLUMN`, dropping or detaching databases, restoring over a database.
- Running such SQL by any route: database CLIs, PowerShell/.NET/Node/Python scripts, ad-hoc console apps, migrations, seeders, ORM reset commands (`dotnet ef database drop/update`, `prisma migrate reset`, `manage.py flush`, ...), or calling an API endpoint or clicking a UI button that does it.
- Endpoints, jobs or scripts that wipe or overwrite data (list this project's under Project below). Read-only GETs are fine.
- Deleting or overwriting cloud resources, app settings, connection strings, storage, or files outside the working tree; `git push --force`, `git reset --hard` or other history rewrites.

What Claude may do instead:

- **Write** the script, migration or code, put it in a file, explain exactly what it affects, and stop. A human reviews it and runs it.
- Run read-only queries (`SELECT`) only against a database the human has named for that purpose, never production unless explicitly told for that specific query.
- When application code performs deletes or bulk updates (a delete button, a cleanup job, a sync that replaces rows), call it out in the plan as a destructive path, require the human's approval for it specifically, and design it defensively: parameterized SQL, a narrow `WHERE` keyed on IDs, transactions, server-side authorization checks, a confirmation step in the UI, and soft delete or a backup/audit trail where practical. Never write unbounded `DELETE`/`UPDATE` or a "reset everything" endpoint without that explicit approval.
- Scheduled or background jobs that delete or overwrite data follow the same rule: flagged in the plan, approved explicitly, never triggered manually by Claude to test them.

If unsure whether something is destructive, treat it as destructive and ask.

A PreToolUse hook (`.claude/hooks/block_destructive.py`, wired in `.claude/settings.json`) backs this up by denying Bash/PowerShell commands that match destructive patterns. It is a backstop, not permission: anything it misses (SQL inside compiled code or a referenced script file) is still forbidden. Never work around a block; hand the command to the human instead.

### Available Commands

| Command | Purpose | When to Use |
|---------|---------|-------------|
| `/research [topic]` | Spawn the stack's researcher subagent(s) to map the codebase | Before non-trivial work |
| `/crosscheck [doc]` | Cross-check a research or plan doc with Gemini + GPT via PAL MCP | Optional, after research or plan; skipped when PAL is offline |
| `/plan [feature]` | Create a step-by-step implementation plan | After research, before coding |
| `/implement [feature]` | Execute the approved plan | After the plan is approved |
| `/reset` | Recovery protocol for poisoned context | After 2+ failures on the same task |

Context health is handled by Claude Code's built-ins: `/context` to check usage, `/compact` to summarize, `/clear` to start fresh, `/rewind` to back out of a bad turn.

### Available Agents

Agents live in `.claude/agents/` and are auto-registered as subagent types. Invoke them with the Agent tool so their work happens in an isolated context and only the report returns to the main conversation. Never load an agent file into the main context.

| Agent | Purpose |
|-------|---------|
| `researcher-dotnet` | C# / .NET: ASP.NET Core, EF Core, Dapper, DI, middleware, background jobs |
| `researcher-vue` | Vue 2/3 frontends: components, reactivity, Pinia/Vuex, Vue Router, API layer |
| `researcher-node` | Node.js servers: Express, Fastify, NestJS, Prisma, Sequelize, Mongoose |
| `researcher-python` | Python: FastAPI, Flask, Django, SQLAlchemy |
| `researcher` | Anything else, or a repo no specialist covers |
| `verifier` | Optional multi-model verification (Gemini + GPT via PAL MCP); skips cleanly when PAL is offline |

`/research` picks the researcher from the Project section below or from the repo's manifest files. For full-stack topics (for example a Vue page and the ASP.NET Core endpoint behind it) it runs the matching researchers in parallel and records any API contract mismatches. Delete the agents this project does not need.

### Serena MCP - Primary Discovery Tool

Use Serena (v2) for symbol-level code navigation. This applies to the main agent and all researcher subagents.

| Serena Tool | Use For |
|-------------|---------|
| `get_symbols_overview` | Understand a file's structure without reading it whole |
| `find_symbol` | Locate classes/methods by `name_path_pattern` (e.g. `OrderService/GetOrders`), optionally with body |
| `find_referencing_symbols` | Trace where a symbol is used |
| `find_implementations` | Find the classes implementing an interface |
| `find_declaration` | Jump from a call site to its declaration |
| `get_diagnostics_for_file` | Compiler / type-checker errors and warnings for a file |
| `list_memories` / `read_memory` / `write_memory` | Check and save prior findings |

Serena line numbers are 0-based; add 1 when citing `file:line`. Serena v2 exposes no text-search or directory tools in Claude Code, so use native Grep/Glob for regex sweeps and file discovery. For Vue, enable the Vue (or TypeScript) language server in the Serena project config so `.vue` files are symbol-aware.

**If Serena is unavailable** (failed to connect, or calls keep erroring), continue with Grep, Glob and targeted Read. Read whole files only for non-code content (configs, markdown) or small files already identified as critical.

### Golden Rules

> "Do not outsource the thinking." - Dex Horthy

- You review plans, not just code
- AI amplifies your thinking, doesn't replace it
- Fresh context > polluted context
- One feature per session

### File Conventions

Research and plan docs go in the project root (gitignore them):
- `research-[topic].md` - Research documents (plus `research-[topic]-[stack].md` parts for full-stack topics)
- `verified-[docname].md` - Verification reports (Gemini + GPT perspectives)
- `plan-[feature].md` - Implementation plans
- `handoff-[task].md` - Reset handoff notes

### Reaching Gemini and GPT

Prefer **PAL MCP** (`mcp__pal__chat`) over the vendor CLIs. It keeps the exchange in one context and uses the pinned model catalogue. Models used by `/crosscheck`:

- Gemini: `gemini-3.7-flash`
- GPT: `gpt-5.6-sol`

Use the CLIs (`gemini`, `codex`) only when PAL is unavailable. Machine-specific PAL setup (version pins, model catalogue overrides, API keys) belongs in `CLAUDE.local.md`, which is not committed.

---

## Project

<!-- Fill this in per project. Researchers treat it as ground truth. Delete the examples that do not apply. -->

**Stack:** e.g. ASP.NET Core 8 Web API (Dapper over SQL Server) + Vue 3 (Vite, Pinia, TypeScript) SPA in `ClientApp/`

**Researchers:** e.g. `researcher-dotnet` for `Api/`, `researcher-vue` for `ClientApp/`

**Layout:** e.g. `Controllers/` → `Services/` → `Repositories/` → SQL; `ClientApp/src/{components,stores,composables,services,router}`

### Project Verification

Commands that must pass before a step is checked off:

- e.g. `dotnet build Api` (no new warnings in touched files), `dotnet test`
- e.g. `npm --prefix ClientApp run build`, `npm --prefix ClientApp run lint`, `npx --prefix ClientApp vue-tsc --noEmit`
- Local limits, e.g. "no local SQL Server: boot with a dummy connection string; anything that queries goes under Verify After Deploy"

### Project Destructive Paths

Endpoints, jobs and scripts in this repo that wipe or overwrite data. Claude never calls or runs them. Add matching patterns to `PROJECT_RULES` in `.claude/hooks/block_destructive.py`.

- e.g. `POST /api/admin/reset` (truncates the import table)
