# 📘 Assignment: Python Functions and Modules

## 🎯 Objective

Practice writing reusable Python functions, organizing code into separate modules, and using imports to build a clean, modular program.

## 📝 Tasks

### 🛠️ Write reusable helper functions

#### Description

Define functions that solve small tasks and return values instead of printing them directly.

#### Requirements
Completed program should:

- Define a function `format_greeting(name, favorite_color)` that returns a greeting string such as `Hello, Alice! Your favorite color is blue.`
- Define a function `calculate_square_area(side_length)` that returns the area of a square.
- Define a function `is_palindrome(text)` that returns `True` when the text reads the same forwards and backwards and `False` otherwise.
- Include example calls in `starter-code.py` to show these functions working.

### 🛠️ Organize code into modules

#### Description

Move helper functions into a separate Python module and import them into the main program.

#### Requirements
Completed program should:

- Create a separate file for helper functions (for example, `helpers.py` or `utils.py`).
- Import the helper module into `starter-code.py`.
- Use at least two functions from the helper module in the main program.
- Keep the main program logic separate from helper function definitions.

### 🛠️ Build a main program with user interaction

#### Description

Use the functions and module imports to create a small interactive program.

#### Requirements
Completed program should:

- Ask the user for their name and favorite color.
- Ask the user for a number and show the square area.
- Ask the user for a word or phrase and tell whether it is a palindrome.
- Print clear results using the helper functions.
