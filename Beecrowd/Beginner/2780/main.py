patern = [(800, 1), (1400, 2), (2000, 3)]
D = int(input())

for c, txt in patern:
    if D <= c:
        print(txt)
        break
