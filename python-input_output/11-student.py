#!/usr/bin/python3
"""
This module defines a Student class with serialization (to_json)
and deserialization (reload_from_json) capabilities.
"""

class Student:
    """
    A Student class that defines a student by first_name, last_name, and age.
    It includes methods for converting to a dictionary representation (to_json)
    and for reloading attributes from a dictionary (reload_from_json).
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
        obj_dict = self.__dict__
        filtered_dict = {}

        if isinstance(attrs, list) and all(isinstance(a, str) for a in attrs):
            for attr_name in attrs:
                if attr_name in obj_dict:
                    filtered_dict[attr_name] = obj_dict[attr_name]
            return filtered_dict
        else:
            return obj_dict

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance with values from a dictionary.

        Args:
            json (dict): A dictionary where keys are attribute names and values
                         are the corresponding attribute values.
                         It is assumed that 'json' will always be a dictionary
                         and its keys will be valid public attribute names.
        """
        for key, value in json.items():
            setattr(self, key, value)


if __name__ == "__main__":
    # Create a Student instance
    student_instance = Student("Alice", "Smith", 21)
    print("Original Student instance attributes:")
    print(student_instance.to_json())

    print("-" * 30)

    # Demonstrate to_json (serialization)
    student_dict = student_instance.to_json()
    print("Serialized Student object (all attributes):")
    print(student_dict)

    print("-" * 30)

    # Demonstrate to_json with selected attributes
    selected_attrs_dict = student_instance.to_json(attrs=["first_name", "age"])
    print("Serialized Student object (selected attributes):")
    print(selected_attrs_dict)

    print("-" * 30)

    # Demonstrate reload_from_json (deserialization)
    new_data = {
        "first_name": "Bob",
        "last_name": "Johnson",
        "age": 30,
        "new_attribute": "value" # Demonstrating adding a new attribute
    }
    print("Reloading Student instance with new data:")
    print(new_data)
    student_instance.reload_from_json(new_data)

    print("\nStudent instance attributes after reloading:")
    print(student_instance.to_json())

    print("-" * 30)

    # Verify individual attributes after reload
    print(f"Student first name: {student_instance.first_name}")
    print(f"Student age: {student_instance.age}")
    print(f"Student new attribute: {student_instance.new_attribute}") # Accessing the newly added attribute
