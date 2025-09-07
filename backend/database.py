import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "..", "journal.db")
def init_db():
    conn = sqlite3.connect(DB_PATH )
    c= conn.cursor()
    c.execute("""
    CREATE TABLE IF NOT EXISTS entries (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT,
        text TEXT,
        sentiment TEXT,
        score REAL
    )
    """)
    print("Database and table created successfully.")
    conn.commit()
    conn.close()



def save_entry(date, text, sentiment, score):
    conn = sqlite3.connect("journal.db")
    c = conn.cursor()
    c.execute("INSERT INTO entries (date, text, sentiment, score) VALUES (?, ?, ?, ?)", (date, text, sentiment, score))
    conn.commit()
    conn.close()

def get_entries():
    conn = sqlite3.connect("journal.db")
    c = conn.cursor()
    c.execute("SELECT * FROM entries ORDER BY date DESC")

    rows = c.fetchall()

    conn.close()
    return rows