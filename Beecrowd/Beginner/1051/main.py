patern = [4500.00, 3000.00, 2000.00]
taxas = [0.28,0.18,0.08]
segmentos = [0,0,0]
S = float(input())
if S <= 2000.00:
    print("Isento")
else:
    for i in range(0,3):
        segmentos[i] +=  S - patern[i]
        if segmentos[i] > 0:
            S -= segmentos[i] 
    valor = 0   
    for c in range(0,3):
        if segmentos[c] > 0:
            valor += segmentos[c] * taxas[c]
    print(f"R$ {valor:.2f}")