students = []

while True: 

    print("\n1. Lägg till student\n2. Lista alla studenter\n3. Sök student\n4. Räkna genomsnittsålder\n5. Ta bort student\n6. Avsluta")
    val = input("Välj: ")

    if val == "1":
        namn = input("Namn: ")
        try:
            alder = int(input("Ålder: "))
        except:
            print("Åldern måste vara en siffra.")
            input("Tryck Enter för att återgå till menyn...")
            continue
        students.append({"namn": namn, "ålder": alder})
        print(f"{namn} lades till.")
        input("Tryck Enter för att återgå till menyn...")

    elif val == "2":
        if students:
            print("\nAlla studenter:")
            for s in students:
                print(s["namn"], s["ålder"])
        else:
            print("Inga studenter registrerade.")
        input("Tryck Enter för att återgå till menyn...")

    elif val == "3":
        n = input("Ange namn: ")
        fanns = False
        for s in students:
            if s["namn"].lower() == n.lower():
                print("Hittad:", s["namn"], s["ålder"])
                fanns = True
        if not fanns:
            print("Studenten finns inte.")
        input("Tryck Enter för att återgå till menyn...")

    elif val == "4":
        if students:
            print("Genomsnittsålder:", sum(s["ålder"] for s in students)/len(students))
        else:
            print("Inga studenter registrerade.")
        input("Tryck Enter för att återgå till menyn...")

    elif val == "5":
        n = input("Namn att ta bort: ")
        nya = [s for s in students if s["namn"].lower() != n.lower()]
        if len(nya) < len(students):
            students = nya
            print(n, "har tagits bort.")
        else:
            print("Studenten fanns inte.")
        input("Tryck Enter för att återgå till menyn...")

    elif val == "6":
        print("Avslutar.")
        break

    else:
        print("Ogiltigt val.")
        input("Tryck Enter för att återgå till menyn...")
