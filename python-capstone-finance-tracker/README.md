# Personal Finance Tracker

A simple command-line tool to help manage and track your personal expenses by category. This script allows you to add expenses, view detailed entries, and generate summaries based on spending categories. All data is saved between sessions using Python's `pickle` module.

---

## Features

- Add expenses categorized by type (e.g., Food, Transport)
- View a full list of recorded expenses
- View a summary of total spending by category
- Persistent storage of data using `tracker.pkl`

---

## How to Run

1. **Ensure Python 3.10 or higher is installed.**  
   This script uses `match-case`, which was introduced in Python 3.10.

2. **Save the script.**  
   Save the code as `finance_tracker.py`.

3. **Run the script from the terminal:**

   ```bash
   python finance_tracker.py
   ```

4. **Follow the on-screen prompts:**

   ```
   what would you like to do?
   1. Add Expense
   2. View All Expenses
   3. View Summary
   4. Exit
   ```

---

## Python Concepts Demonstrated

### 1. Classes and Object-Oriented Programming

Encapsulation of related behavior in a `FinanceTracker` class:

```python
class FinanceTracker():
    def __init__(self):
        ...
```

### 2. File I/O and Data Persistence

Storing and retrieving data using `pickle`:

```python
with open(self.pickle_path, "wb") as f:
    pkl.dump(self.tracker_dict, f)

with open(self.pickle_path, "rb") as f:
    return pkl.load(f)
```

### 3. Pattern Matching (`match-case`)

Clean control flow using Python's structural pattern matching:

```python
match val:
    case 1:
        self.add_expense()
    case 2:
        self.view_summary()
    ...
```

### 4. Input Validation with `try-except`

Robust input handling:

```python
try:
    val = int(input("Choose an option: "))
except ValueError:
    print("Please enter a number!")
```

### 5. Dictionaries and Lists for Data Organization

Expenses are stored as a dictionary of lists:

```python
self.tracker_dict.setdefault(cat, []).append((desc, amount))
```

### 6. Loops and Conditional Logic

Used for user interaction and input enforcement:

```python
while True:
    ...
    if val < 1 or val > 4:
        print("Not a valid selection!")
```

---

## Example Usage

### Adding an Expense

```
Enter category: Food
Enter expense description: Lunch at cafe
Enter amount: 12.5
Expense added successfully
```

### Viewing Summary

```
-----Summary-----
 - Food: 42.7
 - Transport: 15.0
```

---

## Output

The script will automatically create a file called `tracker.pkl` in the working directory. This file contains all tracked expenses in a serialized format and is loaded when the program starts.

