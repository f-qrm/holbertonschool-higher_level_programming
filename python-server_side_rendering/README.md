# Python - Server-Side Rendering

## Overview

This project builds a small Flask application incrementally, moving from raw string templating to a Jinja2/Flask app that reads its data from a static list, then a JSON file, then a CSV file, and finally a SQLite database. It targets the server-side rendering skill area — how a backend turns structured data into HTML on the server before it ever reaches the browser.

## What's Inside

| File | Description |
|---|---|
| `task_00_intro.py` | Not Flask/Jinja2 — `generate_invitations(template, attendees)` does manual `str.replace()` substitution of `{name}`, `{event_title}`, `{event_date}`, `{event_location}` placeholders in a template string, validates its inputs (type checks on `template`/`attendees`, per-item dict checks, empty-template/empty-list checks logged via the `logging` module), and writes one `output_<n>.txt` file per attendee. It establishes the "why templating engines exist" baseline before Jinja2 is introduced. |
| `task_01_jinja.py` | First Flask app. Three routes (`/`, `/about`, `/contact`) each call `render_template()` on a static `.html` file — no dynamic data passed in yet. |
| `task_02_logic.py` | Adds `/items`, which opens `items.json`, extracts the `items` list, and passes it into `items.html` so the template can loop over it. |
| `task_03_files.py` | Adds `/products`, which reads a `source` query parameter (`json` or `csv`) and an optional `id` parameter. Loads `products.json` via `json.load()` or `products.csv` via `csv.DictReader()`, optionally filters down to a single product by id, and renders `product_display.html` with either a `products` list or an `error` message. |
| `task_04_db.py` | Extends `/products` with a third source, `sql`, which opens `products.db` with `sqlite3.connect()`, sets `row_factory = sqlite3.Row`, runs `SELECT * FROM Products`, and converts each row to a `dict` — so the same template now renders data coming from a list literal, a JSON file, a CSV file, or a database row set, all normalized to the same `dict`-like shape. |
| `create_db.py` | Standalone script (not a Flask route) that creates `products.db` via `sqlite3`, defines a `Products` table (`id`, `name`, `category`, `price`), and inserts two seed rows (Laptop, Coffee Mug). Must be run once before exercising the `sql` source in `task_04_db.py`. |
| `items.json` | Static data source for `/items`: `{"items": ["Python Book", "Flask Mug", "Jinja Sticker"]}`. |
| `products.json` | Static data source for `/products?source=json`: a list of product dicts (`id`, `name`, `category`, `price`). |
| `products.csv` | Static data source for `/products?source=csv`: same product fields as `products.json`, in CSV form, read with `csv.DictReader`. |
| `templates/header.html` | Shared nav bar (`Home`/`About`/`Contact` links), pulled into every page via `{% include %}`. |
| `templates/footer.html` | Shared copyright footer, also pulled in via `{% include %}`. |
| `templates/index.html`, `about.html`, `contact.html` | Static pages, each wrapping `{% include 'header.html' %}` / `{% include 'footer.html' %}` around page-specific content. |
| `templates/items.html` | Uses `{% if items %} ... {% for item in items %}<li>{{ item }}</li>{% endfor %} ... {% else %}` to render the list or a "No items found" fallback. |
| `templates/product_display.html` | Uses `{% if error %}` to show an error message, then `{% for product in products %}` to build one table row per product with `{{ product['name'] }}`, `{{ product['category'] }}`, `{{ product['price'] }}`. |

## Technical Notes

**Template mechanics.** Every page template (`index.html`, `about.html`, `contact.html`, `items.html`, `product_display.html`) uses Jinja2's `{% include 'header.html' %}` / `{% include 'footer.html' %}` directives to pull in shared markup fragments — composition by inclusion rather than `{% extends %}`/block-based inheritance. Dynamic output uses `{{ }}` expression interpolation (e.g. `{{ product['name'] }}`) for values passed from the Flask view function, and control flow uses `{% for %}` / `{% if %}` / `{% else %}` / `{% endif %}` / `{% endfor %}` tags — for example `items.html` branches on whether the `items` list passed to `render_template()` is empty, and `product_display.html` iterates over a `products` list to build table rows and separately checks for an `error` string to render a message instead.

**Routing and data source per task.** Each task adds routes on top of the same three static pages. `task_01_jinja.py` calls `render_template('index.html')` with no context — the template renders pure static HTML. `task_02_logic.py`'s `/items` route reads `items.json` with the standard library `json` module and passes the resulting list as a template variable (`items=items_list`), so the same `items.html` template can render zero, one, or many items without code changes. `task_03_files.py`'s `/products` route branches on the `source` query string: `json.load()` for `source=json`, `csv.DictReader()` (converted to a `list`) for `source=csv`; an unrecognized or missing source renders `product_display.html` with `error="Wrong source"`, and a valid `id` that matches nothing renders it with `error='Product not found'`. `task_04_db.py` adds a third branch, `source=sql`, which queries `products.db` (created by `create_db.py`) through `sqlite3`, using `row_factory = sqlite3.Row` so each row can be converted with `dict(row)` — the same shape the JSON and CSV branches already produce, which is why `product_display.html` needs no changes to support the database-backed source.

## Why This Approach

Rendering the same table from a static file, a JSON file, a CSV file, and a SQLite database against one unchanged template demonstrates the core value of server-side rendering: the view layer is decoupled from where the data actually lives. That separation is the same one that matters when serving an ML model's predictions through a dashboard or internal tool — the page that displays inference results shouldn't need to change when the underlying store moves from a flat file to a database or a feature store. Starting with `task_00_intro.py`'s manual string-replacement templating, before introducing Jinja2, also makes explicit what a templating engine actually automates (looping, conditionals, escaping, fragment reuse) rather than treating `render_template()` as a black box.

## Usage

Requires `Flask` (`pip install Flask`); `task_04_db.py` additionally needs `products.db`, created once via `create_db.py`.

```bash
# One-time setup for the SQLite-backed task
python3 create_db.py

# Run any task's Flask dev server (port 5000)
python3 task_01_jinja.py
python3 task_02_logic.py
python3 task_03_files.py
python3 task_04_db.py
```

```bash
# Example requests once a server is running
curl http://127.0.0.1:5000/
curl http://127.0.0.1:5000/items
curl "http://127.0.0.1:5000/products?source=json"
curl "http://127.0.0.1:5000/products?source=csv&id=2"
curl "http://127.0.0.1:5000/products?source=sql"   # task_04_db.py only
```

```bash
# task_00_intro.py is a plain function, not a server
python3 -c "from task_00_intro import generate_invitations; \
generate_invitations(open('template.txt').read(), \
[{'name': 'John', 'event_title': 'Python Meetup', \
'event_date': '2024-07-01', 'event_location': 'New York'}])"
```
