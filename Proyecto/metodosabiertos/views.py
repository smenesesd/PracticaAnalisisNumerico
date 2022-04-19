from django.shortcuts import render, HttpResponse
from django.views import View

# Create your views here.
class punto_fijo(View):
    template_name = 'punto_fijo/punto_fijo.html'

    def get(self,request,*args,**kwargs):
        return render(request, self.template_name)

class newton(View):
    template_name = 'newton/newton.html'

    def get(self,request,*args,**kwargs):
        return render(request, self.template_name)   

class raices(View):
    template_name = 'raices/raices.html'

    def get(self,request,*args,**kwargs):
        return render(request, self.template_name)
class secante(View):
    template_name = 'secante/secante.html'

    def get(self,request,*args,**kwargs):
        return render(request, self.template_name)
