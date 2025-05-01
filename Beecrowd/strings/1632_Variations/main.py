for _ in range(int(input())):
    X = input()
    total = 1
    for i in X:
        if i in "AEIOSaeios":
            total *=3
        else:
            total *=2
    print(f"{total}")

