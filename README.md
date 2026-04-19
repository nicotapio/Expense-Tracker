# Expense Tracker (CLI)

A simple command-line expense tracker written in Python.
This project allows users to record expenses, assign categories, list all expenses, and view the total amount spent.
Expenses are stored in a JSON file so they persist between program runs.

## Features

- Add expenses with a name, category, and amount
- List all recorded expenses
- Show total amount spent
- Input validation and error handling
- Data persistence using a JSON file

## Installation

Clone the repository and navigate to the project directory:


```bash
git clone https://github.com/nicotapio/Expense-Tracker.git
cd Expense-Tracker
```

(Optional but recommended) Create and activate a virtual environment:

```bash
python3 -m venv venv  
source venv/bin/activate
```

## Usage

Run the program from the terminal:

```bash
python3 tracker.py
```

You will see a menu like this:

```text
=== Expense Tracker ===  
1. Add expense  
2. List expenses  
3. Show total  
4. Save and exit 
```

Type the number of the option you want and press Enter.

## What I Learned

Building this project helped me understand how to structure a small Python CLI application using functions and persistent storage.
I learned how to use Git and GitHub properly, including branching, merging, commits, and resolving conflicts.
I also gained confidence using the terminal and writing clear project documentation with Markdown.

## Requirements

- Python 3.8 or newer
