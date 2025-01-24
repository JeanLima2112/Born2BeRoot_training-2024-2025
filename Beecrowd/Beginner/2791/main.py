cups =  list(map(int, input().split()))

for i in range(0,4):
    if cups[i] == 1:
        print(i+1)
        break