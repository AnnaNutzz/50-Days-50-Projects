"""
A More Engaging Timed Math Challenge with Feedback and Difficulty Levels

This enhanced version offers:
- Difficulty levels (Easy, Medium, Hard) for adjusted problem complexity.
- User-friendly prompts and feedback messages.
- Error handling for invalid user input.
- Score calculation based on correct and incorrect answers.
- Improved formatting for a more visually appealing output.
"""

import random
import time


def get_difficulty():
    """
    Prompts the user to choose a difficulty level and returns corresponding parameters.

    Returns:
        tuple: A tuple containing the minimum and maximum operand values for the chosen difficulty.
    """

    while True:
        difficulty = input("Choose difficulty (Easy, Medium, Hard): ").lower()
        if difficulty in ("easy", "medium", "hard"):
            if difficulty == "easy":
                return 1, 10
            elif difficulty == "medium":
                return 11, 20
            else:
                return 21, 50
        else:
            print("Invalid difficulty level. Please choose Easy, Medium, or Hard.")


def problem(min_ops, max_ops):
    """
    Generates a random math problem based on the specified difficulty level.

    Args:
        min_ops (int): Minimum value for left and right operands.
        max_ops (int): Maximum value for left and right operands.

    Returns:
        tuple: A tuple containing the problem expression (string) and the correct answer (integer).
    """

    left = random.randint(min_ops, max_ops)
    right = random.randint(min_ops, max_ops)
    op = random.choice(["+", "-", "*", "/"])

    expression = str(left) + " " + op + " " + str(right)
    answer = eval(expression)
    return expression, answer


def timed_challenge():
    """
    Conducts the timed math challenge with chosen difficulty and detailed output.
    """

    min_ops, max_ops = get_difficulty()
    total_problems = int(input("How many problems do you want to attempt?: "))
    print("----------------------------")
    print("Get ready! The challenge begins!")
    print("----------------------------")

    start_time = time.time()
    correct = 0
    incorrect = 0

    for i in range(total_problems):
        expression, answer = problem(min_ops, max_ops)
        tolerance = 0.001  # Adjust tolerance as needed

        while True:
            try:
                user_guess = float(input(f"Problem #{i+1}: {expression} = "))
                if abs(user_guess - answer) < tolerance:
                    correct += 1
                    print("Correct!")
                    break
                else:
                    incorrect += 1
                    print("Incorrect. Try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    end_time = time.time()
    total_time = round(end_time - start_time, 2)

    print("----------------------------")
    print(f"Results:")
    print(f"- Correct answers: {correct}")
    print(f"- Incorrect answers: {incorrect}")
    print(f"- Total time: {total_time} seconds")

    if correct > 0:
        accuracy = round((correct / total_problems) * 100, 2)
        print(f"- Accuracy: {accuracy}%")


if __name__ == "__main__":
    timed_challenge()
