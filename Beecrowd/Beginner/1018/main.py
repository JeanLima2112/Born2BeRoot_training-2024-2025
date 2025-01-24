notas = [100,50,20,10,5,2,1]
N = int(input())
resto = N
print(N)
for c in notas:
    print(f"{resto//c} nota(s) de R$ {c},00") 
    resto = resto % c
