# Execute com `python e.py < in.txt > out.txt && diff expected.txt out.txt`

estacionamento = {}

try:
    while True:
        placa = input()
        somaPlaca = 0

        for ch in placa:
            if ch.isdigit():
                somaPlaca += int(ch) # converte digito em inteiro
            else:
                somaPlaca += ord(ch) # retorna valor unicode do caractere

        # Observação: Fórmula no caderno de questões está errada
        vaga = (somaPlaca % 15 + 10) % 15
        if vaga == 0:
            vaga = 15

        # Tenta obter a vaga, e caso não tenha, retorna False
        if not estacionamento.get(vaga, False):
            # Caso tenha sido retornado False (não tem bike estacionada na vaga), guarda a placa
            estacionamento[vaga] = placa

except EOFError:
    vagasEstacionamento = estacionamento.keys()
    vagasEstacionamento = sorted(vagasEstacionamento)

    for vaga in vagasEstacionamento:
        print(vaga, estacionamento[vaga])
