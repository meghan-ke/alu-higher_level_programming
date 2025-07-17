#!/usr/bin/python3
"""
Module: to_json_string
This module provides a function that returns the JSON representation of a Python object as a string.
"""

import json

def to_json_string(my_obj):
    """
    Returns the JSON representation of a Python object (as a string).

    Args:
        my_obj: The Python object to serialize.

    Returns:
        str: The JSON-formatted string representing the object.

    Notes:
        - Assumes that the object is serializable.
        - Does not handle serialization exceptions.
    """
    return json.dumps(my_obj)
