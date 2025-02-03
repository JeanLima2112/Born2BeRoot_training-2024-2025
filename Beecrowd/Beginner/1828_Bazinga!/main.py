regras = {
    "tesoura": ["papel", "lagarto"],
    "papel": ["pedra", "Spock"],
    "pedra": ["lagarto", "tesoura"],
    "lagarto": ["Spock", "papel"],
    "Spock": ["tesoura", "pedra"]
}

for _ in range(int(input())):
    sheldon, raj = input().split()
    if raj in regras[sheldon]:
        out = "Bazinga!" 
    elif raj == sheldon:
        out = "De novo!" 
    else: 
        out = "Raj trapaceou!"
    print(f"Caso #{_+1}: {out}")