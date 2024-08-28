import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('users.db')

# Create a cursor object
c = conn.cursor()

# Create a users table
c.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT UNIQUE,
        password TEXT
    )
''')

# Commit changes and close the connection
conn.commit()
conn.close()
