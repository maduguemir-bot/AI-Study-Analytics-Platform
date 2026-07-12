import sqlite3


# Create connection

connection = sqlite3.connect(
"students.db"
)


cursor = connection.cursor()


print(
"Database created successfully"
)


connection.close()
