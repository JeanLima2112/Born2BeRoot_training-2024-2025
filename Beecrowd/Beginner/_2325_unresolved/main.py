C, N =  map(int, input().split())
todos = []
disponiveis = []

for i in range(0,C):
    todos.append(list(map(int,input().split())))
instalados = todos.copy()
for i in range(0,N):
    todos.append(list(map(int,input().split())))

# print(sorted(instalados, key=lambda x: x[0]))
# print(sorted(todos, key=lambda x: x[0]))

# print(instalados)
# print(todos)
# for c in range(len(instalados), len(todos)):
#     for i in range(0,len(instalados)):
  