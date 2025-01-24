n_por_linha, ate = map(int, input().split())
for i in range (1,ate+1,n_por_linha):
    for c in range(i,i +n_por_linha -1):
        print(c, end=' ')
    print(i + n_por_linha  - 1)

