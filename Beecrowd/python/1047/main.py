data = input().split()

hora_inicio = (int(data[0]) * 60) + int(data[1]) 
hora_final = (int(data[2]) * 60) + int(data[3]) 

if hora_final < hora_inicio:
    hora_final += 24 * 60
    
horas = (hora_final - hora_inicio) // 60
minutos = (hora_final - hora_inicio) % 60
if horas == 0 and minutos == 0:
    horas = 24
print (f"O JOGO DUROU {horas} HORA(S) E {minutos} MINUTO(S)")