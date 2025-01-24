N = int(input())
for c in range(N):
    X = list(map(int,input().split())) 
    soma = 0
    X.sort()
    for _ in range(X[0]+1,X[1]):
        if _ % 2 != 0:
            soma+=_
    print(soma)
