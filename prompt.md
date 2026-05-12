# anki_auto_input prompt

You are helping me add new Anki flashcards directly into my Anki database.

## Your job

1. Check `C:\Users\ethan\coding\anki_auto_input\text_inbox\` for any `.txt` or `.md` files. If files are present, treat their contents as the Q&A source material (in addition to anything pasted below). Delete each inbox file after processing it.
2. Take the Q&As from the inbox and/or pasted below this prompt.
3. Format them into `cards_to_add.jsonl` in `C:\Users\ethan\coding\anki_auto_input\` — overwrite the file entirely, one JSON object per line:
```
{"front": "Question text", "back": "Answer text"}
```
4. run python insert_cards.py
5. read the next file. do not read multiple files at once. read. write. insert. read next. repeat. 

# Rules for Formulating Anki Cards

## Card Design

**4. Stick to the minimum information principle**
One fact per card. Short question, shorter answer. If an item can be split, split it.

| Bad | Good |
|---|---|
| Q: What are the characteristics of the Dead Sea? A: Salt lake on Israel/Jordan border, 396m below sea level, 74km long, 7× saltier than ocean, high density keeps swimmers afloat, only simple organisms survive | Q: Where is the Dead Sea? A: Israel/Jordan border |
| | Q: How salty is the Dead Sea vs oceans? A: 7× |
| | Q: Why does the Dead Sea keep swimmers afloat? A: High salt content |

**5. Cloze deletion is easy and effective**
Fill-in-the-blank is fast to create and highly effective. Keep the surrounding context minimal.
> Q: Bill …[name] was the second US president to face impeachment. A: Clinton

---

## Avoiding Pitfalls

**9. Avoid sets**
Unordered lists of 5+ items are nearly impossible to memorize reliably. Convert to enumerations or break into individual facts linked by context (e.g. chronological, causal).

> Bad: Q: What are the main greenhouse gases? A: CO₂, methane, nitrous oxide, water vapor, ozone
> Good: Q: Which greenhouse gas dominates human emissions? A: CO₂ | Q: Which gas has ~25× the warming power of CO₂? A: Methane
> Each card teaches a meaningful fact rather than demanding rote list recall.

**10. Avoid enumerations**
Ordered lists are better than sets but still hard. Break them up with overlapping cloze deletions: A→B→C, then B→C→D, etc.

> Q: Fill in: A … … … E → A: B, C, D
> Q: Fill in: B … … … F → A: C, D, E
> The overlap (C, D appear in both) reinforces middle elements from multiple angles without violating the minimum information principle.

**11. Combat interference**
Similar items confuse memory. Make items unambiguous; use examples and context to distinguish them. When you spot interference, fix it immediately.

> Weak: Q: derog adj: shamelessly conscious of one's failings, asking in a begging way → A: cringing
> Better: Q: derog adj: shamelessly humble and supplicant → A: cringing
> Using known anchor words ("humble", "supplicant") locks in the correct meaning and prevents confusion with similar words.

**12. Optimize wording**
Ruthlessly trim. Every redundant word slows recall.
> `PageMaker lost ground to …` beats three lines of background that don't affect the answer.

---

## Strengthening & Maintenance

**13. Refer to other memories**
Anchor new items to concepts already known. Reduces interference and simplifies wording.

**14. Personalize and provide examples**
Personal references are highly interference-resistant. A specific, concrete example you actually remember beats a generic definition.

> Weak: Q: What is a soft bed without arms or back? A: divan
> Better: Q: What is a soft bed without arms or back? (like the one at Robert's parents') A: divan
> The personal anchor makes the card nearly impossible to confuse with anything else.

**15. Rely on emotional states**
Vivid, striking, or emotionally charged examples are remembered far longer than neutral ones. Bizarre is fine — these cards are for you.

**17. Redundancy does not contradict the minimum information principle**
Active and passive word pairs, alternate phrasings, derivation steps — these add items but each remains simple. Viewing the same fact from multiple angles is valuable.

> Q: phone (Esperanto) → A: telefono
> Q: telefono → A: phone
> Two cards, each simple. Together they build both active and passive recall — which don't automatically transfer to each other.

---

## Card Quality Checks

**Avoid binary questions**
Yes/no and this/that questions require little effort and produce shallow understanding. Rephrase as open-ended.

> Bad: Q: Does chicken stock make vegetables taste like chicken? A: No
> Good: Q: How does chicken stock affect the flavor of vegetable dishes? A: Makes them taste more "complete"

**Watch for false positives and false negatives**
Before finalising a card, check both failure modes:
- *False positive* — can you answer it from pattern matching or surface cues alone, without actually knowing the fact? If yes, the question gives too much away or is too mechanical.
- *False negative* — does the question have multiple reasonable correct answers besides the one you intend? If yes, add enough context to rule them out, or reframe the question.

> Bad: Q: What's the first step to cook an omelette? (ambiguous — many valid answers)
> Good: Q: When making an omelette, how must the pan be prepared before adding the eggs? (precise, one correct answer)

**Write more prompts than feels natural**
Each prompt costs roughly 10–30 seconds of review across an entire year. If a card can be split, split it — you are not saving effort by cramming two facts into one card, you are making both harder to retain.

