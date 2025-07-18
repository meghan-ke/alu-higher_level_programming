#!/usr/bin/env python3
"""
This module provides a function to convert an object's attributes
into a dictionary for JSON serialization, focusing on simple data types.
"""

def class_to_json(obj):
    """
    Returns the dictionary description with simple data structure
    (list, dictionary, string, integer, and boolean) for JSON serialization of an object.

    Args:
        obj: An instance of a Class. All attributes of the obj Class are
             assumed to be serializable: list, dictionary, string, integer, and boolean.

    Returns:
        dict: A dictionary containing the serializable attributes of the object.
    """
    # Use obj.__dict__ to get the instance's attribute dictionary.
    # This automatically includes only the attributes directly set on the instance,
    # which are typically the ones we want to serialize.
    return obj.__dict__
