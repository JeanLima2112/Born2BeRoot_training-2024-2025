tam_vetor, n_queries = map(int, input().split()) 
vetor = list(map(int, input().split()))

def gcd(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a % b
    return a

try:
    for _ in range(1,n_queries+1):
        querie = list(map(int, input().split()))
        if len(querie) < 3:
            print(_)
        elif querie[0] == 1:
            for c in range(querie[1]-1,querie[2]):
                vetor[c] += querie[3]
        else:
            result = vetor[querie[1]]
            for c in range(querie[1]-1,querie[2]):
                result = gcd(result,vetor[c])
            print(result)
except EOFError:
    print(n_queries)
    pass


   