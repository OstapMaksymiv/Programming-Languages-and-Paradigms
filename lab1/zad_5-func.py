from functools import reduce
def wybierz_zadania_funkcyjnie(zadania):
    zadania_posortowane = sorted(zadania, key=lambda x: x[1])
    def wybierz(zadania, zadanie):
        czas_startu, czas_zakonczenia, nagroda = zadanie
        ostatnie_zadanie = zadania[-1] if zadania else (0, 0, 0)
        if czas_startu >= ostatnie_zadanie[1]:
            return zadania + [zadanie]
        return zadania

    wybrane_zadania = reduce(wybierz, zadania_posortowane, [])
    return wybrane_zadania
zadania = [
    (1, 3, 50),
    (2, 5, 20),
    (3, 6, 30),
    (5, 8, 40),
    (6, 9, 70)
]
wynik_funkcyjny = wybierz_zadania_funkcyjnie(zadania)
print("Wybrane zadania (funkcyjnie):", wynik_funkcyjny)
