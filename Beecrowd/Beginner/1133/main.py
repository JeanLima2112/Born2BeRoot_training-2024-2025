N = []
for _ in range(2):
    N.append(int(input()))
N.sort()
X = N[0]
Y = N[1]

for _ in range(X+1,Y):
    if _ % 5 == 2 or _ % 5 == 3:
        print(_)