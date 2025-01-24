tops = [(25.0,"Intervalo [0,25]"), (50.0,"Intervalo (25,50]"), (75.0,"Intervalo (50,75]"), (100.0,"Intervalo (75,100]")]
N = float(input())

if N < 0 or N > 100:
    print("Fora de intervalo")
    exit()
for c, text in tops:
    if N <= c:
        print(text)
        break