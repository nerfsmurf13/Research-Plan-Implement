---
description: Write an implementation plan (plan-[feature].md) from existing research, then stop for human approval
argument-hint: <feature>
---

# Plan Command

Create an implementation plan for: $ARGUMENTS

## Rules
1. **Do not write implementation code.** The plan is reviewed before any code changes.
2. **Research must exist.** Find the matching `research-*.md` in the project root (for full-stack topics, the index and every per-stack part). If there is none, stop and suggest `/research` first.
3. **Check the research against the code.** Confirm the symbols the plan depends on still exist where the research says; code may have changed since it was written. Use Serena (`find_symbol`, `get_symbols_overview`) if available, otherwise Grep/Read.
4. **Point to symbols, not just lines.** Name the target as `path/File.ext` → `Class/Method` (Serena name path) or the component / store / function name. Line numbers go stale; add them only as a hint.
5. **Scale the plan to the change.** A small, low-risk change gets a short plan (objective, steps, verification). Add the dependencies, risk table and testing sections only when the change touches several files, data access, scheduling, external integrations, auth or security.
6. **Flag destructive paths.** Any step whose code deletes, truncates or bulk-updates data, or adds an endpoint, job, button or migration that can, goes under "Destructive Paths" and needs the human's explicit approval of that item. Follow "Data Safety" in CLAUDE.md: Claude writes scripts and migrations but never runs them.
7. **Resolve what you can.** Answer questions the code can answer yourself. List only real decisions for the human under Open Questions.

## Full-stack changes

When the change spans backend and frontend (for example ASP.NET Core and Vue):
- Order the steps so the contract lands first: backend model/DTO and endpoint, then the frontend API call, store and components.
- State the contract once in the plan (method, route, request and response shape, JSON casing) and make both sides' steps reference it.
- Note whether old and new frontend and backend versions must keep working together during deploy.

## Verification

Every step needs a concrete check that works on this machine. Use the commands in the Project section of CLAUDE.md when it lists them. Otherwise use what the research found, for example:
- **.NET:** `dotnet build` with no new warnings in touched files (or Serena `get_diagnostics_for_file`); `dotnet test` if a test project exists; boot the app when startup, DI or routing changed.
- **Vue:** `npm run build`, `npm run lint`, `vue-tsc --noEmit` for TypeScript, `npm run test` (Vitest/Jest) if present; check the page in the dev server or browser for UI changes.
- **Node / Python:** the project's build, lint, type-check and test commands.
- Never verify by running anything destructive (see Data Safety). Anything that needs production data, cloud resources or a database you cannot reach goes under "Verify After Deploy".

## Output

Save as `plan-[feature].md` in the project root:

```markdown
# Plan: [Feature/Fix]

Research: research-[topic].md

## Objective
[One sentence]

## Success Criteria
- [ ] ...

## Steps

### [ ] Step 1: [Short description]
**Target:** `path/to/File.ext` → `Class/Method` (Modify / Create)
**Change:** [What to change and why, specific enough to implement without guessing]
**Verify:** [Concrete check from the list above]

### [ ] Step 2: ...

## Verify After Deploy
- [Checks that need real data or cloud resources, if any]

## Destructive Paths (if any)
| Step | What it can delete/overwrite | Safeguards (WHERE scope, transaction, auth, confirmation, soft delete/backup) |
|------|------------------------------|-------------------------------------------------------------------------------|

## Risks (only for non-trivial changes)
| Risk | Impact | Mitigation |
|------|--------|------------|

## Open Questions
- [ ] [Question] (blocker: yes/no)
```

Rollback is `git revert` by default. Write a rollback note for a step only when reverting the code is not enough (cloud app settings, a database change, data already written by a job, a cached frontend bundle).

## Approval

Stop after writing the plan and summarize it in a few lines: step count, files touched, risk level, blocking questions. Do not implement. The human approves with "plan approved" or asks for changes. If they ask for changes, update the plan file and stop again.
