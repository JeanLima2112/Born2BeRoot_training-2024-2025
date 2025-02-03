X = input()


if "-" in X:
    aux = "-"
else:
    aux = "+"

X = float(X)
print(f"{aux}{abs(X):.4E}")