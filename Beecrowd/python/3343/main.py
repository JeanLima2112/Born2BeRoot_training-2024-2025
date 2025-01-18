N, TM = map(int,input().split())
TG = input().strip()
C = list(map(int, input().split()))
mudou = False
paredes = []
dicionario = {"P": [0, C[0]],
            "M": [0, C[1]],
            "G":[0,C[2]]}

for titan in TG:  
    mudou = False
    i = dicionario[titan][0]

    if i >= len(paredes):
        paredes.append(TM)

    for c in range (i,len(paredes)):
        if paredes[c] >= dicionario[titan][1]:
            paredes[c] -= dicionario[titan][1]
            mudou = True
            dicionario[titan][0] = c
            break
    if mudou != True:
        paredes.append(TM - dicionario[titan][1])
        dicionario[titan][0] = c+1


print(len(paredes))




    

     
   