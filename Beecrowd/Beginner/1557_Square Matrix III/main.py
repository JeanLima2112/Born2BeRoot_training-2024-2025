while True:
    inic = 1
    X = int(input())
    ind = 2 ** ((X-1) * 2)
    prefix = len(str(ind))
    if X == 0:
        break
    for _ in range(0,X):
        aux = inic
        for i in range(1,X):
            print(f"{aux:>{prefix}}",end=" ")
            aux *= 2
        inic *= 2
        print(f"{aux:>{prefix}}")
    print()
