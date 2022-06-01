from django import forms


class Formulario_gaussiana(forms.Form):
    matrizA = forms.CharField(label='MatrizA', required=True, widget=forms.TextInput(attrs={'placeholder':'Ingrese los valores de la matriz A...'}))
    tam = forms.IntegerField(label='n', required=True, widget=forms.NumberInput(attrs={'placeholder':'Ingrese el tamaño de la matriz...'}))
    matrizB = forms.CharField(label='MatrizB', required=True, widget=forms.TextInput(attrs={'placeholder':'Ingrese los valores de la matriz B...'}))
