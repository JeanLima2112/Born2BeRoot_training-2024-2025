x = int(input())

def recursive_division(d, x):
    if x == 1:
        return 1 + 1 / d
    return recursive_division(1 + 1 / d, x - 1)

print(f'{recursive_division(1, x):.15f}')
