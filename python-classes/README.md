# Python - Classes and Objects

## Overview

This project is an introduction to object-oriented programming in Python, built entirely around a single evolving example: a `Square` class. Each task adds one more OOP fundamental on top of the last — attributes, input validation, encapsulation via properties, and instance methods — rather than jumping straight to a "finished" design. As the first project in this series, it lays the groundwork (classes, `__init__`, private attributes, `@property`) that the later projects (`python-more_classes`, `python-inheritance`, `python-abc`) build on directly.

## What's Inside

| File | What it implements |
|---|---|
| `0-square.py` | An empty `Square` class (`pass`) — the starting skeleton for a class definition. |
| `1-square.py` | Adds `__init__(self, size)`, storing the argument in a private attribute `__size` without validation. |
| `2-square.py` | Adds validation in `__init__`: raises `TypeError` if `size` is not an `int`, `ValueError` if `size < 0`. |
| `3-square.py` | Adds an `area()` method returning `self.__size * self.__size`. |
| `4-square.py` | Replaces direct attribute access with a `size` property (getter + setter); validation logic moves into the setter. |
| `5-square.py` | Adds `my_print()`, which renders the square as a grid of `#` characters (or a blank line when `size == 0`). |
| `6-square.py` | Adds a `position` property (a validated tuple of 2 non-negative integers) and updates `my_print()` to offset the printed square using spaces (x-offset) and blank lines (y-offset). |

## Technical Notes

**Encapsulation with name-mangled attributes.** From `1-square.py` onward, the size is stored as `self.__size`, which Python name-mangles to `self._Square__size`. Combined with the `@property` pattern introduced in `4-square.py`, this keeps the internal state private while still exposing a clean, attribute-like public interface (`square.size` instead of `square.get_size()`).

**Validation lives in the setter, not `__init__`.** In `4-square.py` and later, `__init__` no longer validates anything directly — it simply does `self.size = size`, which routes through the `@size.setter`:

```python
@size.setter
def size(self, value):
    if not isinstance(value, int):
        raise TypeError("size must be an integer")
    if value < 0:
        raise ValueError("size must be >= 0")
    self.__size = value
```

Because the setter is invoked both from `__init__` and from any later `square.size = new_value` assignment, validation is enforced consistently regardless of how the attribute is set — there is no way to bypass it through the public interface.

**Position validation (`6-square.py`).** The `position` setter checks four conditions in one guard clause: that the value is a `tuple`, that it has exactly 2 elements, and that both elements are non-negative integers. `my_print()` then uses `position[1]` to print leading blank lines and `position[0]` to prepend spaces to each row — translating validated data directly into rendering logic.

## Why This Approach

Deliberately re-implementing the same small class six times, each with one added capability, mirrors how production code actually evolves: validation and encapsulation are rarely bolted on up front, they get layered in as an API's contract firms up. Writing setters that reject invalid input at the boundary (wrong type, negative size, malformed position) is the same defensive habit that keeps larger systems — API request handlers, data pipeline configs, model constructors — from silently accepting garbage and failing confusingly three calls later.

Getting comfortable with `@property` also pays off directly in any codebase that exposes computed or validated attributes, which is standard practice in most non-trivial Python libraries.

## Usage

Each task ships with its own `N-main.py` demonstrating the corresponding `N-square.py`. Run them directly from this directory:

```bash
python3 0-main.py
python3 2-main.py
python3 6-main.py
```

All classes require Python 3 and have no external dependencies.
