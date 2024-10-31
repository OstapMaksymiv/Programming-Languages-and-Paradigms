def podziel(wagi, max_waga):
    for waga in wagi:
        if waga > max_waga:
            raise ValueError(f"Paczka o wadze {waga} przekracza dozwolona wage kursu {max_waga} kg.")

    wagi_sorted = sorted(wagi, reverse= True)
    kursy = []
    for waga in wagi_sorted:
        dodana = False
        for kurs in kursy:
            if sum(kurs) + waga <= max_waga:
                kurs.append(waga)
                dodana= True
                break
        if not dodana:
            kursy.append(([waga]))
    return len(kursy), kursy
wagi = [10,15,25,8,5,7]
max_waga = 25
liczba_kursuw, kursy = podziel(wagi , max_waga)
print(f'LIczba kursuw {liczba_kursuw}')
for i, kurs in enumerate (kursy, 1):
    print(f'Kurs {i}: {kurs} - suma wag: {sum(kurs)} kg')