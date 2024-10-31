def zadania_zachlanny(zadania):
    zadania.sort(key=lambda x: x[1]) 
    wybrane_zadania = []
    ostatnie_zakonczone = 0
    for zadanie in zadania:
        czas_startu, czas_zakonczenia, nagroda = zadanie
        if czas_startu >= ostatnie_zakonczone:
            wybrane_zadania.append(zadanie)
            ostatnie_zakonczone = czas_zakonczenia
    return wybrane_zadania
zadania = [
    (1, 3, 50),
    (2, 5, 20),
    (3, 6, 30),
    (5, 8, 40),
    (6, 9, 70)
]
wynik = zadania_zachlanny(zadania)
print("Wybrane zadania (proceduralnie):", wynik)
