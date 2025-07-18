#!/usr/bin/python3
"""
This module provides a function to generate Pascal's Triangle up to n rows.
"""

def pascal_triangle(n):
    """
    Generates Pascal's Triangle up to n rows.

    Args:
        n (int): The number of rows for Pascal's Triangle.

    Returns:
        list: A list of lists of integers representing Pascal's Triangle.
              Returns an empty list if n <= 0.
    """
    if n <= 0:
        return []
    
    # Initialize the triangle with the first row
    triangle = [[1]]

    # Generate subsequent rows
    for i in range(1, n):
        # The previous row is needed to calculate the current row
        prev_row = triangle[i - 1]
        
        # Start the current row with 1 (the first element of every row)
        current_row = [1]

        # Calculate the middle elements of the current row
        # Each element is the sum of the two elements directly above it in the previous row
        for j in range(len(prev_row) - 1):
            current_row.append(prev_row[j] + prev_row[j+1])
        
        # End the current row with 1 (the last element of every row)
        current_row.append(1)
        
        # Add the newly generated row to the triangle
        triangle.append(current_row)
        
    return triangle

if __name__ == "__main__":
    print("Pascal's Triangle for n = 0:")
    print(pascal_triangle(0)) # Expected: []

    print("\nPascal's Triangle for n = 1:")
    print(pascal_triangle(1)) # Expected: [[1]]

    print("\nPascal's Triangle for n = 5:")
    # Expected:
    # [[1],
    #  [1, 1],
    #  [1, 2, 1],
    #  [1, 3, 3, 1],
    #  [1, 4, 6, 4, 1]]
    for row in pascal_triangle(5):
        print(row)

    print("\nPascal's Triangle for n = 10:")
    for row in pascal_triangle(10):
        print(row)
