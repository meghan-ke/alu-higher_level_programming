#!/usr/bin/python3
"""
This module provides a function to load a Python object from a JSON file.
"""
import json

def load_from_json_file(filename):
    """
    Loads a Python object from a JSON file.

    Args:
        filename (str): The path to the JSON file.

    Returns:
        object: The Python object represented by the JSON file.
    """
    with open(filename, 'r') as f:
        # Use json.load() to parse the JSON content directly from the file object
        data = json.load(f)
    return data
