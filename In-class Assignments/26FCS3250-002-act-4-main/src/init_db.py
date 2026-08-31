import sqlite3

# Connect to SQLite database (it will be created if it doesn't exist)
conn = sqlite3.connect('students.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Create the 'students' table with 'id' and 'name' columns
cursor.execute('''
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
)
''')

# Commit the changes and close the connection
conn.commit()
conn.close()

print("SQLite database 'students.db' with table 'students' has been created successfully.")
