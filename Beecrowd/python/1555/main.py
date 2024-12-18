partern = ['Beto ganhou', 'Carlos ganhou', 'Rafael ganhou']
N = int(input())

for c in range(0,N):
    x = list(map(int,input().split()))
    rafael = ((3*x[0])**2) + (x[1]**2)
    beto = (2*(x[0]**2)) + ((5*x[1])**2)
    Carlos = (-100 * x[0]) + (x[1]**3)
    if rafael > beto and rafael > Carlos:
        print(partern[2])
    elif beto > rafael and beto > Carlos:
        print(partern[0])
    else:
        print(partern[1])


