#Write a python program to count given character in given string
#Input : Hello ! How are you ?
#Character to find : H
#Output : 2

string = input("Enter a string: ")
char = input("Character to find: ")

count = string.count(char)

print("Output:", count)