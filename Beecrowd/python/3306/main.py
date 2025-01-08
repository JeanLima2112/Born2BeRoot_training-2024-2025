tam_vetor, n_queries = map(int, input().split()) 
vetor = list(map(int, input().split()))

def gcd(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a % b
    return a

for _ in range(0, n_queries):
    querie = list(map(int, input().split()))
    if querie[0] == 1:
        for c in range(querie[1]-1,querie[2]):
            vetor[c] += querie[3]
    else:
        result = vetor[querie[1-1]]
        for c in range(querie[1]-1,querie[2]):
           result = gcd(result,vetor[c])
        print(result)