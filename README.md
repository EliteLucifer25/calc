# Advanced Terminal Calculator

A comprehensive, robust, and safe mathematical evaluator written in pure Python.

## Features
- **Object-Oriented Design**: Portable `Calculator` class makes it easy to embed into other Python applications.
- **Robust Math Evaluation**: Safely parses and evaluates string expressions without the typical security vulnerabilities of raw `eval()`.
- **Comprehensive Function Library**: Built-in support for trigonometry (`sin`, `cos`), logarithms (`log`, `ln`), exponential logic, and common constants (`pi`, `e`, `tau`).
- **Interactive REPL**: Launch the script without arguments to enter an interactive math session.
- **Answer History**: Dynamically refer back to the previous answers using `_` or `ans` (e.g. `ans * 2`).
- **Command-Line Interface**: Run calculations directly from bash/cmd without entering the loop (e.g. `python calc.py "sqrt(144) + 10"`).

## Usage

### 1. Interactive REPL Mode
Simply run the script to drop into the interactive calculator session:
```bash
python calc.py
```
> Example:
> ```text
> calc> 5 + 10
> = 15
> calc> _ * 2
> = 30
> ```

### 2. Command Line Mode
Pass an expression inside quotes directly into the execution string:
```bash
python calc.py "(10 * 5) / 2"
# Output: 25
```

### 3. Testing
This project includes a fully built-out `unittest` suite measuring edge cases, order of operations, and mathematical accuracy. Run tests with:
```bash
python test_calc.py
```

## Supported Math functions
Uses Python's native `math` library safely mapped into the evaluator context. Some examples: `sin`, `cos`, `tan`, `sqrt`, `log`, `ln`, `pow`, `abs`, `round`, `min`, `max`, `pi`, `e`.
