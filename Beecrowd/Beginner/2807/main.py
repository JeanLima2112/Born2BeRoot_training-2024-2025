N = int(input())
lista = [1,1]
if N == 1:
     print(lista[-1])
else:
    for c in range(2,N):
        lista.append(lista[c-1]+lista[c-2])
    lista.sort(reverse=True)
    for _ in range(0,len(lista)-1):
        print(lista[_],end=' ')
    print(lista[-1])