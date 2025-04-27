import random

Q = random.randint(0,15)
V = random.randint(0,50)
print(Q)
for _ in range(Q):
    print(random.randint(0,30), end=" ")
print()
print(V)
for i in range(V):
    print("ABRET", end=" ")    
    for _ in range(Q):
        print(random.randint(0,300),end=" ")
    print()


