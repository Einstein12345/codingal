# Connect to SQLite database
# Outline:
# Write a program to connect with the given SQLite database and print all the tables present inside the database.
# Project:
# https://colab.research.google.com
import sqlite3

# Connect to the SQLite database
# Replace 'your_database.db' with your actual database file
conn = sqlite3.connect('your_database.db')

# Create a cursor object
cursor = conn.cursor()

# Query to get all table names
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")

# Fetch all results
tables = cursor.fetchall()

# Print table names
print("Tables in the database:")
for table in tables:
    print(table[0])

# Close the connection
conn.close()