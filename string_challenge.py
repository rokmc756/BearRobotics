#!/usr/bin/python3
#
# Have the function StringChallenge(str) take the str parameter being passed and determine
# if it passes as a valid password that follows the list of constraints:
#
# 1. It must have a capital letter.
# 2. It must contain at least one number.
# 3. It must contain a punctuation mark or mathematical symbol.
# 4. It cannot have the word "password" in the string.
# 5. It must be longer than 7 characters and shorter than 31 characters.
#
# If all the above constraints are met within the string, the your program should return the string true,
# otherwise your program should return the string false.
# For example: if str is "apple!M7" then your program should return "true".

import re

def StringChallenge(str):
    # Constraint 1: Check for at least one capital letter
    if not any(char.isupper() for char in str):
        return "false"

    # Constraint 2: Check for at least one number
    if not any(char.isdigit() for char in str):
        return "false"

    # Constraint 3: Check for a punctuation mark or mathematical symbol
    if not any(char in r"!@#$%^&*()-+_=,.<>/?;:'\"[]{}" for char in str):
        return "false"

    # Constraint 4: Check if the word "password" is present
    if "password" in str.lower():
        return "false"

    # Constraint 5: Check length
    if len(str) < 8 or len(str) > 30:
        return "false"

    return "true"

# Test cases
print("Input: \"passWord123!!!!\"")
print("Output: " + StringChallenge("passWord123!!!!"))
print("")

print("Input: \"turkey90AAA=\"")
print("Output: " + StringChallenge("turkey90AAA="))
print("")

print("Input: \"apple!M7\"")
print("Output: " + StringChallenge("apple!M7"))

