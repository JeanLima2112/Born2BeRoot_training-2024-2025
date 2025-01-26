N = list(map(int, input().split()))
A = N[0]
for _ in range(1, len(N)):
    if N[_] > 0:
        B = N[_]
total = 0
for _ in range(0,B):
    total += A + _
print(total)