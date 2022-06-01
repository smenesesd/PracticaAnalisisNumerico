def dif_dividas(x, y):
    tabla = [x,y]                                   #Creamis las dos primeras columnas de la matruz, X y Y
    for i in range(2,len(x)+1):                     #Empezamos desde la segunda diferencia
        fila = []
        for j in range(i-1):                        #LLenamo con x la diagonal superior desde la segunda diferencia
            fila.append("x")
        for j in range(i-1,len(x)):                 #Recorremos la diferencia y empezamos a realizar el proceso
            num = tabla[i-1][j]-tabla[i-1][j-1]     #Calculamos el numerador, recorar que i representa la columna en la que vamos, j la fila
            dem = tabla[0][j]-tabla[0][j+1-i]       #Calculamos el denominador
            dif = num/dem
            fila.append(dif)                        #Anexamos a la fila
        tabla.append(fila)                          #Anexamos a la tabla      
    resultado = []
    for j in range(len(tabla[0])):                  #Recorremos la tabla y la reorganizamos de manera correcta
        fila = []
        for z in range(len(tabla[0])+1):            
            fila.append(tabla[z][j])
        resultado.append(fila)
    return resultado                                #Retoramos el resultado
