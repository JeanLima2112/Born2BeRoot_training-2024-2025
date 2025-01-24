N = int(input())

K = N + 1 
circle = [0] * N + [1] * N 
while True:
    aux_circle = circle.copy()
    pos = 0  
    eliminados = 0  
    
    while eliminados < N: 
        pos = (pos + K - 1) % len(aux_circle) 
        if aux_circle[pos] == 1:  
            aux_circle.pop(pos)  
            print(aux_circle)
            eliminados += 1  
        else: 
            break  
    
    if eliminados == N:  
        print(K) 
        break  
    
    K += 1  

