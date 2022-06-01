import numpy as np

def met_seidel(a, b, maxite, tol):
    a = np.array(a)
    b = np.array(b)
    n = len(b)
    x = np.zeros(n)
    diferencia = np.ones(n, dtype=float)
    error = tol+1
    ite = 0
    while not(error<=tol or ite> maxite):
        for i in range(0, n):
            suma = 0
            for j in range(0,n):
                if(i!=j):
                    suma = suma-a[i][j]*x[j]
            nuevo = (b[i]+suma)/a[i][i]
            diferencia[i]=np.abs(nuevo-x[i])
            x[i] = nuevo
        error = np.max(diferencia)
        ite +=1
    x= np.transpose([x])
    return x

