"""
    matriz_premagica_vf.py

    DESCRIPCION: El programa determina si una matriz dada es premagica. 
                 Una matriz es premagica si la suma de al menos una fila 
                 y una columna es la misma. 
                 Esta es la version final con algunos comentarios.

    Autor: Gerardo Carrillo (15-11662)

    Ultima modificacion: 10/07/2020
"""
import sys

def es_premag(A:list, m:int, n:int)->bool:

    def suma_fila(arr:list, num_fil:int, num_col:int, fila:int)->int:
        suma = 0
        for c in range(num_col):
            suma += arr[fila][c]
        return suma

    def suma_col(arr:list, num_fil:int, num_col:int, columna:int)->int:
        suma = 0
        for f in range(num_fil):
            suma += arr[f][columna]
        return suma

    fila = 0
    pre_mag = False

    while (fila < m) and (pre_mag == False):   
        sumaf = suma_fila(A, m, n, fila)    # Sumamos los elementos de la fila
        
        colum = 0   
        while (colum < n) and (pre_mag == False): 
            sumac = suma_col(A, m, n, colum) # Sumamos los elementos de la columna
            pre_mag = (sumaf == sumac)       # Si las sumas son iguales, la matriz es premagica y sale del ciclo. 
            colum += 1                        
        fila += 1                           
    return pre_mag

def resultado(arr:list, pre_mag:bool)->'void':
    if pre_mag == True:
        print("")
        print("La matriz "+ str(arr) +" es premagica")
    else: 
        print("")
        print("La matriz "+ str(arr) +" NO es premagica")

while True:
    try: 
        m = int(input("Ingrese la cantidad de filas de la matriz: "))
        n = int(input("Ingrese la cantidad de columnas de la matriz: "))
        assert((m > 0) and (n > 0))  
        break
    except:
        print("--El numero de filas y columnas debe ser positivo y diferente de cero.-- \n")
        sys.exit

A = [[0 for j in range(n)] for i in range(m)]
for i in range(m):
    for j in range(n):
        while True:    
            try:
                A[i][j] = int(input("A["+ str(i) +"]["+ str(j) +"]= "))
                break
            except:
                print("--Entrada invalida--")
                sys.exit

pre_mag = es_premag(A, m, n)
resultado(A, pre_mag)