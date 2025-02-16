import random

N = random.randint(3, 5)


print(N)
for _ in range(N):
   for i in range(6):
    for i in range(2):
        print(random.randint(0, 1), end=' ')
    print(random.randint(0, 1))