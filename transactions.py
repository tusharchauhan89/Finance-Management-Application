# transactions.py
from database import get_connection
from datetime import date


from budget import check_budget_alert
    
def add_transaction(user_id, t_type):
    category = input("Enter category (Food, Rent, Salary etc): ")
    amount = float(input("Enter amount: "))
    today = date.today().isoformat()

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO transactions (user_id, type, category, amount, date)
    VALUES (?, ?, ?, ?, ?)
    """, (user_id, t_type, category, amount, today))

    conn.commit()
    conn.close()
    if t_type == "expense":
        check_budget_alert(user_id, category)
    print("✅ Transaction added successfully!")

def view_transactions(user_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT id, type, category, amount, date
    FROM transactions WHERE user_id=?
    """, (user_id,))

    rows = cursor.fetchall()
    conn.close()

    if not rows:
        print("No transactions found.")
        return

    print("\nID | Type | Category | Amount | Date")
    print("-" * 40)
    for row in rows:
        print(row)

def update_transaction(user_id):
    trans_id = input("Enter transaction ID to update: ")
    new_amount = float(input("Enter new amount: "))

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    UPDATE transactions SET amount=?
    WHERE id=? AND user_id=?
    """, (new_amount, trans_id, user_id))

    conn.commit()
    conn.close()
    print("✅ Transaction updated!")

def delete_transaction(user_id):
    trans_id = input("Enter transaction ID to delete: ")

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    DELETE FROM transactions
    WHERE id=? AND user_id=?
    """, (trans_id, user_id))

    conn.commit()
    conn.close()
    print("🗑 Transaction deleted!")
