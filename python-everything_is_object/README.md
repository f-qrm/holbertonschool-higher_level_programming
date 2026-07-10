# Python - Everything is Object

## Overview

This project is a conceptual quiz (plus one small implementation task) on CPython's object model: what `type()` and `id()` actually expose, when two names refer to the *same* object versus two *equal* objects, and how mutability determines whether a function call or an in-place operator can affect data the caller still holds a reference to. Every answer is a short text file predicted from reasoning about identity (`is`), equality (`==`), and memory addresses (`id()`) rather than from running code and guessing.

## What's Inside

| File(s) | What it tests |
|---|---|
| `0-answer.txt`, `1-answer.txt` | The built-ins used to introspect an object: `type` returns an object's class, `id` returns its unique memory-address-derived identifier. |
| `2-answer.txt`, `3-answer.txt` | Integer identity: two variables holding the *different* values `89` and `100` are not the same object (`No`), but two variables independently set to the *same* value `89` are (`Yes`) — a direct consequence of CPython's small-integer caching. |
| `4-answer.txt`, `5-answer.txt` | Further identity comparisons between variables, showing that whether two names point to the same object depends on how each was created/assigned, not just on what value it holds. |
| `6-answer.txt` – `13-answer.txt` | Eight paired questions alternating `==` and `is` on strings. Every `==` case is `True` (value equality), while `is` varies (`True`, `False`, `False`, `True`) depending on how each string was constructed — demonstrating that string interning is an implementation detail, not a guarantee. |
| `14-answer.txt`, `15-answer.txt` | Contrasts `list.append()` (mutates the existing object in place — the second variable sees `[1, 2, 3, 4]`) against `+` (builds a *new* list — the original reference stays `[1, 2, 3]`). |
| `16-answer.txt` – `18-answer.txt` | The same contrast applied across a function call: mutating a list argument via `append` inside a function is visible to the caller (`[1, 2, 3, 4]`), but reassigning an int parameter (`1`) or rebinding a list parameter to a new list inside the function (`[1, 2, 3]`) is not — because immutable rebinding and reassignment only change the local name, never the caller's object. |
| `19-copy_list.py` / `19-main.py` | Implements `copy_list(a_list)` using slice syntax `a_list[:]` to return a shallow copy — a new list object with equal content (`==` is `True`) but distinct identity (`is` is `False`). |
| `20-answer.txt` – `23-answer.txt` | A four-part series on tuples and parentheses, establishing that in Python it is the **comma**, not the parentheses, that makes a tuple. |
| `24-answer.txt` – `26-answer.txt` | Identity edge cases: a parenthesized integer without a comma behaves like a plain cached int (`True`), two independently built tuples with identical content are equal but not identical (`False`), and two empty tuples are identical (`True`) because CPython treats the empty tuple as a shared singleton. |
| `27-answer.txt`, `28-answer.txt` | Lists under `+` versus `+=`: `+` allocates a new list (`No`, identity changes), while `+=` on a list mutates it in place via `__iadd__` (`Yes`, identity is preserved) — the same append-vs-rebind distinction as questions 14/15, expressed through operators instead of methods. |

## Technical Notes

The recurring theme across every answer is the distinction between **identity** and **equality**, and between **mutation** and **rebinding**:

- `id(obj)` returns a value guaranteed unique and constant for an object's lifetime (in CPython, its memory address); `is` compares these identities, while `==` calls `__eq__` to compare values. Two objects can be equal without being identical (`25-answer.txt`: two equal-content tuples, `is` is `False`), but identical objects are always equal.
- CPython caches small integers (`-5` to `256`) and often interns short/simple string literals, so `a is b` can be `True` for two independently assigned variables holding the same small int or literal string — this is what questions `3`, `7`, `13`, `24`, and `26` are demonstrating. This caching is a CPython implementation detail, not a language guarantee, which is exactly why the `is`-based answers to the string questions (`9`, `11`) come out `False` in other cases.
- **Mutable objects (lists) can be changed in place**: `append()` and `+=` (which invokes `__iadd__`) modify the existing object, so every reference to it — including a second variable, or the caller's copy after a function call — observes the change. **Immutable objects (int, str, tuple)** can never be modified in place; any operation that looks like a change (`a += 1`, string concatenation) actually rebinds the name to a brand-new object, leaving anything else still pointing at the old object untouched. This is exactly why questions `16`–`18` show a function mutating a list parameter *does* affect the caller, while rebinding an int or list parameter *does not*.
- `+` on two lists always builds a new list object (`15`, `27`); `+=` on a list is sugar for the in-place `__iadd__` and keeps the same object identity (`28`). Confusing these two is a classic source of bugs when a function is expected to mutate its argument.
- `19-copy_list.py`'s `a_list[:]` performs a **shallow copy**: it creates a new outer list object (`new_list is my_list` is `False`) containing the same element references as the original, with equal content (`new_list == my_list` is `True`).

## Why This Approach

Object identity and mutability are not academic trivia — they are a direct source of real bugs in Python-heavy engineering work. Passing a mutable default argument, sharing a list or dict reference across function boundaries without realizing it, or assuming `is` and `==` are interchangeable are recurring mistakes that produce state that silently changes out from under other parts of a program. This is especially relevant adjacent to numerical/ML code: NumPy arrays and pandas objects follow similar aliasing rules (slicing a NumPy array returns a *view*, not a copy), so a solid mental model of when Python creates a new object versus reuses an existing one — built here with plain lists, ints, and tuples — transfers directly to avoiding subtle, hard-to-reproduce state bugs in data-processing code.

## Usage

Most tasks are plain-text conceptual answers with nothing to execute. The one runnable task is `19-copy_list.py`, exercised through its main file:

```bash
python3 19-main.py
```

Expected output shows the original list, the copy, that they compare equal (`==` → `True`), and that they are not the same object (`is` → `False`).
