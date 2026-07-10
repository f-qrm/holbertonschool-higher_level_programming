# Python - Hello, World

## Overview

This project is the entry point into the Higher Level Programming track and focuses on the absolute basics of Python: running a script from the shell, printing output, and manipulating strings through indexing, slicing, and concatenation. Each task is a short standalone script rather than a reusable function, which keeps the focus on syntax fluency — string formatting, `f-strings`, and Python's slice notation — before functions and control flow are introduced in later projects.

## What's Inside

| File | What it does |
|---|---|
| `2-print.py` | Prints a string containing an escaped double quote using `\"`. |
| `3-print_number.py` | Uses an f-string to print an integer variable inside a sentence (`f"{number} Battery street"`). |
| `4-print_float.py` | Prints a float formatted to two decimal places with the `{:.2f}` format spec. |
| `5-print_string.py` | Prints a string repeated three times (`str * 3`) and then a slice of its first 9 characters (`str[0:9]`). |
| `6-concat.py` | Concatenates two strings with `+` and interpolates the result into an f-string. |
| `7-edges.py` | Extracts the first 3 characters, last 2 characters, and the "middle" of a string using positive and negative slice indices (`word[0:3]`, `word[-2:]`, `word[1:-1]`). |
| `8-concat_edges.py` | Builds a new string by slicing three different, non-contiguous ranges out of a longer paragraph (`str[39:66]`, `str[107:111]`, `str[0:6]`) and joining them with spaces. |
| `9-easter_egg.py` | Runs `import this` to print the Zen of Python. |

## Technical Notes

- Every slicing exercise (`7-edges.py`, `8-concat_edges.py`) relies on Python's `start:stop` slice semantics, including negative indices to count from the end of the string (`word[-2:]`) — no manual loops or `len()` arithmetic are used, which is the idiomatic way to do it in Python.
- `4-print_float.py` uses a format specifier (`:.2f`) rather than manually rounding the float, showing awareness of Python's string formatting mini-language instead of doing math to truncate decimals.
- `8-concat_edges.py` demonstrates that a single long string literal can be split across two source lines with a trailing backslash while still being treated as one string, then reassembles a new sentence purely through slicing and index arithmetic on the original text.
- All scripts start with the `#!/usr/bin/python3` shebang and are executable, so they can be run directly rather than only via `python3 file.py`.

## Why This Approach

These tasks look trivial on their own, but they build the reflexes that make everything downstream faster: knowing slice syntax cold, reaching for f-strings instead of string concatenation with `%` or `.format()` clutter, and being comfortable with negative indexing. That fluency pays off directly later when working with pandas Series/DataFrame slicing or numpy array indexing, which follow the same mental model as native Python slices.

## Usage

Each script is self-contained and executable. Run any file directly:

```bash
./2-print.py
```

or explicitly through the interpreter:

```bash
python3 5-print_string.py
```

No external dependencies are required; only the Python 3 standard library is used.
