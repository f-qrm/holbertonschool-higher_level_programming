# Python - Input/Output

## Overview

This project covers file input/output and JSON persistence in Python: reading
and writing text files, converting Python objects to and from their JSON
representation, and building a small CLI tool that persists state across
executions. It progressively builds toward serializing custom class
instances (`Student`, `MyClass`) — the same `object -> dict -> JSON` pattern
used throughout real-world config files, API payloads, and cached data.

## What's Inside

| File | Description |
|---|---|
| `0-read_file.py` | Reads a UTF-8 text file and prints its content to stdout. |
| `1-write_file.py` | Writes a string to a file (`'w'` mode, overwrite) and returns the number of characters written. |
| `2-append_write.py` | Appends a string to a file (`'a'` mode) and returns the number of characters added. |
| `3-to_json_string.py` | Wraps `json.dumps` to return the JSON string representation of a Python object. |
| `4-from_json_string.py` | Wraps `json.loads` to parse a JSON string back into a Python object. |
| `5-save_to_json_file.py` | Wraps `json.dump` to write a Python object directly to a JSON file. |
| `6-load_from_json_file.py` | Wraps `json.load` to read a Python object directly from a JSON file. |
| `7-add_item.py` | CLI script: appends `sys.argv` arguments to a list persisted in `add_item.json`, across runs. |
| `8-my_class.py` | `MyClass`, a plain object with a `name` and `number` attribute, used to demonstrate that arbitrary objects are not JSON-serializable out of the box. |
| `8-class_to_json.py` | `class_to_json(obj)` — returns `obj.__dict__`, the dictionary description used to make an object JSON-serializable. |
| `9-student.py` | `Student` class with a `to_json()` method returning `self.__dict__`. |
| `10-student.py` | `Student.to_json(attrs=None)` — same as above, but can filter the returned dictionary to a given list of attribute names. |
| `11-student.py` | Adds `reload_from_json(json)`, which repopulates an instance's attributes from a dictionary via `setattr`. |
| `12-pascal_triangle.py` | `pascal_triangle(n)` — builds Pascal's triangle as a list of lists (data-structure exercise from the same module). |
| `*-main.py` | Corresponding driver scripts for each task, used to exercise the functions above. |
| `my_file_0.txt`, `my_first_file.txt`, `file_append.txt` | Sample/target text files for the read, write, and append tasks. |
| `my_list.json`, `my_dict.json`, `my_set.json`, `my_fake.json`, `filename.json` | JSON fixtures used across tasks 3-6: valid list/dict data, an empty file left by a failed set serialization, and a deliberately malformed JSON file used to exercise error handling. |
| `add_item.json` | Persistent store written and re-read by `7-add_item.py` on every run. |

## Technical Notes

**JSON round-tripping.** Tasks 3-6 all follow the same pattern:
a Python object (`dict`/`list`) is converted with `json.dumps`/`json.dump`
into text, and later reconstructed with `json.loads`/`json.load`. The
string-based helpers (`to_json_string`/`from_json_string`) and the
file-based helpers (`save_to_json_file`/`load_from_json_file`) are the same
operation at two different I/O layers:

```python
with open(filename, 'w', encoding='utf-8') as file:
    json.dump(my_obj, file)
...
with open(filename, 'r', encoding='utf-8') as file:
    my_obj = json.load(file)
```

`my_set.json` is empty on disk precisely because this pattern fails for
types `json` doesn't know how to encode: attempting to `json.dump` a
`set` raises `TypeError: Object of type set is not JSON serializable`
after the file has already been opened in `'w'` mode (which truncates
it), leaving a 0-byte file. `my_fake.json` intentionally contains invalid
JSON (`{"is_active": true, 12 }`) to exercise the `JSONDecodeError` path
of `load_from_json_file`.

**Serializing custom objects.** `json` only knows how to encode built-in
types (`dict`, `list`, `str`, `int`, `float`, `bool`, `None`) — it cannot
serialize an arbitrary class instance like `MyClass` directly. The fix
demonstrated in `8-class_to_json.py` is the standard Python idiom: expose
the instance's state as a plain `dict` via `obj.__dict__`, then hand that
dict to `json.dumps`/`json.dump`. `Student` takes this further by making
`to_json()` a method of the class itself (tasks 9-11), first returning
the full `__dict__`, then an attribute-filtered subset, and finally adding
`reload_from_json()` which does the inverse — `setattr(self, key, value)`
for every key in an incoming dict — to rehydrate an existing instance from
previously-saved JSON.

**Write vs. append vs. read modes.** `1-write_file.py` opens in `'w'`
(truncates and overwrites), `2-append_write.py` opens in `'a'` (writes are
added to the end of the file), and `0-read_file.py` opens in the default
read mode. All file operations explicitly pass `encoding='utf-8'` for
portability, and all use `with` blocks so files are closed automatically
even if an exception is raised mid-operation.

**Stateful CLI script.** `7-add_item.py` combines the read/write helpers
into a small persistence workflow: it tries to `load_from_json_file`
first, falls back to an empty list on `FileNotFoundError` (handling the
"first run, no file yet" case), extends that list with `sys.argv[1:]`,
and saves it back — so `add_item.json` accumulates arguments across
repeated invocations.

## Why This Approach

JSON is the de-facto interchange format for configuration files, API
payloads, and lightweight data caching — including in ML workflows, where
hyperparameter configs, dataset metadata, and model evaluation results are
routinely round-tripped through JSON. The `object.__dict__ -> json.dump`
pattern shown here is the same mechanism underlying serialization layers
in frameworks like Django REST Framework or Pydantic, just without the
abstraction: understanding it directly makes it much easier to reason
about what those higher-level tools are actually doing, and to debug
serialization failures (like the non-serializable `set` case above) when
they happen in production.

## Usage

Each task has a corresponding `*-main.py` driver. Run any of them directly
from this directory:

```bash
python3 0-main.py
python3 7-add_item.py Best School 89 Python C
python3 8-main.py
python3 11-main.py student.json
```

`12-pascal_triangle.py` also includes an inline doctest example that can be
verified with:

```bash
python3 -m doctest -v 12-pascal_triangle.py
```
