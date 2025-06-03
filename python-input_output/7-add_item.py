#!/usr/bin/python3
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
