# backup.py
import shutil
import os

DB_NAME = "finance.db"
BACKUP_NAME = "finance_backup.db"

def backup_database():
    if os.path.exists(DB_NAME):
        shutil.copy(DB_NAME, BACKUP_NAME)
        print("✅ Database backup created successfully!")
    else:
        print("❌ Database file not found!")

def restore_database():
    if os.path.exists(BACKUP_NAME):
        shutil.copy(BACKUP_NAME, DB_NAME)
        print("✅ Database restored successfully!")
    else:
        print("❌ Backup file not found!")
