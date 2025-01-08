N, TM = map(int,input().split())
TG = input()

P , M , G = map(int, input().split())

mapa_tamanhos = {'P': P, 'M': M, 'G': G}

paredes = [TM]

for titan in TG:
    tamanho_titan = mapa_tamanhos[titan]
    i = 0
    while True:
        if tamanho_titan <= paredes[i]:
            wall -= tamanho_titan
            if wall < P:
                paredes.pop(wall)
 
print(paredes)
