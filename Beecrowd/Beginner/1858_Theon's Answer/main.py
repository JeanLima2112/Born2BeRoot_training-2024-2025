n = int(input())  
valores = list(map(int, input().split()))
menor_posicao = valores.index(min(valores)) 
print(menor_posicao+1)