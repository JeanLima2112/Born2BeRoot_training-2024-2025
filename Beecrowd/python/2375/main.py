D = int(input())
X = list(map(int, input().split()))
for c in X:
    if c < D:
        print("N")
        exit()
print("S")