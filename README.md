
# Studentregister – README


## Vad är detta?

studentregister.py är ett program som fungerar som en digital klasslista i terminalen.

Funktioner:
- Lägg till studenter
- Se vilka som finns
- Sök efter en person
- Räkna ut snittåldern
- Ta bort någon
- Avsluta när du är klar


## Hur funkar programmet?

1. Lägger grunden
  - Startar med en tom lista: `students = []`
  - Tänk dig en stor låda med små lappar (namn + ålder)

2. En evig meny
  - `while True:` gör att menyn alltid kommer tillbaka tills du säger stopp

3. Menyn
  - Programmet visar en lista med siffror:
    1. Lägg till student
    2. Lista alla
    3. Sök student
    4. Räkna genomsnittsålder
    5. Ta bort student
    6. Avsluta
  - Skriv en siffra och tryck Enter

4. Vad varje val gör

| Val | Funktion |
|-----|----------|
| 1 | Frågar om namn & ålder, lägger till i listan |
| 2 | Visar alla studenter eller säger att listan är tom |
| 3 | Sök efter namn, visar om studenten finns |
| 4 | Räknar snittålder, säger till om listan är tom |
| 5 | Tar bort student, säger om någon togs bort |
| 6 | Avslutar programmet |

5. Pauser mellan val
  - Efter varje åtgärd: "Tryck Enter för att återgå till menyn..."
  - Du hinner läsa vad som hänt innan menyn visas igen


## Kortfattat
- `students` = lådan med lappar
- `while True` = hjulet som snurrar tills du stoppar det
- Menyval = lägger till, visar, söker, räknar eller tar bort lappar
- Enter-paus = du hinner se resultatet


## Så kör du

1. Spara filen som studentregister.py
2. Öppna terminalen (svart ruta med text)
3. Kör:
  ```bash
  python/python3 studentregister.py
  ```
4. Följ instruktionerna på skärmen

## Reflektion under uppgiftens gång

Det svåraste var att förstå hur while-loopen tillsammans med if/elif/else kan styra programmet så att menyn alltid visas på nytt tills man väljer att avsluta. Nästan allt i koden var nytt för mig. Jag lärde mig hur man skapar en lista (students) som kan innehålla små paket (dictionary) med nycklar som "namn" och "ålder", och hur man med append() kan lägga till fler studenter. Jag använde flera variabler som val för menyvalet, namn och alder för den inmatade informationen, fanns som flagga när man söker, och nya för att skapa en ny lista när någon tas bort.

Jag fick också arbeta med funktioner och metoder som int() för att göra om text till tal, input() för att ta emot data, print() för att visa text, och lower() för att kunna jämföra namn utan att bry sig om stora och små bokstäver. För att räkna snittåldern använde jag både sum() för att addera alla åldrar och len() för att räkna hur många studenter som finns.

En viktig detalj var hur menyn skrivs ut i en enda print med radbrytningar:
print("\n1. Lägg till student\n2. Lista alla studenter\n3. Sök student\n4. Räkna genomsnittsålder\n5. Ta bort student\n6. Avsluta").
Genom att använda \n blir menyn snygg, ren och lätt att läsa, istället för att ha många separata print-rader.

Sammanlagt har jag lärt mig hur man kombinerar loopar, villkor, listor och dictionaries med funktioner som len, sum och lower för att bygga ett helt program som både sparar, visar, söker, räknar och tar bort information på ett tydligt sätt.

"Walk like you just got the best news of your life. Talk like the world is listening. Move like life is designed in your favor. Energy is magnetic. And confidence bends reality. Some will call it arrogance. Others will say you´re naive. But the people who believe good things happen to them? They´re usually right" 
- Said Ebadi