from django.shortcuts import render, HttpResponse
from django.views import View
from metodoscerrados.forms import Formulario_biseccion


# Create your views here.
#[[2,34,4] [-2, 34,4]]
def validador_matriz(a):
    division = a.split(" ")
    matriz = []
    for i in range(len(division)):
        i = i.replace("[",'')
        i = i.replace("]",'')
        final = i.split(",")
        fila =[]
        try:
            for j in range(len(final)):
                fila.append(int(j))
            matriz.append(fila)
        except:
            return "Ocurrio un error"
    for j in range(len(matriz)):
        if len(matriz) != len(j):
            return "dimensiones erroneas"
    print(matriz)

class metodo_biseccion(View):
    template_name = 'biseccion/biseccion.html'
    template_response = 'biseccion/biseccion_response.html'
    form_class = Formulario_biseccion()

    def get(self, request, *args, **kwargs):
        form = self.form_class
        return render(request, self.template_name,{'form':form})

    def post(self, request, *args, **kwargs):
        form = Formulario_biseccion(request.POST)
        if form.is_valid():
            funcion = form.cleaned_data['funcion']
            xi = float(form.cleaned_data['xi'])
            xf = float(form.cleaned_data['xf'])
            tolerancia = float(form.cleaned_data['tolerancia'])
            opcion = form.cleaned_data['opcion']
            resultado =""
            try:
                if opcion == "1":
                    resultado = biseccion(xi,funcion,xf,tolerancia,True)
                else:
                    resultado = biseccion(xi,funcion,xf,tolerancia,True)
                return render(request,self.template_response, {'tabla':resultado[1], 'resultado':resultado[0]})
            except:
                print("Error en el metodo")
            print(resultado)
        return render(request, self.template_name, {'form':Formulario_biseccion})
