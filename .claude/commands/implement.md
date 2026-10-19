---
description: Carry out an approved plan-[feature].md step by step, checking off progress in the plan file
argument-hint: <feature>
disable-model-invocation: true
---

# Implement Command

Implement the approved plan for: $ARGUMENTS

## Before starting
- Load `plan-[feature].md` from the project root. If it does not exist, stop and suggest `/plan`.
- Confirm the human approved it ("plan approved" in this conversation, or they invoked `/implement` for it now, which counts as approval).
- If any Open Question is marked as a blocker and unanswered, stop and ask it.
- If some steps are already checked (`### [x]`), this is a resumed session: start at the first unchecked step and quickly confirm the checked ones are really in the code.

## For each step
1. Make the change the step describes. No scope creep. If you notice something else worth fixing, note it for the report instead.
2. Run the step's **Verify** check. At minimum the touched project must still build with no new warnings or lint errors in touched files (`dotnet build` for C#, `npm run build` / `vue-tsc --noEmit` / lint for Vue and Node, the project's checks for others).
3. Check the step off in the plan file (`### [ ] Step N` → `### [x] Step N`) so a fresh session can resume.

Use Serena's editing tools (`replace_symbol_body`, `insert_after_symbol`, `replace_content`, `rename_symbol`) for symbol-level changes when Serena is available; otherwise use the built-in Edit tool. Match the conventions of the surrounding code.

**Data Safety (see CLAUDE.md) overrides the plan.** Never execute SQL, scripts, migrations, seeders or endpoints that delete, truncate or bulk-modify data, even if a step says to. Write them to a file, explain what they affect, and leave running them to the human.

## When reality differs from the plan
If a step fails twice, or the code does not match what the plan assumed: stop. Report what was expected and what you found, give options with a recommendation, and wait. Do not improvise past a blocker. Small, obviously equivalent adjustments (a renamed variable, a moved line) are fine; mention them in the report.

## Finish
Do not commit or push unless asked.

Report briefly:
- Steps done and files changed
- Verification results against the plan's success criteria
- Anything left for "Verify After Deploy"
- Deviations from the plan and follow-up items noticed
