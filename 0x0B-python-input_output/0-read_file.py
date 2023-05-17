#!/usr/bin/python3
"""Defines a text file. """


def read_file(filename=""):
    """This function reads a text file with encoding (UTF-8) and
    prints the content to stdout."""
    with open(filename, encoding="utf-8") as f:
        for line in f:
            print(line, end="")
