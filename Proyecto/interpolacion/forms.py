from django import forms

class Formulario_vander(forms.Form):
    matrizA = forms.CharField(label='MatrizA', required=True, widget=forms.TextInput(attrs={'placeholder':'Ingrese los valores de la matriz A...'}))
    matrizB = forms.CharField(label='MatrizB', required=True, widget=forms.TextInput(attrs={'placeholder':'Ingrese los valores de la matriz B...'}))
    tam = forms.IntegerField(label='n', required=True, widget=forms.NumberInput(attrs={'placeholder':'Ingrese el tamaño de la matriz...'}))

class Formulario_dif(forms.Form):
    matrizA = forms.CharField(label='MatrizA', required=True, widget=forms.TextInput(attrs={'placeholder':'Ingrese los valores de la matriz A...'}))
    matrizB = forms.CharField(label='MatrizB', required=True, widget=forms.TextInput(attrs={'placeholder':'Ingrese los valores de la matriz B...'}))
    tam = forms.IntegerField(label='n', required=True, widget=forms.NumberInput(attrs={'placeholder':'Ingrese el tamaño de la matriz...'}))

class Formulario_spline(forms.Form):
    matrizA = forms.CharField(label='MatrizA', required=True, widget=forms.TextInput(attrs={'placeholder':'Ingrese los valores de la matriz A...'}))
    matrizB = forms.CharField(label='MatrizB', required=True, widget=forms.TextInput(attrs={'placeholder':'Ingrese los valores de la matriz B...'}))
    tam = forms.IntegerField(label='n', required=True, widget=forms.NumberInput(attrs={'placeholder':'Ingrese el tamaño de la matriz...'}))
