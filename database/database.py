import sqlite3


connection = sqlite3.connect(
"students.db"
)


cursor = connection.cursor()


cursor.execute("""

CREATE TABLE IF NOT EXISTS students (

id INTEGER PRIMARY KEY,

name TEXT,

gender TEXT,

attendance INTEGER,

study_hours INTEGER,

exam_score INTEGER

)

""")


connection.commit()


connection.close()


print("Student table created")

connection.close()
