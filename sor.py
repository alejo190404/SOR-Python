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

#Transormar la matriz para remover el último termino
for i in range(n):
    matrix[i] = matrix[i][:-1]

imprimirMatriz(matrix)

if (np.linalg.det(matrix) == 0):
    print("El sistema no tiene solución")

#Despejar cada una de las variables
#Transformar también el vector de valores independientes
    
for i in range(n):
    divisor = matrix[i][i]
    terminosIndependientes[i] = terminosIndependientes[i] / divisor
    for j in range(n):
        matrix[i][j] = matrix[i][j] / divisor

#Construir la matriz Tj

for i in range(n):
    for j in range(n):
        if (i == j):
            matrix[i][j] = 0
        else:
            matrix[i][j] = - matrix[i][j]

imprimirMatriz(matrix)

#Conseguir los valorse propios (eigen values)
            
eigenvalues = np.linalg.eigvals(matrix)

normalizados = []
for i in range(n):
    normalizados.append(np.linalg.norm(eigenvalues[i]))

#Obtener omega
#Para despejar por omega, asignarle a ro el máximo de los valores propios

ro = max(normalizados)

w = 2/(1 + np.sqrt(1-np.power(ro, 2)))

if (w <= 1):
    print("El sistema no se puede resolver")
    exit()

if (w >= 2):
    print("El sistema no se puede resolver")
    exit()

#Comenzar iteración Seidel hasta que el error sea menor que 1x10^-6
#Inicializar respuestas en 0
respuestas = []
for i in range(n):
    respuestas.append(0)

respuestasAnteriores = []
for i in range(n):
    respuestasAnteriores.append(0)

error = 1
contador = 1

while (error):
    for i in range(n):
        sumatoria = 0
        for j in range(n):
            if (i != j):
                print("VALOR DE LA MATRIZ: ", matrix[i][j])
                print("VALOR DE LA RESPUESTA: ", respuestas[j])
                print("VALOR DE LA TERMINO INDEPENDIENTE: ", terminosIndependientes[j])
                sumatoria += matrix[i][j] * respuestas[j]
        sumatoria+= terminosIndependientes[i]
        print("SUMATORIA: ", sumatoria)
        print()
        temp = w*(sumatoria) + (1-w)*respuestas[i]

        respuestas[i] = temp
    
    error = 0

    for i in range(n):
        error += abs(respuestas[i] - respuestasAnteriores[i])

    print("RESPUESTAS ITERACIÓN: ", respuestas)
    print("ERROR FINAL: ", error)

    if (error < 0.000001):
        break

    for i in range(n):
        respuestasAnteriores[i] = respuestas[i]
    contador += 1

print("RESPUESTAS: ", respuestas)
