from logic_utils import check_guess, get_range_for_difficulty

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"

# Bug fix #1: reversed hint messages
def test_too_high_message_says_go_lower():
    # When guess is too high, the message must tell the player to go LOWER, not higher
    outcome, message = check_guess(60, 50)
    assert "LOWER" in message, f"Expected 'LOWER' in message when guess > secret, got: '{message}'"

def test_too_low_message_says_go_higher():
    # When guess is too low, the message must tell the player to go HIGHER, not lower
    outcome, message = check_guess(40, 50)
    assert "HIGHER" in message, f"Expected 'HIGHER' in message when guess < secret, got: '{message}'"

# Bug fix #2: Hard difficulty must have a larger range than Normal
def test_hard_range_larger_than_normal():
    _, normal_high = get_range_for_difficulty("Normal")
    _, hard_high = get_range_for_difficulty("Hard")
    assert hard_high > normal_high, (
        f"Hard range (1-{hard_high}) should be larger than Normal (1-{normal_high})"
    )
