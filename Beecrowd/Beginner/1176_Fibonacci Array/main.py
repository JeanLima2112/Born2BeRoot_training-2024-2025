fib = [0,1]

for _ in range(1,60+1):
    fib.append(fib[_]+fib[_-1])

N = int(input())
for _ in range(N):
    X = int(input())
    print(f"Fib({X}) = {fib[X]}")