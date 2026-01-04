# auth.py
import hashlib
from database import get_connection

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register_user():
    username = input("Enter username: ")
    password = input("Enter password: ")

    hashed = hash_password(password)

    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO users (username, password) VALUES (?, ?)",
            (username, hashed)
        )

        conn.commit()
        conn.close()
        print("✅ Registration successful!")

    except Exception:
        print("❌ Username already exists!")

def login_user():
    username = input("Enter username: ")
    password = input("Enter password: ")

    hashed = hash_password(password)

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE username=? AND password=?",
        (username, hashed)
    )

    user = cursor.fetchone()
    conn.close()

    if user:
        print("✅ Login successful!")
        return user[0]  # return user id
    else:
        print("❌ Invalid username or password")
        return None
