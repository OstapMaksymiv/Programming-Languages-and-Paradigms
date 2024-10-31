lista = [
    [12, 400],
    [1, 3],
    [75, 90],
    [14, 96]
]
plecak = 40
def alg_plecaka_dp(lista, max_waga):
    n = len(lista)
    dp = [[0 for _ in range(max_waga + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        waga, wartosc = lista[i - 1]
        for j in range(max_waga + 1):
            if waga <= j:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - waga] + wartosc)
            else:
                dp[i][j] = dp[i - 1][j]
    maks_wartosc = dp[n][max_waga]
    wybrane_przedmioty = []
    waga = max_waga
    for i in range(n, 0, -1):
        if dp[i][waga] != dp[i - 1][waga]:
            wybrane_przedmioty.append(lista[i - 1])
            waga -= lista[i - 1][0]

    return maks_wartosc, wybrane_przedmioty

maks_wartosc, wybrane_przedmioty = alg_plecaka_dp(lista, plecak)
print("Max wartosc:", maks_wartosc)
print("Wybrane przedmioty:", wybrane_przedmioty)