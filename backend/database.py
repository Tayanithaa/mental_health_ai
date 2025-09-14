import sqlite3
import os

DB_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "journal.db"))

def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    # Create table
    c.execute("""
    CREATE TABLE IF NOT EXISTS entries (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT,
        text TEXT,
        emotion TEXT,
        joy REAL,
        sadness REAL,
        anger REAL,
        fear REAL,
        surprise REAL,
        disgust REAL,
        neutral REAL
    )
    """)

    conn.commit()
    conn.close()
    print("Database initialized successfully.")

def save_entry(date, text, emotion, scores):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("""
        INSERT INTO entries (date, text, emotion, joy, sadness, anger, fear, surprise, disgust, neutral)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        date, text, emotion,
        scores.get("joy", 0.0),
        scores.get("sadness", 0.0),
        scores.get("anger", 0.0),
        scores.get("fear", 0.0),
        scores.get("surprise", 0.0),
        scores.get("disgust", 0.0),
        scores.get("neutral", 0.0)
    ))
    conn.commit()
    conn.close()

def get_entries():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT * FROM entries ORDER BY date DESC")
    rows = c.fetchall()
    conn.close()
    return rows
