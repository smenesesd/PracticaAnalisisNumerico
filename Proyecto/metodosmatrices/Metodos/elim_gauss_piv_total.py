def pivoteo_total(A,n,k):
    mayor = 0
    columna = 0
    fila = k
    for i in range(k, n):
        for j in range(k,n):
            if abs(A[i][j])>mayor:
                mayor = A[i][j]
                fila = i 
                columna = j
    
    A_auxiliar = A.copy()
    A[k] = A[fila]
    A[fila] = A_auxiliar[k]
    A_auxiliar = A.copy()
    for i in range(0, n):
        cambio_columna = A_auxiliar[i][k]
        A[i][k] = A[i][columna]
        A[i][columna] = cambio_columna
    return A

def elim_gauss_piv_total(A,b,n):
    x = []
    
    for i in range(n):
        A[i].append(b[i])
        x.append(0)
    
    for k in range(0, n):
        for i in range(k+1, n):
            A = pivoteo_total(A,n,k)
            M = A[i][k]/A[k][k]
            A[i][k] = 0
            for j in range(k+1, n+1):
                A[i][j] = A[i][j]-M*A[k][j]
    for k in range(n, 0, -1):
        sum = 0
        for j in range(k, n):
            sum = A[k-1][j] * x[j] + sum
        
        x[k-1] = (A[k-1][n]-sum)/A[k-1][k-1]
    
    return x

#A = [[-7, 2, -3, 4],
#     [5, -1, 14, -1],
#     [1, 9, -7, 5],
#     [-12, 13, -8, -4],]
  
#b = [-12, 13, 31, -32]

#x = [0, 1, 2, 3]

#elim_gauss_piv_total(A, b, 4)