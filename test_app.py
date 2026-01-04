# test_app.py
import unittest
from auth import hash_password
from database import create_tables, get_connection

class TestFinanceApp(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        create_tables()

    def test_password_hashing(self):
        pwd = "test123"
        hashed = hash_password(pwd)
        self.assertNotEqual(pwd, hashed)

    def test_database_connection(self):
        conn = get_connection()
        self.assertIsNotNone(conn)
        conn.close()

    def test_user_table_exists(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='users'")
        table = cursor.fetchone()
        conn.close()
        self.assertIsNotNone(table)

if __name__ == "__main__":
    unittest.main()
