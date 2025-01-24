instancia = 1
while True:
    if instancia != 1:
        print()
    print("Instancia", instancia)
    instancia += 1
    M, N = map(int, input().split())
    if N == 0 and M == 0:
        print('sim\n')
        break
    matriz = [list(map(int, input().split())) for _ in range(M)]
    aux = 0
    
    i, j = 0, 0
    
    try:
        while True:
            if i < 0 or i > M or j < 0 or j > N:
                print ('nao')
                break
            aux += 1
            if aux > N * M:
                print("sim")
                break
            if matriz[i][j] == 1:
                matriz[i][j] = 'X'
                i -= 1
            elif matriz[i][j] == 'X':
                print("nao")
                break
            elif matriz[i][j] == 2:
                matriz[i][j] = 'X'
                i -= 1
                j += 1
            elif matriz[i][j] == 3:
                matriz[i][j] = 'X'
                j += 1
            elif matriz[i][j] == 4:
                matriz[i][j] = 'X'
                i += 1
                j += 1
            elif matriz[i][j] == 5:
                matriz[i][j] = 'X'
                i += 1
            elif matriz[i][j] == 6:
                matriz[i][j] = 'X'
                i += 1
                j -= 1
            elif matriz[i][j] == 7:
                matriz[i][j] = 'X'
                j -= 1
            elif matriz[i][j] == 8:
                matriz[i][j] = 'X'
                i -= 1
                j -= 1
            
        
    except:
        print("nao")