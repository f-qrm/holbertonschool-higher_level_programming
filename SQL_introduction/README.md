# SQL - Introduction

## Overview

This project is a hands-on introduction to relational databases using MySQL. It covers the fundamental lifecycle of working with a database from the command line: creating and dropping databases, defining tables, and running the core SQL statements (`SELECT`, `INSERT`, `UPDATE`, `DELETE`) needed to manipulate data. Each script is a small, self-contained `.sql` file that solves one specific task, mirroring how SQL is typically exercised and tested in isolation before being embedded in application code.

## What's Inside

| File | Description |
|---|---|
| `0-list_databases.sql` | Lists all databases on the MySQL server (`SHOW DATABASES`). |
| `1-create_database_if_missing.sql` | Creates database `hbtn_0c_0` only if it does not already exist. |
| `2-remove_database.sql` | Drops database `hbtn_0c_0` if it exists. |
| `3-list_tables.sql` | Lists all tables in the currently selected database. |
| `4-first_table.sql` | Creates `first_table(id INT, name VARCHAR(256))` if it doesn't already exist. |
| `5-full_table.sql` | Prints the full `CREATE TABLE` statement for `first_table` via `SHOW CREATE TABLE`. |
| `6-list_values.sql` | Selects every row from `first_table`. |
| `7-insert_value.sql` | Inserts a row `(89, 'Best School')` into `first_table`. |
| `8-count_89.sql` | Counts rows in `first_table` where `id = 89`. |
| `9-full_creation.sql` | Creates `second_table(id, name, score)` and bulk-inserts four rows in a single `INSERT`. |
| `10-top_score.sql` | Lists `score, name` from `second_table` sorted by score descending, then name. |
| `11-best_score.sql` | Same as above but filtered to rows with `score >= 10`. |
| `12-no_cheating.sql` | Updates Bob's score to 10 in `second_table`. |
| `13-change_class.sql` | Deletes all rows in `second_table` with `score <= 5`. |
| `14-average.sql` | Computes the average score across all rows using `AVG()`. |
| `15-groups.sql` | Groups rows by `score` and counts how many records share each score, sorted by frequency. |
| `16-no_link.sql` | Selects `score, name` excluding rows where `name` is `NULL` or an empty string. |

## Technical Notes

Every script targets the `hbtn_0c_0` database and uses standard MySQL DDL/DML syntax. A few points worth calling out:

- **Idempotent DDL**: `CREATE DATABASE IF NOT EXISTS` and `CREATE TABLE IF NOT EXISTS` are used throughout so scripts can be re-run safely without erroring on duplicate objects.
- **Multi-row insert**: `9-full_creation.sql` inserts four rows with a single `INSERT INTO ... VALUES (...), (...), (...), (...)` statement instead of four separate statements, which is both more concise and more efficient (one round trip, one transaction).
- **Aggregation**: `14-average.sql` and `15-groups.sql` use `AVG()` and `GROUP BY` respectively, with `15-groups.sql` further demonstrating column aliasing (`AS number`) combined with `ORDER BY` on the aggregated result.
- **Filtering on NULL vs empty string**: `16-no_link.sql` explicitly checks `NAME IS NOT NULL AND NAME != ''`, which is a common gotcha in SQL since `NULL` and `''` are distinct values that `=`/`!=` comparisons treat differently (a plain `!= ''` check would silently pass through `NULL` rows since any comparison against `NULL` evaluates to `NULL`, not `TRUE`).
- **Introspection**: `SHOW CREATE TABLE` is used instead of just describing a schema from memory, which is the standard way to verify exactly how MySQL stored a table definition (including implicit defaults and engine/charset info).

## Why This Approach

Writing raw SQL rather than reaching for an ORM at this stage is intentional: it forces direct engagement with how MySQL actually parses, executes, and optimizes statements, and it builds the vocabulary (DDL vs DML, aggregate functions, `GROUP BY` semantics, `NULL` handling) that every ORM eventually compiles down to. Understanding this layer first makes it much easier to reason about what an ORM-generated query is actually doing, and to debug it when the abstraction leaks.

Each task is deliberately scoped to one operation per file, which keeps the scripts easy to test independently against a live MySQL instance and easy to grade/verify by diffing expected output.

## Usage

These scripts are meant to be run against a MySQL server via the `mysql` client. For example:

```bash
# Run a script that doesn't require selecting a database first
mysql -hlocalhost -uroot -p < 0-list_databases.sql

# Run a script against a specific database
mysql -hlocalhost -uroot -p hbtn_0c_0 < 7-insert_value.sql
```

Scripts that use `CREATE TABLE`/`SELECT`/`INSERT`/`UPDATE`/`DELETE` against `first_table` or `second_table` assume the `hbtn_0c_0` database has already been created (via `1-create_database_if_missing.sql`) and selected, either with `USE hbtn_0c_0;` or by passing the database name on the command line as shown above.
