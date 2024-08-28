import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('appointments.db')

# Create a cursor object
c = conn.cursor()

# Create the appointments table if it doesn't exist
c.execute('''
    CREATE TABLE IF NOT EXISTS appointments (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT,
        date TEXT UNIQUE
    )
''')

# Commit changes and close the connection
conn.commit()
conn.close()
