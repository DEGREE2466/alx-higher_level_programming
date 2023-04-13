#!/usr/bin/python3
"""
Contains a function that returns the dictionary description with the
simple data structures (list, dictionary, string, integer and boolean) for a JSON
serialization of an object.
"""


def class_to_json(obj):
    """
    A string that returns a dictionary description with simple data structure for JSON
    serialization of an object.
    Args:
        obj: The object to serialize.
    Returns:
        A dictionary with a simple data structure for JSON serialization.
    """
    return obj.__dict__
