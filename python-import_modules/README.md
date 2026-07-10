# Python - Import & Modules

## Overview

This project covers how Python's import system actually behaves: module-level code executing on import, the `if __name__ == "__main__":` guard that distinguishes "run as a script" from "imported as a module," passing arguments through `sys.argv`, and introspecting a module's namespace with `dir()`. Each numbered task is a runnable script paired with a small helper module it imports from.

## What's Inside

| File | Description |
|---|---|
| `add_0.py` | Helper module defining `add(a, b)`, documented with a docstring; has no `__main__` guard, so importing it only defines the function, nothing executes. |
| `0-add.py` | Imports `add` from `add_0` with `from add_0 import add`, then, inside an `if __name__ == "__main__":` guard, computes and prints `1 + 2`. |
| `0-import_add.py` | A single line, `__import__("0-add")`, that imports `0-add` dynamically by string name. Running it prints **nothing**, because `__import__` executes the target module with `__name__` set to `"0-add"`, not `"__main__"` — so the guarded `print` inside `0-add.py` never runs. This is the clearest demonstration in the project of what the `__main__` guard is actually for. |
| `calculator_1.py` | Helper module defining four documented functions — `add`, `sub`, `mul`, `div` (division truncated to `int`) — with no top-level executable code. |
| `1-calculation.py` | Imports all four functions from `calculator_1` *inside* the `__main__` guard (`from calculator_1 import add, sub, mul, div`), then prints the result of each operation on `10` and `5`. |
| `2-args.py` | Reads `sys.argv` to report how many command-line arguments were passed (with correct singular/plural wording for exactly one argument) and lists each one with its 1-based index. |
| `3-infinite_add.py` | Reads an arbitrary number of command-line arguments via `sys.argv`, converts each to `int`, and prints their sum — no fixed argument count. |
| `4-hidden_discovery.py` | Imports a module named `hidden_4` (intentionally not present in this repository — supplied externally at evaluation time) and prints every public name in it, sorted, using `dir(hidden_4)` filtered to exclude dunder attributes. Demonstrates that `dir()` works on any importable module regardless of what it contains. |
| `variable_load_5.py` | Helper module that simply defines `a = 98` at module level — a plain attribute, not a pickled or serialized value. |
| `5-variable_load.py` | Imports the single variable `a` from `variable_load_5` with `from variable_load_5 import a` and prints it. |
| `.gitignore` | Ignores all generated/compiled artifacts except `.gitignore` itself and any `*.py` source file, keeping the repository limited to source code. |

## Technical Notes

- **Module-level code runs once, at import time.** `add_0.py` and `calculator_1.py` contain only function/def statements, so importing them has no visible side effect beyond making the functions available. `variable_load_5.py` shows the same for a plain variable assignment: `a = 98` executes immediately on import and becomes an attribute of the module object.
- **The `if __name__ == "__main__":` guard** distinguishes code meant to run only when a file is executed directly from code meant to be reusable on import. Every task file (`0-add.py`, `1-calculation.py`, `2-args.py`, `3-infinite_add.py`, `4-hidden_discovery.py`, `5-variable_load.py`) wraps its executable logic in this guard. `0-import_add.py` makes the effect concrete: because `__import__("0-add")` sets `0-add`'s `__name__` to `"0-add"` rather than `"__main__"`, its guarded `print` statement is skipped entirely — confirmed by running the file, which produces no output.
- **`from module import name`** (used throughout) binds a specific function or variable directly into the importing script's namespace, versus `import module` followed by `module.name`. `1-calculation.py` and `5-variable_load.py` both use the `from ... import` form; `0-import_add.py` instead uses the dynamic, string-based `__import__()` form, which is the mechanism the curriculum's own `*-main.py` test scripts rely on elsewhere in this repository.
- **`sys.argv`** is a list where index `0` is always the script's own path, so `2-args.py` and `3-infinite_add.py` both iterate starting from index `1` and compute the argument count as `len(sys.argv) - 1`.
- **`dir(module)`** returns every name bound in a module's namespace, including imported names and dunder attributes; `4-hidden_discovery.py` filters out anything starting with `__` to list only the module's own public members.

## Why This Approach

Understanding exactly when module-level code executes — and guarding script-only logic behind `__name__ == "__main__"` — is what makes a Python file safely reusable as both a library and a command-line tool, which is the standard shape of scripts in data and ML tooling (a preprocessing script that is also imported by a training pipeline, for instance). `sys.argv`-based argument reading is the minimal foundation underneath every CLI tool before reaching for a framework like `argparse`, and knowing precisely how `import`, `from ... import`, and `__import__()` differ avoids subtle bugs where a module is imported multiple times, imported for its side effects unintentionally, or fails silently because a guarded block never runs.

## Usage

Each script is runnable directly; several also demonstrate behavior through command-line arguments:

```bash
python3 0-add.py
python3 0-import_add.py
python3 1-calculation.py
python3 2-args.py a b c
python3 3-infinite_add.py 1 2 3 4
python3 5-variable_load.py
```

`4-hidden_discovery.py` requires a `hidden_4` module to be present on the Python path (not included in this repository) and will raise `ModuleNotFoundError` without it.
