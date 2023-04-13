#!/usr/bin/python3
""" A function that writes a string to a text file. """


def write_file(filename="", text=""):
    """This function is meant to write a string to a text file with the encoding (UTF-8)
    and returns the number of characters written in a stdout."""
    with open(filename, encoding="utf-8", mode="w+") as f:
        return f.write(text)
