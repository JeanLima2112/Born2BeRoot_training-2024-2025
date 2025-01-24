N = []
for _ in range(2):
    N.append(int(input()))
N.sort()
X = N[0]
Y = N[1]
soma = 0
for _ in range(X, Y + 1):
    if _ % 13 != 0:
        soma += _
print(soma) 