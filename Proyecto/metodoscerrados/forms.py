from django import forms


class Formulario_biseccion(forms.Form):
    opciones = [('1','Error absoluto'),('2','Error Relativo')]
    funcion = forms.CharField(label='Funcion fx', required=True, widget=forms.TextInput(attrs={'placeholder':'Ingrese la funcion fx...'}))
    xi = forms.IntegerField(label='Xi', required=True, widget=forms.NumberInput(attrs={'placeholder':'Ingrese el x inicial...','step':'0.0001'}))
    xf = forms.IntegerField(label='Xi', required=True, widget=forms.NumberInput(attrs={'placeholder':'Ingrese el x final...','step':'0.0001'}))
    tolerancia = forms.IntegerField(label='Xi', required=True, widget=forms.NumberInput(attrs={'placeholder':'Ingrese la tolerancia...','step':'0.0001'}))
    opcion = forms.ChoiceField(label='opcion', required=True, widget=forms.RadioSelect, choices=opciones)

