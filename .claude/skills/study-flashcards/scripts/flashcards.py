import json
import sys
import os
import random
from datetime import date

DECKS_DIR = os.path.join(os.path.dirname(__file__), "..", "..", "..", "..", "flashcard-decks")


def deck_path(name):
    return os.path.join(DECKS_DIR, f"{name}.json")


def load_deck(name):
    path = deck_path(name)
    if not os.path.exists(path):
        return None
    with open(path) as f:
        return json.load(f)


def save_deck(name, deck):
    os.makedirs(DECKS_DIR, exist_ok=True)
    with open(deck_path(name), "w") as f:
        json.dump(deck, f, indent=2)


def create(name):
    if load_deck(name):
        print(json.dumps({"error": f"Deck '{name}' already exists"}))
        sys.exit(1)
    deck = {"name": name, "created": str(date.today()), "cards": []}
    save_deck(name, deck)
    print(json.dumps({"success": True, "deck": name, "message": f"Deck '{name}' created"}))


def add(name, question, answer):
    deck = load_deck(name)
    if not deck:
        print(json.dumps({"error": f"Deck '{name}' not found"}))
        sys.exit(1)
    deck["cards"].append({"q": question, "a": answer, "reviewed": 0})
    save_deck(name, deck)
    print(json.dumps({"success": True, "deck": name, "total_cards": len(deck["cards"])}))


def list_decks():
    os.makedirs(DECKS_DIR, exist_ok=True)
    decks = []
    for f in sorted(os.listdir(DECKS_DIR)):
        if f.endswith(".json"):
            deck = load_deck(f[:-5])
            if deck:
                decks.append({"name": deck["name"], "cards": len(deck["cards"])})
    print(json.dumps({"decks": decks}))


def show(name):
    deck = load_deck(name)
    if not deck:
        print(json.dumps({"error": f"Deck '{name}' not found"}))
        sys.exit(1)
    print(json.dumps({"deck": name, "cards": deck["cards"]}))


def quiz(name, count):
    deck = load_deck(name)
    if not deck:
        print(json.dumps({"error": f"Deck '{name}' not found"}))
        sys.exit(1)
    if not deck["cards"]:
        print(json.dumps({"error": f"Deck '{name}' has no cards"}))
        sys.exit(1)
    count = min(count, len(deck["cards"]))
    selected = random.sample(deck["cards"], count)
    for card in selected:
        card["reviewed"] += 1
    save_deck(name, deck)
    print(json.dumps({"deck": name, "quiz_cards": selected, "total_in_deck": len(deck["cards"])}))


def delete_card(name, index):
    deck = load_deck(name)
    if not deck:
        print(json.dumps({"error": f"Deck '{name}' not found"}))
        sys.exit(1)
    if index < 0 or index >= len(deck["cards"]):
        print(json.dumps({"error": f"Card index {index} out of range (0-{len(deck['cards'])-1})"}))
        sys.exit(1)
    removed = deck["cards"].pop(index)
    save_deck(name, deck)
    print(json.dumps({"success": True, "removed": removed, "remaining": len(deck["cards"])}))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(json.dumps({"error": "Usage: flashcards.py <command> [args]"}))
        sys.exit(1)

    cmd = sys.argv[1]

    if cmd == "create" and len(sys.argv) == 3:
        create(sys.argv[2])
    elif cmd == "add" and len(sys.argv) == 5:
        add(sys.argv[2], sys.argv[3], sys.argv[4])
    elif cmd == "list":
        list_decks()
    elif cmd == "show" and len(sys.argv) == 3:
        show(sys.argv[2])
    elif cmd == "quiz" and len(sys.argv) == 4:
        quiz(sys.argv[2], int(sys.argv[3]))
    elif cmd == "delete" and len(sys.argv) == 4:
        delete_card(sys.argv[2], int(sys.argv[3]))
    else:
        print(json.dumps({"error": f"Unknown command or wrong arguments: {cmd}"}))
        sys.exit(1)
