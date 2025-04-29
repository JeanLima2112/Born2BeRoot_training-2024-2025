areas = {"superior": 0, "esquerda": 0, "centro": 0, "direita": 0, "inferior": 0 }

for _ in range(int(input())):
    areas["superior"] += sum(list(map(int, input().split())))
    for i in range (4):
        X = list(map(int, input().split()))
        areas["esquerda"]+= X[0]
        areas["centro"]+= X[1]
        areas["direita"]+= X[2]
    areas["inferior"] += sum(list(map(int, input().split())))

    sorted_areas = sorted(areas.items(), key=lambda x: x[1], reverse=True)

 
print(sorted_areas[0][0])
