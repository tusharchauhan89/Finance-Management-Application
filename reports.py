# reports.py
from database import get_connection

def monthly_report(user_id):
    month = input("Enter month (MM): ")
    year = input("Enter year (YYYY): ")

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT type, SUM(amount)
    FROM transactions
    WHERE user_id=?
    AND strftime('%m', date)=?
    AND strftime('%Y', date)=?
    GROUP BY type
    """, (user_id, month, year))

    results = cursor.fetchall()
    conn.close()

    income = 0
    expense = 0

    for r in results:
        if r[0] == "income":
            income = r[1]
        elif r[0] == "expense":
            expense = r[1]

    savings = income - expense

    print("\n📅 Monthly Report")
    print(f"Month/Year: {month}/{year}")
    print(f"Total Income : ₹{income}")
    print(f"Total Expense: ₹{expense}")
    print(f"Savings      : ₹{savings}")

def yearly_report(user_id):
    year = input("Enter year (YYYY): ")

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT type, SUM(amount)
    FROM transactions
    WHERE user_id=?
    AND strftime('%Y', date)=?
    GROUP BY type
    """, (user_id, year))

    results = cursor.fetchall()
    conn.close()

    income = 0
    expense = 0

    for r in results:
        if r[0] == "income":
            income = r[1]
        elif r[0] == "expense":
            expense = r[1]

    savings = income - expense

    print("\n📆 Yearly Report")
    print(f"Year: {year}")
    print(f"Total Income : ₹{income}")
    print(f"Total Expense: ₹{expense}")
    print(f"Savings      : ₹{savings}")
