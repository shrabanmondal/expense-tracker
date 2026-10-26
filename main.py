import tracker

def main():
    while True:
        print("\n--- CLI EXPENSE & BUDGET TRACKER ---")
        print("1. Set Monthly Budget")
        print("2. Add Expense")
        print("3. View Summary & Breakdown")
        print("4. Export Expenses to CSV")
        print("5. Exit")
        
        choice = input("\nChoose an option (1-5): ").strip()
        
        if choice == "1":
            try:
                amt = float(input("Enter monthly budget amount ($): "))
                tracker.set_monthly_budget(amt)
            except ValueError:
                print("[!] Invalid input. Please enter a valid number.")
                
        elif choice == "2":
            try:
                amt = float(input("Enter amount ($): "))
                category = input("Enter category (e.g., Food, Travel, Studies): ")
                desc = input("Enter brief description: ")
                tracker.add_expense(amt, category, desc)
            except ValueError:
                print("[!] Invalid amount. Please try again.")
                
        elif choice == "3":
            tracker.view_summary()
            
        elif choice == "4":
            filename = input("Enter export filename (default 'expenses_export.csv'): ").strip()
            if not filename:
                filename = "expenses_export.csv"
            if not filename.endswith(".csv"):
                filename += ".csv"
            tracker.export_to_csv(filename)
            
        elif choice == "5":
            print("\nExiting. Keep tracking your goals! Goodbye!")
            break
        else:
            print("[!] Invalid choice. Please select between 1 and 5.")

if __name__ == "__main__":
    main()