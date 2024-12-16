N, TM = map(int,input().split())
TG = input()
C = list(map(int, input().split()))

paredes = [TM]
tamanho_ord = []

tamanho_ord = [C[0] if t == "P" else C[1] if t == "M" else C[2] for t in TG]

i = 0  
j = 0
while True:
    if tamanho_ord[j] > paredes[i] and len(paredes) <= i+1:
        paredes.append(TM)
        i +=1
    elif tamanho_ord[j] > paredes[i]:
        i +=1
    elif tamanho_ord[j] <= paredes[i]:
        paredes[i]-= tamanho_ord[j]
        j+=1
        i = 0
    if j  == N: break
        
print(len(paredes))

