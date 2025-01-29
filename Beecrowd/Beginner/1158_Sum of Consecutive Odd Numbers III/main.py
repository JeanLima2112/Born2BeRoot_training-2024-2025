N = int(input())

for _  in range(N):
    X, Y = map(int,input().split())
    soma = 0
    if X % 2 == 0:
         for i in range(X+1,X + (2*Y),2):
            soma+= i
    else:
         for i in range(X,X + (2*Y),2):
            soma+= i
    print(soma)