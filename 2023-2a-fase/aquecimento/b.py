tamanho = int(input())
linha = input()

for i in range(0, len(linha) - tamanho):
    trecho = linha[i:i+tamanho]
    if trecho == trecho[::-1]:
        print('S')
        break
else:
    print('N')
