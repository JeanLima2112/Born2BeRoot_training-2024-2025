try: 
    while True:
        x = int(input())
        lista = list(map(int,input().split()))
        max_speed = max(lista)
        if max_speed < 10:
            print(1)
        elif max_speed < 20:
            print(2)
        else:
            print(3)

except EOFError:
    pass