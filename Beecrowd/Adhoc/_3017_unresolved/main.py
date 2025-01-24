import math
MOD = (10 **9) * 7
S, B = map(int, input().split())
resto = B - S
possibilidades = math.factorial(S + resto - 1) // (math.factorial(resto) * math.factorial(S - 1))
data = []
possibilidades = possibilidades % MOD 
print(possibilidades)
