total = 0
n = 0
while True:
    X = int(input())
    if X <= 0:
        break
    total += X
    n+=1
print(f"{total/n:.2f}")