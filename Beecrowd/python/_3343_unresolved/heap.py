import heapq

N, TM = map(int, input().split())
TG = input()
C = list(map(int, input().split()))

tamanho_ord = [C[0] if t == "P" else C[1] if t == "M" else C[2] for t in TG]

paredes = []
heapq.heappush(paredes, -TM)  
for tamanho in tamanho_ord:
    maior_parede = -heapq.heappop(paredes)  
    
    if tamanho <= maior_parede:  
        heapq.heappush(paredes, -(maior_parede - tamanho))
    else:
        heapq.heappush(paredes, -maior_parede)
        heapq.heappush(paredes, -(TM - tamanho))

print(len(paredes))
