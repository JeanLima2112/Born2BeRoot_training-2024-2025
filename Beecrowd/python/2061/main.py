N , M = map(int, input().split())

for i in range(0, M):
    action = input()
    if action == "fechou":
        N += 1
    else: 
        N -= 1
print(N)