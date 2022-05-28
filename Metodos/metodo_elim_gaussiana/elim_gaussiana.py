
def elim_gaussiana(A,b,n):      #n es la dimension de la matriz
    table = []
    X = []

    for i  in range(n):         #Se crea la matria ampliada y se le dan valores a X
        A[i].append(b[i])
        X.append(0)
    
    for k in range(0, n):     #Eliminacion gaussiana, crea la M, el de abajo dividido el de arriba 
        for i in range(k+1, n):
            M = A[i][k]/A[k][k]
            A[i][k]=0
            for j in range(k+1, n+1):   #se le realiza la operacion al resto de la fila
                A[i][j] = A[i][j]-M*A[k][j]
    for k in range(n, 0, -1):   # porque vamos de abajo hacia arriba, esto es sust regresivva
        sum = 0
        for j in range(k, n):      #Proceso para calcular el valor de la suma 
           sum = A[k-1][j] * X[j] + sum

        X[k-1] = (A[k-1][n]-sum)/A[k-1][k-1]    #Operacion para calcular el valor de X
    
    for i in range(n):
        print('x' + str(i) + '=' + str(X[i]))   #Quitar

