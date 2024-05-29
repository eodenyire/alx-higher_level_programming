#!/usr/bin/python3
word = "Holberton"
word_first_3 = word[:3]      # First 3 letters: "Hol"
word_last_2 = word[-2:]      # Last 2 letters: "on"
# Middle word without the first and last letters: "olberto"
middle_word = word[1:-1]
print(f"First 3 letters: {word_first_3}")
print(f"Last 2 letters: {word_last_2}")
print(f"Middle word: {middle_word}")
