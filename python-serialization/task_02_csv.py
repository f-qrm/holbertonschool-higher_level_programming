#!/usr/bin/env python3
"""
Module to convert data from a CSV file into a JSON file.

The resulting JSON is saved in a file named 'data.json'.
"""
import csv
import json
def convert_csv_to_json(filename):
    """
    Convert the contents of a CSV file into a JSON file.

    Reads data from the specified CSV file and writes it into a JSON file
    named 'data.json'. Each row in the CSV becomes a dictionary in a list.

    Args:
        filename (str): The name of the CSV file to convert.

    Returns:
        bool: True if the conversion was successful,
              False if the file was not found.
    """
    try:
        with open(filename, mode='r') as f:
            data = list(csv.DictReader(f))
        with open('data.json', 'w') as file:
            json.dump(data, file)
        return True
    except FileNotFoundError:
        return False
