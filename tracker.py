# tracker.py

# PLAN:
# - expenses = []  list to store data
# - add_expense (): ask user for amount + description, add to list
# - list_expenses(): show all expenses: Display all expenses in a clean, readable format
# - total(): sum all expenses
# - save_expenses(): write expenses to file
# - load_expenses(): read file at start, restores all saved expenses
# - main(): menu loop : 1. Add expense 2. List expenses 3. Show total 4. Save and exit

import json
import os
FILE_NAME = "expenses.json"


expenses = [] # List to store expenses

def add_expense():
    """Add a new expense to the list"""
    name = input("Enter expense name: ")
    amount = input("Enter amount: ")

    try:
        amount = float(amount)
    except ValueError:
        print("Invalid amount! Please enter a Number.")
        return

    expense = {"name": name, "amount": amount}
    expenses.append(expense)

    save_expenses()

    print("Expense added!")


def list_expenses():
    """Print all expenses"""
    if not expenses:
        print("No expenses recorded.")
        return

    print("\nYour expenses:")
    for i, exp in enumerate(expenses, start=1):
        print(f"{i}. {exp['name']} - {exp['amount']:.2f}")




def total():
    """Calculate and print total expenses"""
    if not expenses:
        print("Total: 0.00")
        return 0

    total_amount = 0
    for exp in expenses:
       total_amount += exp["amount"]

    print(f"Total: {total_amount:.2f}")
    return total_amount



def save_expenses():
    """Save expenses to a file"""
    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file, indent=4)


def load_expenses():
    """Load expenses from a file"""
    global expenses

    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as file:
                expenses = json.load(file)
        except json.JSONDecodeError:
            print("Error: expenses file is corrupted. Starting fresh.")
            expenses = []
    else:
        expenses = []


def main():
    """Main program loop."""
    load_expenses()

    while True:
        print("\n=== Expense Tracker ===")
        print("1. Add expense")
        print("2. List expenses")
        print("3. Show total")
        print("4. Save and exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            list_expenses()
        elif choice == "3":
            total()
        elif choice == "4":
            save_expenses()
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")



if __name__ == "__main__":
    main()



