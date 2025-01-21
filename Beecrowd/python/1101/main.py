while True:
    soma = 0
    N = list(map(int,input().split()))
    N.sort()
    if N[0] <= 0:
        break
    for _ in range(N[0],N[1]+1):
        soma += _
        print(_,end=' ')
    print(f"Sum={soma}")