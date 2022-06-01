from django import forms

class Formulario_crout(forms.Form):
    matrizA = forms.CharField(label='MatrizA', required=True, widget=forms.TextInput(attrs={'placeholder':'Ingrese los valores de la matriz A...'}))
    matrizB = forms.CharField(label='MatrizB', required=True, widget=forms.TextInput(attrs={'placeholder':'Ingrese los valores de la matriz B...'}))

class Formulario_doolittle(forms.Form):
    matrizA = forms.CharField(label='MatrizA', required=True, widget=forms.TextInput(attrs={'placeholder':'Ingrese los valores de la matriz A...'}))
    matrizB = forms.CharField(label='MatrizB', required=True, widget=forms.TextInput(attrs={'placeholder':'Ingrese los valores de la matriz B...'}))

class Formulario_gaussiana(forms.Form):
    matrizA = forms.CharField(label='MatrizA', required=True, widget=forms.TextInput(attrs={'placeholder':'Ingrese los valores de la matriz A...'}))
    tam = forms.IntegerField(label='n', required=True, widget=forms.NumberInput(attrs={'placeholder':'Ingrese el tamaño de la matriz...'}))
    matrizB = forms.CharField(label='MatrizB', required=True, widget=forms.TextInput(attrs={'placeholder':'Ingrese los valores de la matriz B...'}))

class Formulario_gauss_piv_parcial(forms.Form):
    matrizA = forms.CharField(label='MatrizA', required=True, widget=forms.TextInput(attrs={'placeholder':'Ingrese los valores de la matriz A...'}))
    tam = forms.IntegerField(label='n', required=True, widget=forms.NumberInput(attrs={'placeholder':'Ingrese el tamaño de la matriz...'}))
    matrizB = forms.CharField(label='MatrizB', required=True, widget=forms.TextInput(attrs={'placeholder':'Ingrese los valores de la matriz B...'}))

class Formulario_gauss_piv_total(forms.Form):
    matrizA = forms.CharField(label='MatrizA', required=True, widget=forms.TextInput(attrs={'placeholder':'Ingrese los valores de la matriz A...'}))
    tam = forms.IntegerField(label='n', required=True, widget=forms.NumberInput(attrs={'placeholder':'Ingrese el tamaño de la matriz...'}))
    matrizB = forms.CharField(label='MatrizB', required=True, widget=forms.TextInput(attrs={'placeholder':'Ingrese los valores de la matriz B...'}))

class Formulario_factorizacion_LU(forms.Form):
    matrizA = forms.CharField(label='MatrizA', required=True, widget=forms.TextInput(attrs={'placeholder':'Ingrese los valores de la matriz A...'}))
    tam = forms.IntegerField(label='n', required=True, widget=forms.NumberInput(attrs={'placeholder':'Ingrese el tamaño de la matriz...'}))
    matrizB = forms.CharField(label='MatrizB', required=True, widget=forms.TextInput(attrs={'placeholder':'Ingrese los valores de la matriz B...'}))

class Formulario_seidel(forms.Form):
    matrizA = forms.CharField(label='MatrizA', required=True, widget=forms.TextInput(attrs={'placeholder':'Ingrese los valores de la matriz A...'}))
    matrizB = forms.CharField(label='MatrizB', required=True, widget=forms.TextInput(attrs={'placeholder':'Ingrese los valores de la matriz B...'}))
    maxite = forms.IntegerField(label='maxite', required=True, widget=forms.NumberInput(attrs={'placeholder':'Ingrese la maxima iteracion...'}))
    tolerancia = forms.FloatField(label='tol', required=True, widget=forms.NumberInput(attrs={'placeholder':'Ingrese la tolerancia...','step':'0.0001'}))
