import modulepro
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
        modulepro.addcntct()
    elif choice == "2":
       modulepro.editcntct()
    elif choice == "3":
       modulepro.searchcntct()
    elif choice == "4":
        modulepro.displaycntcts()
    elif choice == "5":
        modulepro.deletecntct()
    elif choice == "6":
        modulepro.exitprogram()
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")