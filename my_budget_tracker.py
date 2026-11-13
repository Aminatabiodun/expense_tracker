import json
import os
from datetime import datetime

FILE_NAME = "my_budget.json"

monthly_budget = 900.00

def load_expenses():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as file:
        return json.load(file)


def save_expense(expenses):

    with open(FILE_NAME, "w")as file:
        json.dump(expenses, file, indent=4)

def add_expense(expenses):
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

    new_expense = {
        "amount": amount,
        "category" : category,
        "payment_method": payment_method,
        "date": date_str,
        "description": description
    }

    expenses.append(new_expense)
    save_expenses(expenses)
    print(f"success! record ${amount:.2f} under '{category}'.")



def view_expenses(expenses):
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

    if total_spent > monthly_budget:
        exceeded = total_spent - monthly_budget
        print(f"WARNING: You have exceeded your ${monthly_budget:.2f} budget by ${exceeded:.2f}!")
    else:
        remaining = monthly_budget - total_spent
        print(f"Budget Status: You have ${remaining:.2f} left for the month.")

def calculate_by_category(expenses):
    if not expenses:
        print("\nNo expenses recorded yet.")
        return
    category_total ={}
    for items in expenses:
        cat = items["category"]
        amt = items["amount"]

        if cat not in category_total:
            category_total[cat] = amt
        else:
            category_total[cat]+= amt
    print("\n--- spending by Category---")
    for cat, total in category_total.items():
        print(f"-{cat}: ${total:.2f}")
    

def filter_by_category(expenses):
    if not expenses:
        print("\nNo expenses recorded yet.")
        return

    search_cat = input("Enter category name to search (e.g., Food): ").strip().title()
    print(f"\n--- Expenses in '{search_cat}' ---")

    found = False
    for item in expenses:

        if item["category"] == search_cat:
            print(f"- [{item['date']}] ${item['amount']:.2f} via {item['payment_method']} ({item['description']})")
            found = True

    if not found:
        print(f"No expenses found matching '{search_cat}'.")
    
def delete_expense(expenses):
        if not expenses:
            print("\nNo expense to delete.")
            return
        view_expenses(expenses)

        try:
            choice = int(input("\nEnter the number of the expense to delete:"))
            if 1 <= choice <= len(expenses):
                removed = expenses.pop(choice -1)
                save_expenses(expenses)
                print(f"Deleted: {removed['category']} ${removed['amount']:.2f}")
            else:
                print("Invalid expense number. Not found on the list.")
        except ValueError:
            print("Invalid input: please enter a valid number.")
        
def main():
    
    expenses = load_expenses()

    while True:
        print("\n=== Personal Expense Tracker ===")
        print("1. Add an Expense")
        print("2. View All Expenses")
        print("3. Calculate Total Spending")
        print("4. Calculate by Category")
        print("5. filter by Category")
        print("6. Delete an Expense")
        print("7. Exit")

        choice = input("Choose an option (1-6): ").strip()

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            calculate_total_spending(expenses)
        elif choice == "4":
            calculate_by_category(expenses)
        elif choice == "5":
            filter_by_category(expenses)
        elif choice =="6" :
            delete_expense(expenses)
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number from 1 to 7.")


if __name__ == "__main__":
    main()