# Algorithms & Data Structures in Python 🐍

## Info 🔎

Includes the following all in pure python 🐍:

- Common Data Structures 🧬
- Common Algorithms 🪜
- Problems with Tests 🧩

(This is an example project for my students)

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
$ poetry install
# Installing dependencies from lock file
```

### Update Packages

```bash
$ poetry update
# Updating dependencies
```

### REPL (IPython)

```bash
$ ipython
# In [1]:
```

### Code formatting

```bash
$ ruff format
# 20 files left unchanged
```

### Code Linting

```bash
$ ruff check
# All checks passed!
```

### Testing

```bash
$ pytest
# --> runs tests using pytest
```
