"""
A Simple Number Guessing Game with Improved Guidance
"""

import random

# Generate a random number between 1 and 100 (inclusive)
secret_num = random.randrange(1, 101)

# Main game loop
while True:
    try:
        # Get user input, handling non-numeric input with a clear error message
        ans = input("Guess a number between 1 and 100 (inclusive): ")
        ans = int(ans)

        # Check for a valid positive number guess
        if ans <= 0:
            print("Invalid guess! Please enter a positive number.")
            continue

        # Check for correct guess
        if ans == secret_num:
            print("YES! You guessed the number correctly!")
            break

        """
        Provide guidance based on the user's guess
        Calculate a reasonable and dynamic range hint for the user
        """
        half_range = (secret_num - ans) // 2  # Ensure range around the guess
        lower_bound = max(1, ans - half_range)  # Lower bound to 1
        upper_bound = min(100, ans + half_range)  # Upper bound to 100

        if ans > secret_num:
            print(f"Too high! Try a number between {lower_bound} and {upper_bound}.")
        else:
            print(f"Too low! Try a number between {lower_bound} and {upper_bound}.")

    except ValueError:
        # Handle non-numeric input 
        print("Invalid guess! Please enter a number.")

print("Thanks for playing!")
