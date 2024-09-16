def backtracking_iterativo(coords: list, y, x, h, w):
    # Usa uma pilha para simular a recursão
    stack = [(y, x)]
    
    while stack:
        cy, cx = stack.pop()
        
        if coords[cy][cx] == 1:
            # Marca a posição como visitada
            coords[cy][cx] = 0

            # Explora as quatro direções: baixo, cima, direita, esquerda
            if cy + 1 < h and coords[cy + 1][cx]:
                stack.append((cy + 1, cx))

            if cy - 1 >= 0 and coords[cy - 1][cx]:
                stack.append((cy - 1, cx))

            if cx + 1 < w and coords[cy][cx + 1]:
                stack.append((cy, cx + 1))

            if cx - 1 >= 0 and coords[cy][cx - 1]:
                stack.append((cy, cx - 1))

try:
    while True:
        # Lê as dimensões da matriz
        y, x = map(int, input().split())  # y = altura (linhas), x = largura (colunas)

        # Lê a matriz de coordenadas das obras (valor 1) e espaços vazios (valor 0)
        coords = []
        for i in range(y):
            coords.append(list(map(int, input().split())))

        # Conta o número de "obras" (componentes conectados)
        obras = 0
        for i in range(y):
            for j in range(x):
                if coords[i][j]:  # Se encontrar uma obra (valor 1)
                    obras += 1
                    backtracking_iterativo(coords, i, j, y, x)  # Usa a função iterativa

        print(obras)
except EOFError:
    pass
