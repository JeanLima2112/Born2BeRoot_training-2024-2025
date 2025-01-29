while True:
    soma = 0
    X = int(input())
    if X == 0:
        break
    for _ in range(X,X+10):
        if _ % 2 == 0:
            soma += _
    print(soma)