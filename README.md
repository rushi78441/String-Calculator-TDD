# String Calculator TDD Kata

A clean, test-driven implementation of the classic **String Calculator Kata** following **Software Craftsmanship** principles, built as preparation for Incubyte Software Craftsperson Intern.

## Features Implemented
- Empty string returns 0
- Supports comma (`,`) and newline (`\n`) delimiters
- Custom delimiter support (e.g. `//;\n1;2`)
- Negative numbers throw clear exception
- Numbers greater than 1000 are ignored
- Full TDD approach with frequent commits

## Folder Structure

```bash
String-Calculator-TDD/
├── string_calculator/
│   ├── __init__.py
│   └── calculator.py          # Main OOP implementation
├── tests/
│   ├── __init__.py
│   └── test_calculator.py     # All test cases
├── README.md
├── requirements.txt
└── .gitignore
```

## SOLID Principles Applied
This project demonstrates SOLID design principles:

S — Single Responsibility Principle:
DefaultNumberParser is responsible only for parsing the input string into numbers, while StringCalculator handles business rules (negatives, filtering, and summation).
O — Open/Closed Principle:
The design is open for extension — new parsing strategies can be added without modifying existing classes.
L — Liskov Substitution Principle:
Any implementation of NumberParser can safely replace DefaultNumberParser.
I — Interface Segregation Principle:
Small, focused abstract class with only one method.
D — Dependency Inversion Principle:
High-level module (StringCalculator) depends on abstraction (NumberParser) rather than concrete implementation.

## TDD Lifecycle Followed
Every feature was developed using strict Red → Green → Refactor cycle:

Red: Write a failing test.
Green: Write minimal code to make the test pass.
Refactor: Improve code quality, readability, and structure.
Commit: Small, meaningful commits showing the evolution.

## Commit History Highlights
Initial setup + empty string test
Support for single and multiple numbers
Newline delimiter support
Custom delimiter support
Negative number exception handling
Ignore numbers greater than 1000
Refactoring to OOP with SOLID principles
Final cleanup and documentation

# 1. Clone the repo
git clone https://github.com/rushi78441/String-Calculator-TDD.git

# 2. Setup environment
cd String-Calculator-TDD
python -m venv venv
source venv/bin/activate    # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run tests
python -m pytest tests/ --cov