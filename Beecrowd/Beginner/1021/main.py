
notas = [10000, 5000, 2000, 1000, 500, 200]  
moedas = [100, 50, 25, 10, 5, 1]  


N = float(input())  
resto = int(N * 100)  

print("NOTAS:")
for c in notas:
    print(f"{resto // c} no
          ta(s) de R$ {c / 100:.2f}")  
    resto = resto % c 

print("MOEDAS:")
for c in moedas:
    print(f"{resto // c} moeda(s) de R$ {c / 100:.2f}") 
    resto = resto % c
