import random

X = 50
Y = 100000
lista = [random.randint(30, 200) for _ in range(Y)]


print(X, Y)
for num in lista:
    print(num)