import json
import os
import csv
from datetime import datetime

DATA_FILE = "expenses.json"

def load_data():
    """Loads expense data from the JSON file."""
    if not os.path.exists(DATA_FILE):
        return {"budget": 0.0, "expenses": []}
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return {"budget": 0.0, "expenses": []}

def save_data(data):
    """Saves expense data to the JSON file."""
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

def set_monthly_budget(amount):
    """Sets or updates the monthly budget limit."""
    data = load_data()
    data["budget"] = float(amount)
    save_data(data)
    print(f"\n[+] Monthly budget successfully set to ${amount:.2f}")

def add_expense(amount, category, description):
    """Adds a new expense with a timestamp."""
    data = load_data()
    expense = {
        "amount": float(amount),
        "category": category.strip().capitalize(),
        "description": description.strip(),
        "date": datetime.now().strftime("%Y-%m-%d %H:%M")
    }
    data["expenses"].append(expense)
    save_data(data)
    print(f"\n[+] Added: ${amount:.2f} for '{description}' ({category})")
    
    # Check if budget is exceeded
    total_spent = sum(item["amount"] for item in data["expenses"])
    budget = data["budget"]
    if budget > 0 and total_spent > budget:
        print(f"[!] Warning: You have exceeded your monthly budget of ${budget:.2f}! Total spent: ${total_spent:.2f}")

def view_summary():
    """Displays total spending, budget status, and category breakdown."""
    data = load_data()
    expenses = data["expenses"]
    budget = data["budget"]
    
    if not expenses:
        print("\nNo expenses recorded yet.")
        return

    total_spent = sum(item["amount"] for item in expenses)
    
    print("\n" + "="*40)
    print("           EXPENSE SUMMARY")
    print("="*40)
    print(f"Total Budget : ${budget:.2f}" if budget > 0 else "Total Budget : Not Set")
    print(f"Total Spent  : ${total_spent:.2f}")
    if budget > 0:
        remaining = budget - total_spent
        status = f"${remaining:.2f} remaining" if remaining >= 0 else f"${abs(remaining):.2f} over budget!"
        print(f"Status       : {status}")
    print("-" * 40)
    
    # Category breakdown
    categories = {}
    for item in expenses:
        cat = item["category"]
        categories[cat] = categories.get(cat, 0) + item["amount"]
        
    print("Breakdown by Category:")
    for cat, amt in categories.items():
        print(f"  - {cat}: ${amt:.2f}")
    print("="*40)

def export_to_csv(filename="expenses_export.csv"):
    """Exports all recorded expenses to a CSV file."""
    data = load_data()
    expenses = data["expenses"]
    
    if not expenses:
        print("\n[!] No expenses to export.")
        return

    try:
        with open(filename, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Description", "Amount ($)"])
            for item in expenses:
                writer.writerow([item["date"], item["category"], item["description"], item["amount"]])
        print(f"\n[+] Successfully exported expenses to '{filename}'!")
    except Exception as e:
        print(f"[!] Error exporting to CSV: {e}")