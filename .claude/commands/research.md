# Research Command

Activate the **Researcher Agent** to investigate: $ARGUMENTS

## Agent Location
Load and execute: `.claude/agents/researcher.md`

## Quick Reference

The Researcher Agent will:
1. **Reconnaissance** - Broad scan of project structure
2. **Deep Dive** - Targeted analysis of relevant files
3. **Data Flow Mapping** - Trace how data moves
4. **Pattern Recognition** - Identify conventions
5. **Landmine Detection** - Find risks and tech debt

## Rules (Enforced by Agent)
- ❌ NO implementation code
- ❌ NO full file dumps
- ✅ Cite specific file:line references
- ✅ Compress insights, not raw data
- ✅ Surface problems, don't hide them

## Output
Agent produces: `research-[topic].md`

## After Research
- Review the research document
- Answer any blocking questions
- Run `/plan [feature]` when ready

---

**Activating Researcher Agent...**

Load `.claude/agents/researcher.md` and begin investigation of: $ARGUMENTS
