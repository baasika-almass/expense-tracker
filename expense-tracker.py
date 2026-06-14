import json
import os
from datetime import datetime

FILENAME = "expenses.json"
CATEGORIES = ["Food", "Travel", "Shopping", "Bills", "Entertainment", "Other"]


# ─── File Handling ────────────────────────────────────────────────────────────

def load_expenses():
    """Load expenses from file."""
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as f:
            return json.load(f)
    return []


def save_expenses(expenses):
    """Save expenses to file."""
    with open(FILENAME, "w") as f:
        json.dump(expenses, f, indent=2)


# ─── Helpers ──────────────────────────────────────────────────────────────────

def get_valid_amount():
    """Get a valid positive amount from the user."""
    while True:
        try:
            amount = float(input("  Amount (₹): "))
            if amount > 0:
                return amount
            print("  Amount must be greater than 0.")
        except ValueError:
            print("  Please enter a valid number.")


def get_category():
    """Let the user pick a category from the list."""
    print("  Categories:")
    for i, cat in enumerate(CATEGORIES, 1):
        print(f"    {i}. {cat}")
    while True:
        try:
            choice = int(input("  Choose category (1-6): "))
            if 1 <= choice <= len(CATEGORIES):
                return CATEGORIES[choice - 1]
            print("  Please choose a valid number.")
        except ValueError:
            print("  Please enter a valid number.")


def get_date():
    """Get a date from the user, defaults to today."""
    date_str = input("  Date (YYYY-MM-DD, leave blank for today): ").strip()
    if not date_str:
        return datetime.now().strftime("%Y-%m-%d")
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return date_str
    except ValueError:
        print("  Invalid format, using today's date instead.")
        return datetime.now().strftime("%Y-%m-%d")


# ─── Core Functions ───────────────────────────────────────────────────────────

def add_expense():
    """Add a new expense."""
    print("\n  ADD EXPENSE")
    print("  " + "-" * 20)

    amount = get_valid_amount()
    category = get_category()
    description = input("  Description: ").strip() or "(no description)"
    date = get_date()

    expenses = load_expenses()
    expenses.append({
        "amount": amount,
        "category": category,
        "description": description,
        "date": date
    })
    save_expenses(expenses)
    print(f"\n  Added ₹{amount:.2f} under '{category}' on {date}")


def show_all_expenses():
    """Display all expenses in a table."""
    expenses = load_expenses()
    if not expenses:
        print("\n  No expenses recorded yet!")
        return

    expenses_sorted = sorted(expenses, key=lambda e: e["date"], reverse=True)

    print("\n  ALL EXPENSES")
    print("  " + "=" * 60)
    print(f"  {'Date':<12} {'Category':<15} {'Description':<20} {'Amount'}")
    print("  " + "-" * 60)
    for e in expenses_sorted:
        print(f"  {e['date']:<12} {e['category']:<15} {e['description']:<20} ₹{e['amount']:.2f}")
    print("  " + "=" * 60)
    total = sum(e["amount"] for e in expenses)
    print(f"  Total: ₹{total:.2f} across {len(expenses)} transactions\n")


def show_category_summary():
    """Show total spending grouped by category."""
    expenses = load_expenses()
    if not expenses:
        print("\n  No expenses recorded yet!")
        return

    totals = {}
    for e in expenses:
        totals[e["category"]] = totals.get(e["category"], 0) + e["amount"]

    grand_total = sum(totals.values())

    print("\n  CATEGORY SUMMARY")
    print("  " + "=" * 40)
    for cat, amount in sorted(totals.items(), key=lambda x: x[1], reverse=True):
        percent = (amount / grand_total) * 100
        bar = "█" * int(percent // 5)
        print(f"  {cat:<15} ₹{amount:>8.2f}  {bar} {percent:.1f}%")
    print("  " + "-" * 40)
    print(f"  {'Total':<15} ₹{grand_total:>8.2f}")
    print("  " + "=" * 40 + "\n")


def show_monthly_summary():
    """Show total spending for a specific month."""
    expenses = load_expenses()
    if not expenses:
        print("\n  No expenses recorded yet!")
        return

    month_input = input("\n  Enter month (YYYY-MM, leave blank for current month): ").strip()
    if not month_input:
        month_input = datetime.now().strftime("%Y-%m")

    monthly = [e for e in expenses if e["date"].startswith(month_input)]

    if not monthly:
        print(f"\n  No expenses found for {month_input}")
        return

    total = sum(e["amount"] for e in monthly)
    print(f"\n  MONTHLY SUMMARY — {month_input}")
    print("  " + "=" * 40)
    print(f"  Transactions : {len(monthly)}")
    print(f"  Total spent  : ₹{total:.2f}")
    print(f"  Average      : ₹{total / len(monthly):.2f}")
    print("  " + "=" * 40 + "\n")


def delete_expense():
    """Delete an expense."""
    expenses = load_expenses()
    if not expenses:
        print("\n  No expenses recorded yet!")
        return

    show_all_expenses()
    expenses_sorted = sorted(expenses, key=lambda e: e["date"], reverse=True)

    try:
        num = int(input("  Enter row number to delete (1 = most recent): "))
        if not (1 <= num <= len(expenses_sorted)):
            print("  Invalid number!")
            return
    except ValueError:
        print("  Please enter a valid number!")
        return

    target = expenses_sorted[num - 1]
    expenses.remove(target)
    save_expenses(expenses)
    print(f"\n  Deleted: {target['description']} — ₹{target['amount']:.2f}")


def export_to_csv():
    """Export expenses to a CSV file."""
    expenses = load_expenses()
    if not expenses:
        print("\n  No expenses to export!")
        return

    with open("expenses_export.csv", "w") as f:
        f.write("Date,Category,Description,Amount\n")
        for e in expenses:
            f.write(f"{e['date']},{e['category']},{e['description']},{e['amount']:.2f}\n")

    print("\n  Exported to 'expenses_export.csv' — open it in Excel!")


# ─── Menu ─────────────────────────────────────────────────────────────────────

def show_menu():
    print("\n  💰 EXPENSE TRACKER")
    print("  " + "=" * 25)
    print("  1. Add expense")
    print("  2. View all expenses")
    print("  3. Category summary")
    print("  4. Monthly summary")
    print("  5. Delete expense")
    print("  6. Export to CSV")
    print("  7. Exit")


# ─── Main ─────────────────────────────────────────────────────────────────────

def main():
    print("\n  Welcome to your Expense Tracker!")

    while True:
        show_menu()
        choice = input("\n  Choose an option (1-7): ").strip()

        if choice == "1":
            add_expense()
        elif choice == "2":
            show_all_expenses()
        elif choice == "3":
            show_category_summary()
        elif choice == "4":
            show_monthly_summary()
        elif choice == "5":
            delete_expense()
        elif choice == "6":
            export_to_csv()
        elif choice == "7":
            print("\n  Goodbye! Spend wisely! 💸\n")
            break
        else:
            print("  Invalid choice. Please enter 1-7.")


if __name__ == "__main__":
    main()