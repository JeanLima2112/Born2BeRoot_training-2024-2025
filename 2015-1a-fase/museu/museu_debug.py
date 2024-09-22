import time
import sys

def debug(coords, depth):
    print(f"Profundidade: {depth}")
    for line in coords:
        print(" ".join(line))
    print()
    sys.stdout.flush()
    time.sleep(1)


def backtracking(coords: list, y, x, h, w, depth=0):
    coords[y][x] = "\033[0;34m" + 'X' + '\033[0m'

    # Adiciona o debug com a profundidade atual
    debug(coords, depth)
    
    # Aumenta a profundidade antes da próxima chamada recursiva
    if y + 1 < h and coords[y + 1][x] == '1':
        backtracking(coords, y + 1, x, h, w, depth + 1)

    if y - 1 >= 0 and coords[y - 1][x] == '1':
        backtracking(coords, y - 1, x, h, w, depth + 1)

    if x + 1 < w and coords[y][x + 1] == '1':
        backtracking(coords, y, x + 1, h, w, depth + 1)

    if x - 1 >= 0 and coords[y][x - 1] == '1':
        backtracking(coords, y, x - 1, h, w, depth + 1)

try:
    while True:
        x, y = map(int, input().split())
        coords = []

        for i in range(y):
            coords.append(list(input().split()))

        obras = 0
        for i in range(y):
            for j in range(x):
                if coords[i][j] == '1':
                    obras += 1
                    backtracking(coords, i, j, y, x)
        print(obras)
        print("-" * 20)
except EOFError:
    pass
