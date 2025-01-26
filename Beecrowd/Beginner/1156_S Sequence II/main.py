N = input()
total = 0
exp = 0
for _ in range (1,40,2):
    total += _ / (2 ** exp)
    exp+=1
print(f"{total:.2f}")