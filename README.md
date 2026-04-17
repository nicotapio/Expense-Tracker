
# Expense Tracker (CLI)

A simple command-line expense tracker written in Python.
The program allows users to add expenses, list them, and view the total amount spent.
Expenses are stored in a JSON file so they persist between runs.

## Features

- Add an expense with a name and amount
- List all recorded expenses
- Show the total amount spent
- Data persistence using a JSON file
- Error handling for invalid user input

## Installation

Clone the repository and move into the project directory:

```bash
git clone https://github.com/nicotapio/
expense-tracker.git
cd expense-tracker



Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```


## Usage

Run the program from the terminal:

```bash
python3 tracker.py
```

The program will display a menu in the terminal.
Type the number of the option you want and press Enter.

Menu options:
- Add expense
- List expenses
- Show total
- Save and exit

Expenses are automatically saved and loaded between program runs.

## Requirements

- Python 3.8 or newer

