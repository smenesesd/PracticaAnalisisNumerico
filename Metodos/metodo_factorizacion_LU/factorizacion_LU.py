from sympy import N


def pivoteo_parcial(A,n,k):     #Metodo para calcular el mayor pivote con parcial
    mayor = 0
    fila = k
    for i in range(k, n):           #Ciclo para encontrar el mayor denominador
        if abs(A[i][k])>mayor:
            mayor = A[i][k]
            fila = i
    
    return fila                     #Retornamos la fila

def cambio(A,k,fila):               #Metodo para realizar el cambio de fila
    A_auxiliar = A.copy()
    A[k] = A[fila]
    A[fila] = A_auxiliar[k]
    return A

def susti_regresiva(A,z):                       #Metodo de sustitucion regresiva
    N = len(A)
    x = []
    for i in range(N):                          #Juntamos la matriz A y z
        A[i].append(z[i])
        x.append(0)                             #Llenamos la matriz de x con 0
    for k in range(N,0,-1):                     #Ciclo para realizar sustitucion regresiva
        sum = 0
        for j in range(k,N):                    #Ciclo para calcular la sumatoria de la fila
            sum = A[k-1][j]*x[j]
        x[k-1] = (A[k-1][N]-sum)/A[k-1][k-1]    #Ecuacion para despejar x
        return x

def susti_progresiva(A,n,b):                    #Metodo de sustitucion progresiva, lo mismo de arriba pero de arriba hacia abajo
    z = []
    sum = 0 
    for k in range(n):
        sum = 0
        for j in range(k):
            sum = A[k][j]*z[j]
        z.append((b[k]-sum)/A[k][k])
    return z

def fac_LU(A,b,n):
    L = []
    P = []
    cont = 0
    for i in range(n):                  #Ciclo para crear las amtriz L y U 
        list = []
        for i in range(n):
            if i == cont:               #Para llenar la diagonal con 1
                list.append(1)
            else:
                list.append(0)
        L.append(list)                  #Se agrega la fila a la matriz
        P.append(list)
        cont += 1
    for k in range(0, n):                   #Ciclo para realizar la factorizacion LU
        for i in range(k+1, n):
            fila = pivoteo_parcial(A,n,k)       #Se halla el mayor pivote
            A = cambio(A,k,fila)                #Cambio de fila para todas las matrices
            P = cambio(P,k,fila)
            b = cambio(b,k,fila)
            M = A[i][k]/A[k][k]                 #Calculamos el valor de M
            L[i][k] = M
            A[i][k] = 0
            for j in range(k+1, n):             #Ciclo para realizar la operacion de resta en toda la fila
                A[i][j] = A[i][j]-M*A[k][j]
    z = susti_progresiva(L,n,b)                 #Sustitucion progresiva para despejar zs
    x = susti_regresiva(A,z)                    #Sustitucion regresiva para despejar x
        

A = [[4, 3, -2, -7],
     [3, 12, 8, -3],
     [2, 3, -9, 3],
     [1, -2, -5, 6],]
  
b = [20, 18, 31, 12]

A = [[4, 3, -2, -7],
     [3, 12, 8, -3],
     [2, 3, -9, 3],
     [1, -2, -5, 6],]
  
b = [20, 18, 31, 12]

fac_LU(A, b, 4)  


