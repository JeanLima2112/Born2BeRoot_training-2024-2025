patern = {1:[0,'Alcool'], 2:[0,'Gasolina'],3:[0,"Disel"]}

while True:
    N = int(input())
    if N == 4 :
        break
    if N in patern:
        patern[N][0] += 1
print("MUITO OBRIGADO")
print(f"Alcool: {patern[1][0]}")
print(f"Gasolina: {patern[2][0]}")
print(f"Diesel: {patern[3][0]}")
