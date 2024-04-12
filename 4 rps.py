"""
This program implements a best-of-n rock, paper, scissors game.

The user plays against the computer, and the first to win a certain number of rounds
(n / 2, rounded up) is declared the champion.
"""

import random
import math


def play():
    """
    Plays a single round of rock, paper, scissors.

    Prompts the user for their choice (r/p/s), validates it, and compares it to
    the computer's random choice. Returns 0 for a tie, 1 for user win, and -1 for computer win.
    """

    user_choice = input("What do you choose? (r/p/s): ")
    user_choice = user_choice.lower()

    # Validate user input
    if user_choice not in ('r', 'p', 's'):
        print("Invalid choice. Please enter 'r', 'p', or 's'.")
        return None  # Indicate an invalid choice

    computer_choice = random.choice(('r', 'p', 's'))

    # Determine the winner based on the choices
    if user_choice == computer_choice:
        return 0
    elif win(user_choice, computer_choice):
        return 1
    else:
        return -1


def win(player, opponent):
    """
    Checks if the player wins against the opponent.

    Returns True if the player wins, False otherwise.
    """

    # Define winning combinations
    winning_combos = {
        'r': 's',
        'p': 'r',
        's': 'p'
    }

    return winning_combos[player] == opponent


def play_best(n):
    """
    Plays a best-of-n rock, paper, scissors game.

    Tracks the number of wins for the player (p_win) and computer (c_win).
    The first to reach wins_needed (n / 2, rounded up) wins the game.

    Prints messages for each round result, and declares the winner at the end.
    """

    player_wins = 0
    computer_wins = 0
    wins_needed = math.ceil(n / 2)

    while player_wins < wins_needed and computer_wins < wins_needed:
        result = play()

        if result is None:
            # Skip the round if user input is invalid
            continue

        if result == 0:
            print(f"It's a tie. You both chose the same thing!")
        elif result == 1:
            player_wins += 1
            print(f"YOU WIN! 🎉")
        else:
            computer_wins += 1
            print(f"YOU LOSE!")

    if player_wins > computer_wins:
        print(f"You are the Champion!")
    else:
        print("You lost to a computer... cheater?")


if __name__ == "__main__":
    """
    Starts the game with a best-of-3 format. You can adjust the value of n in play_best()
    """
    play_best(3)
