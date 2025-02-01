def verifica_3 (a,b,c):
    if a < b+c and b < a+c and c < b+a:
        print("S")
        exit()
   

X = list(map(int,input().split()))
verifica_3(X[0],X[1],X[2])
verifica_3(X[0],X[1],X[3])
verifica_3(X[3],X[2],X[1])
verifica_3(X[3],X[2],X[0])
print('N')