X = int(input())
enter = 0 
out = 0
for c in range(0,X):
    N = int(input())
    if N >= 10 and N <= 20:
        enter += 1
    else: out+= 1
print(f"{enter} in")
print(f"{out} out")