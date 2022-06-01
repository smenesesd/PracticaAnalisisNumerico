import numpy as np

def doolittle(A,b):
    A = np.array(A)
    b = np.array(b)
    n = len(A[0])
    l = np.zeros((n,n))
    u = np.zeros((n,n))
    for i in range(n):
        l[i][i] = 1
        if i == 0:
            u[0][0] = A[0][0]
            for j in range(1,n):
                u[0][j]= A[0][j]
                l[j][0] = A[j][0]/u[0][0]
        else:
            for j in range(i, n):
                temp = 0
                for k in range(0,i):
                    temp = temp+l[i][k]*u[k][j]
                u[i][j] = A[i][j]-temp
            for j in range(i+1, n):
                temp = 0
                for k in range(0, i):
                    temp = temp + l[j][k] *u[k][i]
                l[j][i] = (A[j][i]-temp)/u[i][i]
    y = np.linalg.solve(l, b)
    x = np.linalg.solve(u,y)
    for i in range(n):
        print("x"+str(i+1)+"=",x[i])


a = [[2,4,2,6],[4,9,6,15],[2,6,9,18],[6,15,18,40]]
b = [9,23,22,47]
doolittle(a,b)