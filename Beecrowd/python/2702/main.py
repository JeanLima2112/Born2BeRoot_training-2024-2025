D = list(map(int, input().split()))
R = list(map(int, input().split()))

falta = 0

for i in range(0,len(D)):
    if D[i] < R[i]:
        falta += R[i] - D[i]
print(falta)