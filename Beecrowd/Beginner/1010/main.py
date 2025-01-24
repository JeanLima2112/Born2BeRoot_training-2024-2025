total = 0
try:
    while True:
        C, Q, P = map(float,input().split())
        total += Q * P

except EOFError:
    print(f"VALOR A PAGAR: R$ {total:.2f}")
    pass