#!/usr/bin/python3
"""
This module defines the function text_indentation.
"""
def text_indentation(text):
    """
    Print a text with two new lines after each '.', '?', or ':' character.
    Removes any spaces following these characters before continuing.
    TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    characters = ['.', '?', ':']
    i = 0
    longeur = len(text)
    while i < longeur:
        print(text[i], end='')
        if text[i] in characters:
            print("\n")
            i += 1
            while i < longeur and text[i] == ' ':
                i += 1
            continue
        i += 1
