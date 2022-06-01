from sympy import N


def pivoteo_parcial(A,n,k):
    mayor = 0
    fila = k
    for i in range(k, n):
        if abs(A[i][k])>mayor:
            mayor = A[i][k]
            fila = i
    
    return fila
def cambio(A,k,fila):
    A_auxiliar = A.copy()
    A[k] = A[fila]
    A[fila] = A_auxiliar[k]
    return A

def susti_regresiva(A,z):
    N = len(A)
    x = []
    for i in range(N):
        A[i].append(z[i])
        x.append(0)
    for k in range(N,0,-1):
        sum = 0
        for j in range(k,N):
            sum = A[k-1][j]*x[j]
        x[k-1] = (A[k-1][N]-sum)/A[k-1][k-1]
        return x
def susti_progresiva(A,n,b):
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
    for i in range(n):
        list = []
        for i in range(n):
            if i == cont:
                list.append(1)
            else:
                list.append(0)
        L.append(list)
        P.append(list)
        cont += 1
    for k in range(0, n):
        for i in range(k+1, n):
            fila = pivoteo_parcial(A,n,k)
            A = cambio(A,k,fila)
            P = cambio(P,k,fila)
            b = cambio(b,k,fila)
            M = A[i][k]/A[k][k]
            L[i][k] = M
            A[i][k] = 0
            for j in range(k+1, n):
                A[i][j] = A[i][j]-M*A[k][j]
    z = susti_progresiva(L,n,b)
    x = susti_regresiva(A,z)

    print('U')
    print(A)
    print('L')
    print(L)
    print('z')
    print(z)
    print('x')
    print(x)
        

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


