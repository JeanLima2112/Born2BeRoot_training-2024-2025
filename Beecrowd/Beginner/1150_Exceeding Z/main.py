A = int(input())
B = 0
while B <= A:
    B = int(input())
total = 0
numbers = 0
for _ in range(A,B):
    numbers +=1
    total += _
    if total > B:
        break
print(numbers)
