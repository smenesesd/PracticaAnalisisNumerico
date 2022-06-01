def pivoteo_parcial(A,n,k):
    mayor = 0
    fila = k
    for i in range(k, n):           #Recorremos todo lo que queda de matriz para conocer cual es el numero mayor
        if abs(A[i][k])>mayor:      #En caso de que halla un numero mayor
            mayor = A[i][k]
            fila = i
    A_auxiliar = A.copy()           #Copiamos la matriz para hacer el cambio de filas
    A[k] = A[fila]
    A[fila] = A_auxiliar[k]         #Cambiamos la filas
    return A


def elim_gauss_piv_parcial(A,b,n):
    x = []
    
    for i in range(n):          #For para adjuntar las matrices A y b y para llenar la matriz x de 0
        A[i].append(b[i])
        x.append(0)
    
    for k in range(0, n):
        for i in range(k+1, n):
            A = pivoteo_parcial(A,n,k)          #Llamamlos a pivoteo_ parcial para que nos organice la matriz con el mayor denominador
            M = A[i][k]/A[k][k]                 #Clculamos la constante M para el proceso de eliminacion
            A[i][k] = 0                         #Igualamos el primer elemento de la fila a 0
            for j in range(k+1, n+1):           #Ciclo para realiza r al resta a los demas elementos de la fila
                A[i][j] = A[i][j]-M*A[k][j]
    for k in range(n, 0, -1):                   #Hacemos sustitucion regresiva para despejar la x
        sum = 0
        for j in range(k, n):                   #Hacemos la sumatoria de todos los valores conocidos de la lista
            sum = A[k-1][j] * x[j] + sum
        
        x[k-1] = (A[k-1][n]-sum)/A[k-1][k-1]    #Realizamos operacion para calcular x
    
    for i in range(n):
        print('x' + str(i) + '=' + str(x[i]))

A = [[4, 3, -2, -7],
     [3, 12, 8, -3],
     [2, 3, -9, 3],
     [1, -2, -5, -6],]
  
b = [20, 18, 31, 12]
elim_gauss_piv_parcial(A, b, 4)