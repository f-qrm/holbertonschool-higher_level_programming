# Python - Serialization

## Overview

This project compares four ways to serialize Python data — plain JSON,
`pickle`, CSV, and XML — by implementing the same round-trip
(serialize an object, write it to disk, read it back, deserialize it) with
each format's standard-library tools. It's a deliberate survey of format
tradeoffs: what each one can represent, how lossy or lossless the round
trip is, and where each format is actually used in practice.

## What's Inside

| File | Description |
|---|---|
| `task_00_basic_serialization.py` | `serialize_and_save_to_file` / `load_and_deserialize` — a plain dict/list round trip through `json.dump`/`json.load`. |
| `task_01_pickle.py` | `CustomObject` class with `serialize()`/`deserialize()`, persisting a full class instance to disk with the `pickle` module. |
| `task_02_csv.py` | `convert_csv_to_json(filename)` — reads a CSV with `csv.DictReader` and writes the rows as a JSON array of objects to `data.json`. |
| `task_03_xml.py` | `serialize_to_xml` / `deserialize_from_xml` — converts a flat dictionary to/from an XML document using `xml.etree.ElementTree`. |
| `test_serialization.py`, `test_pickle.py`, `test_csv.py`, `test_xml.py` | Demonstration/driver scripts for each task above — they import the task module and print results. None of them import `unittest` or `pytest`; they are runnable examples, not automated test suites. |
| `data.csv` | Sample CSV input for `task_02_csv.py` (currently empty in this checkout — running the conversion on it produces an empty JSON array). |

## Technical Notes

**JSON (`task_00`).** The most portable option: `json.dump`/`json.load`
handle `dict`, `list`, `str`, `int`, `float`, `bool`, and `None` and produce
human-readable, language-agnostic text. It cannot serialize arbitrary
Python objects (class instances, sets, etc.) without first converting
them to one of those basic types.

**Pickle (`task_01`).** `CustomObject.serialize()` calls
`pickle.dump(self, file)` in binary mode (`'wb'`), and
`CustomObject.deserialize()` (a `classmethod`) calls `pickle.load(file)`
in `'rb'` mode to reconstruct the *entire* object — instance attributes
**and** class identity — with no manual conversion step. That's pickle's
advantage over JSON: it can serialize arbitrary Python objects directly.
The tradeoffs are real, though: pickle output is a Python-specific binary
format (not readable by other languages, not human-inspectable), and
`pickle.load` on untrusted input is a known code-execution risk, since
unpickling can invoke arbitrary constructors. Both methods here wrap the
file operations in `try/except Exception: return None`, silently
swallowing I/O errors rather than propagating them.

**CSV (`task_02`).** `csv.DictReader` turns each row of a CSV file into a
dict keyed by its header row, so `list(csv.DictReader(f))` produces
exactly the list-of-dicts shape JSON expects — the conversion is really
just "read structured tabular text, write structured JSON text." CSV's
strength is native tabular data (spreadsheets, exported datasets); it has
no concept of nested structure or explicit types (every value comes back
as a string), which is why converting it to JSON is often a first step
before further processing.

**XML (`task_03`).** `serialize_to_xml` builds an `ElementTree` with a
`<data>` root and one child element per dictionary key
(`ET.SubElement(root, key)`), writing the value as that element's text
via `str(value)`. `deserialize_from_xml` walks the parsed tree's direct
children and rebuilds a dict from `child.tag` / `child.text`. This works
cleanly for flat dictionaries, but it highlights a real limitation of
XML text nodes: everything comes back out as a string (`str`), so a round
trip through this code does not preserve the original Python type of a
value — the caller has to know to re-cast it. XML remains relevant mainly
for interoperating with older enterprise systems, SOAP APIs, and config
formats that predate JSON's dominance.

**How correctness is checked.** Rather than assertions, each `test_*.py`
script exercises its module end-to-end and prints the "before" and "after"
state (e.g. `obj.display()` before and after a pickle round trip, or the
dict returned by `deserialize_from_xml` after a serialize/deserialize
cycle) so correctness is verified by visual inspection of the output
rather than by an automated pass/fail assertion.

## Why This Approach

Choosing a serialization format is a real production decision, not a
stylistic one: JSON is the default for APIs and config because it's
portable and human-readable; pickle is convenient for caching Python
objects between processes but is unsafe to accept from an untrusted
source and unreadable outside Python, which matters when it shows up in
ML pipelines for caching trained models or intermediate objects; CSV is
still how most tabular datasets are exchanged, including in data science
workflows, and converting it to JSON is a common preprocessing step; XML
persists mainly in legacy and enterprise integrations. Having implemented
the same round trip four times with the standard library — instead of
only ever calling a framework's `.to_json()` — makes it possible to reason
about *why* a given format was chosen in a real codebase, and to spot the
tradeoff (lossy types, security risk, portability) it accepted in the
process.

## Usage

There is no automated test runner here — each `test_*.py` file is a
standalone script that exercises the corresponding task and prints its
output:

```bash
python3 task_00_basic_serialization.py   # module only, import it or run test_serialization.py
python3 test_serialization.py
python3 test_pickle.py
python3 test_csv.py
python3 test_xml.py
```
