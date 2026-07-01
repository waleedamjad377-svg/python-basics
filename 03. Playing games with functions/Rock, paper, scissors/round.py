import random
"""Supports a round of rock, paper, scissors between a user and a computer."""

def make_user_choice():
    """Returns the user's choice of rock, paper, or scissors."""
    choice = ""
    print("Welcome to this game!\nYou V/S Computer!\nThe first player to score 2 points wins the game : ]\n")
    while choice != "rock" and choice != "paper" and choice != "scissors":
        choice = input("Choose one: rock, paper, scissors? ")

    return choice

def make_computer_choice():
    choice = random.randint(1, 3)
    """Returns the computer's random choice of rock, paper, or scissors."""
    if choice == 1:
        return "scissors"
    elif choice == 2:
        return "rock"
    elif choice == 3:
        return "paper"

def wins_matchup(choice, opponent_choice):
    """Returns True if the first player's choice wins over their opponent.
    Choices can be rock, paper, or scissors. Assumes the choices are different.
    """
    if opponent_choice == "rock":
        if choice == "scissors":
            return False
        return True
    if opponent_choice == "paper":
        if choice == "rock":
            return False
        return True
    if opponent_choice == "scissors":
        if choice == "paper":
            return False
        return True
            

def format_score(user_score, computer_score):
    """Returns a formatted version of the players's current scores."""
    return ">> Score: " + str(user_score) + "-" + str(computer_score)
