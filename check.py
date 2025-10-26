import sqlite3, os
path = "Database.db"
print("Using DB at:", os.path.abspath(path))
conn = sqlite3.connect(path)
cur = conn.cursor()
cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
print("Tables found:", cur.fetchall())
conn.close()