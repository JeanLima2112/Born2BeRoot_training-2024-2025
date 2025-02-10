X, Y = map(int, input().split())
lista =[]
contador = {i: 0 for i in range(30, 201)}
a_ser_achado = 200 - X
for _ in range (Y):
    aux = int(input())
    if aux < a_ser_achado -1:
        if contador[aux]< 3:
            lista.append(aux)
            contador[aux] +=1

lista.sort()
print(lista)
Y = len(lista)


for i in range(Y-2):
    left = i + 1
    right = Y - 1
    while left < right:
        soma = lista[i] + lista[left] + lista[right]
        if soma == a_ser_achado:
            print("fretegratis")
            exit()
        elif soma < a_ser_achado:
            left += 1
        else:
            right -= 1
print("fretepago")
