# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?

The first time I ran it, the game seemed functionnal with a good UI.

- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

1  Hard returns (1, 50) while Normal is (1, 100) – the hardest setting is actually easier   than normal.
2 The hints lie sometimes (The outcome messages are reversed: when guess > secret you get "📈 Go HIGHER!" (you should be told to go lower) and vice‑versa.)
3 The restart button doesn't work 

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
I used Copilot and Claude.

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
I used  the #codebase or #file variables (e.g., #file:app.py and #file:logic_utils.py) to give the AI context of your project code. And I asked him to not modify the code, just to tell me the problems he found on the code. It gave me a number of logical/UX bugs and “glitches” sprinkled throughout. Like : 'get_range_for_difficulty()
• Hard returns (1, 50) while Normal is (1, 100) – the hardest setting is actually easier than normal.'

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
When the AI tried to resolve the bug where the hardest setting is easier  than the normal, it choosed Hard returns (1, 200) while Normal is (1, 100). I told the him to change that to Hard returns (1, 100) while Normal is (1, 50).

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
I used pytest to test if the bug was really fixed or not.

- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
  # Bug fix #1: reversed hint messages
def test_too_high_message_says_go_lower():
    # When guess is too high, the message must tell the player to go LOWER, not higher
    outcome, message = check_guess(60, 50)
    assert "LOWER" in message, f"Expected 'LOWER' in message when guess > secret, got: '{message}'"

def test_too_low_message_says_go_higher():
    # When guess is too low, the message must tell the player to go HIGHER, not lower
    outcome, message = check_guess(40, 50)
    assert "HIGHER" in message, f"Expected 'HIGHER' in message when guess < secret, got: '{message}'"

    tests/test_game_logic.py::test_too_high_message_says_go_lower PASSED                                                            
    tests/test_game_logic.py::test_too_low_message_says_go_higher PASSED 

- Did AI help you design or understand any tests? How?
Yes the AI, help me to design and understand the test. After, he gave me the new codes, I ask him to modify the file test_game_logic.py in order to test our debug. After implanting the test in test_game_logic.py, he explain me the test codes.

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
Streamlit re-runs the entire app.py file from top to bottom every time the user does anything — clicks a button, types in a field, etc.
So this line was running on every single re-run:
st.session_state.secret = random.randint(low, high)

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
Think of app.py like a script that replays from scratch every time you interact with the page — like refreshing the browser.
session_state is a persistent drawer that survives between reruns. Values you put in there are still there on the next rerun.
If you know React: rerun = re-render, session_state = useState().

- What change did you make that finally gave the game a stable secret number?
The if check at app.py:30-31:
if "secret" not in st.session_state:
    st.session_state.secret = random.randint(low, high)
Translation: "only generate a secret if one doesn't already exist."
Without the if → new secret on every rerun.
With the if → secret is generated once and stays in session_state for the rest of the game.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

In the future, I want to reuse pytest, it was a very good experience.
Next time I would like to leave with the AI just the coding aspect and try to have the control on all the reflection like finding bugs, suggesting new implementations, ...
This project really change the way I think about the AI, it bring efficiency and rapidity by making quick changes within files. And I admired how the AI can read between files. 

