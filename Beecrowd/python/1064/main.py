soma = 0
qtn = 0
try:
    while True:
        x = float(input())
        if x > 0:
            soma += x
            qtn +=1
except:
    pass
print(f"{qtn} valores positivos")
print(f"{soma/qtn:.1f}")