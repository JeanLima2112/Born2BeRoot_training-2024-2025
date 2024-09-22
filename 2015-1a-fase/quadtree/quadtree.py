def split_matrix(matrix):
    n = len(matrix)
    mid = n // 2

    top_left = [row[:mid] for row in matrix[:mid]]
    top_right = [row[mid:] for row in matrix[:mid]]
    bottom_right = [row[mid:] for row in matrix[mid:]]
    bottom_left = [row[:mid] for row in matrix[mid:]]

    return top_left, top_right, bottom_right, bottom_left

def calc_quadtree(quadtree: list[list]):
    zeros = 0
    ones = 0

    for row in quadtree:
        ones += row.count(1)
        zeros += row.count(0)
        if ones and zeros:
            return 2

    return 1 if ones else 0

first_loop = True

while True:
    n = int(input())
    if n == 0:
        break
    if not first_loop:
        print()
    first_loop = False

    root_quadtree = []
    for _ in range(n):
        root_quadtree.append(list(map(int, input().split())))

    root_color = calc_quadtree(root_quadtree)
    print(n, root_color)

    if root_color == 2:
        # Primeira quadtree é a raiz, ou seja, o quadrado inteiro
        quadtrees_current_level = [root_quadtree]

        while len(quadtrees_current_level):
            quadtrees_next_level = [] # As quadtrees com zeros e uns são armazenadas aqui para serem processadas no próximo nível

            for quadtree in quadtrees_current_level:
                sub_quadtrees = split_matrix(quadtree) # obtém as 4 subquadtrees dentro de uma quadtree
                sub_results = []

                for sub in sub_quadtrees:
                    result = calc_quadtree(sub) # calcula a subquadtree
                    sub_results.append(result)

                    if result == 2: # caso a subquadtree tenha o valor 2, guarda para processá-la no nível seguinte
                        quadtrees_next_level.append(sub)

                print(''.join(map(str, sub_results)))

            quadtrees_current_level = quadtrees_next_level
