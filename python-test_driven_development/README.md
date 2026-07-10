# Python - Test-Driven Development

## Overview

This project practices test-driven development in Python using the
`doctest` module: each function's docstring-adjacent behavior is captured
as an interactive `>>>` transcript in a `tests/*.txt` file, which doubles
as executable documentation and a regression test. One task
(`6-max_integer`) is instead covered with a `unittest.TestCase` suite,
giving direct, hands-on comparison of the two standard testing approaches
the standard library offers.

## What's Inside

| File | Description |
|---|---|
| `0-add_integer.py` | `add_integer(a, b=98)` — adds two numbers, raising `TypeError` if either isn't an `int`/`float`. |
| `2-matrix_divided.py` | `matrix_divided(matrix, div)` — divides every element of a matrix by `div`, rounded to 2 decimals; validates types, rectangularity, division by zero, and `NaN`/infinite values. |
| `3-say_my_name.py` | `say_my_name(first_name, last_name="")` — prints `"My name is <first> <last>"`, raising `TypeError` for non-string arguments. |
| `4-print_square.py` | `print_square(size)` — prints an `size x size` square of `#`; raises `TypeError` for non-`int` and `ValueError` for negative sizes. |
| `5-text_indentation.py` | `text_indentation(text)` — prints text with two newlines inserted after each `.`, `?`, or `:`, skipping following spaces. |
| `6-max_integer.py` | `max_integer(list=[])` — returns the largest element of a sequence (or `None` if empty), via manual iteration rather than `max()`. |
| `100-matrix_mul.py` | `matrix_mul(m_a, m_b)` — multiplies two matrices after validating shape, type, and dimension compatibility. |
| `tests/0-add_integer.txt`, `2-matrix_divided.txt`, `3-say_my_name.txt`, `4-print_square.txt`, `5-text_indentation.txt`, `100-matrix_mul.txt` | Doctest transcripts: `>>>` sessions covering both normal and error-path behavior for each function above. |
| `tests/6-max_integer_test.py` | `unittest.TestCase` suite (`TestMaxInteger`) for `max_integer`, with one method per scenario. |
| `*-main.py` | Simple driver scripts used to sanity-check each task manually. |

## Technical Notes

**The doctest workflow.** Each `tests/*.txt` file is a literal transcript
of a Python interactive session: lines starting with `>>>` are commands,
the following lines (until the next `>>>` or blank line) are the exact
expected output. Running

```bash
python3 -m doctest -v tests/0-add_integer.txt
```

replays every `>>>` line and diffs the real output against the recorded
one — this was verified directly against this repository (`9 tests in
0-add_integer.txt`, all passing). Because the transcript itself contains
`__import__('0-add_integer').add_integer`, doctest can run the file
standalone from the project root without any extra harness. For error
cases, the transcripts use doctest's built-in traceback matching: a block
of

```
Traceback (most recent call last):
    ...
TypeError: div must be a number
```

tells doctest to ignore the actual call-stack frames (the `...`) and
compare only the final exception type and message — so the test pins
down *what* error is raised and *why*, without coupling to internal
implementation details.

**Edge cases actually exercised.** `tests/2-matrix_divided.txt` covers:
a non-numeric divisor (`TypeError`), division by zero
(`ZeroDivisionError`), a matrix that isn't a list of lists (`TypeError`),
ragged rows of differing length (`TypeError: Each row of the matrix must
have the same size`), an infinite element (`OverflowError`), a `NaN`
element (`ValueError`), an infinite divisor (which correctly returns an
all-zero matrix, since `x / inf == 0.0`), and a `NaN` divisor
(`ValueError`). `tests/100-matrix_mul.txt` similarly walks through
non-list operands, non-list-of-lists operands, empty matrices, non-numeric
elements, ragged rows, incompatible dimensions for multiplication, and
even missing-argument `TypeError`s from calling the function with too
few arguments. `0-add_integer.py` itself doesn't special-case infinity or
`NaN` — its doctest exploits the fact that Python's own `int()` conversion
already raises `OverflowError` for infinity and `ValueError` for `NaN`,
so the transcript documents behavior that emerges from the language
itself rather than from hand-written validation code.

**Mixing testing styles.** `6-max_integer.py` is instead tested with
`tests/6-max_integer_test.py`, a `unittest.TestCase` with one method per
scenario: ordered/unordered lists, the max at the first position, a
single-element list, an empty list (`assertIsNone`), negative numbers,
mixed positive/negative values, duplicate maxima, floats, and — notably —
passing a plain string, relying on the fact that `max_integer` only needs
`>` comparisons and indexing to work, so it happens to work on any
ordered sequence, not just lists of `int`. This suite runs with:

```bash
python3 -m unittest tests/6-max_integer_test.py -v
```

## Why This Approach

Writing the test transcript alongside (or before) the implementation
forces explicit thinking about a function's contract up front: what types
are accepted, what happens on empty input, and — critically for anything
touching numeric data — what happens with `NaN`, infinity, division by
zero, or malformed shapes. Those are exactly the failure modes that
silently corrupt results in a data or ML pipeline (a `NaN` that
propagates through a matrix operation instead of failing loudly is a
classic, hard-to-trace bug). Doctest's extra benefit is that the tests
are also the documentation: anyone reading the docstring transcript sees
real, executable input/output pairs rather than a prose description that
can drift out of sync with the code. Using `unittest` for `max_integer`
alongside the doctest files also demonstrates familiarity with both of
Python's standard testing paradigms, not just one.

## Usage

Run any task's driver script directly:

```bash
python3 0-main.py
python3 2-main.py
python3 100-main.py
```

Run the doctest suite for any task (all commands are run from the
project root so the transcripts' `__import__` calls resolve):

```bash
python3 -m doctest -v tests/0-add_integer.txt
python3 -m doctest -v tests/2-matrix_divided.txt
python3 -m doctest -v tests/3-say_my_name.txt
python3 -m doctest -v tests/4-print_square.txt
python3 -m doctest -v tests/5-text_indentation.txt
python3 -m doctest -v tests/100-matrix_mul.txt
```

Run the `unittest` suite for `max_integer`:

```bash
python3 -m unittest tests/6-max_integer_test.py -v
```
