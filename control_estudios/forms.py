from django import forms

class Torneoformulario(forms.Form):
   nombre_torneo = forms.CharField(required=True, max_length=64)
   fecha_comienzo = forms.DateField(required=True)
   
class Jugadorformulario(forms.Form):
   nombre = forms.CharField(required=True, max_length=64)
   apellido = forms.CharField(max_length=256)
   fecha_nacimiento = forms.DateField()
   telefono = forms.CharField(max_length=20)
   

class Rankingformulario(forms.Form):
   nombre = forms.CharField(max_length=256)
   apellido = forms.CharField(max_length=256)
   cantidad_puntos = forms.CharField(max_length=10000000000000)
   torneos_jugados = forms.CharField(max_length=10000000000000)
   