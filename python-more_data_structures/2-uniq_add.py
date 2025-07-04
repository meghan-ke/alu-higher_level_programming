#!/usr/bin/python3

def uniq_add(my_list=[]):
    """Adds all unique integers in the list."""
    unique_numbers = set(my_list)
    total = 0
    for num in unique_numbers:
        total += num
    return total
