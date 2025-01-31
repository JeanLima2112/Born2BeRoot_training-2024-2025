lista = []
X = int(input())
while len(lista) < 1000:
    for _ in range(X):
        lista.append(_)
for _ in range(1000):
    print(f"N[{_}] = {lista[_]}")