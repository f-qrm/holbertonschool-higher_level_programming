# SQL - More Queries

## Overview

This project builds on basic SQL by introducing user and privilege management, table-level constraints, and multi-table queries (subqueries and joins) across two schemas: `hbtn_0d_usa` (states/cities) and `hbtn_0d_tvshows` (TV shows and genres). It moves from "how do I read and write rows" to "how do I model relationships between tables and control who can access them," which are the two skills that separate toy database usage from real schema design.

## What's Inside

| File | Description |
|---|---|
| `0-privileges.sql` | Displays the grants for MySQL users `user_0d_1` and `user_0d_2` via `SHOW GRANTS`. |
| `1-create_user.sql` | Creates `user_0d_1@localhost` with a password and grants it `ALL PRIVILEGES` on every database (`*.*`), then reloads the grant tables. |
| `2-create_read_user.sql` | Creates database `hbtn_0d_2` and user `user_0d_2@localhost`, granting only `SELECT` on that database (read-only access). |
| `3-force_name.sql` | Creates `force_name(id INT, name VARCHAR(256) NOT NULL)`, enforcing that `name` can never be null. |
| `4-never_empty.sql` | Creates `id_not_null(id INT DEFAULT 1, name VARCHAR(256))`, giving `id` a default value instead of a `NOT NULL` constraint. |
| `5-unique_id.sql` | Creates `unique_id(id INT DEFAULT 1 UNIQUE, name VARCHAR(256))`, combining a default value with a uniqueness constraint. |
| `6-states.sql` | Creates database `hbtn_0d_usa` and table `states(id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(256) NOT NULL)`. |
| `7-cities.sql` | Creates table `cities` with a `FOREIGN KEY (state_id) REFERENCES states(id)`, establishing a one-to-many relationship. |
| `8-cities_of_california_subquery.sql` | Lists cities in California using a correlated **subquery** against `states` to resolve the state id. |
| `9-cities_by_state_join.sql` | Same intent as above but implemented with an explicit `JOIN` between `cities` and `states`, returning both city and state names. |
| `10-genre_id_by_show.sql` | Joins `tv_shows` and `tv_show_genres` to list each show's title alongside its genre ids. |
| `11-genre_id_all_shows.sql` | Same as above but uses a `LEFT JOIN` so shows with no linked genre still appear (with `NULL` genre_id). |
| `12-no_genre.sql` | Uses a `LEFT JOIN` plus `WHERE genre_id IS NULL` to isolate shows that have no genre linked at all. |
| `13-count_shows_by_genre.sql` | Joins `tv_genres` to `tv_show_genres`, groups by genre, and counts shows per genre using `HAVING` to exclude empty genres. |
| `14-my_genres.sql` | Three-way join across `tv_shows`, `tv_show_genres`, and `tv_genres` to list all genres for the show "Dexter". |
| `15-comedy_only.sql` | Same three-way join pattern, filtered to `tv_genres.name = 'Comedy'` to list all Comedy shows. |
| `16-shows_by_genre.sql` | Lists every show with every linked genre using `LEFT JOIN` twice, so shows without genres still appear with a `NULL` genre name. |

## Technical Notes

- **Privilege model**: `1-create_user.sql` and `2-create_read_user.sql` demonstrate MySQL's `GRANT` syntax at two different scopes — global (`ON *.*`) for a superuser-like account, and database-scoped (`ON hbtn_0d_2.*`) with a single privilege (`SELECT`) for a read-only account. This models the principle of least privilege at the database layer rather than leaving everything on a single admin credential.
- **Constraints as schema documentation**: `3-force_name.sql`, `4-never_empty.sql`, and `5-unique_id.sql` progressively combine `NOT NULL`, `DEFAULT`, and `UNIQUE` constraints, showing how invariants (a name that must exist, an id that always has a fallback value, an id that can never collide) are enforced by the database engine itself rather than relying on application code to validate them.
- **Referential integrity**: `7-cities.sql` declares an explicit `FOREIGN KEY (state_id) REFERENCES states(id)`, which requires `states` to exist first and prevents inserting a city with a `state_id` that doesn't correspond to a real state.
- **Subquery vs. join for the same result**: `8-cities_of_california_subquery.sql` and `9-cities_by_state_join.sql` solve the identical problem two different ways — a scalar subquery in the `WHERE` clause versus an explicit `JOIN` — which is a deliberate comparison of two query strategies that a query planner may optimize differently at scale.
- **INNER vs. LEFT JOIN semantics**: Files 10–12 and 16 make the distinction between `JOIN` (rows must match on both sides) and `LEFT JOIN` (all rows from the left table are kept, with `NULL` filling in unmatched right-side columns) explicit and testable — `12-no_genre.sql` in particular uses `LEFT JOIN ... WHERE right_col IS NULL` as the standard SQL idiom for "find rows with no match," a pattern that has no direct subquery equivalent as clean as this join form.
- **Aggregation with HAVING**: `13-count_shows_by_genre.sql` groups by genre and uses `HAVING number_of_shows > 0` (a filter applied after aggregation) rather than `WHERE` (which filters before aggregation and cannot reference an aggregate alias).

## Why This Approach

Modeling `states`/`cities` and `tv_shows`/`tv_show_genres` with explicit foreign keys and join queries, instead of denormalizing everything into flat tables, demonstrates an understanding of normalization: each fact is stored once, and relationships are reconstructed at query time. This is the same reasoning that underlies relational schema design in production systems, where getting joins, indexes, and constraints right up front avoids data-integrity bugs that are expensive to fix later.

Handling user privileges directly with `CREATE USER`/`GRANT` rather than assuming a single shared credential also reflects a production concern: database accounts should be scoped to what a given service or role actually needs, which is a habit worth building before it becomes a compliance requirement.

## Usage

Run each script against a running MySQL server with the `mysql` client:

```bash
# Privilege / user management scripts (run as an account with sufficient rights)
mysql -hlocalhost -uroot -p < 1-create_user.sql
mysql -hlocalhost -uroot -p < 2-create_read_user.sql

# Schema setup for the USA states/cities database
mysql -hlocalhost -uroot -p < 6-states.sql
mysql -hlocalhost -uroot -p < 7-cities.sql

# Queries against hbtn_0d_usa
mysql -hlocalhost -uroot -p hbtn_0d_usa < 9-cities_by_state_join.sql

# Queries against hbtn_0d_tvshows (assumes this database and its tables
# already exist and are populated, e.g. from a provided dump)
mysql -hlocalhost -uroot -p hbtn_0d_tvshows < 13-count_shows_by_genre.sql
```

The TV shows scripts (`10-*` through `16-*`) assume the `hbtn_0d_tvshows` database, with tables `tv_shows`, `tv_genres`, and the join table `tv_show_genres`, already exists and is populated — these scripts only query, they do not create that schema.
