# Python - if/else, Loops, Functions

## Overview

This project moves from single-shot scripts into control flow and function design: conditionals (`if`/`elif`/`else`), `for` loops (including nested loops), and the first reusable functions of the curriculum. It covers common interview-style micro-problems — classifying a number, extracting digits without converting to a string, printing formatted sequences, and case-folding characters using ASCII arithmetic — building the foundation for writing logic that isn't just top-to-bottom script execution.

## What's Inside

| File | What it does |
|---|---|
| `0-positive_or_negative.py` | Picks a random integer in `[-10, 10]` and prints whether it is positive, negative, or zero. |
| `1-last_digit.py` | Picks a random integer in `[-10000, 10000]`, computes its last digit (correctly handling negative numbers), and classifies it as `> 5`, `== 0`, or neither. |
| `2-print_alphabet.py` | Prints the lowercase alphabet on one line using `chr()` over the range `97-122`. |
| `3-print_alphabt.py` | Same as above but skips `'e'` and `'q'`, printing the remaining 24 letters. |
| `4-print_hexa.py` | Prints `i = hex(i)` for every integer from 0 to 98. |
| `5-print_comb2.py` | Prints every two-digit number from `00` to `99`, comma-separated, using zero-padded formatting (`{:02d}`). |
| `6-print_comb3.py` | Prints all unique two-digit combinations `ij` where `i < j` (e.g. `01, 02, ..., 89`) using nested loops, with the final pair ending in a newline instead of a comma. |
| `7-islower.py` | `islower(c)` — returns whether a single character is a lowercase ASCII letter, computed via `ord()` comparisons rather than `str.islower()`. |
| `8-uppercase.py` | `uppercase(str)` — builds and prints an uppercase copy of a string by shifting lowercase ASCII codes down by 32 (`chr(ord(c) - 32)`), leaving non-lowercase characters untouched. |
| `9-print_last_digit.py` | `print_last_digit(number)` — prints and returns the last digit of an integer using `abs(number) % 10`, so it works for negative numbers too. |
| `10-add.py` | `add(a, b)` — returns `a + b`. |
| `11-pow.py` | `pow(a, b)` — returns `a ** b`. |
| `12-fizzbuzz.py` | `fizzbuzz()` — prints numbers 1 to 100 space-separated, replacing multiples of 3 with `Fizz`, multiples of 5 with `Buzz`, and multiples of both with `FizzBuzz`. |
| `*-main.py` | Test harnesses (e.g. `10-main.py`, `11-main.py`, `12-main.py`) that import each function with `__import__('N-name').name` and call it with sample inputs to verify behavior. |

## Technical Notes

- Digit extraction is done with arithmetic, not string conversion: `1-last_digit.py` uses `number % 10 if number >= 0 else -(-number % 10)` to get a correctly-signed last digit for negative numbers, and `9-print_last_digit.py` simplifies this with `abs(number) % 10`, which is the cleaner idiom once sign only matters for display.
- Case conversion in `7-islower.py` and `8-uppercase.py` is done manually with `ord()`/`chr()` and the fact that `'a'`-`'z'` and `'A'`-`'Z'` are each contiguous 32-value-apart ranges in ASCII, rather than calling `str.upper()`/`str.islower()` — this is a deliberate exercise in understanding character encoding, not a shortcut.
- `6-print_comb3.py` generates only the strictly-increasing pairs (`i < j`) via a nested loop where the inner loop starts at `i + 1`, avoiding duplicate/reversed pairs instead of filtering them out after generation.
- `5-print_comb2.py` and `6-print_comb3.py` both handle the "last element has no trailing comma" edge case with a conditional inside the `print(..., end=...)` call instead of building a list and calling `str.join()`.
- Every task function is imported dynamically in its corresponding `*-main.py` via `__import__('N-file').function_name`, the standard Holberton test-harness pattern, rather than a normal `import` statement.

## Why This Approach

Solving digit and character problems with raw arithmetic instead of built-in shortcuts (`str(n)[-1]` or `.upper()`) forces a real understanding of how numbers and characters are represented, which pays off when debugging off-by-one errors or working with binary/bitwise operations later. Writing small, single-purpose functions with clear inputs and outputs here is also the same discipline needed for writing testable, composable code in larger data-processing or ML pipelines — functions like `add`, `pow`, and `fizzbuzz` are toy-sized, but the shape (pure function, deterministic output, no side effects) is the shape that scales.

## Usage

Functions are meant to be imported and tested via the provided main files:

```bash
python3 10-main.py
```

```python
#!/usr/bin/python3
add = __import__('10-add').add
print(add(1, 2))
```

Scripts without a corresponding main file (tasks 0-6) are meant to be run directly:

```bash
./2-print_alphabet.py
```
