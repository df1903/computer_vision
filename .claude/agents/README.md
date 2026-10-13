# agents/

One `.md` file per subagent, with frontmatter:

```markdown
---
name: agent-name
description: When to use it (the orchestrator decides based on this).
tools: Read, Grep, Glob
model: sonnet
---

Agent instructions in the body.
```

Only create an agent here if you'll reuse it several times in this project and it has a clear, bounded scope (e.g., "SQL migration reviewer"). For a one-off use, don't create an agent — ask the `general-purpose` agent directly.
