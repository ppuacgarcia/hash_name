import numpy as np

# Entrada de datos
name = input("Ingrese su nombre: ")
skey = input("Ingrese su clave en formato separado por comas: ")

# nombre de 3 filas por n columnas
if len(name) % 3 != 0:
    name = name + " " * (3 - len(name) % 3)

# Convertir el string de clave en una lista de enteros
key = skey.split(',')
key = [int(num) for num in key]

# Convertir el nombre en valores ASCII
ascii_name = [ord(char) for char in name]

# Convertir key en una matriz 3x3
if len(key) == 9:
    key_matrix = np.array(key).reshape(3, 3)
else:
    raise ValueError("La lista de claves debe tener exactamente 9 elementos.")

# Convertir ascii_name en una matriz con 3 filas
num_columns = len(ascii_name) // 3
ascii_name_matrix = np.array(ascii_name).reshape(3, num_columns)

print("key (3x3):")
print(key_matrix)
print("\nMatriz ascii_name (3 filas, n columnas):")
print(ascii_name_matrix)

# Multiplicación de matrices
result_matrix = np.dot(key_matrix, ascii_name_matrix)

print("\nMatriz resultante (producto de key_matrix y ascii_name_matrix):")
print(result_matrix)

# Calcular la inversa de key_matrix
try:
    key_matrix_inv = np.linalg.inv(key_matrix)
except np.linalg.LinAlgError:
    raise ValueError("La matriz key_matrix no es invertible.")

name_matrix_new = np.dot(key_matrix_inv, result_matrix)

print("\nMatriz recuperada (ascii_name_matrix a partir de result_matrix):")
print(name_matrix_new)

# Redondear valores para evitar problemas de precisión y convertir a enteros
name_matrix_new = np.round(name_matrix_new).astype(int)

# Convertir la matriz recuperada a una lista de caracteres ASCII
# Asegúrate de que los valores estén en el rango de códigos ASCII válidos (0-127)
recovered_ascii_characters = [chr(int(value)) for value in name_matrix_new.flatten() if 0 <= int(value) <= 127]

# Concatenar los caracteres en un string
recovered_string = ''.join(recovered_ascii_characters)

print("\nString recuperado:")
print(recovered_string)
