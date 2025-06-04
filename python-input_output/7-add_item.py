#!/usr/bin/python3
"""
7-add_item.py

This script adds all command line arguments to a Python list,
then saves them to a JSON file (`add_item.json`).

It uses the functions `save_to_json_file` and `load_from_json_file`
from previous modules to persist data between script executions.
"""

import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

try:
    new_list = load_from_json_file(filename)
except FileNotFoundError:
    new_list = []

new_list.extend(sys.argv[1:])
save_to_json_file(new_list, filename)
