X = []
for _ in range(20):
    X.append(int(input()))
idx = 0
for _ in range(len(X)-1,-1,-1):
    print(f"N[{idx}] = {X[_]}")
    idx += 1