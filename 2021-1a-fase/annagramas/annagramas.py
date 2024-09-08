# Execute com `python h.py < in.txt > out.txt && diff expected.txt out.txt`

casos = int(input())

for i in range(casos):
    frase = input()
    anagrama = input()
    anagrama = sorted(anagrama)
    anagramaLen = len(anagrama)

    if anagramaLen > len(frase):
        print('ERRO')
    else:
        anagramas = 0
        for i in range(0, len(frase) - anagramaLen + 1):
            if sorted(frase[i:i + anagramaLen]) == anagrama:
                anagramas += 1
        print(anagramas)
