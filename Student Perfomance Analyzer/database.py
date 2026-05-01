import sqlite3

DB_PATH = "d:/rl-project/Student Perfomance Analyzer/data_base.db"


def connect():
    return sqlite3.connect(DB_PATH)


def create_table():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            name TEXT,
            marks INTEGER
        )
    """)

    conn.commit()
    conn.close()


def insert_default_data():
    conn = connect()
    cursor = conn.cursor()

    # prevent duplicate insert
    cursor.execute("SELECT COUNT(*) FROM students")
    count = cursor.fetchone()[0]

    if count > 0:
        conn.close()
        return

    cursor.executemany("""
        INSERT INTO students (name, marks) VALUES (?, ?)
    """, [
        ("Aman", 78), ("Riya", 85), ("Rahul", 56), ("Sneha", 92),
        ("Arjun", 33), ("Pooja", 67), ("Karan", 45), ("Neha", 88),
        ("Vikas", 72), ("Simran", 39), ("Ankit", 60), ("Priya", 81),
        ("Rohit", 49), ("Meena", 95), ("Suresh", 28),
        ("Deepak", 74), ("Kavya", 90), ("Nitin", 52), ("Isha", 66),
        ("Yash", 41)
    ])

    conn.commit()
    conn.close()


def add_student():
    conn = connect()
    cursor = conn.cursor()

    name = input("Enter Student Name: ").strip()
    marks = int(input("Enter Student Marks: "))

    cursor.execute(
        "INSERT INTO students (name, marks) VALUES (?, ?)",
        (name, marks)
    )

    conn.commit()
    conn.close()

    print("✅ Student added successfully!")