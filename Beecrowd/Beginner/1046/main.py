data = list(map(int, input().split()))

hora_inicio = data[0]  
hora_final = data[1]

if hora_final < hora_inicio:
    hora_final += 24 
    
horas = (hora_final - hora_inicio)
if horas == 0:
    horas = 24
print (f"O JOGO DUROU {horas} HORA(S)")