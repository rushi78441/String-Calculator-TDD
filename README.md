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

## SOLID Principles Applied

This project demonstrates **SOLID** design principles:

- **S — Single Responsibility Principle**:  
  `DefaultNumberParser` is responsible only for parsing the input string, while `StringCalculator` handles the business logic (negatives, summing, filtering > 1000).

- **O — Open/Closed Principle**:  
  The design is open for extension — you can easily add new parser strategies without modifying existing classes.

- **L — Liskov Substitution Principle**:  
  Any class implementing `NumberParser` can replace `DefaultNumberParser` without breaking the application.

- **I — Interface Segregation Principle**:  
  Small and focused abstract class (`NumberParser`) with only one method.

- **D — Dependency Inversion Principle**:  
  High-level module (`StringCalculator`) depends on abstraction (`NumberParser`) rather than concrete implementation.

## TDD Lifecycle Followed

Every feature was developed using strict **Red → Green → Refactor** cycle:

1. **Red**: Write a failing test first.
2. **Green**: Write the minimal code to make the test pass.
3. **Refactor**: Improve the code structure and readability while keeping tests green.
4. **Commit**: Make a small, meaningful commit after each cycle.

### Commit History Highlights
You can see the complete history on GitHub:

- Initial setup + empty string test
- Support for single and multiple numbers
- Newline delimiter support
- Custom delimiter support
- Negative number exception handling
- Ignore numbers greater than 1000
- OOP refactoring with SOLID principles
- Final code cleanup and documentation

---

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