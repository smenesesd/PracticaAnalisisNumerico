from django import forms


class Formulario_punto_fijo(forms.Form):
    opciones = [('1','Error absoluto'),('2','Error Relativo')]
    funcion = forms.CharField(label='Funcion fx', required=True, widget=forms.TextInput(attrs={'placeholder':'Ingrese la funcion fx...'}))
    funciong = forms.CharField(label='Funcion gx', required=True, widget=forms.TextInput(attrs={'placeholder':'Ingrese la funcion gx...'}))
    xi = forms.FloatField(label='Xi', required=True, widget=forms.NumberInput(attrs={'placeholder':'Ingrese el x inicial...','step':'0.0001'}))
    iteraciones = forms.IntegerField(label='iteacion', required=True, widget=forms.NumberInput(attrs={'placeholder':'Ingrese el numero de iteraciones...'}))
    tolerancia = forms.FloatField(label='Xi', required=True, widget=forms.NumberInput(attrs={'placeholder':'Ingrese la tolerancia...','step':'0.0001'}))
    opcion = forms.ChoiceField(label='opcion', required=True, widget=forms.RadioSelect, choices=opciones)

