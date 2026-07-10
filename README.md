# Higher-Level Programming

A portfolio of backend-focused programming projects covering Python, SQL, and JavaScript fundamentals through to web APIs, ORMs, and server-side rendering. Each project lives in its own directory with a dedicated README explaining what it does, how it works, and why it was built that way — this file is the index and the map of how the pieces connect.

The projects are organized as a deliberate progression: language fundamentals first, then object-oriented design, then the language internals that make Python's object model predictable, then the practical skills (file I/O, serialization, testing discipline) that production code depends on, and finally the systems layer — relational databases, ORMs, server-side rendering, and REST APIs with real authentication. The intent is not just to show that each topic was "covered," but to demonstrate the reasoning behind each implementation choice, since that reasoning is what actually transfers to production and ML-systems work.

## Why this repository is structured this way

Most of these exercises could be solved faster with a framework or a library shortcut. They're deliberately not, at least not at first: raw SQL before an ORM, a hand-rolled HTTP server before Flask, manual `try`/`except` branching before relying on library-level error handling, doctest-driven functions before reaching for a test framework's full machinery. The point is to understand what the abstraction is actually doing underneath, so that when something breaks in a framework-heavy production system — a leaking N+1 query, a misbehaving auth token, a serialization edge case — the underlying mechanics aren't a black box. That habit of building from first principles before adopting the shortcut is the throughline across every project below.

## Project Index

### Language fundamentals

| Project | Focus |
|---|---|
| [python-hello_world](./python-hello_world) | Entry-level scripts: `f-string` formatting and string slicing (positive/negative indices). |
| [python-if_else_loops_functions](./python-if_else_loops_functions) | Control flow and first functions; digit/character problems solved with raw arithmetic (`ord()`/`chr()`, modulo) instead of built-in shortcuts. |
| [python-data_structures](./python-data_structures) | List/tuple manipulation: indexing, in-place mutation vs. returning copies, multi-value returns, manual algorithms instead of built-ins. |
| [python-more_data_structures](./python-more_data_structures) | Sets, dictionaries, `map`/`lambda`, set algebra, and a Roman-numeral parser implementing the subtractive-notation algorithm. |
| [javascript-warm_up](./javascript-warm_up) | Core JavaScript/Node.js: `process.argv`, recursion, array methods, CommonJS `module.exports`/`require`. |
| [javascript-dom_manipulation](./javascript-dom_manipulation) | Browser DOM APIs: `querySelector`, `addEventListener`, `classList`, dynamic node creation, and async `fetch` against live public REST APIs. |

### Object-oriented design

| Project | Focus |
|---|---|
| [python-classes](./python-classes) | OOP fundamentals via an evolving `Square` class: `__init__` validation, private attributes via name mangling, `@property` getters/setters. |
| [python-more_classes](./python-more_classes) | Python's data model on a `Rectangle` class: `__str__`/`__repr__`, `__del__`, class attributes, `@staticmethod` vs. `@classmethod` (with `cls`-aware factories). |
| [python-inheritance](./python-inheritance) | A `BaseGeometry → Rectangle → Square` hierarchy using `super()`, `type() is` vs. `isinstance()`, and an informal (exception-raising) abstract method. |
| [python-abc](./python-abc) | Formal `ABC`/`@abstractmethod` enforcement, duck typing, a hand-rolled iterator protocol (`__iter__`/`__next__`), and multiple inheritance/MRO. |

### Language internals

| Project | Focus |
|---|---|
| [python-exceptions](./python-exceptions) | `try`/`except`/`finally` mechanics: narrow exception catching, cleanup blocks around pending returns, custom exception raising. |
| [python-everything_is_object](./python-everything_is_object) | A conceptual tour of CPython's object model: `id()`, identity vs. equality, integer/string interning, and in-place mutation vs. rebinding. |
| [python-import_modules](./python-import_modules) | Import mechanics: module-level execution on import, the `__name__ == "__main__"` guard, `from ... import`, `__import__()`, `sys.argv`. |

### Practical engineering discipline

| Project | Focus |
|---|---|
| [python-input_output](./python-input_output) | File read/write/append and JSON round-tripping, including serializing custom class instances and a stateful CLI tool. |
| [python-serialization](./python-serialization) | Head-to-head comparison of JSON, pickle, CSV, and XML serialization, implemented directly against the standard library, with their real tradeoffs. |
| [python-test_driven_development](./python-test_driven_development) | Doctest-driven development: numeric edge cases (`NaN`, infinity, division by zero, ragged matrices) captured as executable `>>>` transcripts, plus a `unittest` suite. |

### Databases, web, and APIs

| Project | Focus |
|---|---|
| [SQL_introduction](./SQL_introduction) | MySQL fundamentals: database/table lifecycle, `SELECT`/`INSERT`/`UPDATE`/`DELETE`, aggregation, correct `NULL` handling. |
| [SQL_more_queries](./SQL_more_queries) | User/privilege management (least-privilege `GRANT`s), multi-table schema design with `FOREIGN KEY` constraints, joins, and subqueries. |
| [python-object_relational_mapping](./python-object_relational_mapping) | Raw `MySQLdb` queries (including a deliberately unsafe vs. parameterized comparison) evolving into a full SQLAlchemy ORM layer. |
| [python-server_side_rendering](./python-server_side_rendering) | A Flask + Jinja2 app rendering the same template from four different data sources: static list, JSON, CSV, and SQLite. |
| [restful-api](./restful-api) | API development from the wire up: consuming an API with `requests`, a raw `http.server`, a Flask rewrite, then HTTP Basic Auth + JWT with role-based access control. |

## Technology Coverage

- **Languages:** Python 3, SQL (MySQL), JavaScript (Node.js and browser)
- **Python standard library:** `abc`, `json`, `pickle`, `csv`, `xml.etree.ElementTree`, `unittest`, `doctest`, `http.server`, `sys`
- **Frameworks/libraries:** Flask, Jinja2, SQLAlchemy, `requests`, `flask_httpauth`, `flask_jwt_extended`, Werkzeug (password hashing)
- **Databases:** MySQL, SQLite

## How to use this repository

Each directory is self-contained and independently runnable — none of them depend on each other. Start with a project's own README for exact run instructions (they differ: `.sql` files run through the `mysql` client, Python tasks generally pair with an `N-main.py` driver, Flask apps are run with `python3 task_XX.py` and then hit with `curl`). The root-level grouping above is meant to be read top to bottom as a skill progression, but each project can also be reviewed in isolation.

## About this repository

This work was completed as part of the Holberton School / ALX Higher-Level Programming curriculum and is maintained here as a personal portfolio. The curriculum defines the task scope; the implementations, design choices, and this documentation are original.
