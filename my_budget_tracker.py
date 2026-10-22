import json
import os
from datetime import datetime

FILE_NAME = "my_budget.json"

monthly_budget = 900.00

def load_expenses():
    if not os.path.exists(FILE_NAME):
        return[]

    with open(FILE_NAME, "r")as file:
        return json.load(file)

def add_expenses():
    print("\n--- Add a New Expense---")

    while True:
        try:
            amount = float(input("Enter amount(e.g, 15.50):"))
            if amount <= 0:
                print("Amount must be greater than 0.")
                continue 
            break
        except ValueError:
            print("Invalid input! Please enter a valid number (not letters).")
    category = input("Enter category (e.g, Food, Transport):").strip().title()

    payment_method = input("Enter payment_method(e.g, cash, card, transfer):").strip().title()

    description = input("Enter a brief description:").strip()

    date_str = datetime.now().strftime("%y-%m-%d")


def view_all_expenses(expenses):
    print("\n--- All Record Expenses---")
    if not expenses:
        print("No expenses recorded yet,")
        return
    for index, product  in enumerate(expenses, start=1):
        print(f"{index}. [{product['date']} {product['category']}: ${product['amount']:.2f} ({product['description']})]")

def calculate_total_spending(expenses):
    if not expenses:
        print("\nNo expenses recorded yet.")
        return

    total_spent = 0
    for item in expenses:
        total_spent += item["amount"]
    print(f"\nTotal Spent (Global Total): ${total_spent:.2f}")

    while True:
        try:
            amount = float(input ("Enter amount spent (e.g, 200)"))
            if amount >= 900:
                print("Amount should not be more than 900")
                continue
            break 
        except ValueError:
            print("Invalid input! Please enter a valid number (not letters).")



