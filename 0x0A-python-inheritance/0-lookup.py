#!/usr/bin/python3
""" Defines the attribute lookup function """


def lookup(obj):
    """
    Used to return the sorted list of all the attributes and methods of an object.
    """
    return (dir(obj))
