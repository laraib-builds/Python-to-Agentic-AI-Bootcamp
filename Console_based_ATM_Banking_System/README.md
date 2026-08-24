# ATM Banking System

A simple command-line ATM Banking System built in Python as a learning project. The project focuses on practicing functions, file handling, exception handling, timestamps, validation, and basic program structure.

## Features
- Check current balance
- Deposit money
- Withdraw money
- Validate invalid transaction amounts
- Handle invalid numerical input
- Record successful and failed transactions
- Store transaction history in detail.txt
- Add date and time to each transaction
- View transaction history
- Exit through a menu


## How It Works

The program starts with an initial balance:

```python
balance = 3500
```
The user interacts with the ATM through a menu. Each operation is handled by a separate function:

`display_balance()` — displays the current balance.
`deposit()` — adds money to the balance.
`withdraw()` — subtracts money after checking the available balance.
`show_history()` — reads and displays previous transactions.
`record_transaction()` — saves transaction details to the history file.


## Why These Things Were Used

### Functions

The program uses separate functions instead of putting everything inside the main loop. This makes each part of the ATM responsible for one particular task and keeps the code easier to follow.

### global balance

`deposit()` and `withdraw()` modify the balance, so global balance is used to allow those functions to modify the balance defined outside them.

This was useful for understanding variable scope and how functions interact with shared data.

### Exception Handling

`try/except` is used to handle invalid numerical input:

```python
try:
    amount = int(input(...))
except ValueError:
    ...
```
This prevents the program from crashing when the user enters something like "abc".

Normal ATM validation, such as checking whether a withdrawal exceeds the balance, is handled with if conditions rather than exceptions.

### File Handling

Transactions are stored in `detail.txt` using append mode:

```python
with open("detail.txt", "a") as file:
```

Append mode was chosen so that new transactions are added without deleting previous transaction records.

### Timestamps

`datetime` is used to record when each transaction occurred. This makes the transaction history more useful and realistic.

### Example Transaction Record:
```python
2026-08-15 22:30:15 | Withdrawal | Amount: 500 | Balance: 3000 | Status: Success
```

Failed transactions are also recorded so the history contains the complete transaction attempt history, rather than only successful operations.

## Purpose

This project was built to practice how basic Python concepts work together in a real program:

Variables → Functions → Conditionals → Exception Handling → File Handling → Program Structure
