import random

N = random.randint(1,100)

print(N)

words = [
        "AMOR", "PAZ", "FELICIDADE", "VIDA", "FAMILIA", "AMIZADE", "SUCESSO", "SAUDE", "ALEGRIA", "ESPERANCA",
        "FORCA", "CORAGEM", "LIBERDADE", "RESPEITO", "HONESTIDADE", "SOLIDARIEDADE", "GRATIDAO", "CARINHO", "DEDICACAO", "PERSEVERANCA"
    ]
    


for _ in range(N):
    print(random.choice(words))