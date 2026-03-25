import os

FILE_NAME = "expenses.txt"


def add_expense():
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category (Food/Travel/Shopping/etc): ")
    amount = input("Enter amount: ")
    desc = input("Enter description: ")

    with open(FILE_NAME, "a") as file:
        file.write(f"{date},{category},{amount},{desc}\n")

    print(" Expense Added Successfully!\n")

def view_expenses():
    if not os.path.exists(FILE_NAME):
        print("No records found.\n")
        return

    with open(FILE_NAME, "r") as file:
        data = file.readlines()

    print("\n--- All Expenses ---")
    for i, line in enumerate(data, start=1):
        date, category, amount, desc = line.strip().split(",")
        print(f"{i}. {date} | {category} | ₹{amount} | {desc}")
    print()

def delete_expense():
    if not os.path.exists(FILE_NAME):
        print(" No records to delete.\n")
        return

    with open(FILE_NAME, "r") as file:
        data = file.readlines()

    view_expenses()
    try:
        index = int(input("Enter record number to delete: "))

        if 1 <= index <= len(data):
            data.pop(index - 1)

            with open(FILE_NAME, "w") as file:
                file.writelines(data)

            print(" Expense Deleted Successfully!\n")
        else:
            print(" Invalid choice!\n")

    except:
        print(" Please enter a valid number!\n")

def summary():
    if not os.path.exists(FILE_NAME):
        print(" No data available.\n")
        return

    month = input("Enter month (YYYY-MM): ")
    total = 0
    category_total = {}

    with open(FILE_NAME, "r") as file:
        for line in file:
            date, category, amount, desc = line.strip().split(",")

           
            if date.startswith(month):
                amount = float(amount)
                total += amount

                
                if category in category_total:
                    category_total[category] += amount
                else:
                    category_total[category] = amount

    print("\n--- Monthly Summary ---")
    print(f"Total Expense: ₹{total}")

    print("\nCategory-wise Spending:")
    for cat, amt in category_total.items():
        print(f"{cat}: ₹{amt}")
    print()



while True:
    print("===== Smart Expense Tracker =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Delete Expense")
    print("4. Monthly Summary")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        delete_expense()
    elif choice == "4":
        summary()
    elif choice == "5":
        print("Exiting program...")
        break
    else:
        print(" Invalid choice! Please try again.\n")