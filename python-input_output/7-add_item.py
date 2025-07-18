#!/usr/bin/python3
"""
This script adds command-line arguments to a list stored in 'add_item.json'.
If the file does not exist, it will be created.
"""
import sys
import json
import os

# Assuming load_from_json_file is available from 6-load_from_json_file.py
# For this script to be self-contained and runnable, we'll include its definition.
def load_from_json_file(filename):
    """
    Loads a Python object from a JSON file.

    Args:
        filename (str): The path to the JSON file.

    Returns:
        object: The Python object represented by the JSON file.
    """
    with open(filename, 'r') as f:
        data = json.load(f)
    return data

# Assuming save_to_json_file is available from 5-save_to_json_file.py
# For this script to be self-contained and runnable, we'll include its definition.
def save_to_json_file(my_obj, filename):
    """
    Saves a Python object to a JSON file.

    Args:
        my_obj (object): The Python object to be saved.
        filename (str): The path to the JSON file.
    """
    with open(filename, 'w') as f:
        json.dump(my_obj, f)

def main():
    """
    Main function to load, add arguments, and save the list to add_item.json.
    """
    json_filename = "add_item.json"
    items_list = []

    # Attempt to load existing items from the file
    if os.path.exists(json_filename):
        try:
            # Use the provided load_from_json_file function
            loaded_data = load_from_json_file(json_filename)
            # Ensure the loaded data is a list, or initialize an empty list
            if isinstance(loaded_data, list):
                items_list = loaded_data
            else:
                print(f"Warning: '{json_filename}' does not contain a JSON list. Starting with an empty list.")
        except json.JSONDecodeError:
            print(f"Warning: Could not decode JSON from '{json_filename}'. Starting with an empty list.")
        except Exception as e:
            # Catch any other potential errors during file loading
            print(f"An unexpected error occurred while loading '{json_filename}': {e}. Starting with an empty list.")

    # Add command-line arguments (excluding the script name itself) to the list
    items_list.extend(sys.argv[1:])

    # Save the updated list back to the file using the save_to_json_file function
    save_to_json_file(items_list, json_filename)

    # Optional: Print the current state of the file for verification
    # print(f"Current content of '{json_filename}': {items_list}")

if __name__ == "__main__":
    main()
