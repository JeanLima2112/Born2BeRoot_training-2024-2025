pessoas,jipes = 0,0

while True:
    try:
        Ind,n = input().split()
        if Ind == "SALIDA":
            jipes += 1
            pessoas += int(n)
        else: 
            pessoas -= int(n)
            jipes -= 1
    except:
        break
print(f"{pessoas}\n{jipes}")