patern = {2000.01:1.04, 1200.01: 1.07, 800.01: 1.10, 400.01: 1.12, 0: 1.15}

S = float(input())

for i in patern:
    if S >= i:
        S = S * patern[i]
        break
print(f"Novo salario: {S:.2f}\nReajuste ganho: {S - S/patern[i]:.2f}\nEm percentual: {patern[i]*100-100:.0f} %")