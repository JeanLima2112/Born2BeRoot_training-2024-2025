N = int(input())
lista = []
lista.append(int(input())) 
lista.append(int(input())) 

lista.append(N - lista[0] - lista[1])

lista.sort(reverse=True)
print(lista[0])