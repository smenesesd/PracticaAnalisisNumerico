import sympy 
from tabulate import tabulate

def incremental(fx, xi, maxite, difx):
    xi = float(xi)
    difx = float(difx)
    tabla = []
    if fx.subs(x, xi)==0:
        return "xi si es raiz",tabla
    else:
        xf = xi + difx
        ite = 0
        tabla.append([ite,xi,round(fx.subs(x, xi),4)])
        while(fx.subs(x, xi)*fx.subs(x, xf)>0)and (ite<maxite):
            xi = xf
            xf = xi + difx
            ite += 1
            tabla.append([ite,xi,round(fx.subs(x, xi),4)])
        tabla.append([ite+1,xf,round(fx.subs(x, xf),4)])
        if fx.subs(x, xi)*fx.subs(x, xf)==0:
            return "xf es raiz",tabla
        elif fx.subs(x, xi)*fx.subs(x, xf)<0:
            return "Entre ellos hay raiz",tabla
        else:
            return "No encontre raiz en el maximo de iteraciones",tabla

x = sympy.Symbol('x')
fdx = x**3-7.51*x**2+18.4239*x-14.8331
resultado=incremental(fdx,0,250,0.1)
print(resultado[0])
print(tabulate(resultado[1],headers=["Iteracion", "x", "F(x)"]))
            
