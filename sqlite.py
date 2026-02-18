import sqlite3

# Connect to SQLite (in memory for testing)
conn = sqlite3.connect(':memory:')

# this is important because foreign keys are OFF by default in SQLite
conn.execute("PRAGMA foreign_keys = ON;")

cursor = conn.cursor()

# Helper function to inspect table contents
def print_table(cursor, table_name):
    cursor.execute(f"SELECT * FROM {table_name}")
    rows = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]

    print(f"\nTable: {table_name}")
    print(" | ".join(columns))
    print("-" * 30)

    for row in rows:
        print(" | ".join(str(value) for value in row))

# Create tables
cursor.execute("""
CREATE TABLE student (
    student_id INT PRIMARY KEY,
    name TEXT NOT NULL,
    age INT
)
""")

students = [
    (1, 'Alice', 20),
    (2, 'Bob', 22),
    (3, 'Charlie', 21)
]
cursor.executemany("INSERT INTO student VALUES (?, ?, ?)", students)

conn.commit()

print_table(cursor, "student")

# Example SELECT query
cursor.execute("SELECT * FROM student")
print("\nResult of: SELECT * FROM student")
for row in cursor.fetchall():
    print(row)

conn.close()



import sqlite3


conn = sqlite3.connect(':memory:')
conn.execute("PRAGMA foreign_keys = ON;")
cursor = conn.cursor()

def print_table(cursor, table_name):
    cursor.execute(f"SELECT * FROM {table_name}")
    rows = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]

    print(f"\nTable: {table_name}")
    print(" | ".join(columns))
    print("-" * 30)

    for row in rows:
        print(" | ".join(str(value) for value in row))


cursor.execute("""
CREATE TABLE student (
    student_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER
);
""")


cursor.execute("""
CREATE TABLE registered_courses (
    student_id INTEGER NOT NULL,
    course_id  INTEGER NOT NULL,
    PRIMARY KEY (student_id, course_id),
    FOREIGN KEY (student_id) REFERENCES student(student_id) 
);
""")

cursor.execute("""
CREATE TABLE grades (
    student_id INTEGER NOT NULL,
    course_id  INTEGER NOT NULL,
    grades     INTEGER NOT NULL,
    PRIMARY KEY (student_id, course_id),
    FOREIGN KEY (student_id, course_id)
        REFERENCES registered_courses(student_id, course_id)
);
""")



students = [
    (1, 'Alice', 20),
    (2, 'Bob', 22),
    (3, 'Charlie', 21)
]


registered_courses = [
    (1, 340),
    (1,330),
    (2, 330),
    (3, 310)
]
grades = [
    (1, 340, 90),
    (1, 330, 93),
    (2, 330 , 83),
    (3, 310 , 75)
]


cursor.executemany("INSERT INTO student VALUES (?, ?, ?)", students)
cursor.executemany("INSERT INTO registered_courses VALUES (?, ?)", registered_courses)
cursor.executemany("INSERT INTO grades  VALUES (?, ?, ?)", grades)

print_table(cursor, "student")
print_table(cursor, "registered_courses")
print_table(cursor, "grades")




print(" Maximum grade per student")
cursor.execute("""
SELECT student_id, MAX(grades)
FROM grades
GROUP BY student_id
""")
for row in cursor.fetchall():
    print(row)

print(" Average grade per student")
cursor.execute("""
SELECT student_id, AVG(grades)
FROM grades
GROUP BY student_id
""")
for row in cursor.fetchall():
    print(row)


# Example SELECT query
cursor.execute("SELECT * FROM student")
print("\nResult of: SELECT * FROM student")
for row in cursor.fetchall():
    print(row)

conn.close()





