students = []

while True:
    print("\n1. Add student\n2. List students\n3. Find student\n4. Calculate average age\n5. Remove student\n6. Exit")
    option = input("Choose: ")

    if option == "1":
        name = input("Name: ")
        try:
            age = int(input("Age: "))
        except:
            print("Age must be a number.")
            input("Press Enter to return to Menu...")
        
    elif option == "2":
        if students:
            print("\nAll students:")
            for s in students:
                print(s["name"], s["age"])
    
        else:
            print("No students registered")
        input("Press Enter to return to menu...")

    elif option == "3":
        n = input("Submit name: ")
        registered = False
        for s in students:
            if s["name"].lower() == n.lower():
                print("Found:", s["name"], s["age"])
                registered = True
        if not registered:
            print("Student not found.")
        input("Press Enter to return to menu...")
    
    elif option == "4":
        if students:
            print