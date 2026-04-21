from file_handler import load_file
from analyzer import *

def menu():
    print("\n---Sales Analyzer---")
    print("1. Total Revenue")
    print("2. Best Selling Product")
    print("3. High Sales Orders")
    print("4. Monthly Sales Revenue")
    print("5. Exit")
    
def main():
    data = load_file("data/sales.csv")
    
    while True:
        menu()
        choice = int(input("Enter Your Choice: "))
        
        if choice==1:
            print(f"Total revenue: {total_revenue(data)}")
        elif choice==2:
            product,sales = best_selling_product(data)
            print(f"Best Selling Product is {product} with {sales} units")
        elif choice==3:
            result = high_sales(data)
            print(f"Highest selling products:\n {result}")
        elif choice==4:
            result = month_sale(data)
            for month,revenue in result.items():
                print(f"{month} : {revenue}")
        elif choice==5:
            print("Exiting.....")
            break
        else:
            print("Invalid Choice")

if __name__ == "__main__":
    main()