C = int(input())
operacao = input()
matriz = []
soma = 0
for i in range(12):
    for j in range(12):
        x = float(input())
        if j == C:
            soma += x        
if operacao == "S":
    print(f"{soma:.2f}")
else: 
    print(f"{soma/12:.1f}")
