# Personal Financial Tracker

## 1. Project Overview
Personal Financial Tracker is a command-line Python application for recording income and expenses and calculating the remaining balance. It is designed as a practical Python Essentials project.

## 2. Problem Statement
Managing daily incomnses manually can make it difficult to know how much money has been received, how much has been spent, and what balance remains. This project provides a simple command-line solution for maintaining these records.

## 3. Features
- Add salary and extra income
- Add expenses with category and amount
- View all recorded expenses
- Calculate total income, total expenses, and remaining balance
- Menu-driven command-line interaction
- Basic invalid-choice handling

## 4. Technologies
- Python 3
- Python built-in data structures: dictionaries and lists
- Functions
- Loops and conditional statements
- `sys` module

## 5. Project Structure
For the VITyarthi submission, use a modular structure such as:

```text
financial-tracker/
├── main.py
├── income.py
├── expense.py
├── balance.py
├── storage.py
├── validators.py
├── reports.py
├── tests/
│   └── test_tracker.py
├── README.md
└── statement.md
```

The current prototype is contained in one Python file. Split the functions into the modules above before final submission if you are targeting the stated 5–10 file technical expectation.

## 6. Requirements
- Python 3.x
- No external packages are required for the basic version.

## 7. How to Run
1. Install Python 3.
2. Open a terminal in the project folder.
3. Run:
   `python main.py`
4. Follow the menu shown in the terminal.
5. Select Income, Expense, View Expense, Balance, or Exit.

## 8. Testing
Test the following cases:
- Add salary and extra income and verify the total.
- Add one or more expenses and verify the expense total.
- Check that remaining balance equals total income minus total expenses.
- View expenses when no expense has been added.
- Enter an invalid menu choice.
- Enter decimal monetary values.

## 9. Limitations
The current implementation keeps data in memory, so records are lost when the program exits. It does not currently provide login, persistent database storage, graphical dashboards, or date-based reports.

## 10. Future Enhancements
- Persistent CSV/JSON or SQLite storage
- Transaction dates
- Edit and delete transactions
- Budget limits
- Monthly reports
- Input validation and exception handling
- Automated unit tests
