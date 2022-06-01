def pivoteo_total(A,n,k):
    mayor = 0
    columna = 0
    fila = k
    for i in range(k, n):               #Ciclo para recorrer todo el resto de matriz y encontrar el mayor pivote
        for j in range(k,n):
            if abs(A[i][j])>mayor:      #En caso de encontrar un nuevo mayor, cambiamos la columna y la fila
                mayor = A[i][j]
                fila = i 
                columna = j
    
    A_auxiliar = A.copy()                   #Copiamos la matriz
    A[k] = A[fila]                          #Realizamos el cambio de fila
    A[fila] = A_auxiliar[k]
    A_auxiliar = A.copy()
    for i in range(0, n):                   #Ciclo parar realiza el cambio de columna
        cambio_columna = A_auxiliar[i][k]
        A[i][k] = A[i][columna]
        A[i][columna] = cambio_columna
    return A

def elim_gauss_piv_total(A,b,n):
    x = []
    
    for i in range(n):              #Ciclo para juntar las dos matrices (A, b)
        A[i].append(b[i])
        x.append(0)                 #Llenamos la matriz de x con 0
    
    for k in range(0, n):                       #Metodo par arecorrer toda la matriz y hacer pivote total          
        for i in range(k+1, n):
            A = pivoteo_total(A,n,k)            #Metodo para reorganizar la matriz con el mayor denominador (pivote)    
            M = A[i][k]/A[k][k]                 #Calculamos el valor de M
            A[i][k] = 0                         #Hacemos el primer elemento de la fila en 0
            for j in range(k+1, n+1):           #Ciclo para realizar la resta en los demas elementos de la fila
                A[i][j] = A[i][j]-M*A[k][j]
    for k in range(n, 0, -1):                   #Ciclo para hacer sustitucion regresiva y calcular las x
        sum = 0
        for j in range(k, n):                   #Ciclo para calcular la sumatoria de los valores conocidos
            sum = A[k-1][j] * x[j] + sum
        
        x[k-1] = (A[k-1][n]-sum)/A[k-1][k-1]    #Calculamos el valor de x
    
    for i in range(n):
        print('x' + str(i) + '=' + str(x[i]))

A = [[-7, 2, -3, 4],
     [5, -1, 14, -1],
     [1, 9, -7, 5],
     [-12, 13, -8, -4],]
  
b = [-12, 13, 31, -32]

x = [0, 1, 2, 3]

elim_gauss_piv_total(A, b, 4)