---
name: web-researcher
description: This skill should be used when the user asks to "research a topic", "summarize information", "look something up", "find articles about", "what can you find about", "research X for me", "gather information on", or mentions any academic or general research request where web search is needed.
version: 0.1.0
---

# Web Research Summarizer

Research any topic by searching the web and producing concise, well-sourced study notes.

## Process

1. Use the WebSearch tool to find relevant results for the user's topic
2. Use WebFetch on the top 2-3 most relevant URLs to get full content
3. Synthesize the information into structured study notes

## Output Format

Always format research results as study notes:

```
### [Topic Title]

**Quick Summary** (2-3 sentences max)

**Key Points**
- Point with specific detail
- Point with specific detail
- Point with specific detail
(aim for 5-8 key points)

**Important Details**
One or two short paragraphs expanding on the most significant findings.

**Sources**
- [Source Title](URL)
- [Source Title](URL)
```

## Guidelines

- Prioritize recent, reliable sources (educational sites, established publications)
- Keep it concise — study notes, not essays
- Include specific facts, numbers, and dates where available
- If the topic is controversial, present multiple perspectives
- If the user specifies a focus area, narrow the research to that
- Always include at least 2 source links
- If the user asks a follow-up, build on previous research rather than starting over

## Subject-Specific Formatting

See `references/format-guide.md` for format variations by subject area.
