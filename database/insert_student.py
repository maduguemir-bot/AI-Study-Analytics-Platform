import sqlite3


connection = sqlite3.connect(
"students.db"
)


cursor = connection.cursor()


cursor.execute("""

INSERT INTO students

VALUES

(
1,
'John',
'Male',
90,
15,
85
)

""")


connection.commit()


connection.close()


print("Student added")
