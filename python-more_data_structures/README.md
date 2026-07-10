# Python - More Data Structures: Sets, Dictionaries

## Overview

This project extends the previous data-structures work into sets and dictionaries, along with the functional-programming tools Python offers for transforming collections (`map`, `lambda`). It covers set algebra (intersection, symmetric difference), dictionary iteration and mutation, and closes with a small parsing algorithm — converting Roman numerals to integers — that combines dictionary lookups with a subtractive-notation edge case.

## What's Inside

| File | What it does |
|---|---|
| `0-square_matrix_simple.py` | `square_matrix_simple(matrix=[])` — returns a new matrix with every element squared, built with a nested `map`/`lambda` instead of nested loops. |
| `1-search_replace.py` | `search_replace(my_list, search, replace)` — returns a new list with every occurrence of `search` replaced by `replace`, leaving the original list untouched. |
| `2-uniq_add.py` | `uniq_add(my_list=[])` — sums only the unique values of a list by first converting it to a `set`. |
| `3-common_elements.py` | `common_elements(set_1, set_2)` — returns the intersection of two sets using the `&` operator. |
| `4-only_diff_elements.py` | `only_diff_elements(set_1, set_2)` — returns the symmetric difference of two sets using the `^` operator (elements in exactly one of the two sets). |
| `5-number_keys.py` | `number_keys(a_dictionary)` — returns the number of keys in a dictionary. |
| `6-print_sorted_dictionary.py` | `print_sorted_dictionary(a_dictionary)` — prints `key: value` pairs in ascending key order using `sorted()` on the dictionary. |
| `7-update_dictionary.py` | `update_dictionary(a_dictionary, key, value)` — adds or overwrites a key/value pair via `dict.update()` and returns the dictionary. |
| `8-simple_delete.py` | `simple_delete(a_dictionary, key="")` — removes a key if present (guarded with a membership check before `.pop()`) and returns the dictionary. |
| `9-multiply_by_2.py` | `multiply_by_2(a_dictionary)` — returns a **new** dictionary with every value doubled, leaving the input dictionary unmodified. |
| `10-best_score.py` | `best_score(a_dictionary)` — returns the key with the highest value in a dictionary, or `None` for an empty dictionary. |
| `11-multiply_list_map.py` | `multiply_list_map(my_list=[], number=0)` — multiplies every element of a list by `number` using `map()` with a `lambda`. |
| `12-roman_to_int.py` | `roman_to_int(roman_string)` — converts a Roman numeral string to its integer value, including subtractive pairs like `IX` and `XL`. |
| `*-main.py` | Test harnesses for each task, importing functions dynamically and running them against sample lists, sets, and dictionaries. |

## Technical Notes

- **Functional style with `map`/`lambda`**: `0-square_matrix_simple.py` and `11-multiply_list_map.py` both avoid explicit `for` loops for the transformation itself, using `map(lambda x: ..., iterable)` wrapped in `list(...)` to force evaluation. `0-square_matrix_simple.py` nests two `map` calls — one over rows, one over each row's elements — to square every value of a 2D list in a single expression.
- **Set algebra maps directly to Python operators**: `3-common_elements.py` and `4-only_diff_elements.py` use `&` (intersection) and `^` (symmetric difference) rather than calling `.intersection()`/`.symmetric_difference()` methods, which is the more idiomatic, terser choice once the reader knows set operator syntax.
- **New collection vs. in-place mutation, again**: `9-multiply_by_2.py` builds a brand-new dictionary (`b_dictionary = {}`, populated via `.items()`) instead of mutating the input, mirroring the same copy-vs-mutate discipline seen in the sibling `python-data_structures` project — while `7-update_dictionary.py` and `8-simple_delete.py` deliberately mutate and return the same dictionary object.
- **`12-roman_to_int.py`** implements the standard Roman-numeral algorithm: iterate left to right, and whenever a numeral's value is smaller than the value immediately to its right, subtract it instead of adding it (this is what correctly handles `IV` = 4, `IX` = 9, `XL` = 40, etc.). It also defensively returns `0` for any non-string input via `isinstance()` before attempting dictionary lookups, avoiding a `KeyError` on bad input.
- **`2-uniq_add.py`** relies on `set(my_list)` to deduplicate before summing, converting an O(n) linear-scan dedup problem into a single built-in call backed by hash-table semantics.

## Why This Approach

Sets and dictionaries are where Python's data structures start to resemble the tools used in real data work — hash-based lookups, deduplication, and key-value transformations are the same operations that later show up as `groupby`, `drop_duplicates`, or dictionary-based feature mappings in pandas. Practicing the functional idioms (`map`, `lambda`, set operators) alongside the explicit loop-based equivalents from the previous project builds fluency in reading both styles, which matters when working in a codebase — or a notebook — that mixes vectorized and imperative code. The Roman numeral converter is the first task in the curriculum that requires an actual algorithm rather than a one-line built-in call, and getting the subtractive-notation edge case right (checking the next character before deciding to add or subtract) is a small but real lesson in not solving a problem by brute-force pattern matching.

## Usage

Each task has a matching `N-main.py` test harness:

```bash
python3 12-main.py
```

```python
#!/usr/bin/python3
roman_to_int = __import__('12-roman_to_int').roman_to_int
print(roman_to_int("LXXXVII"))
```

Modules only define functions with no top-level execution code, so they are meant to be imported (as the main files do) rather than run directly.
