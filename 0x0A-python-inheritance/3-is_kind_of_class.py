#!/usr/bin/python3
"""Returns True if the object is an instance of, or an instance of a class that it is inherited from,
that is, the specified class; otherwise False"""


def is_kind_of_class(obj, a_class):
    """returns true if is isinstance is true else return false"""

    return isinstance(obj, a_class)
