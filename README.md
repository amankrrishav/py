# 🐍 My Python Learning

[![Python CI](https://github.com/amankrrishav/py/actions/workflows/ci.yml/badge.svg)](https://github.com/amankrrishav/py/actions)
[![Python Version](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Repo Status](https://img.shields.io/badge/Status-Active%20Learning-brightgreen.svg)](#-the-learning-roadmap)

> **Hey there! 👋**  
> Welcome to my Python repository. This repository documents my step-by-step journey mastering Python—from absolute fundamentals, control flow, and data structures to Object-Oriented Programming (OOP) and advanced language features.
>
> ✍️ **100% Hand-Typed — Zero AI-generated code:** Every single script, logic exercise, and challenge here was manually typed, tested, and debugged by me.

---

## ⭐ Why Star This Repo?

If you are learning Python, brushing up on fundamentals, or transitioning from another language (like C++), here is why you will find this repo helpful:

1. **Standalone & Runnable**: Every script is self-contained. No complex setups or third-party packages required—just pure Python.
2. **Organized by Meta-Topics**: Structured hierarchically into thematic folders with descriptive filenames reflecting exactly what each program does.
3. **Pointers from C++**: Transition smoothly from compiled languages to Python's dynamic typing, high-level abstractions, and memory model.
4. **Comprehensive Progression**: Covers everything from basic I/O and data structures to advanced OOP, decorators, dunder methods, and exception handling.
5. **Automated CI Verified**: Every file is syntax-verified automatically via GitHub Actions on every push.

---

## 🗺️ The Learning Roadmap

Here is how the concepts progress through this repository:

| Stage | Folder | What You'll Learn | Key Files |
|:---|:---|:---|:---|
| **A. Basics & I/O** | [`src/a_basics_and_io/`](src/a_basics_and_io/) | Comments, escape sequences, `print()` parameters (`sep`, `end`), user input with `input()` | `comments.py`, `escape_sequences.py`, `print_formatting.py`, `user_input.py` |
| **B. Variables & Types** | [`src/b_variables_and_types/`](src/b_variables_and_types/) | Dynamic typing, primitive data types (`str`, `int`, `float`, `bool`), typecasting, naming rules, constants & `None`, object identity & memory (`id()`, `is` vs `==`) | `variables_and_data_types.py`, `typecasting.py`, `variable_naming_and_assignment.py`, `constants_and_none.py`, `object_identity_and_memory.py` |
| **C. Operators** | [`src/c_operators/`](src/c_operators/) | Arithmetic (`+`, `-`, `*`, `/`, `//`, `%`, `**`), comparison (`<`, `>`, `==`, `!=`), logical (`and`, `or`, `not`) | `arithmetic_operations.py`, `relational_operations.py`, `logical_operations.py` |
| **D. Control Flow** | [`src/d_control_flow/`](src/d_control_flow/) | Decision making: `if`, `if-else`, `if-elif-else` ladder, nested `if` | `simple_if.py`, `if_else_even_odd.py`, `grade_calculator.py`, `positive_even_check.py` |
| **E. Loops** | [`src/e_loops/`](src/e_loops/) | Iteration with `for` & `range()`, `while` loops, string traversal, `break`, `continue` | `for_range_basics.py`, `string_iteration.py`, `while_counter.py`, `break_and_continue.py` |
| **F. Strings** | [`src/f_strings/`](src/f_strings/) | Quotes in strings (single, double, triple, raw), indexing (positive/negative), slicing, string methods, f-strings | `string_quotes.py`, `string_indexing.py`, `string_slicing.py`, `string_methods.py`, `f-string.py` |
| **G. Functions & Modules** | [`src/g_functions/`](src/g_functions/) | Functions, parameters & return values, recursion, lambda functions, docstrings (`__doc__`, `help()`), modules & pip, variable scopes (LEGB rule, `global`, `nonlocal`) | `prime_checker.py`, `factorial.py`, `recursion_in_py.py`, `lambda.py`, `docstring/`, `a_modules&pip/`, `b_variables&scopes/` |
| **H. Data Structures** | [`src/h_ds_in_py/`](src/h_ds_in_py/) | Lists (methods, comprehension), tuples & unpacking, sets & set operations, dictionaries (methods, comprehension) | `a_lists/`, `b_tuples/`, `c_set/`, `dictionaries/` |
| **I. Object-Oriented Programming (OOP)** | [`src/i_oops_in_py/`](src/i_oops_in_py/) | Classes, objects, constructors (`__init__`), instance vs class attributes, single/multiple/multilevel inheritance, `super()` | `class.py`, `constructors.py`, `instance_and_attributes.py`, `inheritance.py` |
| **J. Advanced Python** | [`src/j_ADVANCED_PY/`](src/j_ADVANCED_PY/) | Decorators, getters & setters (`@property`), `@staticmethod` & `@classmethod`, dunder magic methods (`__str__`, `__repr__`, `__len__`), error & exception handling (`try-except-else-finally`, `raise`, custom exceptions) | `a_decorators/`, `b_getters_nd_setters/`, `c_static_class_methods/`, `d_dunder_methods/`, `e_error/` |
| **Z. Practice Questions** | [`src/z_practice_questions/`](src/z_practice_questions/) | Hands-on challenges: math problems, OOP simulations (Bank Account), string & list manipulation, logic drills | `q1_odd_even.py` to `bankAcc.py` |

---

## 🚀 Quick Start — How to Run

Clone the repository and run any program directly using Python 3:

```bash
# Clone the repository
git clone https://github.com/amankrrishav/py.git
cd py

# Run any script directly
python3 src/a_basics_and_io/print_formatting.py
python3 src/f_strings/string_methods.py
python3 src/h_ds_in_py/dictionaries/dict_comprehension.py
python3 src/i_oops_in_py/inheritance.py
python3 src/j_ADVANCED_PY/e_error/error.py
```

---

## 📜 License

This project is open source and available under the [MIT License](LICENSE).
