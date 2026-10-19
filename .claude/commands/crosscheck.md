---
description: Optional Gemini + GPT review of an RPI research or plan doc via PAL MCP (skips if PAL is offline)
argument-hint: research <topic> | plan <feature> | <file>.md
---

# Crosscheck Command (optional)

Crosscheck: $ARGUMENTS

This step is optional. If PAL MCP failed to connect this session (it shows in the MCP server status, or `mcp__pal__chat` cannot be loaded), tell the user in one line that verification was skipped and suggest the next RPI phase. Do not spawn the agent.

Otherwise, spawn the **`verifier`** subagent with the Agent tool, passing $ARGUMENTS as its prompt. Do not load the agent file into the main conversation.

## Usage

```
/crosscheck research [topic]     # research-[topic].md (and its per-stack parts)
/crosscheck plan [feature]       # plan-[feature].md
/crosscheck [filename.md]        # any markdown document
```

The verifier sends the document and the source files it cites to a Gemini and a GPT model in parallel (names from "Reaching Gemini and GPT" in CLAUDE.md), spot-checks a few citations itself, and writes `verified-[docname].md`. Disagreements between the models are shown side by side for the human to decide.

## After verification
- Review the verdicts and action items.
- Fix critical items, then continue to the next RPI phase.
