import pandas as pd
import numpy as np
import sqlite3
from database import *

def load_data():
    return sqlite3.connect("d:/rl-project/Student Perfomance Analyzer/data_base.db")

def pass_fail():
    data = load_data()
    name = input("Enter Students Name: ")
    cursor = data.cursor()
    
    
    cursor.execute("SELECT marks FROM students WHERE LOWER(name)=LOWER(?)",(name,))
    result = cursor.fetchone()
    
    if result is None:
        print("No Student Found!!")
        data.close()
        return
    
    marks = result[0]
    if marks >= 34:
        print(f"{name} Is Passed")
    else:
        print(f"{name} Is Failed!")
    
def mean_marks():
    data = load_data()
    cursor = data.cursor()
    
    cursor.execute('''
    SELECT AVG(marks) FORM students               
                   ''')
    
    result = cursor.fetchone()
    
    data.close()
    return result