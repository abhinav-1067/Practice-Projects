import matplotlib.pyplot as plt
import seaborn as sns
import sqlite3
from database import *
# Visulisation histogram graph of NAME vs MARKS,

def graph():
    data = sqlite3.connect("d:/rl-project/Student Perfomance Analyzer/data_base.db")
    cursor = data.cursor()
    
    cursor.execute('''
     SELECT name, marks FROM students             
                   ''')
    dat = cursor.fetchall()
    
    if not dat:
        print("No Data Found!!")
        return
    
    name = []
    marks = []
    
    for row in dat:
        name.append(row[0])
        marks.append(row[1])
    
    # now we can plot graph,
    
    plt.bar(name,marks)
    plt.xlabel('Students Name')
    plt.ylabel('Marks')
    plt.xticks(rotation=45)
    plt.title('Student Performance Graph 📊')
    
    plt.show()
    data.close()