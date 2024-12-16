names = [['huguinho'],['zezinho'],['luisinho']]

data = input().split()

for c in range(0,3):
    names[c].append(data[c])
names.sort(key=lambda x: x[1])
print(names[1][0])
