from database import *
from analyzer import *
from graphs import *
import sqlite3


def menu():
    print(f"\n ---Student Performance Analyzer---")
    print(f"1. Add Students")
    print(f"2. Student Result")
    print(f"3. Average Marks Of Class")
    print(f"4. Performance Graph")
    print(f"5. Exiting....")
    
def main():
    create_table()
    insert_default_data()
    
    while True:
        menu()
        choice = int(input("Enter Your Choice: "))
        
        if choice == 1:
            add_student()
        elif choice == 2:
            pass_fail()
        elif choice == 3:
            result = mean_marks()
            print(f"Class's Average Marks: {result}")
        elif choice == 4:
            graph()
        elif choice == 5:
            print("Exiting The Programm !!")
            break
        else:
            print("Invalid Choice!!!")
        
if __name__ == "__main__":
    main()