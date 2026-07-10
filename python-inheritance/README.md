# Python - Inheritance

## Overview

This project moves from single classes (`python-classes`, `python-more_classes`) into class hierarchies: subclassing built-in types, introspection helpers for distinguishing "same class" from "same family," and a `BaseGeometry` → `Rectangle` → `Square` chain that uses `super()` and shared validation. It reimplements, without the formal `abc` module, the same "subclasses must implement this" contract that `python-abc` later formalizes with `ABC`/`@abstractmethod` — here it's done by raising a plain `Exception` from the base class instead.

## What's Inside

| File | What it implements |
|---|---|
| `0-lookup.py` | `lookup(obj)` returns `dir(obj)` — lists all attributes/methods available on an object. |
| `1-my_list.py` | `MyList(list)` subclasses the built-in `list` and adds `print_sorted()`, which prints the list in ascending order via `sorted()` without mutating the original. |
| `2-is_same_class.py` | `is_same_class(obj, a_class)` returns `type(obj) is a_class` — true only for an *exact* type match, excluding subclasses. |
| `3-is_kind_of_class.py` | `is_kind_of_class(obj, a_class)` returns `isinstance(obj, a_class)` — true for the class and any of its subclasses. |
| `4-inherits_from.py` | `inherits_from(obj, a_class)` returns `True` only if `obj` is an instance of a *subclass* of `a_class`, not of `a_class` itself. |
| `5-base_geometry.py` | An empty `BaseGeometry` class — the starting skeleton. |
| `6-base_geometry.py` | `BaseGeometry.area()` raises `Exception("area() is not implemented")` — an informal "must override" contract. |
| `7-base_geometry.py` | Adds `integer_validator(name, value)`, raising `TypeError` if not an `int`, `ValueError` if not `> 0`. |
| `8-rectangle.py` | `Rectangle(BaseGeometry)` uses `integer_validator` for `width`/`height` and defines `__str__`; `area()` is inherited unmodified, so it still raises. |
| `9-rectangle.py` | Self-contained `BaseGeometry` + `Rectangle`, now with `Rectangle` overriding `area()` and `__str__` (`"[Rectangle] {width}/{height}"`). |
| `10-square.py` | `Square(Rectangle)` (imports `9-rectangle.py`), calling `super().__init__(size, size)`; `area()` reaches into the parent's name-mangled attributes (`self._Rectangle__width`). |
| `11-square.py` | Self-contained `BaseGeometry` + `Rectangle` + `Square`; `Square` now stores its own `__size` and overrides both `area()` and `__str__` (`"[Square] {size}/{size}"`) independently of the parent's internals. |

## Technical Notes

**Three flavors of "is this an X".** `2-is_same_class.py`, `3-is_kind_of_class.py`, and `4-inherits_from.py` implement three related but distinct checks: exact type equality (`type(obj) is a_class`), inheritance-inclusive membership (`isinstance`), and strict-subclass-only membership (`isinstance` true but `type(obj) is not a_class`). Together they demonstrate why `isinstance()` is almost always the right tool for polymorphic code, while `type() is` is reserved for cases that must exclude subclasses.

**An informal abstract method.** `6-base_geometry.py` defines `area()` to unconditionally `raise Exception("area() is not implemented")`. There is no language-level enforcement here — nothing stops a subclass from never overriding `area()`, as `8-rectangle.py` demonstrates: it inherits `BaseGeometry.area()` verbatim and calling it still raises, because `8-rectangle.py` doesn't override it (only `9-rectangle.py` does). This is a deliberate contrast with `python-abc`, where `@abstractmethod` makes the same contract enforced by Python itself at instantiation time.

**The inheritance chain and `super()`.** The chain is `BaseGeometry → Rectangle → Square`. `Square.__init__` in both `10-square.py` and `11-square.py` calls `self.integer_validator("size", size)` (inherited from `BaseGeometry`) and then `super().__init__(size, size)` to delegate to `Rectangle.__init__`, which performs its own validation and sets `__width`/`__height`.

**Name mangling across inheritance (`10-square.py` vs `11-square.py`).** In `10-square.py`, `Square.area()` is written as `self._Rectangle__width * self._Rectangle__height` — reaching directly into the parent class's name-mangled private attributes rather than storing its own. This works, but it is exactly why leading-double-underscore attributes are described as "private by convention, not by enforcement": the mangled name is predictable and accessible from anywhere. `11-square.py` shows the cleaner alternative — `Square` stores its own `self.__size` and computes `area()`/`__str__` from it directly, without depending on the parent's internal representation.

## Why This Approach

`isinstance`/`type()` checks and inheritance hierarchies are the backbone of any codebase built around interfaces — plugin systems, visitor patterns, or ML pipeline steps that all extend a common base transformer/estimator. Knowing precisely when to use `isinstance` (accepting subclasses, the usual case for polymorphic APIs) versus `type() is` (rejecting subclasses, useful for exact serialization or dispatch logic) avoids a common class of subtle bugs. The contrast between `10-square.py` reaching into `_Rectangle__width` and `11-square.py` keeping its own `__size` is a small but concrete illustration of a real design decision: whether a subclass should depend on a parent's private implementation details or maintain its own state — the latter is more robust to changes in the parent class and is the pattern worth defaulting to.

## Usage

Each task has a matching `N-main.py` (some, like tasks 5-7, share a `*-main.py` demonstrating `*-base_geometry.py`):

```bash
python3 1-main.py
python3 7-main.py
python3 11-main.py
```

Unit tests for a couple of tasks are also included under `tests/` (`1-my_list.txt`, `7-base_geometry.txt`), runnable via the standard library `doctest`/`unittest` tooling. All code requires Python 3 and has no external dependencies.
