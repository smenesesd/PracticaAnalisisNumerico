import sympy 
from tabulate import tabulate

def incremental(fx, xi, maxite, difx):
    xi = float(xi)
    difx = float(difx)
    table = []                                                                    
    if fx.subs(x, xi)==0:                                           
        return "xi is a root ",table
    else:                                                           
        xf = xi + difx
        ite = 0
        table.append([ite,xi,round(fx.subs(x, xi),4)])
    
        while(fx.subs(x, xi)*fx.subs(x, xf)>0)and (ite<maxite):
            xi = xf
            xf = xi + difx
            ite += 1
            table.append([ite,xi,round(fx.subs(x, xi),4)])         
        table.append([ite+1,xf,round(fx.subs(x, xf),4)])            
        if fx.subs(x, xi)*fx.subs(x, xf)==0:                        
            return "xf is a root ",table
        elif fx.subs(x, xi)*fx.subs(x, xf)<0:                       
            return "Between them there is a root ",table
        else:                                                       
            return "I dont find a root in the max ite",table

#Main
x = sympy.Symbol('x')                                               
fdx = x**3-7.51*x**2+18.4239*x-14.8331
result=incremental(fdx,0,250,0.1)                                
print(result[0])                                                 
print(tabulate(result[1],headers=["Ite", "x", "F(x)"]))   