import os

print("In this program we are going to learn about the Os Module in Python")

# Get the current working directory
current_directory = os.getcwd()
print("Current Directory:", current_directory)

# List files in the current directory
files = os.listdir(current_directory)
print("Files in Directory:", files)

# # Create a new directory
# os.mkdir("new_folder")