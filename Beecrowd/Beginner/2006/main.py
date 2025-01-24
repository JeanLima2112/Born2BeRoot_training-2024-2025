T = int(input())
res = input()
acerto = 0

for c in res.split(" "):
    if str(T) == c: 
        acerto += 1
print(acerto)
    