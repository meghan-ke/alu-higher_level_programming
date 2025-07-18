#!/usr/bin/python3
"""
This module defines a Student class with an enhanced to_json method
that allows filtering of attributes for JSON serialization.
"""

class Student:
    """
    A Student class that defines a student by first_name, last_name, and age.
    It includes a method to retrieve a dictionary representation for JSON serialization,
    with an option to filter attributes.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a new Student instance.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        If 'attrs' is a list of strings, only attribute names contained in this list
        will be retrieved. Otherwise, all attributes will be retrieved.

        Args:
            attrs (list, optional): A list of strings representing the names of
                                    attributes to retrieve. Defaults to None.

        Returns:
            dict: A dictionary containing the specified (or all) serializable
                  attributes of the student instance.
        """
        # Get all attributes of the instance
        obj_dict = self.__dict__
        filtered_dict = {}

        # Check if attrs is a list of strings
        if isinstance(attrs, list) and all(isinstance(a, str) for a in attrs):
            # If attrs is provided and valid, filter the attributes
            for attr_name in attrs:
                if attr_name in obj_dict:
                    filtered_dict[attr_name] = obj_dict[attr_name]
            return filtered_dict
        else:
            # Otherwise, return all attributes
            return obj_dict


if __name__ == "__main__":
    # Create a Student instance
    student_instance = Student("Alice", "Smith", 21)

    # Demonstrate to_json with no arguments (retrieves all attributes)
    all_attrs_dict = student_instance.to_json()
    print("Student object with all attributes:")
    print(all_attrs_dict)

    print("-" * 30)

    # Demonstrate to_json with a specific list of attributes
    selected_attrs_dict = student_instance.to_json(attrs=["first_name", "age"])
    print("Student object with selected attributes (first_name, age):")
    print(selected_attrs_dict)

    print("-" * 30)

    # Demonstrate to_json with an invalid attrs argument (should return all attributes)
    invalid_attrs_dict = student_instance.to_json(attrs="not a list")
    print("Student object with invalid attrs argument (returns all attributes):")
    print(invalid_attrs_dict)

    print("-" * 30)

    # Demonstrate to_json with an attribute that doesn't exist (it will be ignored)
    non_existent_attr_dict = student_instance.to_json(attrs=["first_name", "non_existent_attribute"])
    print("Student object with a non-existent attribute in attrs list:")
    print(non_existent_attr_dict)
