print("=" * 40)
print("        PYTHON EXPENSE TRACKER")
print("=" * 40)

total = 0

while True:

    expense = input("Enter Expense (or type 'quit' to exit): ")

    if expense.lower() == "quit":
        break

    try:
        expense = int(expense)
        total += expense
        print(f"Current Total: ₹{total}")

    except ValueError:
        print("Invalid Expense! Please enter numbers only.")

print("\n==============================")
print(f"Final Total Spent: ₹{total}")
print("==============================")