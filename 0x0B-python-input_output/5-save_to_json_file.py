#!/usr/bin/python3
"""writes an Object to a text file, using a JSON representation"""

def save_to_json_file(my_obj, filename):
    """Writes Python obj to file using JSON represenation
    Args:
        my_obj: python object
        filename: file
    """
    import json

    with open(filename, mode="w", encoding="utf-8") as f:
        json.dump(my_obj, f)
