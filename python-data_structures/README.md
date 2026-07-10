# Python - Data Structures: Lists, Tuples

## Overview

This project focuses on Python's core sequence types — lists and tuples — and the operations built on top of them: indexing, mutation, copying, iteration, and building new collections from existing ones. It also introduces functions with default mutable arguments and functions that return multiple values as a tuple, both of which surface real Python gotchas around object identity and mutability that go beyond simple scripting.

## What's Inside

| File | What it does |
|---|---|
| `0-print_list_integer.py` | `print_list_integer(my_list=[])` — prints each integer in a list on its own line using `{:d}` formatting. |
| `1-element_at.py` | `element_at(my_list, idx)` — returns the element at `idx`, or `None` if the index is out of range. |
| `2-replace_in_list.py` | `replace_in_list(my_list, idx, element)` — replaces an element in place at a given index and returns the same (mutated) list. |
| `3-print_reversed_list_integer.py` | `print_reversed_list_integer(my_list=[])` — reverses a list of integers in place with `.reverse()` and prints each value. |
| `4-new_in_list.py` | `new_in_list(my_list, idx, element)` — returns a **new** list with an element replaced at `idx`, leaving the original list untouched (uses a full-slice copy `my_list[:]`). |
| `5-no_c.py` | `no_c(my_string)` — returns a copy of a string with every `'c'`/`'C'` character removed. |
| `6-print_matrix_integer.py` | `print_matrix_integer(matrix=[[]])` — prints a 2D list as a space-separated grid, one row per line, using a generator expression inside `" ".join(...)`. |
| `7-add_tuple.py` | `add_tuple(tuple_a=(), tuple_b=())` — element-wise sum of two 2-value tuples, treating any missing element (tuple shorter than 2) as `0`. |
| `8-multiple_returns.py` | `multiple_returns(sentence)` — returns a `(length, first_character)` tuple, or `(0, None)` for an empty string. |
| `9-max_integer.py` | `max_integer(my_list=[])` — returns the largest value in a list (or `None` if empty) via manual linear scan rather than `max()`. |
| `10-divisible_by_2.py` | `divisible_by_2(my_list=[])` — returns a new list of booleans indicating which elements of the input are even, built from a copy of the original list. |
| `11-delete_at.py` | `delete_at(my_list=[], idx=0)` — deletes the element at `idx` in place with `del` and returns the mutated list; no-ops on an out-of-range index. |
| `12-switch.py` | Swaps two variables in a single line using tuple unpacking (`a, b = b, a`) and prints the result. |
| `*-main.py` | Test harnesses (`0-main.py` through `11-main.py`) that dynamically import each task function and exercise it against sample lists/tuples/strings. |

## Technical Notes

- **Mutation vs. copy is deliberate and consistent across the project**: functions like `2-replace_in_list.py` and `11-delete_at.py` intentionally mutate the list they receive and return the same reference, while `4-new_in_list.py` and `10-divisible_by_2.py` explicitly copy first with slice notation (`my_list[:]`) before making any change, so the caller's original list is never touched. This is the same distinction that trips up developers coming from languages with value semantics, and the code demonstrates understanding it rather than accidentally getting it right.
- **Mutable default arguments** (`my_list=[]`, `matrix=[[]]`, `tuple_a=()`) appear throughout. Since tuples are immutable, defaulting to `()` is safe; defaulting to `[]` is the classic Python foot-gun (a single shared list object reused across calls) but is safe here specifically because none of these functions mutate the default in place without first replacing/copying it (e.g. `print_list_integer` only reads, `divisible_by_2` copies before writing).
- `6-print_matrix_integer.py` prints a matrix without manually building an intermediate string with string concatenation — it composes a generator expression with `str.join`, which is the idiomatic, allocation-efficient way to stringify a row in Python.
- `7-add_tuple.py` handles tuples shorter than length 2 defensively with conditional expressions (`tuple_a[0] if len(tuple_a) > 0 else 0`) rather than assuming fixed-length input, avoiding an `IndexError` on short or empty tuples.
- `9-max_integer.py` implements the max-finding algorithm manually (linear scan with a running maximum) instead of calling the built-in `max()`, which is the point of the exercise — understanding the O(n) algorithm underneath the built-in.

## Why This Approach

Lists and tuples are the backbone of virtually every data-processing task in Python, and the distinction between "mutate in place" and "return a new copy" is exactly the kind of subtlety that causes real bugs once code grows beyond a single file — a function that silently mutates a caller's list is a common source of hard-to-trace defects. Practicing both patterns deliberately, on toy problems, builds the instinct to know which one a given function should use before it matters in a larger codebase. This same list/tuple mental model — slicing, copying, in-place mutation, iteration — carries over directly into working with numpy arrays and pandas Series later, where the copy-vs-view distinction is even more consequential.

## Usage

Each task has a matching `N-main.py` test harness that imports the function dynamically and prints example output:

```bash
python3 6-main.py
```

```python
#!/usr/bin/python3
print_list_integer = __import__('0-print_list_integer').print_list_integer

my_list = [1, 2, 3, 4, 5]
print_list_integer(my_list)
```

Individual modules are not intended to be run directly since they only define functions with no top-level execution code.
