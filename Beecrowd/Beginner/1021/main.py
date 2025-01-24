from decimal import Decimal, getcontext


getcontext().prec = 6

notas = [100, 50, 20, 10, 5, 2]
moedas = [Decimal('1.00'), Decimal('0.50'), Decimal('0.25'), Decimal('0.10'), Decimal('0.05'), Decimal('0.01')]
N = float(input())  
resto = Decimal(N) 

print("NOTAS:")
for c in notas:
    print(f"{resto // c:.0f} nota(s) de R$ {c:.2f}")  
    resto = resto % c 
print("MOEDAS:")

for c in moedas:
    print(f"{resto // c:.0f} moeda(s) de R${c: .2f}") 
    resto = resto % c 
