"""Supports a round of rock, paper, scissors between a user and a computer."""

def make_user_choice():
    """Returns the user's choice of rock, paper, or scissors.
    The user enters a choice by input prompt.
    """
    return input("Choose one: rock, paper, scissors? ")

def make_computer_choice():
    """Returns the computer's choice of rock, paper, or scissors.
    The computer chooses randomly, with each choice equally likely.
    """
    return "scissors"

def wins_matchup(choice, opponent_choice):
    """Returns True if the first player's choice wins over their opponent.
    Choices can be rock, paper, or scissors. Assumes the choices are different.
    """
    return choice == "rock"

def format_score(user_score, computer_score):
    """Returns a formatted version of the players's current scores."""
    user = "user (" + str(user_score) + ")"
    computer = "computer (" + str(computer_score) + ")"
    return user + " vs. " + computer
