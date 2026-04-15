---
name: study-flashcards
description: This skill should be used when the user asks to "create flashcards", "study with flashcards", "quiz me", "make a study deck", "add a flashcard", "review cards", "list my decks", or mentions anything related to flashcard-based studying or memorization practice.
version: 0.1.0
---

# Study Flashcard Manager

Create, manage, and quiz with flashcard decks stored as JSON files.

## Commands

### Create a new deck

```bash
python3 .claude/skills/study-flashcards/scripts/flashcards.py create <deck-name>
```

### Add a card to a deck

```bash
python3 .claude/skills/study-flashcards/scripts/flashcards.py add <deck-name> "<question>" "<answer>"
```

### List all decks

```bash
python3 .claude/skills/study-flashcards/scripts/flashcards.py list
```

### Show all cards in a deck

```bash
python3 .claude/skills/study-flashcards/scripts/flashcards.py show <deck-name>
```

### Quiz mode — pull random cards

```bash
python3 .claude/skills/study-flashcards/scripts/flashcards.py quiz <deck-name> <num-cards>
```

### Delete a card from a deck

```bash
python3 .claude/skills/study-flashcards/scripts/flashcards.py delete <deck-name> <card-index>
```

All commands output JSON. Deck names should use lowercase with hyphens (e.g. `biology-101`).

## Storage

Decks are stored as JSON files in the `flashcard-decks/` directory at the project root. Each file is named `<deck-name>.json`.

## Interaction Guidelines

- When the user says "quiz me", run quiz mode and present one card at a time: show the question, wait for the user's response, then reveal the correct answer
- When adding cards, confirm each card was added
- When listing decks, show the deck name and how many cards it has
- Keep responses encouraging and study-focused
- If a deck doesn't exist, suggest creating it first
