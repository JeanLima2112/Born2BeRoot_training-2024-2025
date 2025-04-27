X = int(input())
patern = list(map(int, input().split()))
for _ in range(int(input())):
    regiao = list(map(str,input().split()))
    menor = int(regiao[1]) // patern[0]
    for _ in range(1,X):
        Y = int(regiao[_+1]) // patern[_]
        if Y < menor:
            menor = Y
    print(f"{regiao[0]} {menor}")



        




