N = int(input())
LA,LB = map(int,input().split())
SA, SB = map(int,input().split())

if N < LA or N > LB or N < SA or N > SB:
    print("impossivel")
else:
    print("possivel")
