import random 

X = 100

for i in range (X):
    for _ in range(random.randint(0,10**5)):
        print(f"{random.choice(["A","T","G","C"])}",end="")
    print()
