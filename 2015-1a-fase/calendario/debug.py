total_days = 0
mayan_cicles = [144000, 7200, 360, 20, 1]

mayan_date = list(map(int, input().split('.')))

for i, n in enumerate(mayan_cicles):
    total_days += mayan_date[i] * n

print(total_days)
