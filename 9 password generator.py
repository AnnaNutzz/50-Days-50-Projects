"""
Generates a random password that meets the specified criteria.

"""

import random
import string

def generator(min_len, numbers= True, special_characters= True):
    """
    Args:
        min_len (int): The minimum length of the password.
        numbers (bool, optional): Include digits (0-9) in the password. Defaults to True.
        special_characters (bool, optional): Include special characters from `string.punctuation` in the password. Defaults to True.

    Returns:
        str: The generated password.
    """

    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    chars = letters
    if numbers:
        chars += digits
    if special_characters:
        chars += special
    
    pwd = ""

    meets_needs = False
    has_number = False
    has_special = False

    while not meets_needs or len(pwd) < min_len:
        new_char = random.choice(chars)
        pwd += new_char

        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True
        
        meets_needs = True

        if numbers:
            meets_needs = has_number
        if special_characters:
            meets_needs = meets_needs and has_special

    return pwd

min_length = int(input("Minimum length?: "))
has_number = input("Need numbers?: ") == "y"
has_special = input("Need specials?: ") == "y"

password = generator(min_length, has_number, has_special)  # Store the generated password in a variable
print(password)
