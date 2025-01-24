N = int(input())

tops = [(1, "Top 1"), (3, "Top 3"), (5, "Top 5"), (10, "Top 10"), 
        (25, "Top 25"), (50, "Top 50"), (100, "Top 100")]

for limit, label in tops:
    if N <= limit:
        print(label)
        break
