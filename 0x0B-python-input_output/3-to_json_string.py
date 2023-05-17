#!/usr/bin/python3
"""Function to return JSON representation of an object (string)."""
import json


def to_json_string(my_obj):
    """
    A function that returns the JSON representation of an object as a string.
    Args:
        my_obj (object): An object to be converted to a JSON string.
    Returns:
        str: The JSON representation of the object returned as a string.
    """
    return json.dumps(my_obj)
