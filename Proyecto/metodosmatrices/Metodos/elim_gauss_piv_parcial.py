def pivoteo_parcial(A,n,k):
    mayor = 0
    fila = k
    for i in range(k, n):
        if abs(A[i][k])>mayor:
            mayor = A[i][k]
            fila = i
    A_auxiliar = A.copy()
    A[k] = A[fila]
    A[fila] = A_auxiliar[k]
    return A
def elim_gauss_piv_parcial(A,b,n):
    x = []
    
    for i in range(n):
        A[i].append(b[i])
        x.append(0)
    
    for k in range(0, n):
        for i in range(k+1, n):
            A = pivoteo_parcial(A,n,k)
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

#A = [[4, 3, -2, -7],
#     [3, 12, 8, -3],
#     [2, 3, -9, 3],
#     [1, -2, -5, -6],]
  
#b = [20, 18, 31, 12]
#elim_gauss_piv_parcial(A, b, 4)