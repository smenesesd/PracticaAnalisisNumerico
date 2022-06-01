
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
        X[i] = 'X'+str(i)+' = '+str(X[i])   
    return X


def vandermonde(x, y):          #Sean X y Y las matrices con los coeficientes
    tam = len(x)                #Tamaño de la lista                
    grado = tam -1              #Grado de la funcion
    matriz = []
    for i in range(tam):                        #Recorremos las listas para generar la matriz
        secuencia = []
        for j in range(tam):
            secuencia.append(x[i]**grado)       #Para cada x, utilizamos en teorema deonde el polimio p(x) = An*X**n + An-1*X**n-1
            grado -=1
        grado = tam -1
        matriz.append(secuencia)                #Adjuntamos a la matriz
    return elim_gaussiana(matriz, y, tam)  #Utilizamos el metodo de eliminacion gausiana para resolver y retornamos
