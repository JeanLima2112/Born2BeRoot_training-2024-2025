N = int(input())

matriz = []
analisando = []
escreva = ""
for _ in range(N+1):
    linha = list(map(int, input().split()))
    matriz.append(linha)

for i in range(N):
  
    for j in range(N):
        analisando.append(matriz[i][j])
        analisando.append(matriz[i+1][j])
        analisando.append(matriz[i][j+1])
        analisando.append(matriz[i+1][j+1])
        analisando.sort()
        if analisando[2]== 1:
            escreva+= "S"
        else: escreva+="U"
        analisando = []
    print(escreva)
    escreva = ""