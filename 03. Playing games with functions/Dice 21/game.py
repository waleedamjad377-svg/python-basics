"""Supports a round of dice 21 between a user and the computer."""

import die

def get_name(total):
    """Returns the name for the given roll total."""
    if total == 21:
        return "perfect roll"
    elif total > 21:
        return "bust"
    else:
        return str(total)

def get_winner(user_total, computer_total):
    """Returns the name of the winner based on the roll totals."""
    if user_total > 21 and computer_total > 21:
        return "no one"
    if user_total == computer_total:
        return "no one"
    if user_total > computer_total:
        if user_total <= 21:
            return "user"
        return "computer"
    else:
        if computer_total <= 21:
            return "computer"
        return "user"
        

def play_user_turn():
    """Plays the user's turn and returns their final roll total."""
    total = die.roll()
    while should_user_roll_again(total):
        total = total + die.roll()

    return total

def play_computer_turn(user_total):
    """Plays the computer's turn and returns their final roll total."""
    total = die.roll()
    while should_computer_roll_again(total, user_total):
        total = total + die.roll()

    return total

def should_user_roll_again(total):
    """Prompts the user and returns True if they choose to roll again."""
    # Skip the prompt if they've already reached 21.
    if total >= 21:
        return False

    display_total = "Your total is " + str(total) + "."
    prompt = "Roll again? (yes/no) "

    roll_again = input(display_total + " " + prompt)
    return roll_again == "yes" or roll_again == "y"

def should_computer_roll_again(total, user_total):
    """Returns True if the computer should roll again."""
    if user_total > 21:
        return False
    return total < user_total
