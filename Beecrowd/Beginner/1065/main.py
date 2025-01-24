try: 
    cont = 0   
    while True:
        x = float(input())
        if x % 2 == 0 :
            cont+=1
except EOFError:
    print(f"{cont} valores pares")
    pass