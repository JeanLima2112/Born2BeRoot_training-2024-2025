cont = 1
try:
    while True:
        N = int(input())
        if N == 0:
            break
        print(f"Teste {cont}")
        entradas = list(map(int, input().split()))
        for i in range(0, len(entradas)):
            if entradas[i] == i+1:
                print (i+1)
                cont += 1
                print()
                break

except:
    pass