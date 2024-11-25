# Función para calcular el determinante de una matriz 3x3
def determinante(matriz):
    return (matriz[0][0] * (matriz[1][1] * matriz[2][2] - matriz[1][2] * matriz[2][1]) -
            matriz[0][1] * (matriz[1][0] * matriz[2][2] - matriz[1][2] * matriz[2][0]) +
            matriz[0][2] * (matriz[1][0] * matriz[2][1] - matriz[1][1] * matriz[2][0]))

# Función para calcular la matriz adjunta (la matriz de cofactores transpuesta)
def adjunta(matriz):
    adj = [[0, 0, 0] for _ in range(3)]
    
    adj[0][0] = matriz[1][1] * matriz[2][2] - matriz[1][2] * matriz[2][1]
    adj[0][1] = -(matriz[1][0] * matriz[2][2] - matriz[1][2] * matriz[2][0])
    adj[0][2] = matriz[1][0] * matriz[2][1] - matriz[1][1] * matriz[2][0]
    
    adj[1][0] = -(matriz[0][1] * matriz[2][2] - matriz[0][2] * matriz[2][1])
    adj[1][1] = matriz[0][0] * matriz[2][2] - matriz[0][2] * matriz[2][0]
    adj[1][2] = -(matriz[0][0] * matriz[2][1] - matriz[0][1] * matriz[2][0])
    
    adj[2][0] = matriz[0][1] * matriz[1][2] - matriz[0][2] * matriz[1][1]
    adj[2][1] = -(matriz[0][0] * matriz[1][2] - matriz[0][2] * matriz[1][0])
    adj[2][2] = matriz[0][0] * matriz[1][1] - matriz[0][1] * matriz[1][0]
    
    return adj

# Función para calcular la inversa
def inversa(matriz):
    det = determinante(matriz)
    
    # Si el determinante es 0, la matriz no tiene inversa
    if det == 0:
        print("La matriz no tiene inversa (determinante = 0).")
        return None
    
    # Calcular la adjunta
    adj = adjunta(matriz)
    
    # Calcular la inversa (adjunta / determinante)
    inversa_matriz = [[adj[i][j] / det for j in range(3)] for i in range(3)]
    return inversa_matriz

# Función para imprimir la matriz
def imprimir_matriz(matriz):
    for fila in matriz:
        print(" ".join([f"{x:.2f}" for x in fila]))  # Mostrar con 2 decimales

# Ejemplo de uso
matriz = [[5, -2, 2],
          [1, 0, 1],
          [3, 1, 4]]

print("Matriz original:")
imprimir_matriz(matriz)

# Calcular la inversa
inversa_matriz = inversa(matriz)

if inversa_matriz is not None:
    print("\nMatriz inversa:")
    imprimir_matriz(inversa_matriz)