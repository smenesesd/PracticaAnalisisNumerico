from django import forms


class Formulario_biseccion(forms.Form):
    opciones = [('1','Error absoluto'),('2','Error Relativo')]
    funcion = forms.CharField(label='Funcion fx', required=True, widget=forms.TextInput(attrs={'placeholder':'Ingrese la funcion fx...'}))
    xi = forms.FloatField(label='Xi', required=True, widget=forms.NumberInput(attrs={'placeholder':'Ingrese el x inicial...','step':'0.00000000001'}))
    xf = forms.FloatField(label='Xi', required=True, widget=forms.NumberInput(attrs={'placeholder':'Ingrese el x final...','step':'0.00000000001'}))
    tolerancia = forms.FloatField(label='Xi', required=True, widget=forms.NumberInput(attrs={'placeholder':'Ingrese la tolerancia...','step':'0.00000000001'}))
    opcion = forms.ChoiceField(label='opcion', required=True, widget=forms.RadioSelect, choices=opciones)

class Formulario_regla_falsa(forms.Form):
    opciones = [('1', 'Error absoluto'),('2','Error Relativo')]
    funcion = forms.CharField(label='Funcion fx', required=True, widget=forms.TextInput(attrs={'placeholder':'Ingrese la funcion fx...'}))
    xi = forms.FloatField(label='Xi', required=True, widget=forms.NumberInput(attrs={'placeholder':'Ingrese el x inicial...','step':'0.00000000001'}))
    xf = forms.FloatField(label='Xi', required=True, widget=forms.NumberInput(attrs={'placeholder':'Ingrese el x final...','step':'0.00000000001'}))
    tolerancia = forms.FloatField(label='Xi', required=True, widget=forms.NumberInput(attrs={'placeholder':'Ingrese la tolerancia...','step':'0.00000000001'}))
    opcion = forms.ChoiceField(label='opcion', required=True, widget=forms.RadioSelect, choices=opciones)

class Formulario_incremental(forms.Form):
    funcion = forms.CharField(label='Funcion fx', required=True, widget=forms.TextInput(attrs={'placeholder':'Ingrese la funcion fx...'}))
    xi = forms.FloatField(label='Xi', required=True, widget=forms.NumberInput(attrs={'placeholder':'Ingrese el x inicial...','step':'0.00000000001'}))
    maxite = forms.IntegerField(label='maxite', required=True, widget=forms.NumberInput(attrs={'placeholder':'Ingrese la maxima iteracion...'}))
    difx = forms.FloatField(label='difx', required=True, widget=forms.NumberInput(attrs={'placeholder':'Ingrese la diferencia de x...','step':'0.00000000001'}))
