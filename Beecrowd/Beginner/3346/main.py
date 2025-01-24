P1, P2 = map(float,input().split())

P1 = 1 + (P1 / 100)  
P2 = 1 + (P2 / 100)  

result = ((P1 * P2) - 1)* 100
print(f"{result:.6f}")