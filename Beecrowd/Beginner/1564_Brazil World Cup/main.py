try:
    while True:
        X = int(input())
        if X != 0:
            print("vai ter duas!")
        else:
            print("vai ter copa!")
except EOFError:
    pass