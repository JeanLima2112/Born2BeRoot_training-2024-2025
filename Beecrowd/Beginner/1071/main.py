X = int(input())
Y = int(input())
soma = 0
for i in range(X-1,Y,-1):
    if i % 2 != 0:
        soma+= i
print(soma)