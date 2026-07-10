# Python - More Classes and Objects

## Overview

This project extends the `Square` groundwork from `python-classes` into a more feature-complete `Rectangle` class, focused on Python's data model: dunder (magic) methods, class attributes shared across instances, and static/class methods. Building on `python-classes`, which covered `@property`-based encapsulation, this project asks "how does an object integrate with the rest of the language" — how it prints, how it's recreated with `eval()`, how it reports its own destruction, and how instances can be counted or built through alternate constructors.

## What's Inside

| File | What it implements |
|---|---|
| `0-rectangle.py` | An empty `Rectangle` class — the starting skeleton. |
| `1-rectangle.py` | `width`/`height` as validated `@property` attributes (same `TypeError`/`ValueError` pattern as `python-classes`). |
| `2-rectangle.py` | Adds `area()` and `perimeter()` (perimeter is `0` if either dimension is `0`). |
| `3-rectangle.py` | Adds `__str__`, rendering the rectangle as rows of `#` characters. |
| `4-rectangle.py` | Adds `__repr__`, returning an `eval()`-able string such as `"Rectangle(4, 6)"`. |
| `5-rectangle.py` | Adds `__del__`, which prints `"Bye rectangle..."` when an instance is garbage-collected. |
| `6-rectangle.py` | Adds the class attribute `number_of_instances`, incremented in `__init__` and decremented in `__del__`. |
| `7-rectangle.py` | Adds the class attribute `print_symbol` and updates `__str__` to render with `str(self.print_symbol)` instead of a hardcoded `"#"`. |
| `8-rectangle.py` | Adds the static method `bigger_or_equal(rect_1, rect_2)`, returning whichever rectangle has the larger area. |
| `9-rectangle.py` | Adds the class method `square(cls, size=0)`, a factory that returns `cls(size, size)`. |

## Technical Notes

**`__str__` vs `__repr__`.** `__str__` (task 3) produces a human-readable ASCII-art rendering used by `print(rectangle)`, while `__repr__` (task 4) produces a machine-readable constructor call, `"Rectangle({width}, {height})"`, such that `eval(repr(r))` reconstructs an equivalent instance. This is the standard Python convention: `__str__` for display, `__repr__` for unambiguous reproduction/debugging.

**Class attributes vs instance attributes.** `number_of_instances` (task 6) is declared once at class level (`number_of_instances = 0`) and mutated through the class itself (`Rectangle.number_of_instances += 1` / `-= 1`) inside `__init__` and `__del__`. Because it is looked up on the class rather than stored per-instance, every `Rectangle` object shares and updates the same counter — a direct contrast to `__width`/`__height`, which are private, per-instance attributes behind `@property`.

**`print_symbol` as an overridable class attribute (task 7).** `__str__` no longer hardcodes `"#"`; it uses `str(self.print_symbol)`. Since `print_symbol` is a class attribute, it can be reassigned per-instance (`my_rect.print_symbol = "*"`) or overridden by a subclass, without touching `__str__` itself — a small but real example of how class-level configuration can decouple behavior from data.

**Static method (`bigger_or_equal`, task 8).** Declared with `@staticmethod`, it takes no `self`/`cls` and is called on the class (`Rectangle.bigger_or_equal(r1, r2)`). It validates both arguments with `isinstance(..., Rectangle)` before comparing `.area()`, making it a pure utility function that is grouped with the class for discoverability but does not depend on instance state.

**Class method as factory (`square`, task 9).** `square(cls, size=0)` uses `cls(size, size)` rather than `Rectangle(size, size)`. Using `cls` instead of the class name directly means that if a subclass inherits `square()` unchanged, calling `Subclass.square(5)` returns a `Subclass` instance, not a `Rectangle` — the classmethod pattern that keeps factory constructors correct under inheritance.

## Why This Approach

Implementing `__str__`/`__repr__` deliberately is what makes custom objects debuggable in a REPL, in logs, and in test failure output — the difference between a stack trace showing `<Rectangle object at 0x7f...>` and one showing `Rectangle(4, 6)` is the difference between guessing and knowing. The `number_of_instances` counter is a minimal but genuine example of shared class-level state, the same mechanism used for things like connection pools or instance registries. The `classmethod`-as-factory pattern (`square`) is the same one used throughout the Python ecosystem for alternate constructors (e.g. `dict.fromkeys`, `datetime.fromtimestamp`), and understanding why it uses `cls` rather than the literal class name matters as soon as any of these classes are subclassed.

## Usage

Each task has a matching `N-main.py`:

```bash
python3 3-main.py
python3 6-main.py
python3 9-main.py
```

All classes require Python 3 and have no external dependencies.
