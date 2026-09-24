"""
(9) Write a python program to enter a string, character to replace and replacement character.
Output will be new string.
Input : Hello ! How are you ?
Character to replace : H
Replacement Character : P
Output : Pello ! Pow are you ?
"""

string = input("Enter a string: ")
char = input("Character to replace: ")
replacement = input("Replacement Character: ")

new_string = string.replace(char, replacement)

print("Output:", new_string)