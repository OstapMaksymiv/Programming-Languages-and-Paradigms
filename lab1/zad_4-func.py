lista = [
    (12, 400),
    (1, 3),
    (75, 90),
    (14, 96)
]
plecak = 40
def alg_plecaka_func(i, max_waga):
    if i == len(lista) or max_waga == 0:
        return 0, []
    waga, wartosc = lista[i]
    wartosc_bez, przedmioty_bez = alg_plecaka_func(i + 1, max_waga)
    wartosc_z = przedmioty_z = 0, []
    if waga <= max_waga:
        wartosc_z, przedmioty_z = alg_plecaka_func(i + 1, max_waga - waga)
        wartosc_z += wartosc
        przedmioty_z = przedmioty_z + [lista[i]]
    if wartosc_bez > wartosc_z:
        return wartosc_bez, przedmioty_bez
    else:
        return wartosc_z, przedmioty_z

maks_wartosc, wybrane_przedmioty = alg_plecaka_func(0, plecak)
print("Maksymalna wartość (funkcyjnie):", maks_wartosc)
print("Wybrane przedmioty (funkcyjnie):", wybrane_przedmioty)