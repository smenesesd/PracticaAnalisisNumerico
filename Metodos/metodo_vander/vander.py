import elim_gaussiana

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
    return elim_gaussiana.elim_gaussiana(matriz, y, tam)  #Utilizamos el metodo de eliminacion gausiana para resolver y retornamos

x = [-2,-1,2,3]
y = [12.135, 6.367, -4.6105, 2.085]
print(vandermonde(x,y))