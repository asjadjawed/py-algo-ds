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
$ autopep8 --in-place --recursive --verbose .
# [file:./tests/__init__.py]
# --->  Applying global fix for E265
# --->  0 issue(s) to fix {}
```

### Code Linting

```bash
$ pylint .
# --------------------------------------------------------------------
# Your code has been rated at 10.00/10 (previous run: 10.00/10, +0.00)
```

### Generate pylint Config

```bash
$ pylint --generate-rcfile > pylintrc
# --> File .pylintrc added with default config
```

### Testing

```bash
$ pytest
# --> runs tests using pytest
```

### Test Coverage

```bash
$ coverage report
# --> displays test coverage report
```
