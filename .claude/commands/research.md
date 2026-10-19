---
description: Research a topic with the stack-specific researcher subagent(s) and write research-[topic].md
argument-hint: <topic>
---

# Research Command

Research: $ARGUMENTS

Research happens in subagents so only the report comes back. Spawn them with the Agent tool, passing the topic as the prompt. Do not load agent files into the main conversation.

## Pick the researcher

If the Project section of CLAUDE.md names the researcher(s) for this repo, use those. Otherwise detect the stack from manifest files with a quick Glob (skip `node_modules`, `bin`, `obj`, `dist`):

| Signal | Agent |
|--------|-------|
| `*.csproj` / `*.sln` | `researcher-dotnet` |
| `package.json` with `vue` or `nuxt`, or `*.vue` files | `researcher-vue` |
| `package.json` with a server framework (express, fastify, koa, @nestjs/core) | `researcher-node` |
| `pyproject.toml`, `requirements*.txt`, `manage.py` | `researcher-python` |
| anything else | `researcher` |

## Full-stack topics

When the repo has more than one stack (for example an ASP.NET Core API with a Vue frontend) and the topic crosses the boundary (a page and the endpoint behind it, a payload change, auth), spawn the matching researchers **in parallel in one message**. Give each the topic, the part it owns, and its own output file: `research-[topic]-dotnet.md`, `research-[topic]-vue.md`, and so on. Ask the frontend researcher to list the endpoints and payload shapes it depends on, and the backend researcher to confirm or contradict them.

When both return, write a short `research-[topic].md` index: one-paragraph summary, links to the parts, and any contract mismatches between them (endpoint, field name, type, casing, nullability). Mismatches go under Open Questions.

If the topic stays on one side, spawn only that researcher.

## Output
`research-[topic].md` in the project root (plus per-stack parts for full-stack topics), with `file:line` citations, risks and open questions.

## After research
- Review the document and answer any blocking questions.
- Optional: `/crosscheck research [topic]` if PAL MCP is online. Skip it otherwise.
- Run `/plan [feature]` when ready.
