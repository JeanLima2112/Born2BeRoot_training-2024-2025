patern = ["A","B","C","D","E","*"]
while True:
    N = int(input())
    if N == 0:
        break
    for i in range(0,N):
        op = list(map(int , input().split()))
        under = 0
        for e in range(0,len(op)):
            if op[e] < 128:
                under += 1
                position = e
        
        if under > 1 or under == 0:
            print(patern[5])
    
        else:
            print(patern[position])
        under = 0
        
