#!/usr/bin/python3
"""Function to check if an object is an instance of a specified class"""


def is_same_class(obj, a_class):
    """
    Returns True if the objective is exactly an instance of a_class, otherwise returns False.
    """
    return isinstance(obj, a_class) and type(obj) == a_class
