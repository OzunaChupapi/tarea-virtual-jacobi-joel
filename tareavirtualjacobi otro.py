import numpy as np


# Definiendo la matriz A y el vector b
A = np.array([[3, -0.1, 0.2],
              [7, -0.3, -0.485421],
              [0, 0.02, 7.14]])

b = np.array([7.85, -19.3, 71.4])

# Calcular los valores de M y C
M = np.linalg.inv(A).dot(b)

# Mostrando resultados
print("Valores de M:")
print(M)

# Definiendo los alfas
Alfa1 = 0.1
Alfa2 = 0.05714286
Alfa3 = 0.05
Max_Alfa = max(Alfa1, Alfa2, Alfa3)

# Resultados de los alfas
print("\nAlfas:")
print(f"Alfa1: {Alfa1}")
print(f"Alfa2: {Alfa2}")
print(f"Alfa3: {Alfa3}")
print(f"Max Alfa: {Max_Alfa}")

# Calculando e1
X = np.array([[0, 0.61666667, 0.0564752,  2.0652186,  2.0562366],
              [0, -2.79452383, -2.682807, -0.4854211, 0],
              [0, 7.00560952, 0.2297906, 0.0087434,  4.9922e-05]])

e1 = np.array([2.61666667, -0.56019143, 0.0087434])

# Mostrando resultados de e1
print("\nValores de e1:")
print(e1)

# Calcular el MAX
MAX = np.max(X)
print(f"\nMAX: {MAX}")