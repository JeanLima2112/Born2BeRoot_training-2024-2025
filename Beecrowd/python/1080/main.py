ind = 1
maior = 0
try:
    while True:
        aux = int(input())
        if aux > maior:
            maior = aux
            idx = ind
        ind +=1
except EOFError:
    pass
print(maior)
print(idx)