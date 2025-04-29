X = int(input())
for _ in range(X):
    N , K = map(int, input().split())
    resto = N % K
    new_bottles = N //K
    print(f"{resto + new_bottles}")
    
