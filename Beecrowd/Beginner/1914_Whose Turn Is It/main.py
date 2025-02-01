for _ in range(int(input())):
    n1,e1,n2,e2 = input().split()
    dic = {e1:n1,e2:n2}
    j1,j2 = map(int, input().split())

    result = j1+j2
    if result % 2 == 0:
        print(f"{dic['PAR']}")
    else: 
        print(f"{dic['IMPAR']}")

