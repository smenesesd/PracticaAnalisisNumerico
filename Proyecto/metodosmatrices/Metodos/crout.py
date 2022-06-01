import numpy as np

def crout(a,b):
    a = np.array(a)
    b = np.array(b)
    m ,n= np.shape(a)           #Numero de filas y columnas
    l = np.zeros((n,n))
    u = np.zeros((n,n))
    s1 = 0
    s2 =0

    for i in range(n):
        l[i][0]= a[i][0]
        u[i][i] = 1
    for j in range(1, n):
        u[0][j] = a[0][j]/l[0][0]
    for k in range(1, n):
        for i in range(k ,n):
            for r in range(k): s1 += l[i][r] * u[r][k]
            l[i][k] = a[i][k] -s1
            s1 = 0
        for j in range(k+1, n):
            for r in range(k): s2 += l[k][r]*u[r][j]
            u[k][j]= (a[k][j]-s2)/l[k][k]
            s2 = 0
    y = np.zeros(n)                 #Sustitucion progresiva
    s3 = 0
    y[0]=b[0]/l[0][0]               #Despeje de la primera x
    for k in range(1, n):           #Ciclo para despejar las demas x
        for r in range(k):          #Sumatoria de todos los valores conocidos
            s3 += l[k][r]*y[r]
        y[k] = (b[k]-s3)/l[k][k]    #Despeje de x
        s3 = 0
    
    x = np.zeros(n)
    s4 = 0
    x[n-1] = y[n-1]
    for k in range(n-2, -1, -1):
        for r in range(k+1, n):
            s4 += u[k][r]*x[r]
        x[k] = y[k]-s4
        s4 = 0
    return x

#a = [[2,4,2,6],[4,9,6,15],[2,6,9,18],[6,15,18,40]]
#b = [9,23,22,47]
#crout(a, b)