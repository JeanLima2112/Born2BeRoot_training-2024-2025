par = []
impar = []

try:

    while True:
        X = int(input())
        if X % 2==0:
            par.append(X)
        else:
            impar.append(X)
        if len(impar)==5:
            for _ in range(0,len(impar)):
                print(f"impar[{_}] = {impar[_]}")
            impar = []
        if len(par)==5:
            for _ in range(0,len(par)):
                print(f"par[{_}] = {par[_]}")
            par = []
except:
    for _ in range(0,len(impar)):
        print(f"impar[{_}] = {impar[_]}")
    for _ in range(0,len(par)):
        print(f"par[{_}] = {par[_]}")