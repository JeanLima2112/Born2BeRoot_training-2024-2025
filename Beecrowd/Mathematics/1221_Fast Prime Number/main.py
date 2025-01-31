N = int(input())

for _ in range(N):
    X = int(input())
    primo = True
    for i in range(2, int(X ** 0.5)+1):
        if X % i==0:
            primo = False
            break
    if primo == True:
        print("Prime")
    else:
        print("Not Prime")
