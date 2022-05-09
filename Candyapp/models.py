from distutils.command.upload import upload
from pyexpat import model
from django.db import models

# Create your models here.
class lugar(models.Model):
    id_lg = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, verbose_name="Lugar")

class usuarios(models.Model):
    id_us = models.IntegerField(primary_key=True, verbose_name="Identificacion")
    nombre = models.CharField(max_length=50, verbose_name="Nombre")
    apellido = models.CharField(max_length=50, verbose_name="Apellido")
    ocupacion = models.CharField(max_length=20, verbose_name="Ocupacion")
    usuario = models.CharField(default='id_us', max_length=20, verbose_name="Usuario")
    contraseña = models.CharField(max_length=50, verbose_name="Contraseña")
    lugar = models.CharField(max_length=20, verbose_name="Lugar")

class producto(models.Model):
    id_pd = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20, verbose_name="nombre")
    imagen = models.ImageField(upload_to='imagenes/', null=True, verbose_name="imagen")
    descripcion = models.TextField(max_length=100, null=True, verbose_name="descripcion")
    precio = models.IntegerField(verbose_name="Precio base")
    id_lg = models.ForeignKey(lugar, verbose_name="Lugar", on_delete=models.CASCADE)

    def __str__(self):
        fila = "Nombre: " + self.nombre + " - Descripcion: " + self.descripcion
        return fila

    def delete(self, using= None, keep_parents= False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()

class materia_s(models.Model):
    id_ms = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20, verbose_name="nombre")
    descripcion = models.TextField(max_length=100, verbose_name="descripcion")
    estado = models.CharField(max_length=20, verbose_name="estado")
    id_lg = models.ForeignKey(lugar, verbose_name="Lugar", on_delete=models.CASCADE)

class materia_p(models.Model):
    id_mp = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20, verbose_name="nombre")
    cantidad = models.IntegerField(verbose_name="cantidad")
    unidad = models.CharField(max_length=10, verbose_name="unidad")
    costo = models.IntegerField(verbose_name="costo")
    costo_u = models.IntegerField(verbose_name="costo unitario")
    proveedor = models.CharField(max_length=30, verbose_name="proveedor")
    contacto = models.CharField(max_length=14, verbose_name="contacto", null=True)
    tiempo = models.CharField(max_length=14, verbose_name="tiempo de entrega", null=True)
    mincant = models.IntegerField(verbose_name="cantidad minima", null=True)
    descripcion = models.TextField(max_length=100, verbose_name="descripcion", null=True)
    estado = models.CharField(max_length=20, verbose_name="estado")
    id_lg = models.ForeignKey(lugar, verbose_name="Lugar", on_delete=models.CASCADE)

class mezcla(models.Model):
    id_mz = models.AutoField(primary_key=True)
    id_ms = models.ForeignKey(materia_s, verbose_name="materia secundaria", on_delete=models.CASCADE)
    id_mp = models.ForeignKey(materia_p, verbose_name="materia primaria", on_delete=models.CASCADE)
    cantidad = models.IntegerField(verbose_name="cantidad")
    costo=models.IntegerField(verbose_name="costo")

class posicion(models.Model):
    id_ps = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20, verbose_name="nombre")
    precio = models.IntegerField(verbose_name="precio")
    id_pd = models.ForeignKey(producto, verbose_name="producto", on_delete=models.CASCADE)

class menu(models.Model):
    id_mn = models.AutoField(primary_key=True)
    id_ms = models.ForeignKey(materia_s, verbose_name="materia secundaria", on_delete=models.CASCADE)
    id_ps = models.ForeignKey(posicion, verbose_name="posicion", on_delete=models.CASCADE)

class factura(models.Model):
    id_ft = models.AutoField(primary_key=True)
    id_lg = models.ForeignKey(lugar, verbose_name="Lugar", on_delete=models.CASCADE)

class candycarrito(models.Model):
    id_cr = models.AutoField(primary_key=True)
    id_pd = models.ForeignKey(producto, verbose_name="producto", on_delete=models.CASCADE)
    nombre_pd = models.CharField(max_length=20, null=True)
    precio = models.IntegerField(verbose_name="precio", null=True)
    id_lg = models.ForeignKey(lugar, verbose_name="Lugar", on_delete=models.CASCADE)

class armado(models.Model):
    id_ar = models.AutoField(primary_key=True)
    id_cr = models.ForeignKey(candycarrito, verbose_name="carrito", on_delete=models.CASCADE)
    id_mn = models.ForeignKey(menu, verbose_name="menu", on_delete=models.CASCADE)
    nombre_ms = models.CharField(max_length=20, null=True)
    precio = models.IntegerField(null=True)
               
class entregado(models.Model):
    id_eg = models.AutoField(primary_key=True) 
    mesa =  models.CharField(max_length=50)    
    cliente = models.CharField(max_length=50, null=True)   
    id_cr = models.CharField(max_length=50, verbose_name="carrito")
    descripcion = models.CharField(max_length=100, null=True)
    precio = models.IntegerField(null=True)
    preciot = models.IntegerField(null=True)
    id_lg = models.ForeignKey(lugar, verbose_name="Lugar", on_delete=models.CASCADE)

class infofactura(models.Model):
    id_if = models.AutoField(primary_key=True)
    precio = models.IntegerField(verbose_name="precio")
    entregado = models.IntegerField(verbose_name="valor entregado")
    producto = models.CharField(max_length=50, verbose_name="producto")
    adiciones = models.CharField(max_length=50, verbose_name="adiciones")
    fecha = models.CharField(max_length=50, verbose_name="Fecha")
    id_ft = models.IntegerField(verbose_name="factura")
    lugar = models.CharField(max_length=50, verbose_name="Lugar")
