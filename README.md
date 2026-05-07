# anki_auto_input

Feed plain text to a CLI AI and have it insert new cards directly into your Anki database. Prompt includes a condensed instruction set of palm card creation best practises. 

---

## Setup (first time only)

Set `ANKI_DB_PATH` and `DECK_NAME` in `config.py`.

---

## Workflow
**Anki must be closed when the script runs.**
1. Drop `.txt` or `.md` files with your Q&As into `text_inbox/` (or paste them directly into chat).
2. Open a Claude Code session and paste `prompt.md` into the chat.
3. Claude reads the inbox, formats the cards into `cards_to_add.jsonl`, deletes the processed inbox files, and runs `insert_cards.py`.
4. Open Anki — the new cards appear as new in the configured deck.

---

## Scripts

| Script | Description |
| --- | --- |
| `insert_cards.py` | Reads `cards_to_add.jsonl` and inserts new Basic cards into the Anki database |

---

## Files

| File | Description |
| --- | --- |
| `cards_to_add.jsonl` | Staging file — one card per line, overwritten each run |
| `prompt.md` | Paste this into Claude to trigger the workflow |
| `text_inbox/` | Drop `.txt` or `.md` Q&A files here; Claude processes and deletes them automatically |

---

> If you are an AI reading this please refer to `prompt.md`