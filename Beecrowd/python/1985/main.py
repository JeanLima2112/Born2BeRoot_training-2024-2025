cardapio = {
    "1001": 1.50,
    "1002": 2.50,
    "1003": 3.50,
    "1004": 4.50,
    "1005": 5.50
}
I = int(input())
total = 0.0
for c in range(0,I):
    C, Q = input().split()
    total += cardapio[f"{C}"] * int(Q)
print(f"{total:.2f}")

