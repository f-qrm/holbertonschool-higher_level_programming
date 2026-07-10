# RESTful API

## Overview

This project builds up API skills in four stages: consuming a third-party REST API as a client, implementing an HTTP server from scratch on top of the `http.server` standard-library module, rebuilding the same endpoints declaratively with Flask, and finally securing a Flask API with both HTTP Basic Authentication and JWT-based authentication with role checks. It targets the web-API skill area of backend development, from the wire protocol up to production-style auth.

## What's Inside

| File | Description |
|---|---|
| `task_02_requests.py` | Client-side use of the `requests` library against `https://jsonplaceholder.typicode.com/posts`. `fetch_and_print_posts()` GETs the list, checks `status_code == 200`, and prints every post's `title`. `fetch_and_save_posts()` GETs the same list and writes `id`, `title`, `body` to `posts.csv` via `csv.DictWriter`. |
| `main_02_requests.py` | Driver script that imports and calls both functions from `task_02_requests.py`. |
| `task_03_http_server.py` | A server built directly on `http.server.BaseHTTPRequestHandler` and `socketserver.TCPServer`, listening on port 8000. `do_GET()` manually inspects `self.path` and branches with `if`/`elif` on `/`, `/data`, `/status`, `/info`; anything else gets a 404. Responses are written by hand: `send_response(code)`, `send_header('Content-Type', ...)`, `end_headers()`, then `self.wfile.write(...)` with UTF-8-encoded bytes. |
| `task_04_flask.py` | The same style of API rebuilt with Flask. Routes are declared with `@app.route(path, methods=[...])` instead of manual path matching, JSON responses use `jsonify()`, and the in-memory `users` dict backs `GET /data`, `GET /status`, `GET /users/<username>` (404 if missing), and `POST /add_user` (201 on success, 400 if `username` is missing from the JSON body). |
| `task_05_basic_security.py` | Adds authentication on top of the Flask pattern: HTTP Basic Auth via `flask_httpauth.HTTPBasicAuth` with `werkzeug.security` password hashing, and JWT issuance/verification via `flask_jwt_extended`, including a role check and custom error handlers for every JWT failure mode. |

## Technical Notes

**Raw HTTP server (`task_03_http_server.py`).** There is no framework routing here: `socketserver.TCPServer(('', 8000), Server)` opens a listening socket and, for each connection, `BaseHTTPRequestHandler` parses the raw HTTP request line and headers itself; `do_GET()` is the hook the standard library calls once a `GET` request has been parsed. Routing is a manual `if self.path == '/': ... elif self.path == '/data': ...` chain, and every response is assembled at the socket level: an explicit status line (`send_response(200)` / `send_response(404)`), an explicit `Content-Type` header, `end_headers()` to terminate the header block, and a `wfile.write()` of the encoded body — there is no automatic content negotiation, no request parsing helpers, and no method dispatch beyond what `do_GET` implements by hand. This is the layer Flask (and every WSGI framework) sits on top of and hides.

**Flask API (`task_04_flask.py`).** Routing is declarative: `@app.route('/users/<username>')` captures a URL segment as a function argument, and `methods=['POST']` restricts a route to one HTTP verb — Flask parses the request, matches it against the registered rule table, and calls the matching view function, none of which is visible to the developer the way it is in the `http.server` version. `jsonify()` handles content-type and serialization for JSON responses. `POST /add_user` reads the body with `request.get_json()`, returns `201` with `{"message": "User added", "user": ...}` on success or `400` with `{"error": "Username is required"}` if the `username` key is absent; `GET /users/<username>` returns `404` with `{"error": "User not found"}` for unknown users. State is a plain in-memory `dict`, so it resets on every restart.

**Auth (`task_05_basic_security.py`).** Two independent auth mechanisms are wired into the same app:
- *HTTP Basic Auth*: `users` stores each account's password as `generate_password_hash(...)` (Werkzeug's salted hash), never in plaintext. `@auth.verify_password` is registered with `HTTPBasicAuth()` and is called by Flask-HTTPAuth on every request to a route decorated with `@auth.login_required` (here, `GET /basic-protected`); it looks up the username, runs `check_password_hash(stored_hash, provided_password)`, and returns the user record (truthy) or `None`. A missing/failed check causes Flask-HTTPAuth to short-circuit the request before the view function runs.
- *JWT Auth*: `POST /login` validates the username/password with the same `check_password_hash` mechanism, then calls `create_access_token(identity={"username": ..., "role": ...})`, embedding both fields as the token's identity claim, and returns it as JSON. `GET /jwt-protected` is guarded by `@jwt_required()`, which requires a valid, non-expired bearer token in the `Authorization` header. `GET /admin-only` additionally calls `get_jwt_identity()` after the `@jwt_required()` check and returns `403 {"error": "Admin access required"}` if `role != "admin"` — an application-level authorization check layered on top of authentication. `app.config['JWT_SECRET_KEY']` is set explicitly (token expiry uses `flask_jwt_extended`'s library default since it is not overridden). Six `@jwt.*_loader` handlers (`unauthorized_loader`, `invalid_token_loader`, `expired_token_loader`, `revoked_token_loader`, `needs_fresh_token_loader`, plus the identity/role check above) replace Flask-JWT-Extended's default error bodies with a consistent `{"error": "..."}` / `401` JSON shape for every failure mode — missing token, malformed token, expired token, revoked token, and missing freshness.

## Why This Approach

Writing the same handful of endpoints against raw sockets, then against Flask, makes explicit what a web framework is actually doing: parsing the request line, matching a route, dispatching to a handler, and serializing a response — all things that matter when a model-serving endpoint is slow or misbehaving and the abstraction needs to be looked through rather than trusted blindly. The security stage is the most directly production-relevant piece: any ML inference endpoint exposed over HTTP needs the same two building blocks used here — hashed credential storage plus token-based auth with role checks — to keep it from being an open door, and the explicit JWT error handlers show the kind of failure-mode coverage (expired/invalid/revoked/missing token) that a real deployment needs rather than a generic 401.

## Usage

Requires `requests` for the client script, and `Flask`, `flask_httpauth`, `flask_jwt_extended`, and `Werkzeug` (installed alongside Flask) for the server scripts.

```bash
# Client: consume a public REST API
python3 main_02_requests.py

# Raw HTTP server (port 8000)
python3 task_03_http_server.py
curl http://127.0.0.1:8000/data
curl http://127.0.0.1:8000/status
curl http://127.0.0.1:8000/unknown   # -> 404

# Flask API (port 5000)
python3 task_04_flask.py
curl -X POST -H "Content-Type: application/json" \
  -d '{"username": "fjolla", "age": 25}' http://127.0.0.1:5000/add_user
curl http://127.0.0.1:5000/users/fjolla

# Secured Flask API (default Flask port 5000)
python3 task_05_basic_security.py
curl -u user1:password http://127.0.0.1:5000/basic-protected

curl -X POST -H "Content-Type: application/json" \
  -d '{"username": "user1", "password": "password"}' \
  http://127.0.0.1:5000/login
# -> {"access_token": "<jwt>"}

curl -H "Authorization: Bearer <jwt>" http://127.0.0.1:5000/jwt-protected
curl -H "Authorization: Bearer <jwt>" http://127.0.0.1:5000/admin-only
```
