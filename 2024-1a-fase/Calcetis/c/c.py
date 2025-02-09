X, Y = map(int, input().split())
lista =[]
contador = {}
a_ser_achado = 200 - X
for _ in range (Y):
    aux = int(input())
    if aux < a_ser_achado:
        if contador.get(aux ,0):
            lista.append(aux)
            contador[aux] = contador.get(aux, 0) + 1

lista.sort()
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


