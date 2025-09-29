# Student Registration system

# NEEDS
# Datastruktur för studenter
# Loop för menyn
# Menyn har 3 val: 1. Add student, 2. List students, 3. Quit

student_list = []

max_no_students_to_print = 10

print("Welcome to the Student Registration System!")
while True:
    print("\nMenu:")
    print("1. Add Student")
    print("2. List Students")
    print("3. Quit program")

    menu_choice = input("Choose an option (1-3): ") 
    if menu_choice == "1":
        new_student_name = input("Enter student name: ")
        new_student_age = input("Enter student age: ")
        new_student_dict = {"name": new_student_name, "age": new_student_age}
        student_list.append(new_student_dict)
        print(f"Student {new_student_name} added.")
        input("Press Enter to return to menu...")
    elif menu_choice == "2":
        if student_list:
            print("\nAlla studenter:")
            for s in student_list:
                print(s["name"], s["age"])
        else:
            print("No students registered.")
        input("Press Enter to return to menu...")


        input("Press Enter to return to menu...")
    elif menu_choice == "3":
        print("Exiting program.")
        break
