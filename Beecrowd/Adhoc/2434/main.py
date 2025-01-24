N, S = input().split()
N = int(N)
S = int(S)
low_value = S
for i in range(0, N):
    value= int(input())
    S += value
    if S < low_value:
        low_value = (S)
print(low_value)