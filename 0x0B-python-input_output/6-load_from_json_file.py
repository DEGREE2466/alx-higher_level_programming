#!/usr/bin/python3
"""Module that loads an object from a JSON file."""


import json


def load_from_json_file(filename):
    """
    Module that loads an object from a JSON file.
    Args:
        filename (str): The path to the JSON file to be loaded.
    Returns:
        The deserialized Python object.
    """
    with open(filename, encoding='utf-8') as f:
        return json.load(f)
