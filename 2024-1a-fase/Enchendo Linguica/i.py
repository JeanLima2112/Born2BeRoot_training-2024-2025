X = []
for _ in range(int(input())):
    X.append(int(input()))

menor = True
maior = True
for i in range(1, len(X)):
    if X[i] > X[0]:
        menor = False
    elif X[i] < X[0]:
        maior = False
if menor == False and maior == False:
    print("0")
elif menor == False:
    print("1")
else:
    print("2")


    



    

