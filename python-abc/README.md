# Python - ABC (Abstract Base Classes)

## Overview

This is the most advanced project in the series: it replaces the informal "raise an Exception if not overridden" contract from `python-inheritance` with Python's formal `abc` module (`ABC`, `@abstractmethod`), then explores the mechanisms that make Python's object model flexible — duck typing, custom iterator protocols, and multiple inheritance via mixins with explicit method resolution order (MRO). Where `python-inheritance` showed a single linear chain (`BaseGeometry → Rectangle → Square`), this project shows classes composed from multiple, independent parents.

## What's Inside

| File | What it implements |
|---|---|
| `task_00_abc.py` | `Animal(ABC)` with an `@abstractmethod sound()`; `Dog` and `Cat` implement it. Instantiating `Animal()` directly raises `TypeError` because the abstract method is unimplemented. |
| `task_01_duck_typing.py` | `Shape(ABC)` with abstract `area()`/`perimeter()`; `Circle` and `Rectangle` implement both. `shape_info(forme)` prints area and perimeter for *any* object with those two methods, regardless of its type. |
| `task_02_verboselist.py` | `VerboseList(list)` overrides `append`, `extend`, `remove`, and `pop`, calling `super()` for the real behavior and printing a status message after each mutation. |
| `task_03_countediterator.py` | `CountedIterator` wraps any iterable, implementing `__iter__`/`__next__` by hand and tracking how many items have been consumed via `get_count()`. |
| `task_04_flyingfish.py` | `Fish` and `Bird` (unrelated classes, each defining `habitat()`); `FlyingFish(Fish, Bird)` uses multiple inheritance and overrides `swim`, `fly`, and `habitat`; includes a helper that prints `FlyingFish.mro()`. |
| `task_05_dragon.py` | `SwimMixin` and `FlyMixin`, each providing exactly one method; `Dragon(SwimMixin, FlyMixin)` combines both via multiple inheritance and adds its own `roar()`. |

## Technical Notes

**Enforced abstraction (`task_00_abc.py`).** `Animal` inherits from `ABC` and marks `sound()` with `@abstractmethod`. Unlike the manual `raise Exception(...)` pattern used in `python-inheritance`, this is enforced by the interpreter: `Animal()` raises `TypeError` at the moment of instantiation, before `sound()` is ever called, because Python refuses to construct any class that still has unimplemented abstract methods. `Dog` and `Cat` are instantiable only because each provides a concrete `sound()`.

**Duck typing alongside ABCs (`task_01_duck_typing.py`).** `shape_info(forme)` does not check `isinstance(forme, Shape)` anywhere — it simply calls `forme.area()` and `forme.perimeter()`. The `Shape` ABC's job is only to force `Circle` and `Rectangle` to implement a consistent interface; the consumer function relies purely on duck typing ("if it has `area()` and `perimeter()`, it can be used here"), which is why `shape_info` would work unmodified on any other object exposing those two methods, ABC or not.

**Manual iterator protocol (`task_03_countediterator.py`).** `CountedIterator.__init__` stores `iter(count)` and a counter `self.j = 0`. `__iter__` returns `self` (making the object its own iterator, the standard pattern for satisfying `for` loops), and `__next__` delegates to the wrapped iterator's `next()`, incrementing `self.j` on every successful fetch and letting `StopIteration` propagate unmodified when the source is exhausted.

**Multiple inheritance and MRO (`task_04_flyingfish.py`).** `FlyingFish(Fish, Bird)` inherits from two unrelated classes that both define `habitat()`. Because `FlyingFish` overrides `swim`, `fly`, and `habitat` itself, the ambiguity between `Fish.habitat` and `Bird.habitat` never surfaces at runtime — but `FlyingFish.mro()` makes the resolution order explicit: `[FlyingFish, Fish, Bird, object]`, confirming that Python resolves attributes left-to-right through the bases listed in the class definition.

**Mixins (`task_05_dragon.py`).** `SwimMixin` and `FlyMixin` each define exactly one method and nothing else — no `__init__`, no shared state. `Dragon(SwimMixin, FlyMixin)` does *not* override `swim()` or `fly()`; it inherits them unchanged from the mixins and only adds its own `roar()`. This is the pattern that distinguishes a mixin from ordinary inheritance: each mixin contributes an independent, non-overlapping capability, so composing them via multiple inheritance introduces no MRO conflicts.

## Why This Approach

`ABC`/`@abstractmethod` is the same mechanism behind interface-style contracts in larger Python codebases — plugin architectures, and libraries that define an extension point (`BaseEstimator`-style classes, custom `Dataset`/`Model` base classes in ML frameworks) rely on exactly this pattern to fail fast at construction time rather than with a confusing `AttributeError` deep inside a training loop. The duck-typing example in `task_01` is a small but faithful illustration of why so much of the Python data/ML ecosystem (iterables, context managers, `sklearn`'s `fit`/`predict` convention) works through informal structural interfaces rather than strict type hierarchies. `CountedIterator` demonstrates the exact protocol (`__iter__`/`__next__`) that underlies every `for` loop, generator, and lazy data-loading pipeline in Python. Finally, mixins and MRO are directly relevant to any codebase composing behavior from multiple small classes (Django class-based views are a well-known real-world example) — understanding MRO explicitly is what prevents subtle "wrong method got called" bugs when two parents define overlapping names.

## Usage

Each task has a matching `main_XX_*.py` driver:

```bash
python3 main_00_abc.py
python3 main_01_duck_typing.py
python3 main_02_verboselist.py
python3 main_03_countediterator.py
python3 main_04_flyingfish.py
python3 main_05_dragon.py
```

All code requires Python 3 (`abc` is part of the standard library) and has no external dependencies.
