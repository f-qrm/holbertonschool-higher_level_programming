# Python - Object Relational Mapping

## Overview

This project is a progressive study of how Python code talks to a relational database: it starts with raw `MySQLdb` cursors and hand-built SQL strings, moves through parameterized queries, and ends with a full SQLAlchemy ORM layer (declarative models, sessions, filtered queries, inserts, updates, deletes, and a join across two mapped classes). It targets the database-access skill area of backend development — specifically the difference between talking to a database and modeling one.

## What's Inside

| File | Description |
|---|---|
| `0-select_states.py` / `.sql` | Connects with `MySQLdb`, runs `SELECT * FROM states ORDER BY id ASC`, prints every row. The `.sql` file creates `hbtn_0e_0_usa` and seeds the `states` table. |
| `1-filter_states.py` | Lists states whose name starts with `N`, using `BINARY name LIKE 'N%'` for a case-sensitive match. |
| `2-my_filter_states.py` | Takes a state-name prefix as a CLI argument and builds the `LIKE` clause with `str.format()` — the query string is assembled from raw user input. |
| `3-my_safe_filter_states.py` | Same lookup as script 2, but the value is passed through a `%s` placeholder and a parameter tuple to `cur.execute()` instead of being interpolated into the string. |
| `4-cities_by_state.py` / `.sql` | Joins `cities` to `states` on `state_id` in a single `execute()` call and prints `(city_id, city_name, state_name)` tuples. The `.sql` file adds the `cities` table (with a `FOREIGN KEY(state_id) REFERENCES states(id)`) and seed data. |
| `5-filter_cities.py` | Joins cities to states, filters by state name using a `%s` placeholder, and prints the matching city names as a comma-separated list. |
| `6-model_state.py` / `.sql` | First SQLAlchemy script: imports `Base`/`State` from `model_state.py` and calls `Base.metadata.create_all(engine)` to create the table from the ORM model instead of a SQL file. |
| `7-model_state_fetch_all.py` | `session.query(State).order_by(State.id).all()` — fetches every state as `State` objects. |
| `8-model_state_fetch_first.py` | Same query with `.first()`, printing `"Nothing"` when no row exists. |
| `9-model_state_filter_a.py` | `session.query(State).filter(State.name.like("%a%")).order_by(State.id).all()` — ORM-level `LIKE` filtering. |
| `10-model_state_my_get.py` | `filter(State.name == sys.argv[4]).first()` — exact-match lookup by name, prints the ID or `"Not found"`. |
| `11-model_state_insert.py` | Creates `State(name="Louisiana")`, `session.add()` + `session.commit()`, then prints the auto-generated primary key. |
| `12-model_state_update_id_2.py` | Fetches the state with `id=2` via `filter_by(id=2).first()`, mutates the `name` attribute in place, and commits — no `UPDATE` SQL is written by hand. |
| `13-model_state_delete_a.py` | Filters states whose name contains `a` and calls `session.delete()` on each before committing. |
| `14-model_city_fetch_by_state.py` / `.sql` | `session.query(City, State).join(State, City.state_id == State.id).order_by(City.id).all()` — an explicit ORM join across two mapped classes, printed as `<state>: (<city id>) <city name>`. |
| `model_state.py` | Declares `Base = declarative_base()` and the `State` model (`id`, `name`) mapped to the `states` table. |
| `model_city.py` | Declares the `City` model (`id`, `name`, `state_id`) mapped to the `cities` table. |

## Technical Notes

**Raw SQL stage (scripts 0-5).** All of these use `MySQLdb.connect()` directly and hand-written SQL. Script 2 is the deliberately unsafe version: `"...LIKE '{}%'".format(searched_name)` builds the query by string substitution, so a crafted value could change the query's meaning — a classic SQL injection surface. Script 3 fixes exactly this by passing `"WHERE name = %s"` together with `(searched_name,)` to `cur.execute()`; the driver binds the value out-of-band from the query text, so user input can never be interpreted as SQL syntax. Scripts 4 and 5 apply the same join logic, with script 5 also using the safe `%s` placeholder pattern for the state-name filter.

**ORM stage (scripts 6-14).** `model_state.py` and `model_city.py` each call `sqlalchemy.ext.declarative.declarative_base()` and define a class with `__tablename__` plus `Column(...)` attributes (`Integer`, `String(128)`, `primary_key=True`, `nullable=False`, `autoincrement=True`). Every script from 7 onward follows the same pattern: build an `Engine` with `create_engine('mysql+mysqldb://user:pass@localhost/db', pool_pre_ping=True)`, call `Base.metadata.create_all(engine)` to ensure the schema exists, open a `Session` via `sessionmaker(bind=engine)`, then express the query as `session.query(Model)` chained with `.filter()`, `.filter_by()`, `.order_by()`, `.first()` or `.all()`. Writes go through the same session object: `session.add()` for inserts, direct attribute mutation followed by `session.commit()` for updates, and `session.delete()` for deletes — no `INSERT`/`UPDATE`/`DELETE` strings appear anywhere in this half of the project. Script 14 demonstrates a multi-model join expressed in Python (`session.query(City, State).join(State, City.state_id == State.id)`) rather than as a SQL `JOIN` clause.

One implementation detail worth noting for a reader going file to file: `model_city.py` imports `Base` from `model_state` but then reassigns `Base = declarative_base()` in its own module scope, so `City` is registered against its own metadata rather than the one `State` uses, and `state_id` is declared as `Column(Integer, foreign_key=True, nullable=False)` rather than using `sqlalchemy.ForeignKey("states.id")`. The join in script 14 still works because it is expressed explicitly (`City.state_id == State.id`), but there is no ORM-level foreign-key constraint or `relationship()` attribute wiring the two models together.

## Why This Approach

Building the same lookup three ways — raw string interpolation, parameterized raw SQL, then a full ORM — makes the SQL-injection risk and its fix tangible instead of abstract, which matters anywhere user input reaches a query, including feature-store lookups, labeling tools, or admin panels backed by a relational database. The ORM stage is directly transferable to ML-adjacent backend work: SQLAlchemy declarative models and session-based querying are how many training-data pipelines, experiment trackers, and metadata stores read and write structured data, and knowing what the ORM generates under the hood (rather than treating `session.query()` as magic) matters when a pipeline needs to be debugged or optimized against a slow query.

## Usage

Requires a running MySQL server on `localhost:3306`, the `mysqlclient` package (`pip install mysqlclient`) for the `MySQLdb`-based scripts, and `SQLAlchemy` (`pip install SQLAlchemy`) for scripts 6-14.

```bash
# Set up a database from one of the provided .sql files
mysql -u root -p < 0-select_states.sql

# Raw MySQLdb scripts
./0-select_states.py root root hbtn_0e_0_usa
./3-my_safe_filter_states.py root root hbtn_0e_0_usa California

# SQLAlchemy ORM scripts (creates tables via Base.metadata.create_all if missing)
./7-model_state_fetch_all.py root root hbtn_0e_6_usa
./11-model_state_insert.py root root hbtn_0e_6_usa
./14-model_city_fetch_by_state.py root root hbtn_0e_14_usa
```
