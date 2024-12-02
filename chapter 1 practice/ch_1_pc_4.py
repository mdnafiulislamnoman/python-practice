import os

# Specify the directory (use '.' for the current directory)
directory_path = "."

try:
    # List the contents of the directory
    contents = os.listdir(directory_path)
    print("Directory contents:")
    for item in contents:
        print(item)
except FileNotFoundError:
    print(f"Error: The directory '{directory_path}' does not exist.")
except PermissionError:
    print(f"Error: Permission denied to access '{directory_path}'.")
