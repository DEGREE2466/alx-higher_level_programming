#!/usr/bin/python3

"""Provides a function for converting
a JSON string to a Python object."""

import json


def from_json_string(my_str):
    """
    Function that converts a JSON string to a Python object.
    Args:
        my_str (str): The JSON string to be converted to a Python object.
    Returns:
        object: The Python object to be represented by the JSON string.
    """
    return json.loads(my_str)
