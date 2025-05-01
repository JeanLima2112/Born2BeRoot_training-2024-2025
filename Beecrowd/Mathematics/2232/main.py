N = int(input())

for c in range(0,N):
    x = int(input())
    total = 0
    for c in range(x, 0,-1):
        total += 2 ** (c-1)
    print(total)
