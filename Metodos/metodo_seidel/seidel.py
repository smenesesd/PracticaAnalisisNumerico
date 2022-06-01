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
    print(x)

a = [[3. , -0.1, -0.2],[0.1,  7  , -0.3],[0.3, -0.2, 10  ]]
b = [7.85,-19.3,71.4]

met_seidel(a,b, 100, 0.0001)