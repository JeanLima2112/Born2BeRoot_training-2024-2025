N = int(input())

table = [(0, "E"), (35, "D"), (60, "C"), (85, "B"), 
        (100, "A")]

for limit, label in table:
    if N <= limit:
        print(label)
        break