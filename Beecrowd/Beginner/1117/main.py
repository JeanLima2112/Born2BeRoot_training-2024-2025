soma = 0
notas = 0
while True:
    N = float(input())
    if N >= 0 and N <=10:
        notas +=1
        soma+= N
        if notas == 2:
            break
    else:
        print("nota invalida")
print(f"media = {soma/notas:.2f}")