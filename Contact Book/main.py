contact = {}

def add_contact():
    name = input("Enter the name: ")
    number = int(input("Enter the number: "))
    
    if name in contact:
        print("Name is already exist in the contact!")
    else:
        contact[name] = number
        print("Number is added in contact list ✅")

def view_contact():
    if not contact:
        print("This number does not exist!")
    else:
        for name,number in contact.items():
            print(f"{name}: {number}")

def search_contact():
    name = input("Enter the name: ")
    
    if name in contact:
        print(f"{name}: {contact[name]}")
    else:
        print("This number does not exist!")

def delete_contact():
    name = input("Enter the name: ")
    
    if name in contact:
        del contact[name]
        print("Deleted Successfully !")
    else:
        print("Contact not found!")

def update_contact():
    name = input("Enter the name: ")
    
    if name in contact:
        number = int(input("Enter new number: "))
        contact[name] = number
    else:
        print("Contact not found!")
    
while True:
    print("1. Add Contact")
    print("2. View Contact")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Update Contact")
    print("6. View All Contacts")
    print("7. Exit")
    
    choice = int(input("Selecte the option: "))
    
    if choice==1:
        add_contact()
    elif choice==2:
        view_contact()
    elif choice==3:
        search_contact()
    elif choice==4:
        delete_contact()
    elif choice==5:
        update_contact()
    elif choice==6:
        print(contact.items())
    elif choice==7:
        print("Exit Successfully ")
        break
    else:
        print("Invalid choice !!")
