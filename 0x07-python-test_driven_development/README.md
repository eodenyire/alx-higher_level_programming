# Python Test-Driven Development (TDD)

This repository contains Python scripts and corresponding test files for the Test-Driven Development (TDD) tasks. Each task focuses on writing functions and ensuring their correctness through test cases.

## Table of Contents

- [Tasks](#tasks)
  - [0. Integers Addition](#0-integers-addition)
  - [1. Divide a Matrix](#1-divide-a-matrix)
  - [2. Say My Name](#2-say-my-name)
  - [3. Print Square](#3-print-square)
  - [4. Text Indentation](#4-text-indentation)
  - [5. Max Integer - Unittest](#5-max-integer---unittest)
  - [6. Matrix Multiplication](#6-matrix-multiplication)
  - [7. Lazy Matrix Multiplication](#7-lazy-matrix-multiplication)
  - [8. CPython #3: Python Strings](#8-cpython-3-python-strings)
- [How to Use](#how-to-use)
- [License](#license)

## Tasks

### 0. Integers Addition

Write a function that adds 2 integers.

Prototype: `def add_integer(a, b=98):`

- `a` and `b` must be integers or floats, otherwise raise a TypeError exception.
- `a` and `b` must be first casted to integers if they are float.
- Returns an integer: the addition of `a` and `b`.

[Link to Task Files](./0x07-python-test_driven_development/0-add_integer.py)

### 1. Divide a Matrix

Write a function that divides all elements of a matrix.

Prototype: `def matrix_divided(matrix, div):`

- `matrix` must be a list of lists of integers or floats.
- Each row of the matrix must be of the same size.
- `div` must be a number (integer or float), and it can't be equal to 0.
- All elements of the matrix should be divided by `div`, rounded to 2 decimal places.
- Returns a new matrix.

[Link to Task Files](./0x07-python-test_driven_development/1-matrix_divided.py)

### 2. Say My Name

Write a function that prints "My name is `<first name>` `<last name>`".

Prototype: `def say_my_name(first_name, last_name=""):`

- `first_name` and `last_name` must be strings.
- Prints the name if provided, otherwise raises a TypeError exception.

[Link to Task Files](./0x07-python-test_driven_development/2-say_my_name.py)

### 3. Print Square

Write a function that prints a square with the character `#`.

Prototype: `def print_square(size):`

- `size` is the size length of the square.
- Raises exceptions for invalid inputs.

[Link to Task Files](./0x07-python-test_driven_development/3-print_square.py)

### 4. Text Indentation

Write a function that prints a text with 2 new lines after each of these characters: `.`, `?`, and `:`.

Prototype: `def text_indentation(text):`

- `text` must be a string.
- Prints the text with indentation.

[Link to Task Files](./0x07-python-test_driven_development/4-text_indentation.py)

### 5. Max Integer - Unittest

Write unittests for a function that finds the maximum integer in a list.

[Link to Task Files](./0x07-python-test_driven_development/tests/5-max_integer_test.py)

### 6. Matrix Multiplication

Write a function that multiplies 2 matrices.

Prototype: `def matrix_mul(m_a, m_b):`

- Validates the input matrices and performs multiplication.
- Raises exceptions for invalid inputs.

[Link to Task Files](./0x07-python-test_driven_development/100-matrix_mul.py)

### 7. Lazy Matrix Multiplication

Write a function that multiplies 2 matrices using NumPy.

Prototype: `def lazy_matrix_mul(m_a, m_b):`

- Multiplies matrices using NumPy arrays.
- Raises exceptions for invalid inputs.

[Link to Task Files](./0x07-python-test_driven_development/101-lazy_matrix_mul.py)

### 8. CPython #3: Python Strings

Create a CPython function that prints Python strings.

Prototype: `void print_python_string(PyObject *p);`

- Prints Python strings and handles different encodings.
- Uses CPython and the C standard library.

[Link to Task Files](./0x07-python-test_driven_development/102-python.c)

## How to Use

Each task has its own set of Python files and test files. To test a task, navigate to the respective directory and run the tests using the provided commands.

Example:

$ python3 -m doctest -v ./tests/0-add_integer.txt

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## Credits

This repository contains solutions implemented by **Emmanuel Odenyire Anyira** for the tasks listed below:
- [0. Integers Addition](./0x07-python-test_driven_development/0-add_integer.py)
- [1. Divide a Matrix](./0x07-python-test_driven_development/1-matrix_divided.py)
- [2. Say My Name](./0x07-python-test_driven_development/2-say_my_name.py)
- [3. Print Square](./0x07-python-test_driven_development/3-print_square.py)
- [4. Text Indentation](./0x07-python-test_driven_development/4-text_indentation.py)
- [5. Max Integer - Unittest](./0x07-python-test_driven_development/tests/5-max_integer_test.py)
- [6. Matrix Multiplication](./0x07-python-test_driven_development/100-matrix_mul.py)
- [7. Lazy Matrix Multiplication](./0x07-python-test_driven_development/101-lazy_matrix_mul.py)
- [8. CPython #3: Python Strings](./0x07-python-test_driven_development/102-python.c)

.

