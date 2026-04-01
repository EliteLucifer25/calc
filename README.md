---
title: Advanced Calculator
emoji: 🧮
colorFrom: blue
colorTo: purple
sdk: gradio
sdk_version: 4.44.0
app_file: app.py
pinned: false
---

# Advanced Python Calculator

A comprehensive, robust, and safe mathematical engine written in pure Python. Supports complex expressions, all standard math functions, and has a live web UI powered by Gradio.

🚀 **Live Demo**: [EliteLucifer25/calc on Hugging Face Spaces](https://huggingface.co/spaces/EliteLucifer25/calc)

📦 **Source Code**: [github.com/EliteLucifer25/calc](https://github.com/EliteLucifer25/calc)

## Features
- **Object-Oriented Design**: Portable `Calculator` class — easy to embed in other Python projects.
- **Safe Math Evaluation**: Evaluates string expressions securely without the typical `eval()` vulnerabilities. All `__builtins__` are stripped.
- **Comprehensive Function Library**: Trigonometry (`sin`, `cos`, `tan`), logarithms (`log`, `ln`), square root (`sqrt`), exponents (`pow`, `**`), and more.
- **Mathematical Constants**: `pi`, `e`, `tau`, `inf` — all supported out of the box.
- **Answer Memory**: Use `_` or `ans` to reference your last computed result.
- **Interactive CLI REPL**: Run `python calc.py` for a full interactive session.
- **CLI One-liner Mode**: `python calc.py "sqrt(144) + sin(pi/2)"` for instant results.
- **Web UI**: A clean Gradio web interface (Hugging Face Space).
- **Unit Tests**: Full `unittest` test coverage including edge cases.

## Usage

### 1. Web Interface (Hugging Face)
Visit the live Space and type any expression directly into the text box!

### 2. Interactive REPL (Terminal)
```bash
python calc.py
```
```text
calc> 5 + 10
= 15
calc> _ * 2
= 30
calc> sin(pi/2)
= 1
calc> sqrt(144)
= 12
calc> history
[1]: 15
[2]: 30
[3]: 1.0
[4]: 12.0
```

### 3. Command Line One-liner
```bash
python calc.py "(10 * 5) / 2"
# Output: 25

python calc.py "sin(radians(90))"
# Output: 1
```

### 4. Run Tests
```bash
python test_calc.py
```

## Supported Functions & Constants

| Category       | Functions / Values                               |
|----------------|--------------------------------------------------|
| Arithmetic     | `+`, `-`, `*`, `/`, `**`, `%`, `//`             |
| Rounding       | `abs`, `round`, `ceil`, `floor`, `trunc`         |
| Trigonometry   | `sin`, `cos`, `tan`, `asin`, `acos`, `atan`      |
| Logarithms     | `log`, `log2`, `log10`, `ln`                     |
| Powers/Roots   | `sqrt`, `pow`, `exp`                             |
| Misc           | `min`, `max`, `gcd`, `factorial`, `degrees`, `radians` |
| Constants      | `pi`, `e`, `tau`, `inf`                          |
| Memory         | `_` or `ans` (last result)                       |

## Installation
```bash
git clone https://github.com/EliteLucifer25/calc.git
cd calc
pip install -r requirements.txt
python calc.py
```
