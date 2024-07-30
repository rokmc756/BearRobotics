#!/usr/bin/python3
#
# Have the function ArrayChallenge(str) take the str parameter and determine how many anagrams exist in the string.
# An anagram is a new word that is produced from rearranging the characters in a different word.
# Your program should determine how many anagrams exist in a given string and return the total number of anagrams.
# If str is "aa aa odg dog gdo" then your program should return 2 because "dog" and "gdo" are anagrams of "odg".
#
# The word "aa" occurs twice in the string. So it isn't an anagram and should not be anagram because it is the same word just repeated.
#
# The string will contain only spaces and lowercase letters, no punctuation, numbers, or uppercase letters.


from collections import Counter

def ArrayChallenge(str):
    words = str.split()
    anagrams = 0
    word_counts = [Counter(word) for word in words]

    for i in range(len(words)):
        if word_counts[i] is None:
            continue
        for j in range(i + 1, len(words)):
            if word_counts[j] is None:
                continue
            if words[i] != words[j] and word_counts[i] == word_counts[j]:
                anagrams += 1
                word_counts[j] = None

    return anagrams

# Test the function
print("Input: \"aa aa odg dog gdo\"")  # Output should be 2
print("Output: " + str(ArrayChallenge("aa aa odg dog gdo")))  # Output should be 2
