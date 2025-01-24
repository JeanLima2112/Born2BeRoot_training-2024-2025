I = int(input())
valor = 0 
for c in range(0, I):
    T,V = input().split(" ")
    valor += (int(T) * int(V))
print(valor)
