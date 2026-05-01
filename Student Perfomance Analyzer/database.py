import sqlite3

def connect():
    return sqlite3.connect("d:/rl-project/Student Perfomance Analyzer/data_base.db")

# creating an cursor,


def create_table():
    cnn = connect()
    cursor = cnn.cursor()
        
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            name TEXT,
            marks INTEGER
        )''')
    
    cnn.commit()
    cnn.close()

# Now inserting the data in database.db

def stu_data():
    cur = connect()
    cursor = cur.cursor()
    cursor.execute('''
    INSERT INTO students(name,marks) VALUES
    ("Aman", 78), ("Riya", 85), ("Rahul", 56), ("Sneha", 92),
    ("Arjun", 33), ("Pooja", 67), ("Karan", 45), ("Neha", 88),
    ("Vikas", 72), ("Simran", 39), ("Ankit", 60), ("Priya", 81),
    ("Rohit", 49), ("Meena", 95), ("Suresh", 28),
    ("Deepak", 74), ("Kavya", 90), ("Nitin", 52), ("Isha", 66),
    ("Yash", 41) ''')
    
    cur.commit()
    cur.close()
    

# Now adding function which can add students,

def add_student():
    conn = connect()
    cursor = conn.cursor()
    name = input("Enter Student Name: ")
    marks = input("ENter Student Marks: ")
    cursor.execute(f'''
    INSERT INTO students(name,marks) VALUES(?,?)
                   ''')
    conn.commit()
    conn.close()