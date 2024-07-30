#!/usr/bin/python3
#
# Have the function GameChallenge(strArr) take the strArr parameter being passed which will be an array of size eleven.
# The array will take the shape of a Tic-tac-toe board with spaces strArr[3] and strArr[7] being the separators ("<>") 
# between the rows, and the rest of the spaces will be either "X", "O", or "-" which signifies an empty space.
# So for example strArr may be ["X","O","-","<>","-","O","-","<>","O","X","-"].
#
# This is a Tic-tac-toe board with each row separated double arrows ("<>").
# Your program should output the space in the array by which any player could win by putting down either an "X" or "O".
# In the array above, the output should be 2 because if an "O" is placed in strArr[2] then one of the players wins.
#
# Each board will only have one solution for a win, not multiple wins.
# You output should never be 3 or 7 because those are the separator spaces.


def GameChallenge(strArr):
    separators = [3, 7]
    winning_combinations = [
        [0, 1, 2], [4, 5, 6], [8, 9, 10],  # Horizontal
        [0, 4, 8], [1, 5, 9], [2, 6, 10],  # Vertical
        [0, 5, 10], [2, 5, 8]              # Diagonal
    ]

    for win_combo in winning_combinations:
        values = [strArr[i] for i in win_combo]
        if values.count("X") == 2 and values.count("-") == 1:
            return win_combo[values.index("-")]
        if values.count("O") == 2 and values.count("-") == 1:
            return win_combo[values.index("-")]

    return None

# Test the function with the provided example
strArr = ["X", "O", "-", "<>", "-", "O", "-", "<>", "O", "X", "-"]

print("Input: " + str(strArr))
print("Output: " + str(GameChallenge(strArr)))  # Output: 2


##################################################################
# Binggo
#
# 0  1  2   <3>
#
# 4  5  6   <7>
#
# 8  9  10
#
##################################################################
# Win Position from Argument
#
# X  0  -(0) <>
#
# -  0  -    <>
#
# 0  X  -
#
##################################################################

