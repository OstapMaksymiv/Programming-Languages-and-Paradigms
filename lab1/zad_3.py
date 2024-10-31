from functools import reduce
zad = [
    [12, 200],
    [4, 15],
    [50, 400],
    [13, 45]
]

def sortowanie(zadania):
    zadania.sort(key=lambda x: x[0])  
    allTime = 0
    actualTime = 0
    
    for czas, nagroda in zadania:
        actualTime += czas
        allTime += actualTime

    return zadania, allTime

kolejnosc, czas_ocz = sortowanie(zad)
print("Optymalna kolejnosc:", kolejnosc)
print("All time:", czas_ocz)

####

kolejnosc_2 = sorted(zad, key=lambda x: x[0])

time = list(map(lambda x: x[0], kolejnosc_2))
calyCzas = reduce(lambda acc, x: acc + x, [sum(time[:i+1]) for i in range(len(time))])

print("Optymalna kolejnosc:", kolejnosc_2)
print("All time:", calyCzas)