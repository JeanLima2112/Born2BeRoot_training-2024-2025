grenais = 0
inter = 0
gremio = 0
empate = 0
while True:
    I, G = map(int,input().split())
    grenais += 1
    if I > G:
        inter+=1 
    elif G > I:
        gremio += 1
    else:
        empate +=1


    print("Novo grenal (1-sim 2-nao)")
    esc =int(input())
    if esc == 2:
        break
print(f"{grenais} grenais")
print(f"Inter:{inter}")
print(f"Gremio:{gremio}")
print(f"Empates:{empate}")
if inter > gremio:
    print("Inter venceu mais") 
elif gremio > inter:
    print("Gremio venceu mais")
else:
    print("Nao houve vencedor")