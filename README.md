# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [ ] Describe the game's purpose.
This is a number guessing game built with Streamlit. The player picks a difficulty, then tries to guess a secret number within a limited number of attempts. After each guess, the game gives a hint to go higher or lower, and tracks a score.

- [ ] Detail which bugs you found.
Bug 1 — Wrong difficulty ranges: Hard mode used the range 1–50 while Normal used 1–100, making Hard actually easier than Normal.

Bug 2 — Reversed hints: When a guess was too high, the message said "Go HIGHER!" and when too low it said "Go LOWER!" — the opposite of what the player needed.

Bug 3 — Broken restart button: Clicking "New Game" didn't reset status or history, so after winning or losing the game was permanently blocked even after restarting.


- [ ] Explain what fixes you applied.
Fix 1: Swapped the ranges in get_range_for_difficulty() — Normal is now 1–50 and Hard is 1–100.

Fix 2: Fixed the messages in check_guess() — "Too High" now correctly shows "Go LOWER!" and "Too Low" shows "Go HIGHER!".

Fix 3: Updated the new_game block in app.py to reset status back to "playing", clear history, and use the correct range based on the selected difficulty.

Refactor: Moved all logic functions (get_range_for_difficulty, parse_guess, check_guess, update_score) from app.py into logic_utils.py and imported them in app.py.

## 📸 Demo

- [x] ![Winning game screenshot](image/Screenshot%202026-03-12%20at%2012.27.11%20AM.png)

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, insert a screenshot of your Enhanced Game UI here]
