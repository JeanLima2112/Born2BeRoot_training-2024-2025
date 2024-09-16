def backtracking(coords: list, y, x, h, w):
    coords[y][x] = 0

    if y + 1 < h and coords[y + 1][x]:
        backtracking(coords, y + 1, x, h, w)

    if y - 1 >= 0 and coords[y - 1][x]:
        backtracking(coords, y - 1, x, h, w)

    if x + 1 < w and coords[y][x + 1]:
        backtracking(coords, y, x + 1, h, w)

    if x - 1 >= 0 and coords[y][x - 1]:
        backtracking(coords, y, x - 1, h, w)

# Try/Catch para sair do loop infinito quando receber EOF do input
try:
    while True:
        # Lê as dimensões da matriz
        x, y = map(int, input().split()) # y = altura (linhas), x = largura (colunas)
        coords = []

        # Lê a matriz de coordenadas das obras (valor 1) e espaços vazios (valor 0)
        for i in range(y):
            coords.append(list(map(int, input().split())))

        # Conta o número de "obras" (componentes conectados)
        obras = 0
        for i in range(y):
            for j in range(x):
                if coords[i][j]: # Se encontrar uma obra (valor 1)
                    obras += 1
                    # Conta a obra e apaga todos os azulejos dessa obra com backtracking
                    backtracking(coords, i, j, y, x)
        print(obras)
except:
    pass
