#!/usr/bin/python3
"""
Module: append_write
This module provides a function to append a string to a UTF-8 encoded text file.
"""

def append_write(filename="", text=""):
    """
    Appends a string to the end of a text file (UTF-8)
    and returns the number of characters added.

    Args:
        filename (str): The name or path of the file to append to.
        text (str): The string to append.

    Returns:
        int: The number of characters written to the file.

    Notes:
        - Uses the 'with' statement to manage the file context.
        - Creates the file if it does not exist.
        - Appends to the file without erasing its existing content.
        - Does not handle exceptions for file permissions or missing files.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
