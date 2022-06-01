import numpy as np

def crout(a,b):
    a = np.array(a)
    b = np.array(b)
    m ,n= np.shape(a)           #Numero de filas y columnas
    l = np.zeros((n,n))
    u = np.zeros((n,n))
    s1 = 0
    s2 =0

    for i in range(n):          #Dada la formila de crout, la primera columna de a es igual a la de l
        l[i][0]= a[i][0]
        u[i][i] = 1             #Volvmeos la diagonal de u en 1
    for j in range(1, n):
        u[0][j] = a[0][j]/l[0][0]   #Formula de la primera fila de u
    for k in range(1, n):
        for i in range(k ,n):       #Formula para calcular L
            for r in range(k): s1 += l[i][r] * u[r][k] #Sumatoria de de Lir*Upk
            l[i][k] = a[i][k] -s1           #Resta del Aik - sumatoria
            s1 = 0
        for j in range(k+1, n):             #Formula para calcualar la u
            for r in range(k): s2 += l[k][r]*u[r][j]    #Sumatoria de Lkr*Urj
            u[k][j]= (a[k][j]-s2)/l[k][k]       # (Akj-sumatoria)/Lkk
            s2 = 0
    y = np.zeros(n)                 #Sustitucion progresiva
    s3 = 0
    y[0]=b[0]/l[0][0]               #Despeje de la primera y
    for k in range(1, n):           #Ciclo para despejar las demas y
        for r in range(k):          #Sumatoria de todos los valores conocidos
            s3 += l[k][r]*y[r]
        y[k] = (b[k]-s3)/l[k][k]    #Despeje de y
        s3 = 0
    
    x = np.zeros(n)
    s4 = 0
    x[n-1] = y[n-1]
    for k in range(n-2, -1, -1):    #Sustitucion regresiva para despejar x con basje a Y y U
        for r in range(k+1, n):
            s4 += u[k][r]*x[r]      #Sumatoria del calculo de la fila
        x[k] = y[k]-s4              #Yk- sumatoria de la fila
        s4 = 0
    for i in range(n):
        print("x"+str(i+1)+"=",x[i])

a = [[2,4,2,6],[4,9,6,15],[2,6,9,18],[6,15,18,40]]
b = [9,23,22,47]
crout(a, b)