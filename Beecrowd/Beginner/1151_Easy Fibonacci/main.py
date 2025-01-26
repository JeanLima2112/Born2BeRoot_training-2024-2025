sequence = [0,1,1]

N = int(input())

for _ in range(3, N):
    sequence.append(sequence[_-1]+sequence[_-2])
for _ in range(N-1):
    print(sequence[_],end=" ")
print(sequence[N-1])