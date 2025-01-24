N = int(input())

for _ in range(N):
    A, B = map(int, input().split())
    try:
         print(A/B)
    except:
         print("divisao impossivel")