#contactbook

def addcntct():
    name = input("Enter name: ")
    mblno = input("Enter mobile number: ")
    contacts[name] = mblno
    print("Contact added successfully.")

def editcntct():
    name = input("Enter name of contact to edit: ")
    if name in contacts:
        mblno = input("Enter new mobile number: ")
        contacts[name] = mblno
        print("Contact updated successfully.")
    else:
        print("Contact not found.")

def searchcntct():
    name = input("Enter name of contact to search: ")
    if name in contacts:
        print(name + " - " + contacts[name])
    else:
        print("Contact not found.")

def displaycntcts():
    if contacts:
        for name, mblno in contacts.items():
            print(name + " - " + mblno)
    else:
        print("No contacts found.")

def  deletecntct():
    name = input("Enter name of contact to delete: ")
    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully.")
    else:
        print("Contact not found.")

def exitprogram():
    print("Exiting program...")
    exit()

contacts = {}

while True:
    print("Enter your choices:")
    print("1. Add")
    print("2. Edit")
    print("3. Search")
    print("4. Display")
    print("5. Delete")
    print("6. Exit")

    choice = input()

    if choice == "1":
        addcntct()
    elif choice == "2":
       editcntct()
    elif choice == "3":
        searchcntct()
    elif choice == "4":
        displaycntcts()
    elif choice == "5":
        deletecntct()
    elif choice == "6":
        exitprogram()
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")















