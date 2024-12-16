P1 , C1 , P2 , C2 = map(int,input().split())
valor = (P1 * C1) - (P2 * C2)

if valor < 0:
    print("1")
elif valor == 0:
    print("0")
elif valor > 0:
    print("-1")