data = [3600,60]
N = int(input())
resto = N

for c in data:
    print(f"{resto//c}:",end='') 
    resto = resto % c
print(resto)
