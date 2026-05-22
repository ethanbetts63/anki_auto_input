"""
Exports all cards from a deck to a JSON file.
Anki must be CLOSED when running this script.

Usage:
    python export_cards.py
    python export_cards.py <output.json>
"""

import sqlite3
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from config import ANKI_DB_PATH, DECK_NAME

OUTPUT_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'deck_cards.json')


def find_deck_id(cur, deck_name):
    cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='decks'")
    if cur.fetchone():
        cur.execute("SELECT id, name FROM decks")
        rows = cur.fetchall()
        for did, name in rows:
            if name.lower() == deck_name.lower():
                return did
        raise ValueError(f"Deck '{deck_name}' not found. Available: {[n for _, n in rows]}")
    cur.execute("SELECT decks FROM col")
    decks_json = json.loads(cur.fetchone()[0])
    rows = [(int(did), d['name']) for did, d in decks_json.items()]
    for did, name in rows:
        if name.lower() == deck_name.lower():
            return did
    raise ValueError(f"Deck '{deck_name}' not found. Available: {[n for _, n in rows]}")


def export_cards(db_path, deck_name, output_path):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    deck_id = find_deck_id(cur, deck_name)

    cur.execute("""
        SELECT n.id, n.flds, n.tags, c.reps, c.lapses, c.ivl, c.due, c.queue
        FROM cards c
        JOIN notes n ON c.nid = n.id
        WHERE c.did = ?
        ORDER BY n.id
    """, (deck_id,))
    rows = cur.fetchall()
    conn.close()

    cards = []
    for note_id, flds, tags, reps, lapses, ivl, due, queue in rows:
        parts = flds.split('\x1f')
        front = parts[0] if len(parts) > 0 else ''
        back = parts[1] if len(parts) > 1 else ''
        cards.append({
            "note_id": note_id,
            "front": front,
            "back": back,
            "tags": tags.strip(),
            "reps": reps,
            "lapses": lapses,
            "interval_days": ivl,
            "queue": queue,
        })

    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(cards, f, ensure_ascii=False, indent=2)

    print(f"Exported {len(cards)} cards from '{deck_name}' to {output_path}")
    return cards


if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) >= 2 else OUTPUT_PATH

    if not os.path.exists(ANKI_DB_PATH):
        print(f"Error: Anki database not found at {ANKI_DB_PATH}")
        sys.exit(1)

    export_cards(ANKI_DB_PATH, DECK_NAME, out)
