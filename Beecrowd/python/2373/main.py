N = int(input())
caiu = 0
for i in range(0,N):
    L , C = map(int,input().split())
    if L > C:
        caiu += C
print(caiu)