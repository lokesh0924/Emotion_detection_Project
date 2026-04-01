import sqlite3

def init_db():
    conn = sqlite3.connect("emotion.db")
    c = conn.cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT,
        text TEXT,
        emotion TEXT
    )
    """)

    conn.commit()
    conn.close()

def insert_data(name, email, text, emotion):
    conn = sqlite3.connect("emotion.db")
    c = conn.cursor()

    c.execute(
        "INSERT INTO users (name, email, text, emotion) VALUES (?, ?, ?, ?)",
        (name, email, text, emotion)
    )

    conn.commit()
    conn.close()

def get_all_data():
    conn = sqlite3.connect("emotion.db")
    c = conn.cursor()

    c.execute("SELECT * FROM users")
    data = c.fetchall()

    conn.close()
    return data
