"""
    matriz_premagica_vr.py

    DESCRIPCION: El programa determina si una matriz dada es premagica. 
                 Una matriz es premagica si la suma de al menos una fila 
                 y una columna es la misma.
                 Esta version permite probar la robustes del programa.

    Autor: Gerardo Carrillo (15-11662)

    Ultima modificacion: 10/07/2020
"""
import sys

def es_premag(A:list, m:int, n:int)->bool:
    
    def suma_fila(B:list, p:int, q:int, f:int)->int:
        assert((p > 0) and (q > 0))  # Precondicion
        t, suma = 0, 0
        cota = q-t
        
        assert(suma == sum(B[f][k] for k in range(t)) and (0 <= t) and (t < q+1))    # Invariante al inicio del ciclo
        assert(cota >= 0)  # Cota positiva 
        ###########################
        while t < q:              #
            suma = suma + B[f][t] #
            t = t + 1             #
        ###########################
            assert(suma == sum(B[f][k] for k in range(t)) and (0 <= t) and (t < q+1)) # Invariante dentro del ciclo
            assert(cota > q-t)  # Cota decreciente
            cota = q-t          # Actualizar cota
            assert(cota >= 0)   # Cota positiva 

        assert(suma == sum(B[f][k] for k in range(q)))  # Postcondicion
        return suma

    def suma_colum(B:list, p:int, q:int, c:int)->int:
        assert((p > 0) and (q > 0))  # Precondicion
        t, suma = 0, 0
        cota = p-t

        assert(suma == sum(B[k][c] for k in range(t)) and (0 <= t) and (t < p+1))   # Invariante al inicio del ciclo
        assert(cota >= 0)  # Cota positiva 
        ###########################
        while t < p:              #
            suma = suma + B[t][c] #
            t = t + 1             #
        ###########################
            assert(suma == sum(B[k][c] for k in range(t)) and (0 <= t) and (t < p+1))   # Invariante dentro del ciclo
            assert(cota > p-t)  # Cota decreciente
            cota = p-t          # Actualizar cota
            assert(cota >= 0)   # Cota positiva 
        
        assert(suma == sum(B[k][c] for k in range(p))) # Postcondicion
        return suma
    
    assert((m > 0) and (n > 0))  # Precondicion
    fil, sumaf, sumac = 0, 0, 0                                         
    pre_mag = False
    
    cota1 = m-fil
    assert(             # Invariante al inicio del ciclo principal
            pre_mag == any( any( (sum(A[i][w] for w in range(n)) == sum(A[z][j] for z in range(m))) 
                       for j in range(n)) for i in range(fil)) and (0 <= fil) and (fil < m+1)
          )  
    assert(cota1 >= 0)  # Cota positiva (ciclo principal)
    #########################################
    while (fil < m) and (pre_mag == False): #   
        sumaf = suma_fila(A, m, n, fil)     #
        col = 0                             #
    #########################################    
        cota2 = n-col   ## Cota (ciclo anidado)
        assert(         ## Invariante al inicio del ciclo anidado
                pre_mag == any( (sum(A[fil][w] for w in range(n)) == sum(A[z][j] for z in range(m))) 
                           for j in range(col)) and (0 <= col) and (col < n+1)
              )
        assert(cota2 >= 0) ## Cota positiva (ciclo anidado)
        #########################################
        while (col < n) and (pre_mag == False): #
            sumac = suma_colum(A, m, n, col)    #
            pre_mag = (sumaf == sumac)          #
            col = col + 1                       # 
        #########################################
            assert(                ## Invariante dentro del ciclo anidado
                    pre_mag == any( (sum(A[fil][w] for w in range(n)) == sum(A[z][j] for z in range(m))) 
                               for j in range(col)) and (0 <= col) and (col < n+1)
                  )
            assert(cota2 > n-col)  ## Cota decreciente (ciclo anidado)
            cota2 = n-col          ## Actualizar cota (ciclo anidado)
            assert(cota2 >= 0)     ## Cota positiva (ciclo anidado)
        
        assert(                    ## Postcondicion (ciclo anidado)
                pre_mag == any( (sum(A[fil][w] for w in range(n)) == sum(A[z][j] for z in range(m))) 
                           for j in range(n)) 
              )
        ###############
        fil = fil + 1 #
        ###############
        assert(               # Invariante dentro del ciclo principal
                pre_mag == any( any( (sum(A[i][w] for w in range(n)) == sum(A[z][j] for z in range(m))) 
                           for j in range(n)) for i in range(fil)) and (0 <= fil) and (fil < m+1)
              )  
        assert(cota1 > m-fil) # Cota decreciente (ciclo principal)
        cota1 = m-fil         # Actualizar cota (ciclo principal)
        assert(cota1 >= 0)    # Cota positiva (ciclo principal)

    assert(                   # Postcondicion (ciclo principal)
            pre_mag == any( any( (sum(A[i][w] for w in range(n)) == sum(A[z][j] for z in range(m))) 
                       for j in range(n)) for i in range(m)) 
          )
    
    return pre_mag

def resultado(B:list, pre_mag:bool)->'void':
    if pre_mag == True:
        print("")
        print("La matriz "+ str(B) +" es premagica")
    else: 
        print("")
        print("La matriz "+ str(B) +" NO es premagica")

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





