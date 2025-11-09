```markdown
# 📘 Assignment: Games in Python — Hangman

## 🎯 Objective

Build a console-based Hangman (word-guessing) game in Python. This assignment practices string manipulation, control flow, and user input handling.

## 🧭 Prerequisites

- Basic Python (variables, loops, conditionals)
- Reading/writing simple files (optional for extended tasks)

## 🔍 Skills practiced

- String manipulation
- Loops and conditionals
- User input validation
- Working with lists and randomness

## 📅 Due date

- 2025-10-10 (see course schedule)

## 📝 Tasks

### 🛠️ Task 1 — Core: Implement Hangman

#### Description
Create a playable Hangman game that runs in the terminal. The program should select a secret word and allow the player to guess letters until they either reveal the word or run out of attempts.

#### Requirements (must-haves)

The completed program must:

- Randomly select a word from a predefined list (embedded or read from a file).
- Accept single-letter guesses from the player and update the displayed progress (use `_ _ _` style placeholders).
- Be case-insensitive when comparing guesses to the secret word.
- Track and display previously guessed letters (correct and incorrect).
- Track the number of incorrect guesses remaining and end the game when attempts are exhausted.
- End the game and display a clear win or lose message (show the correct word on loss).
- Validate input (ignore or warn for empty input, more-than-one-character input, or repeated guesses without counting as new incorrect guess).

### 🛠️ Task 2 — Optional/Bonus (extra credit)

Add one or more of the following features:

- Show ASCII-art hangman stages for incorrect guesses.
- Allow difficulty levels that change the number of attempts or the word list.
- Load the word list from `words.txt` or `data/words.csv` instead of embedding it.
- Allow the player to guess the whole word in one attempt.
- Keep a simple score or high-score file across sessions.

## 📁 Starter files

- `starter-code.py` — minimal scaffold to get started (see this folder).

Run the starter file from the assignment folder or from the repository root:

```bash
python3 assignments/games-in-python/starter-code.py
```

or if you are in the `assignments/games-in-python` directory:

```bash
python3 starter-code.py
```

## ✅ Submission & Grading checklist

When you submit, ensure the following:

- Program runs without syntax errors using Python 3.8+.
- Core requirements (see "Requirements") are implemented and demonstrable.
- Include brief usage instructions at the top of your program or in this README.
- If you added extra files (word lists, score files), include them in the assignment folder.

Grading will consider correctness (game rules), input validation, code clarity (readable and commented), and any bonus features implemented.

## 💡 Hints and Edge Cases

- Handle repeated guesses gracefully (do not double-penalize).
- Normalize input (trim whitespace, convert to lower-case).
- Test with short and long words, and words with repeated letters.

## ✏️ Teacher / Developer notes

- This assignment is intentionally open-ended for creativity. Keep the starter code small and focused on the game loop and input/output.

---

If you want, I can also update or add a `words.txt` file and a small unit test or example gameplay transcript.

```

# 🎮 Hangman Game Challenge

Build the classic word-guessing game using Python strings, loops, and user input.

## � What You'll Build

Create a Hangman game where players guess letters to reveal a hidden word before running out of attempts.

**Skills practiced:** String manipulation, loops, conditionals, random selection

## ✅ Must Have's

Your game must:
- Randomly select words from a predefined list
- Accept letter guesses and show current progress (_ _ _ format)
- Track incorrect guesses remaining
- End when word is guessed or attempts exhausted
- Display win/lose messages
