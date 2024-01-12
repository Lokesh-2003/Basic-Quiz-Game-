import json
from collections import defaultdict
from datetime import datetime

def add_expense():
    description = input("Enter a brief description of the expense: ")
    amount = float(input("Enter the amount spent: "))
    category = input("Enter the category (e.g., food, transportation, entertainment): ")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    expense = {"description": description, "amount": amount, "category": category, "timestamp": timestamp}
    expenses.append(expense)
    save_expenses()

def save_expenses():
    with open('expenses.json', 'w') as file:
        json.dump(expenses, file)

def load_expenses():
    try:
        with open('expenses.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def monthly_summary():
    current_month = datetime.now().strftime("%Y-%m")
    monthly_expenses = [expense for expense in expenses if expense["timestamp"].startswith(current_month)]
    total_expenses = sum(expense["amount"] for expense in monthly_expenses)
    print(f"Total expenses this month: ${total_expenses:.2f}")

def category_summary():
    category_expenses = defaultdict(float)
    for expense in expenses:
        category_expenses[expense["category"]] += expense["amount"]
    for category, amount in category_expenses.items():
        print(f"{category}: ${amount:.2f}")

expenses = load_expenses()

while True:
    print("\nExpense Tracker")
    print("1. Add Expense\n2. Monthly Summary\n3. Category-wise Summary\n4. Exit")
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        monthly_summary()
    elif choice == "3":
        category_summary()
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please enter a valid option.")
