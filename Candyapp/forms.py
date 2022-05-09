from dataclasses import fields
from django.db import models
from django import forms
from .models import *


class lgForm(forms.ModelForm):
    class Meta:
        model=lugar
        fields='__all__'

class productoForm(forms.ModelForm):
    class Meta:
        model=producto
        fields='__all__'

class usuarioForm(forms.ModelForm):
    class Meta:
        model=usuarios
        fields='__all__'

class msForm(forms.ModelForm):
    class Meta:
        model=materia_s
        fields='__all__'

class dtMsForm(forms.Form):
    nombre = forms.CharField(label="Nombre *")
    descripcion = forms.CharField(label="Descripcion", required=False)

class mpForm(forms.ModelForm):
    class Meta:
        model=materia_p
        fields='__all__'

class dtMpForm(forms.Form):
    nombre = forms.CharField(label="Nombre *")
    cantidad = forms.IntegerField(label="Cantidad *")
    unidad = forms.CharField(label="Unidad *")
    costo = forms.IntegerField(label="Costo *")
    proveedor = forms.CharField(label="Proveedor *")
    contacto = forms.CharField(label="Contacto", required=False)
    tiempo = forms.CharField(label="Tiempo de entrega", required=False)
    mincant = forms.IntegerField(label="Minima compra", required=False)
    descripcion = forms.CharField(label="Descripcion", required=False)


class mzForm(forms.ModelForm):
    class Meta:
        model = mezcla
        fields = '__all__'

class dtMzForm(forms.Form):    
    materia_p = forms.CharField(label="Materia prima *") 
    cantidad = forms.IntegerField(label="Cantidad *")   

class psForm(forms.ModelForm):
    class Meta:
        model=posicion
        fields='__all__'

class dtPsForm(forms.Form):
    nombre = forms.CharField(label="Nombre *")
    precio = forms.IntegerField(label="Precio *")

class mnForm(forms.ModelForm):
    class Meta:
        model=menu
        fields='__all__'

class dtMnForm(forms.Form):
    materia_s = forms.CharField(label="Materia secundaria")         

class crForm(forms.ModelForm):
    class Meta:
        model=candycarrito
        fields='__all__'
    
class arForm(forms.ModelForm):
    class Meta:
        model=armado
        fields='__all__'

class dtEnForm(forms.Form):
    mesa = forms.CharField(label="Mesa")
    cliente = forms.CharField(label="Cliente")

class enForm(forms.ModelForm):
    class Meta:
        model=entregado
        fields='__all__'

class ftForm(forms.ModelForm):
    class Meta:
        model=factura
        fields='__all__'

class inftForm(forms.ModelForm):
    class Meta:
        model=infofactura
        fields='__all__'

class enviarForm(forms.Form):
    lugar = forms.CharField(label="Lugar *")
    cantidad = forms.IntegerField(label="Cantidad *")