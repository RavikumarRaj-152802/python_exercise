# Q(1) Write a python program to enter your full name and print your initial.

name = input("Enter your full name: ")

# Print the initials
initials = "".join(word[0].upper() for word in name.split())

print("Your initials are:", initials)