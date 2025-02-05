x = ""
idx = 0
soma = 0
while idx != 3:
    x = input()
    if x == 'caw caw':
        print(soma)
        soma = 0
        idx += 1
    else:
        ind = 2
        for _ in x:
            if _ == '*':
                soma += 2**ind
            ind -= 1
    
