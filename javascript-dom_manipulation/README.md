# JavaScript - DOM Manipulation

## Overview

This project covers browser-side JavaScript: selecting and modifying DOM elements, handling user events, and fetching data from external APIs to update a page dynamically. Each task is a pair of files — an `N-main.html` page and its matching `N-script.js` — so the DOM manipulation logic can be inspected independently of the markup it targets. It progresses from simple style changes to event-driven UI updates to asynchronous data fetching with the Fetch API.

## What's Inside

| Files | Description |
|---|---|
| `0-main.html` / `0-script.js` | Selects the `<header>` with `querySelector` and sets its text color directly via `style.color`. |
| `1-main.html` / `1-script.js` | Adds a `click` listener to a `#red_header` div that turns the header's text red when clicked. |
| `2-main.html` / `2-script.js` | Adds a `click` listener that applies a predefined `.red` CSS class to the header via `classList.add`, instead of setting inline styles. |
| `3-main.html` / `3-script.js` | Toggles the header between `.red` and `.green` classes on each click, checking current state with `classList.contains`. |
| `4-main.html` / `4-script.js` | Appends a new `<li>Item</li>` to a `<ul class="my_list">` each time an "Add item" div is clicked, using `document.createElement` and `appendChild`. |
| `5-main.html` / `5-script.js` | Replaces the header's text content with "New Header!!!" on click via `textContent`. |
| `6-main.html` / `6-script.js` | Fetches a single Star Wars character from the SWAPI REST API and displays the character's name in a `<div>`. |
| `7-main.html` / `7-script.js` | Fetches the list of Star Wars films from SWAPI and renders each title as an `<li>` in a `<ul>`. |
| `8-main.html` / `8-script.js` | Waits for `DOMContentLoaded`, then fetches a French greeting from the Hello Salut API and displays it in a `<div>`. |

## Technical Notes

- **Element selection**: every script uses `document.querySelector` with either a tag selector (`'header'`), an id selector (`'#some_id'`), or a class selector (`'.my_list'`), consistent with modern DOM APIs rather than the older `getElementById`/`getElementsByClassName` family.
- **Event handling**: tasks 1 through 5 attach behavior with `element.addEventListener('click', function () { ... })`, keeping event wiring separate from markup (no inline `onclick` attributes).
- **Inline styles vs. CSS classes**: task 0 mutates `style.color` directly, while tasks 2 and 3 instead toggle predefined `.red`/`.green` classes with `classList.add`/`classList.remove`/`classList.contains`. The latter is the more maintainable pattern since visual styling stays in CSS and JavaScript only manages state.
- **DOM node creation**: task 4 builds a new element with `document.createElement('li')`, sets its `textContent`, and inserts it with `appendChild`, the standard way to add content to the DOM programmatically rather than via `innerHTML` string concatenation (which avoids injection concerns for dynamic content).
- **Fetch API and Promises**: tasks 6, 7, and 8 use `fetch(url).then(response => response.json()).then(data => ...).catch(error => ...)`, the standard two-stage Promise chain for HTTP calls in the browser — first resolving the response, then parsing its JSON body, with a `.catch` for network/parsing failures.
- **Load-order handling**: task 8 places its `<script>` tag in `<head>` (before the DOM exists) and compensates by wrapping all DOM access in a `document.addEventListener('DOMContentLoaded', function () { ... })` callback, ensuring the `#hello` div exists before `querySelector` runs. Tasks 0–7 instead place their `<script>` tag at the end of `<body>`, so the DOM is already parsed by the time the script executes and no such guard is needed.
- **External APIs used**: `https://swapi-api.hbtn.io/api/people/5/?format=json` (a single character), `https://swapi-api.hbtn.io/api/films/?format=json` (a film list), and `https://hellosalut.stefanbohacek.dev/?lang=fr` (a greeting API) — all public, unauthenticated REST endpoints returning JSON.

## Why This Approach

These exercises use vanilla DOM APIs — `querySelector`, `addEventListener`, `classList`, `createElement`, `fetch` — instead of a framework like React or Vue. Frameworks like React are themselves built on top of these primitives (a virtual DOM diff eventually resolves to real `createElement`/`appendChild`/attribute calls), so understanding what happens at this layer makes it possible to reason about what a framework is actually doing under the hood, and to debug issues that leak through the abstraction (event delegation quirks, reflow/repaint costs, why a direct style mutation bypasses a framework's state).

Progressing from inline style mutation, to CSS class toggling, to asynchronous data fetching mirrors a realistic complexity curve: static presentation, then interactive state, then integrating a live remote API — the same building blocks used in any single-page application, just without a framework's abstractions in the way.

## Usage

These are static HTML/JS pairs with no build step or server required. Open the relevant `N-main.html` file directly in a browser (or serve the directory with a simple static server) and interact with the page:

```bash
# Open directly
open 0-main.html          # macOS
xdg-open 0-main.html      # Linux

# Or serve locally and browse to it
python3 -m http.server 8000
# then visit http://localhost:8000/6-main.html
```

Tasks 6, 7, and 8 require network access (they call live public APIs), so a local file may need to be served over `http://` rather than opened directly as a `file://` URL if the browser's fetch/CORS policy blocks local file requests — using the `python3 -m http.server` approach above avoids that issue.
