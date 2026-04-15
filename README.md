# AUM Study Assistant — Claude Telegram Bot

A Claude Channels Telegram bot with 3 custom skills, built as a course project at the American University of Mongolia.

Message the bot on Telegram and it routes to Claude Code running locally, which uses custom skills to handle your request.

## Skills

### 1. MNT Currency Converter

Convert between Mongolian Tugrik and major world currencies using live exchange rates.

**Trigger examples:**
- "How much is 50000 MNT in USD?"
- "Convert 100 dollars to tugrik"
- "What's the exchange rate for EUR to MNT?"

**Supported currencies:** MNT, USD, EUR, KRW, CNY, JPY

**API:** open.er-api.com (free, no key required)

---

### 2. Study Flashcard Manager

Create and study with flashcard decks for exam preparation. Decks are stored as JSON files locally.

**Trigger examples:**
- "Create a flashcard deck called biology-101"
- "Add a card to biology-101: Q: What is DNA? A: Deoxyribonucleic acid"
- "Quiz me on biology-101"
- "List my decks"

**Features:** create decks, add/delete cards, list decks, quiz mode with random cards

---

### 3. Web Research Summarizer

Research any topic and get concise study notes with key points and sources.

**Trigger examples:**
- "Research the Mongol Empire for me"
- "What can you find about machine learning?"
- "Look up the history of Ulaanbaatar"

**Output:** Structured study notes with quick summary, key points, and source links

---

## Setup

### Prerequisites

- [Claude Code CLI](https://docs.anthropic.com/en/docs/claude-code) (v2.1+)
- Python 3.9+
- [Bun runtime](https://bun.sh) (`curl -fsSL https://bun.sh/install | bash`)
- A Telegram account

### Step 1: Create a Telegram Bot

1. Open Telegram, search for [@BotFather](https://t.me/BotFather)
2. Send `/newbot`, pick a name and username
3. Copy the bot token BotFather gives you

### Step 2: Install the Telegram Plugin

Start a Claude Code session and run:

```
/plugin install telegram@claude-plugins-official
/reload-plugins
```

### Step 3: Configure the Token

```
/telegram:configure <your-bot-token>
```

### Step 4: Launch with Channels

Exit and relaunch:

```bash
claude --channels plugin:telegram@claude-plugins-official
```

### Step 5: Pair Your Account

1. DM your bot on Telegram — it replies with a 6-character code
2. In Claude Code: `/telegram:access pair <code>`
3. Lock it down: `/telegram:access policy allowlist`

## Project Structure

```
claude-telegram-bot/
├── .claude/
│   └── skills/
│       ├── currency-converter/
│       │   ├── SKILL.md
│       │   └── scripts/
│       │       └── convert.py
│       ├── study-flashcards/
│       │   ├── SKILL.md
│       │   └── scripts/
│       │       └── flashcards.py
│       └── web-researcher/
│           ├── SKILL.md
│           └── references/
│               └── format-guide.md
├── flashcard-decks/
│   └── .gitkeep
├── .gitignore
└── README.md
```

## Development Process

This project was developed using **git worktrees** for parallel skill development:

- Each skill was tracked as a GitHub issue
- Each skill was developed on its own feature branch in a separate worktree
- PRs were created and merged to main after each skill was complete

## Author

Batbold — AUM, Ulaanbaatar, Mongolia
