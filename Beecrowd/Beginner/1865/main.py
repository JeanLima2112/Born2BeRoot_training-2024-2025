N = int(input())
heroes = []
for c in range(0,N):
    name, aux = input().split() 
    heroes.append(name)

for i in heroes:
    if i == "Thor":
        print("Y")
    else: print("N")

