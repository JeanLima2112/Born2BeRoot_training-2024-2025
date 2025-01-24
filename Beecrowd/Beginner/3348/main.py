from math import gcd
N=int(input())
result = 1
for i in range (N+1, (N*2)+1):
     result = (result * i) // gcd(result, i)
print(result)