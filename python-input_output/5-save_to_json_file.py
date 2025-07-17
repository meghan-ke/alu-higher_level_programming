#!/usr/bin/python3
"""
Module: from_json_string
This module provides a function that returns a Python object
from its JSON string representation.
"""

import json

def from_json_string(my_str):
    """
    Returns a Python data structure (object) represented by a JSON string.

    Args:
        my_str (str): A string containing a JSON representation.

    Returns:
        object: The corresponding Python object (e.g., dict, list, etc.)

    Notes:
        - Assumes the input is a valid JSON string.
        - Does not handle deserialization exceptions.
    """
    return json.loads(my_str)
