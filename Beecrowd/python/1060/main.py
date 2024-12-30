try: 
    cont = 0   
    while True:
        x = float(input())
        if x > 0 :
            cont+=1
except EOFError:
    print(f"{cont} valores positivos")
    pass