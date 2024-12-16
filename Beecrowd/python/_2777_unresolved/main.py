import numpy as np

def matrix_exponentiation(mat, n):
    """
    Calcula a potência n da matriz mat usando exponenciação rápida.
    
    :param mat: matriz quadrada (numpy array)
    :param n: potência (inteiro não negativo)
    :return: mat^n
    """
    size = len(mat)
    result = np.eye(size, dtype=int)  # Matriz identidade
    base = np.array(mat, dtype=int)

    while n > 0:
        if n % 2 == 1:
            result = np.dot(result, base)
        base = np.dot(base, base)
        n //= 2

    return result

def solve_recurrence(n):
    """
    Resolve a recorrência F(n) = F(n-2) + F(n-3) usando exponenciação de matriz.
    
    :param n: Termo desejado (inteiro não negativo)
    :return: Valor de F(n)
    """
    F0, F1, F2 = 1, 2, 2  # Vetor inicial
    
    if n == 0:
        return F0
    if n == 1:
        return F1
    if n == 2:
        return F2

    # Matriz de transição
    transition_matrix = [
        [0, 1, 1],
        [1, 0, 0],
        [0, 1, 0]
    ]
    
    # Elevar a matriz à potência (n-2)
    result_matrix = matrix_exponentiation(transition_matrix, n-2)
    
    # Multiplicar pela matriz inicial [F(2), F(1), F(0)]
    initial_vector = [F2, F1, F0]
    Fn = np.dot(result_matrix, initial_vector)
    
    return Fn[0]  # O primeiro elemento é F(n)

n = 5
result = solve_recurrence(n)
print(f"F({n}) = {result}")