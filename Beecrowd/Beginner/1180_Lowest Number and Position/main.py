X = int(input())
lista = list(map(int,input().split()))
menor = lista[0]
pos = 0
for _ in range(X):
    if lista[_] < menor:
        pos = _
        menor = lista[_]
print(f"Menor valor: {menor}")
print(f"Posicao: {pos}")