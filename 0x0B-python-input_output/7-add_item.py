#!/usr/bin/python3
"""Script to add all arguments to a Python list and 
save them to file"""

# Importing necessary modules
import sys
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

# Define the file name for saving the list

file_name = "add_item.json"
if __name__ == "__main__":
    try:
        my_list = load_from_json_file(file_name)
    except FileNotFoundError:
        my_list = []
    for i, arg in enumerate(sys.argv):
        if i > 0:
            my_list.append(arg)
    save_to_json_file(my_list, file_name)
