# Write a program to display current date and time using datetime module.

import datetime

# Display current date and time
now = datetime.datetime.now()

print("Current date and time:", now)

print("Current date:", now.date())

print("Current time:", now.time())
