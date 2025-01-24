consumo = [300,1500,600,1000,150]
total = 225
idx = 0
try:
    while True:
        N = int(input())
        total += consumo[idx]* N
        idx += 1
except:
    pass
print(total)