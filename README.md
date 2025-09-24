
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


Kör igång och testa!
