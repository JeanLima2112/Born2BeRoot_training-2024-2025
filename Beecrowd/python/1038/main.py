table = [(1,4.0),(2,4.50),(3,5.0),(4,2.0),(5,1.50) ]

C , Q = map(int,input().split())
print(f"Total: R$ {table[C-1][1]* Q:.2f}")