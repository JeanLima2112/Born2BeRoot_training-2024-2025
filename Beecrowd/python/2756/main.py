pattern = [
    (7, 'A', 0),
    (6, 'B', 1),
    (5, 'C', 3),
    (4, 'D', 5),
    (3, 'E', 7),
    (4, 'D', 5),
    (5, 'C', 3),
    (6, 'B', 1),
    (7, 'A', 0)
]

for spaces, char, inner_spaces in pattern:
    line = ' ' * spaces + char
    if inner_spaces > 0:
        line += ' ' * inner_spaces + char
    print(line)


