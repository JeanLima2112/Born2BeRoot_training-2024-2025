N = int(input())
tipos = {"C": 0, "R": 0, "S":0}
total= 0
for _ in range(N):
    Quant, tipo = input().split()
    Quant = int(Quant)
    total += Quant
    tipos[tipo] += Quant

print(f"Total: {total} cobaias")
print(f"Total de coelhos: {tipos['C']}")
print(f"Total de ratos: {tipos['R']}")
print(f"Total de sapos: {tipos['S']}")
print(f"Percentual de coelhos: {(tipos['C'] * 100) / total:.2f} %")
print(f"Percentual de ratos: {(tipos['R'] * 100) / total:.2f} %")
print(f"Percentual de sapos: {(tipos['S'] * 100) / total:.2f} %")



