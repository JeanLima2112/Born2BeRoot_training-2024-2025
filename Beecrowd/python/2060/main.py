N = int(input())
lista = list(map(int,input().split()))
_2 = 0
_3 = 0
_4 = 0
_5 = 0

for i in range(0, N):
    x = lista[i]
    if x % 2 == 0:
        _2 += 1
    if x % 3 == 0:
        _3 += 1
    if x % 4 == 0:
        _4 += 1
    if x % 5 == 0:
        _5 += 1

print(f"{_2} Multiplo(s) de 2")
print(f"{_3} Multiplo(s) de 3")
print(f"{_4} Multiplo(s) de 4")
print(f"{_5} Multiplo(s) de 5")
    