"""
Reads cards_to_add.jsonl and inserts new Basic cards directly into the Anki database.
Anki must be CLOSED when running this script.

Usage:
    python insert_cards.py
    python insert_cards.py <cards.jsonl>
"""

import sqlite3
import json
import os
import sys
import time
import random
import string
import hashlib

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from config import ANKI_DB_PATH, DECK_NAME

JSONL_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'cards_to_add.jsonl')


def make_guid():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=10))


def field_csum(front):
    return int(hashlib.sha1(front.encode()).hexdigest()[:8], 16)


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


def find_basic_model_id(cur):
    cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='notetypes'")
    if cur.fetchone():
        cur.execute("SELECT id, name FROM notetypes")
        rows = cur.fetchall()
        for mid, name in rows:
            if 'basic' in name.lower():
                return mid
        raise ValueError(f"No Basic notetype found. Available: {[n for _, n in rows]}")
    cur.execute("SELECT models FROM col")
    models_json = json.loads(cur.fetchone()[0])
    for mid, model in models_json.items():
        if 'basic' in model['name'].lower():
            return int(mid)
    raise ValueError("No Basic notetype found.")


def next_due_position(cur, deck_id):
    cur.execute("SELECT MAX(due) FROM cards WHERE did=? AND queue=0", (deck_id,))
    row = cur.fetchone()
    return (row[0] or 0) + 1


def insert_cards(db_path, jsonl_path, deck_name):
    cards = []
    with open(jsonl_path, encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line:
                cards.append(json.loads(line))

    print(f"Loaded {len(cards)} cards from {jsonl_path}")

    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    deck_id = find_deck_id(cur, deck_name)
    model_id = find_basic_model_id(cur)
    now = int(time.time())
    now_ms = int(time.time() * 1000)
    due_start = next_due_position(cur, deck_id)

    for i, card in enumerate(cards):
        front = card['front']
        back = card['back']
        note_id = now_ms + i * 2
        card_id = now_ms + i * 2 + 1

        cur.execute(
            "INSERT INTO notes (id, guid, mid, mod, usn, tags, flds, sfld, csum, flags, data) "
            "VALUES (?,?,?,?,?,?,?,?,?,?,?)",
            (note_id, make_guid(), model_id, now, -1, '', front + '\x1f' + back, front, field_csum(front), 0, ''),
        )
        cur.execute(
            "INSERT INTO cards (id, nid, did, ord, mod, usn, type, queue, due, ivl, factor, reps, lapses, left, odue, odid, flags, data) "
            "VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
            (card_id, note_id, deck_id, 0, now, -1, 0, 0, due_start + i, 0, 0, 0, 0, 0, 0, 0, 0, ''),
        )
        print(f"  [{i+1}] {front[:70]}")

    cur.execute("UPDATE col SET mod=?, usn=-1", (now,))
    conn.commit()
    conn.close()
    print(f"\nDone. {len(cards)} cards added to '{deck_name}'.")


if __name__ == "__main__":
    jsonl = sys.argv[1] if len(sys.argv) >= 2 else JSONL_PATH

    if not os.path.exists(ANKI_DB_PATH):
        print(f"Error: Anki database not found at {ANKI_DB_PATH}")
        print("Check ANKI_DB_PATH in speech_to_anki/config.py.")
        sys.exit(1)

    insert_cards(ANKI_DB_PATH, jsonl, DECK_NAME)
