for _ in range(int(input())):
    n = int(input())

    zeros = 0
    base_triangulo = n - 2
    zeros = base_triangulo * (base_triangulo + 1)
    area_total = n * n

    result = 'S' if area_total - zeros < area_total / 2 else 'N'
    print(result, zeros)
