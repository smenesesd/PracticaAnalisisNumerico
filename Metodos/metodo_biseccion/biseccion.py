import sympy 
from tabulate import tabulate

def biseccion(xi,fx,xf,tol,optiontol):
    table = []
    xi = float(xi)
    xf = float(xf)
    tol = float(tol)
    if fx.subs(x,xi)*fx.subs(x,xf)==0:          #Evaluamos si en el intervalo hay hay una raiz
        return "Xi or Xf are roots",table
    elif fx.subs(x,xi)*fx.subs(x,xf)>0:         #En caso de que sea mayor a cero no hay una raiz
        return "Interval not valid"
    else:
        xm = (xi+xf)/2                          #Calculamos el punto tmedio
        error=tol+1.0
        if optiontol:                           #Dependiendo de la opcion calculamos la toleracion
            error=abs(xm-xi)
        else:
            error=abs((xm-xi)/xm)
        table.append([xi,round(fx.subs(x,xi),4),xm,round(fx.subs(x,xm),4),xf,round(fx.subs(x,xf),4),error])     #Evaluamos en los primeros puntos y adjuntamos a respuesta a la tabla
        while(error>=tol and fx.subs(x,xm)!=0):                     #Mientras que seamos mayores que la toleracina y no haya una raiz se ejecuta el ciclo
            if fx.subs(x,xi)*fx.subs(x,xm)<0:               #En caso de que la raiz este en la parte de abajo
                xf = xm
            else:                                           #En caso de que la raiz se encuentre en la parte de arriba
                xi = xm 
            xm = (xi+xf)/2
            if optiontol:                                   #Se calcula el error dependiendo del escojido
                error=abs(xm-xi)
            else:
                error=abs((xm-xi)/xm)
            table.append([xi,round(fx.subs(x,xi),4),xm,round(fx.subs(x,xm),4),xf,round(fx.subs(x,xf),4),error])     #Añadimos los resultado obtenidos a la tabla de respuesta
        if fx.subs(x,xm)==0:                                #En caso de que hallemos la raiz
            return "Xm is a root",table
        else:                                               #En caso de llegar por tolerancia
            return "Xm is a root with tol",table

#Main
x = sympy.Symbol('x')                                               
fdx = (x**3)-(7.51*x**2)+(18.4239*x)-14.8331
result=biseccion(3,fdx,3.5,0.0001,False)                                
print(result[0])                                                 
print(tabulate(result[1],headers=["xi", "f(xi)", "xm","f(xm)","xf","f(xf)","error"]))




