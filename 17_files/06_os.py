# import os

# a = os.listdir("dir")

# print(a)
# print(os.getcwd())
# print(os.path.exists("dir"))
# print(os.remove("delete.txt")) # This function will attempt to delete the file named "delete.txt" from your current directory.


# I already explained all of the code line by line in detail in 06_os.md

import os

# Get the current working directory

current_dir = os.getcwd()

print("Current directory:", current_dir)

# Create a new directory

# os.mkdir("new_directory") # creates only one level of directory

# os.makedirs("path/to/new_directory") # creates nested directories

# Change the current directory

# print(os.chdir("new_directory"))

# List files and directories in a directory

# print(os.listdir("dir")) # "." represents current directory


# Remove a file or directory

# os.remove("delete.txt")

# print(os.rmdir("")) # removes empty directory

# shutil.rmtree("path/to/new_directory") # removes non-empty directory (use w# Rename a file or directory

# os.rename("old_name.txt", "new_name.txt")

# Check if a file or directory exists
# if os.path.exists("my_file.txt"):
#     print("File exists")
# Join path components in a platform-independent way
# path = os.path.join("folder", "subfolder", "file.txt")
# print("Joined path:", path)