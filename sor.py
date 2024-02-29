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

#Función para determinar si la matriz es Diagonal Dominante
        
def esDiagonalDominante(matriz):
    for i in range(len(matriz)):
        suma = 0
        for j in range(len(matriz[i])):
            if(i != j):
                suma += abs(matriz[i][j])
        if (abs(matriz[i][i]) > suma):
            pass
        else:
            return False
    return True

#Función para cambiar de filas

def cambioDeFilas(matriz):
    n = len(matriz)
    sumatoria = 0
    matrizTemp = matriz
    
    for i in range(1, n): #Realzar sumatoria hasta n - 1
        sumatoria += i
    for i in range(sumatoria):
        for j in range(i + 1, n):
            filaTemp = matrizTemp[i]
            matrizTemp[i] = matrizTemp[j]
            matrizTemp[j] = filaTemp
            print("Matriz cambiada:")
            imprimirMatriz(matrizTemp)
            if (esDiagonalDominante(matrizTemp)):
                return matrizTemp
            else:
                pass


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
        row.append(float(input()))
    matrix.append(row)

#Obtener determinante para saber si el sistema tiene solución
    
terminosIndependientes = []

for i in range(n):
    terminosIndependientes.append(matrix[i][-1])

#Transormar la matriz para remover el último termino
for i in range(n):
    matrix[i] = matrix[i][:-1]

if (np.linalg.det(matrix) == 0):
    print("El sistema no tiene solución")

#Determinar si la matriz es diagonal dominante
    
if (esDiagonalDominante(matrix)):
    print("La matriz es diagonal dominante")
else:
    print("La matriz no es diagonal dominante")
    print("Realizando cambio de filas...")

    exit()

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

#Conseguir los valorse propios (eigen values)
            
eigenvalues = np.linalg.eigvals(matrix)

normalizados = []
for i in range(n):
    normalizados.append(np.linalg.norm(eigenvalues[i]))

print("Los valores propios son: ", normalizados)

#Obtener omega
#Para despejar por omega, asignarle a ro el máximo de los valores propios

ro = max(normalizados)

print("El radio espectral de la matriz Tj es: ", ro)

w = 2/(1 + np.sqrt(1-np.power(ro, 2)))

if (w <= 1):
    print("El sistema no se puede resolver")
    exit()

if (w >= 2):
    print("El sistema no se puede resolver")
    exit()

print("El valor óptimo de w es: ", w)

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
                sumatoria += matrix[i][j] * respuestas[j]
        sumatoria+= terminosIndependientes[i]
        temp = w*(sumatoria) + (1-w)*respuestas[i]

        respuestas[i] = temp
    
    sumaNumerador = 0
    sumaDenominador = 0
    error = 0
    
    for i in range(n): #Calular norma euclideana del numerador del error
        sumaNumerador += np.power(respuestas[i] - respuestasAnteriores[i], 2)

    for i in range(n): #Calcular norma euclideana del denominador del error
        sumaDenominador += np.power(respuestas[i], 2)

    error = np.sqrt(sumaNumerador)/sumaDenominador

    if (error <= 0.00001):
        break

    for i in range(n):
        respuestasAnteriores[i] = respuestas[i]
    contador += 1

print("El numero de iteraciones necesearias es: ", contador)
print("Las soluciones del sistema son: ", respuestas)

##########################################################################
# Respuestas del primer punto:

# Los valores propios son:  [0.4913767424054526, 0.25609458469543556, 0.25609458469543556]
# El radio espectral de la matriz Tj es:  0.4913767424054526
# El valor óptimo de w es:  1.0689772959135608
# El numero de iteraciones necesearias es:  4
# Las soluciones del sistema son:  [-19.778299490367253, -3.4546344754270764, -0.05279597250462186]
