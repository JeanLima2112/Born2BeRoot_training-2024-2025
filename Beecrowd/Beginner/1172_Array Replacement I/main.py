ind = 0
try:
    while True:
        X = int(input())
        if X <= 0:
            X = 1
        print(f"X[{ind}] = {X}")
        ind+= 1
except EOFError:
    pass