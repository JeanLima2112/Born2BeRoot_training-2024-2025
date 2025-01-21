d_inic = input().split()
valor_inicial = list(map(int, input().split(":")))
d_final = input().split()
valor_termino = list(map(int, input().split(":")))


soma_inicial = (int(d_inic[1]) * 86400)+(valor_inicial[0] * 3600) + (valor_inicial[1]*60)+ (valor_inicial[2])
soma_termino = (int(d_final[1]) * 86400)+(valor_termino[0] * 3600) + (valor_termino[1]*60)+ (valor_termino[2])

total = soma_termino - soma_inicial
dias = total// 86400
horas = (total % 86400) // 3600
minutos =((total % 86400) % 3600) // 60
segundos = (((total % 86400) % 3600) % 60) 

print(f"{dias} dia(s)")
print(f"{horas} hora(s)")
print(f"{minutos} minuto(s)")
print(f"{segundos} segundo(s)")