#!/usr/bin/python3
"""Function that saves an object to a text file using
a JSON representation."""

import json


def save_to_json_file(my_obj, filename):
    """
    A function that Saves an object to a text file using a JSON representation.
    Args:
        my_obj (object): The object to be saved.
        filename (str): The path to the file saved
    Returns:
        None
    """
    with open(filename, mode='w', encoding='utf-8') as f:
        json.dump(my_obj, f)
