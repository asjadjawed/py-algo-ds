# Algorithms & Data Structures in Python 🐍

## Info 🔎

Well documented code with test cases. This started as a repo for my students to practice.

Just delete the code, re-write your solution and see if the tests pass. Enjoy 😊

Includes the following all in pure python 🐍:

- Common Data Structures 🧬
- Common Algorithms 🪜
- Problems to build your programming 💪

*You can IPython as a REPL (in dependencies).*

## Commands 🏃‍♂️

Please run the following to enable Git Hooks.

On commit this runs:

- testing
- linting
- formatting.

### Install Git Hooks

Please *Install Packages* before installing *Git Hooks*

```bash
$ ./install-hooks.sh
# pre-commit installed at .git/hooks/pre-commit
```

### Install Packages

```bash
$ uv sync
# Installing dependencies from lock file
```

### Update Packages

```bash
$ uv sync --upgrade
$ pre-commit autoupdate
# Updating dependencies
```

### Run pre-commit hooks

```bash
$ pre-commit run --all-files
# 20 files left unchanged
```

### Code formatting

```bash
$ uvx ruff format
# 20 files left unchanged
```

### Code Linting

```bash
$ uvx ruff check
# All checks passed!
```

### Testing

```bash
$ pytest
# --> runs tests using pytest
```
