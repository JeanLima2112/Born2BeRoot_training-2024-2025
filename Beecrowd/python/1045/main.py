valores  = list(map(float, input().split()))
valores.sort(reverse=True)
A,B,C = valores 

if A >= B + C:
    print("NAO FORMA TRIANGULO")
else:
    if (A**2) == (B**2) + (C**2):
        print("TRIANGULO RETANGULO")
    if (A**2) > (B**2) + (C**2):
        print("TRIANGULO OBTUSANGULO")
    if (A**2) < (B**2) + (C**2):
        print("TRIANGULO ACUTANGULO")
    if A == B == C:
        print("TRIANGULO EQUILATERO")
    if A == B and B!=C or A == C and A!=B or B == C and B!=A:
        print("TRIANGULO ISOSCELES")