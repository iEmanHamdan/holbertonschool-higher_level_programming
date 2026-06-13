#!/usr/bin/python3
"""
This is the "5-text_indentation" module.
The module provides one function, text_indentation(text), which formats
strings cleanly by placing double lines behind sentence boundaries.
"""


def text_indentation(text):
    """Prints text with 2 new lines after each of these characters: ., ? and :

    Args:
        text: A string to be parsed and formatted.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Clean leading spaces of the initial line block entirely
    text = text.strip(" ")

    skip_spaces = False
    for char in text:
        if skip_spaces and char == ' ':
            continue
        
        skip_spaces = False
        print(char, end="")

        if char in ['.', '?', ':']:
            print("\n")
            skip_spaces = True
