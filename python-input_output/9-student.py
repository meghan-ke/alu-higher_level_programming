#!/usr/bin/python3
"""
This module defines a Student class and provides a function
to serialize a Student object's attributes into a dictionary.
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
    # This returns all attributes defined on the instance, which are
    # guaranteed to be simple data types as per the problem description.
    return obj.__dict__


class Student:
    """
    A Student class that defines a student by first_name, last_name, and age.
    It includes a method to retrieve a dictionary representation for JSON serialization.
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

    def to_json(self):
        """
        Retrieves a dictionary representation of a Student instance.
        This method uses the class_to_json function to get the object's attributes.

        Returns:
            dict: A dictionary containing the first_name, last_name, and age
                  of the student instance.
        """
        return class_to_json(self)


if __name__ == "__main__":
    # Create a Student instance
    student_instance = Student("Alice", "Smith", 21)

    # Convert the student object to a JSON-serializable dictionary
    student_dict = student_instance.to_json()

    # Print the dictionary representation
    print("Student object as dictionary for JSON serialization:")
    print(student_dict)

    # Example with another student
    student_instance_2 = Student("Bob", "Johnson", 19)
    student_dict_2 = student_instance_2.to_json()
    print("\nAnother Student object as dictionary:")
    print(student_dict_2)
