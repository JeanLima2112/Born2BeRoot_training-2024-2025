N = int(input())

for c in range(0,N):
    X = int(input())
    if X == 0:
        print("NULL")
    else:
        if X % 2 == 0:
            print('EVEN', end= ' ')
        else:
            print('ODD', end= ' ')
    if X > 0:
        print('POSITIVE') 
    elif X < 0:
        print('NEGATIVE')

    