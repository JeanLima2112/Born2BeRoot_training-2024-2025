par = 0
impar = 0
pos = 0
neg = 0
try: 
  
    while True:
        x = float(input())
        if x % 2 == 0 :
            par+=1
        else:
            impar+=1
        if x > 0:
            pos += 1
        elif x != 0 : neg = 1
except EOFError:
    print(f"{par} valor(es) par(es)")
    print(f"{impar} valor(es) impar(es)")
    print(f"{pos} valor(es) positivo(s)")
    print(f"{neg} valor(es) negativo(s)")
    pass

