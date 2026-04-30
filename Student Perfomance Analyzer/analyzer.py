import pandas as pd
import numpy as np
import sqlite3

def load_data():
    return sqlite3.connect('database.db')

def pass_fail():
    data = load_data()
    name = input("Enter Students Name: ")
    cursor = data.cursor()
    
    
    cursor.execute(f'''
    SELECT marks FROM students WHERE name="",({name})              
                   ''')
    result = cursor.fetchone()
    
    if result >= '34':
        print(f"{name} Is Passed")
    elif result < '34':
        print(f"{name} Is Failed!")
    else:
        print("Invalid Name !!")
        
def mean_marks():
    data = load_data()
    cursor = data.cursor()
    
    cursor.execute('''
    SELECT AVG(marks) FORM students               
                   ''')
    
    result = cursor.fetchone()
    
    return result