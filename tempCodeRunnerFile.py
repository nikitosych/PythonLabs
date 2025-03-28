import sil

ntn = lambda n, k: sil.silnia(n) / (sil.silnia(k) * sil.silnia(n - k))

n = int(input("Podaj n: "))
k = int(input("Podaj k: "))

print(ntn(n, k))