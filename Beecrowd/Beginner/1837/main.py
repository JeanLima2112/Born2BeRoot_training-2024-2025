X,Y = input().split(" ")

X = int(X)
Y = int(Y)

quociente, resto = divmod(X,abs(Y))
if Y < 0:
    quociente *= -1
print(quociente,resto)