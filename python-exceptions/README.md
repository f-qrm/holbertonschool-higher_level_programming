# Python - Exceptions

## Overview

This project is a focused set of exercises on Python's exception-handling model: `try` / `except` / `else` / `finally`, catching specific exception types, and raising exceptions (with and without a custom message). Each task is a small, self-contained function paired with a `*-main.py` driver script that exercises both the success path and the failure path, making the behavior of each exception clause observable rather than theoretical.

## What's Inside

| File | Description |
|---|---|
| `0-safe_print_list.py` | `safe_print_list(my_list, x)` prints the first `x` elements of a list, catching `IndexError` so it stops silently instead of crashing when `x` exceeds the list length. |
| `1-safe_print_integer.py` | `safe_print_integer(value)` prints a value only if it can be formatted as an integer, catching both `ValueError` and `TypeError` in a single `except` tuple and returning `True`/`False` to signal success. |
| `2-safe_print_list_integers.py` | `safe_print_list_integers(my_list, x)` combines the two previous ideas: prints the first `x` items formatted as integers, skipping any item that isn't an integer or any index that doesn't exist. |
| `3-safe_print_division.py` | `safe_print_division(a, b)` divides `a` by `b`, catching `ZeroDivisionError`, and uses `finally` to unconditionally print the intermediate result before returning it. |
| `4-list_division.py` | `list_division(my_list_1, my_list_2, list_length)` divides two lists element-wise, using three separate `except` blocks (`ZeroDivisionError`, `(TypeError, ValueError)`, `IndexError`) each printing a distinct message, with `finally` guaranteeing every position appends a value (0 on failure) so the output list always matches `list_length`. |
| `5-raise_exception.py` | `raise_exception()` unconditionally raises a bare `TypeError`, demonstrating the minimal form of `raise`. |
| `6-raise_exception_msg.py` | `raise_exception_msg(message)` raises a `NameError` constructed with a custom message, demonstrating how to attach diagnostic text to a raised exception. |

## Technical Notes

The exercises build up the exception-handling toolkit in layers:

- **Narrow exception catching.** Every `except` clause targets a specific exception type (or a tuple of types, e.g. `except (ValueError, TypeError):`) rather than a bare `except:`. This avoids masking bugs unrelated to the condition being handled — a bare `except` would also silently swallow things like `KeyboardInterrupt` or a typo turned `NameError`.
- **`finally` for guaranteed execution.** `3-safe_print_division.py` and `4-list_division.py` use `finally` to run code regardless of whether an exception was raised. In `3-safe_print_division.py`, `finally` prints the result even though a `return` may already be pending inside `try` — Python still runs the `finally` block before the function actually returns.
- **Multiple `except` blocks with distinct handling** (`4-list_division.py`) show that exception clauses are checked in order and each type can print a different message and produce a different fallback value, letting the function keep processing the remaining list items instead of aborting on the first bad pair.
- **Raising exceptions explicitly** (`5-raise_exception.py`, `6-raise_exception_msg.py`) shows the two common forms: `raise ExceptionType` for a bare signal, and `raise ExceptionType(message)` to attach context a caller can retrieve via `except NameError as ne: print(ne)`.

## Why This Approach

Exception handling that is too broad (bare `except:`) or too narrow (missing a relevant type) is one of the most common sources of silent data corruption in production code, especially in data-processing and ML pipelines where a single malformed record can otherwise crash — or worse, silently poison — an entire batch job. The pattern practiced here — catching only the exceptions that can actually occur, using `finally` for guaranteed cleanup/bookkeeping, and raising exceptions with informative messages — is directly transferable to writing pipeline code that degrades gracefully on bad input while still surfacing enough information to debug failures.

## Usage

Each task can be run directly against its matching `*-main.py` file, which imports the function dynamically via `__import__` and prints the result:

```bash
python3 0-main.py
python3 3-main.py
python3 6-main.py
```

All files target Python 3 and follow the `#!/usr/bin/python3` shebang convention used throughout the curriculum.
