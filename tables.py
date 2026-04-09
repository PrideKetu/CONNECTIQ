import sqlite3
import os

# Path to your DB
db_path = os.path.join(os.getcwd(), "db.sqlite3")

# Connect to DB
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Create table for Intern
cursor.execute("""
CREATE TABLE IF NOT EXISTS reports_intern (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(100) NOT NULL,
    department VARCHAR(100) NOT NULL,
    age INTEGER NOT NULL
);
""")

conn.commit()
conn.close()
print("Table reports_intern created (or already exists).")