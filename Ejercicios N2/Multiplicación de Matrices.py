def multiplicar_matrices(matriz1, matriz2):
    result = [[sum(a * b for a, b in zip(fila, columna)) for columna in zip(*matriz2)] for fila in matriz1]
    return result

# Ejemplo de uso:
matriz_a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matriz_b = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
resultado = multiplicar_matrices(matriz_a, matriz_b)
print(resultado)
