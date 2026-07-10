# JavaScript - Warm Up

## Overview

This project is an introduction to core JavaScript syntax and Node.js scripting fundamentals: variables, command-line arguments, conditionals, loops, functions, recursion, objects, and Node's CommonJS module system (`require`/`module.exports`). Each file is a standalone script executed directly via Node's shebang (`#!/usr/bin/node`), which is the typical entry point for JavaScript before introducing a browser runtime or a framework.

## What's Inside

| File | Description |
|---|---|
| `0-javascript_is_amazing.js` | Declares a `const` string and logs it with `console.log`. |
| `1-multi_languages.js` | Declares three string constants and logs each on its own line. |
| `2-arguments.js` | Reads `process.argv` and prints "No argument", "Argument found", or "Arguments found" depending on how many CLI arguments were passed. |
| `3-value_argument.js` | Prints the first CLI argument, or "No argument" if `process.argv[2]` is `undefined`. |
| `4-concat.js` | Reads two CLI arguments and prints them interpolated into a template literal (`"${arg1} is ${arg2}"`). |
| `5-to_integer.js` | Parses a CLI argument with `parseInt`, printing "Not a number" if `isNaN` or the argument is falsy, otherwise the parsed integer. |
| `6-multi_languages_loop.js` | Iterates an array of language strings with a `while` loop and logs each one. |
| `7-multi_c.js` | Prints `"C is fun"` a number of times equal to a CLI-supplied count, using a `for` loop; prints "Missing number of occurrences" if the argument isn't numeric. |
| `8-square.js` | Prints an `n x n` square made of `'X'` characters by repeating `'X'.repeat(arg)` across `arg` lines. |
| `9-add.js` | Parses two CLI arguments as integers and prints their sum, or `NaN` if either is invalid. |
| `10-factorial.js` | Computes a factorial recursively; returns `1` for `n === 0`, `n === 1`, or a non-numeric input. |
| `11-second_biggest.js` | Converts all CLI arguments to numbers, sorts them descending, and prints the second-highest distinct value (or `0` if fewer than two arguments are given). |
| `12-object.js` | Creates an object literal, logs it, mutates a property, and logs it again to show objects are mutable references. |
| `13-add.js` | Exports an `add(a, b)` function via `module.exports`, demonstrating the CommonJS module pattern. |
| `13-main.js` | Imports `add` from `13-add.js` with `require` and calls it, acting as a small test harness. |

## Technical Notes

- **`process.argv` indexing**: every script that reads CLI input treats `process.argv[0]` (the `node` binary) and `process.argv[1]` (the script path) as fixed, so real arguments start at index `2`. `2-arguments.js` derives the argument count with `process.argv.length - 2` rather than checking `process.argv.length` directly.
- **Input validation with `isNaN`**: `5-to_integer.js`, `7-multi_c.js`, and `9-add.js` all guard against non-numeric input using `isNaN()` before doing arithmetic, since `parseInt`/arithmetic on a non-numeric string silently produces `NaN` rather than throwing.
- **Recursion**: `10-factorial.js` implements factorial as a recursive function with two base cases (`n === 0` and `n === 1`), each recursive call multiplying `n` by `factorial(n - 1)`.
- **Array methods**: `11-second_biggest.js` chains `process.argv.slice(2)` (drop the first two argv entries), `.map(Number)` (coerce strings to numbers), and `.sort((a, b) => b - a)` (descending numeric sort) — a pattern that avoids the classic bug of default `.sort()` doing lexicographic (string) comparison on numbers.
- **CommonJS modules**: `13-add.js` and `13-main.js` demonstrate the `module.exports = { add }` / `require('./13-add').add` pattern, which is Node's default module system and predates ES module `import`/`export` syntax.
- **Objects are reference types**: `12-object.js` shows that reassigning a property on an object (`myObject.value = 89`) mutates the same underlying object referenced by `myObject`, rather than creating a new one — a foundational distinction from primitive value semantics.

## Why This Approach

These scripts intentionally avoid any framework, build step, or third-party dependency: everything runs on plain Node.js using only built-in globals (`process`, `console`) and core language features. The goal at this stage is to internalize how JavaScript actually behaves — type coercion, argument parsing, recursion, mutable vs. primitive values, and the CommonJS module contract — before layering libraries or frameworks on top of it. Debugging a framework's behavior is much easier once you're not simultaneously unsure whether an issue is coming from the language itself or from the abstraction wrapping it.

## Usage

Each numbered script is directly executable via Node, either through its shebang or by invoking `node` explicitly:

```bash
# Direct execution (requires the file to be executable, e.g. chmod +x)
./0-javascript_is_amazing.js

# Or explicitly via node
node 2-arguments.js one two
node 9-add.js 3 5
node 11-second_biggest.js 3 5 1 4 5

# Module example: 13-main.js requires 13-add.js, so run the entry point
node 13-main.js
```

Scripts that read CLI arguments (`2-arguments.js` through `11-second_biggest.js`) require passing values after the script name, as shown above; running them with no arguments exercises their "missing/invalid input" branches.
