#Importar librerías

import numpy as np

#Definición de funciones
#Función para imprimir matriz extendida

def imprimirMatrizExtendida(matriz):
    print("Matriz:")
    for i in range(len(matriz)):
        for j in range(len(matriz) + 1):
            if(j == len(matriz)):
                print("|" + str(matriz[i][j]))
            else:
                print(matriz[i][j], end="\t")
        print()

#Función para imprimir matriz
        
def imprimirMatriz(matriz):
    print("Matriz:")
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            print(matriz[i][j], end="\t")
        print()

#Comienzo del programa
#Insertar matriz

print("Ingresa el numero de variables")

n = int(input())

matrix = []

print("Ingresa el sistema de ecuaciones en forma de matriz extendida")

for i in range(n):
    row = []
    for j in range(n + 1): #n + 1 para incluir la solución
        print("Ingresa el elemento [" + str(i) + "][" + str(j) + "]")
        row.append(int(input()))
    matrix.append(row)

#Obtener determinante para saber si el sistema tiene solución
    
terminosIndependientes = []

for i in range(n):
    terminosIndependientes.append(matrix[i][-1])

for i in range(n):
    matrix[i] = matrix[i][:-1]

imprimirMatriz(matrix)

if (np.linalg.det(matrix) == 0):
    print("El sistema no tiene solución")

#Despejar cada una de las variables
    
for i in range(n):
    divisor = matrix[i][i]
    for j in range(n):
        matrix[i][j] = matrix[i][j] / divisor

imprimirMatriz(matrix)

#Construir la matriz Tj

for i in range(n):
    for j in range(n):
        if (i == j):
            matrix[i][j] = 0
        else:
            matrix[i][j] = - matrix[i][j]

#Conseguir los valorse propios (eigen values)
            
eigenvalues = np.linalg.eigvals(matrix)

normalizados = []
for i in range(n):
    normalizados.append(np.linalg.norm(eigenvalues[i]))

print("NORMALIZADOS: ", normalizados)

#Obtener omega
#Para despejar por omega, asignarle a ro el máximo de los valores propios

ro = max(normalizados)

w = 2/(1 + np.sqrt(1-np.power(ro, 2)))

#Comenzar iteración Seidel hasta que el error sea menor que 1x10^-6



###Hacer el código para que calcule los valores propios sobre la matriz T(j)
###Usar numpy para hallar eigen-values y eigen-vectors