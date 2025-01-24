soma = 0
notas = 0
while True:
    N = float(input())
    if N >= 0 and N <=10:
        notas +=1
        soma+= N
        if notas == 2:
            print(f"media = {soma/notas:.2f}")
            while True:
                print("novo calculo (1-sim 2-nao)")
                esc = int(input())
                if esc == 2:
                    exit()
                if esc == 1:
                    soma = 0 
                    notas = 0
                    break


    else:
        print("nota invalida")
