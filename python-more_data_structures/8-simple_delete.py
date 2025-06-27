#!/usr/bin/python3


def simple_delete(a_dictionary, key=""):
    """
    Delete a key from the dictionary if it exists.
    Do nothing if the key is not found.
    """
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary

