C , P, F = map(int,input().split())
sf = P / F

if C > sf:
    print("N")
elif C < sf:
    print("S")
else: print('S')