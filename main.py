import csv
import json
import os
from datetime import datetime


# File names
EXPENSE_FILE = "expenses.csv"
BUDGET_FILE = "budget.json"


# --------------------------------------------------
# Create files if they do not exist
# --------------------------------------------------
def create_files():
    if not os.path.exists(EXPENSE_FILE):
        with open(EXPENSE_FILE, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Description", "Amount"])

    if not os.path.exists(BUDGET_FILE):
        with open(BUDGET_FILE, "w") as file:
            json.dump({}, file)


# --------------------------------------------------
# Add Expense
# --------------------------------------------------
def add_expense():
    print("\n--- Add Expense ---")

    category = input("Enter category: ").strip()
    description = input("Enter description: ").strip()

    try:
        amount = float(input("Enter amount: ₹"))

        if amount <= 0:
            print("Amount must be greater than 0.")
            return

    except ValueError:
        print("Please enter a valid amount.")
        return

    date = datetime.now().strftime("%Y-%m-%d")

    with open(EXPENSE_FILE, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, description, amount])

    print("Expense added successfully!")


# --------------------------------------------------
# View All Expenses
# --------------------------------------------------
def view_expenses():
    print("\n--- All Expenses ---")

    try:
        with open(EXPENSE_FILE, "r") as file:
            reader = csv.DictReader(file)

            found = False

            for row in reader:
                found = True
                print(
                    f"Date: {row['Date']} | "
                    f"Category: {row['Category']} | "
                    f"Description: {row['Description']} | "
                    f"Amount: ₹{float(row['Amount']):.2f}"
                )

            if not found:
                print("No expenses found.")

    except FileNotFoundError:
        print("Expense file not found.")


# --------------------------------------------------
# Set Monthly Budget
# --------------------------------------------------
def set_budget():
    print("\n--- Set Monthly Budget ---")

    month = input("Enter month (YYYY-MM): ").strip()

    try:
        datetime.strptime(month, "%Y-%m")
    except ValueError:
        print("Invalid month format. Example: 2026-10")
        return

    try:
        amount = float(input("Enter monthly budget: ₹"))

        if amount <= 0:
            print("Budget must be greater than 0.")
            return

    except ValueError:
        print("Please enter a valid amount.")
        return

    try:
        with open(BUDGET_FILE, "r") as file:
            budgets = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        budgets = {}

    budgets[month] = amount

    with open(BUDGET_FILE, "w") as file:
        json.dump(budgets, file, indent=4)

    print(f"Budget set successfully for {month}.")


# --------------------------------------------------
# Get Total Expenses
# --------------------------------------------------
def get_total_expenses():
    total = 0

    try:
        with open(EXPENSE_FILE, "r") as file:
            reader = csv.DictReader(file)

            for row in reader:
                total += float(row["Amount"])

    except (FileNotFoundError, ValueError):
        pass

    return total


# --------------------------------------------------
# Category-wise Summary
# --------------------------------------------------
def category_summary():
    print("\n--- Category-wise Summary ---")

    categories = {}

    try:
        with open(EXPENSE_FILE, "r") as file:
            reader = csv.DictReader(file)

            for row in reader:
                category = row["Category"]
                amount = float(row["Amount"])

                if category in categories:
                    categories[category] += amount
                else:
                    categories[category] = amount

    except FileNotFoundError:
        print("Expense file not found.")
        return

    if not categories:
        print("No expenses found.")
        return

    for category, amount in categories.items():
        print(f"{category}: ₹{amount:.2f}")


# --------------------------------------------------
# Monthly Spending Summary
# --------------------------------------------------
def monthly_summary():
    print("\n--- Monthly Spending Summary ---")

    month = input("Enter month (YYYY-MM): ").strip()

    try:
        datetime.strptime(month, "%Y-%m")
    except ValueError:
        print("Invalid month format. Example: 2026-10")
        return

    total = 0

    try:
        with open(EXPENSE_FILE, "r") as file:
            reader = csv.DictReader(file)

            for row in reader:
                if row["Date"].startswith(month):
                    total += float(row["Amount"])

    except FileNotFoundError:
        print("Expense file not found.")
        return

    print(f"\nMonth: {month}")
    print(f"Total Spending: ₹{total:.2f}")

    # Read budget
    try:
        with open(BUDGET_FILE, "r") as file:
            budgets = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        budgets = {}

    if month in budgets:
        budget = float(budgets[month])
        remaining = budget - total

        print(f"Monthly Budget: ₹{budget:.2f}")

        if remaining >= 0:
            print(f"Remaining Budget: ₹{remaining:.2f}")
        else:
            print(f"Budget Exceeded By: ₹{abs(remaining):.2f}")

    else:
        print("No budget set for this month.")


# --------------------------------------------------
# View Budget
# --------------------------------------------------
def view_budgets():
    print("\n--- Monthly Budgets ---")

    try:
        with open(BUDGET_FILE, "r") as file:
            budgets = json.load(file)

    except (FileNotFoundError, json.JSONDecodeError):
        print("No budgets found.")
        return

    if not budgets:
        print("No budgets found.")
        return

    for month, amount in budgets.items():
        print(f"{month}: ₹{float(amount):.2f}")


# --------------------------------------------------
# Overall Summary
# --------------------------------------------------
def overall_summary():
    print("\n--- Overall Spending Summary ---")

    total = get_total_expenses()

    print(f"Total Expenses: ₹{total:.2f}")

    category_summary()


# --------------------------------------------------
# Main Menu
# --------------------------------------------------
def main():
    create_files()

    while True:
        print("\n====================================")
        print(" PERSONAL EXPENSE & BUDGET TRACKER")
        print("====================================")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Set Monthly Budget")
        print("4. View Monthly Budgets")
        print("5. Category-wise Summary")
        print("6. Monthly Spending Summary")
        print("7. Overall Spending Summary")
        print("8. Exit")
        print("====================================")

        choice = input("Enter your choice (1-8): ").strip()

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            set_budget()

        elif choice == "4":
            view_budgets()

        elif choice == "5":
            category_summary()

        elif choice == "6":
            monthly_summary()

        elif choice == "7":
            overall_summary()

        elif choice == "8":
            print("\nThank you for using Expense Tracker!")
            break

        else:
            print("Invalid choice. Please select 1-8.")


# --------------------------------------------------
# Start Program
# --------------------------------------------------
if __name__ == "__main__":
    main()