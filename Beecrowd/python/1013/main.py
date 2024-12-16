data = input().split()
maior = int(data[0])
for c in range(1,3):
    maior = (maior + int(data[c]) + abs(maior - int(data[c])))/2
print(f"{maior:.0f} eh o maior")