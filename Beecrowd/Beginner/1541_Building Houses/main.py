#Solution in Python
from math import floor
while True:
    X = list(map(int, input().split()))
    if X[0] == 0:
        break
    print(floor(((((X[0]* X[1])* 100))/X[2])**0.5))

        
