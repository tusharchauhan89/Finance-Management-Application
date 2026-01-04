# budget.py
from database import get_connection
from datetime import date

def set_budget(user_id):
    category = input("Enter category: ")
    limit_amount = float(input("Enter monthly budget limit: "))

    conn = get_connection()
    cursor = conn.cursor()

    # Delete old budget if exists
    cursor.execute("""
    DELETE FROM budgets
    WHERE user_id=? AND category=?
    """, (user_id, category))

    # Insert new budget
    cursor.execute("""
    INSERT INTO budgets (user_id, category, limit_amount)
    VALUES (?, ?, ?)
    """, (user_id, category, limit_amount))

    conn.commit()
    conn.close()
    print("✅ Budget set successfully!")

def view_budgets(user_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT category, limit_amount
    FROM budgets WHERE user_id=?
    """, (user_id,))

    rows = cursor.fetchall()
    conn.close()

    if not rows:
        print("No budgets set.")
        return

    print("\n📌 Your Budgets")
    print("Category | Limit")
    print("-" * 25)
    for row in rows:
        print(row)

def check_budget_alert(user_id, category):
    today = date.today()
    month = today.strftime("%m")
    year = today.strftime("%Y")

    conn = get_connection()
    cursor = conn.cursor()

    # Get budget limit
    cursor.execute("""
    SELECT limit_amount FROM budgets
    WHERE user_id=? AND category=?
    """, (user_id, category))

    budget = cursor.fetchone()
    if not budget:
        conn.close()
        return

    limit_amount = budget[0]

    # Calculate total expense for category in current month
    cursor.execute("""
    SELECT SUM(amount)
    FROM transactions
    WHERE user_id=?
    AND type='expense'
    AND category=?
    AND strftime('%m', date)=?
    AND strftime('%Y', date)=?
    """, (user_id, category, month, year))

    total_spent = cursor.fetchone()[0] or 0
    conn.close()

    if total_spent > limit_amount:
        print(f"⚠ ALERT: Budget exceeded for {category}!")
        print(f"Spent: ₹{total_spent} | Limit: ₹{limit_amount}")
