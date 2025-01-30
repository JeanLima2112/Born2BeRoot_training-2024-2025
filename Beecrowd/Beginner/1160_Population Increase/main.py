from math import floor
N = int(input())

for _ in range(N):
    X = list(map(float, input().split()))   
    X[2] = (X[2]/100) +1      
    X[3] = (X[3]/100) +1   
    anos = 0 
    while X[0] <= X[1]:
        X[0] = floor(X[0]*X[2])
        X[1] = floor(X[1]*X[3])
        anos += 1
        if anos > 100:
            break
    if anos > 100:
        print("Mais de 1 seculo.")
    else:
        print(f"{anos} anos.")

