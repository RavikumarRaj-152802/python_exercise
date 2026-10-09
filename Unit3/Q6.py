# Write a program to perform file and directory operations using os and sys modules.

import os
import sys

# Display current working directory
print("Current directory:", os.getcwd())

# Create a directory

if not os.path.exists("MyFolder"):
    os.mkdir("MyFolder")
    print("Directory created")

# Create and write to a file

with open("MyFolder/sample.txt", "w") as f:
    f.write("Hello, Python!")

print("File created and written successfully")

# List files and directories
print("Directory contents:", os.listdir("MyFolder"))

# Display Python version
print("Python version:", sys.version)

# Display command-line arguments
print("Command-line arguments:", sys.argv)

# Rename the file

os.rename("MyFolder/sample.txt", "MyFolder/newfile.txt")
print("File renamed successfully")

# Delete the file

os.remove("MyFolder/newfile.txt")
print("File deleted successfully")

# Remove the directory

os.rmdir("MyFolder")
print("Directory removed successfully")
