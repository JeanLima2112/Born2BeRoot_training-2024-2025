try:    
    while True:
        V,T = map(int, input().split())
        print(f"{V * (T*2)}")
except EOFError:
    pass     
