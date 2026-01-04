# main.py

from database import create_tables
from backup import backup_database, restore_database

from auth import register_user, login_user
from transactions import (
    add_transaction,
    view_transactions,
    update_transaction,
    delete_transaction
)
from reports import monthly_report, yearly_report
from budget import set_budget, view_budgets


def user_menu(user_id):
    while True:
        print("\n--- Transaction Menu ---")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Transactions")
        print("4. Update Transaction")
        print("5. Delete Transaction")
        print("6. Monthly Report")
        print("7. Yearly Report")
        print("8. Set Budget")
        print("9. View Budgets")
        print("10. Logout")
        print("11. Backup Data")
        print("12. Restore Data")
        print("13. Logout")
 

        choice = input("Choose option: ")

        if choice == "1":
            add_transaction(user_id, "income")

        elif choice == "2":
            add_transaction(user_id, "expense")

        elif choice == "3":
            view_transactions(user_id)

        elif choice == "4":
            update_transaction(user_id)

        elif choice == "5":
            delete_transaction(user_id)

        elif choice == "6":
            monthly_report(user_id)

        elif choice == "7":
            yearly_report(user_id)

        elif choice == "8":
            set_budget(user_id)

        elif choice == "9":
            view_budgets(user_id)

        elif choice == "10":
            print("Logged out.")
            break
        elif choice == "11":
         backup_database()
        elif choice == "12":
         restore_database()
        elif choice == "13":
         print("Logged out.")
         break


        else:
            print("Invalid choice. Please try again.")


def main():
    create_tables()

    while True:
        print("\n--- Personal Finance App ---")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            register_user()

        elif choice == "2":
            user_id = login_user()
            if user_id:
                user_menu(user_id)

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
