#!/usr/bin/python3
"""checks object of the if instance of a class that
inherited from a specified class"""


def inherits_from(obj, a_class):
    """
    True if obj is an instance of a class that inherited
    (directly or indirectly) from the specified class; otherwise return False.
    """
    if type(obj) == a_class:
        return False
    return issubclass(type(obj), a_class)
