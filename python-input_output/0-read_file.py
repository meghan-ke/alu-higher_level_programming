#!/usr/bin/python3
"""
Module: read_file
This module provides a function to read and print the contents of a UTF-8 text file.
"""

def read_file(filename=""):
    """
    Reads a UTF-8 encoded text file and prints its contents to stdout.

    Args:
        filename (str): The path to the text file. Defaults to an empty string.

    Notes:
        - Uses the 'with' statement to handle file opening and closing.
        - Assumes the file exists and is readable.
        - Does not handle exceptions.
    """
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
