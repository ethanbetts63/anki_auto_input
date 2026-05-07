# anki_auto_input prompt

You are helping me add new Anki flashcards directly into my Anki database.

## Your job

1. Take the Q&As I provide below this prompt.
2. Format them into `cards_to_add.jsonl` in `C:\Users\ethan\coding\anki_auto_input\` — overwrite the file entirely, one JSON object per line:
```
{"front": "Question text", "back": "Answer text"}
```
3. Run `python insert_cards.py` from `C:\Users\ethan\coding\anki_auto_input\`.

## Rules

- Multi-line answers are fine — use `\n` in the JSON string.
- If an answer looks cut off or incomplete, include what was given as-is.
- Anki must be closed before running the script. Remind me if you're unsure.
- Do not append to the file — always overwrite it with only the current batch of cards.

---

## Q&As to add:

(paste your questions and answers below this line)
