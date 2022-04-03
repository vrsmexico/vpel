from django.db import models
from django.db.models.base import Model
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class profile(models.Model):
    usuario=models.CharField(max_length=100,null=True,blank=True)
    telelefono=models.CharField(max_length=100,null=True,blank=True)
    direccion=models.CharField(max_length=100,null=True,blank=True)
    pedido=models.CharField(max_length=100,null=True,blank=True)
    otros=models.CharField(max_length=100,null=True,blank=True)
    def __str__(self):
        return self.usuario



class historial(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE, related_name='historial')
    timestamp=models.DateTimeField(default=timezone.now)
    content=models.TextField()
    class Meta:
        ordering=['-timestamp']
    def __str__(self):
        return f'{self.user.username}:{self.content}'
class genero(models.Model):

    genero=models.CharField(max_length=50)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name='genero'
        verbose_name_plural='generos'
    def __str__(self):
        return self.genero
class calidad(models.Model):

    calidad=models.CharField(max_length=50)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name='calidad'
        verbose_name_plural='calidades'
    def __str__(self):
        return self.calidad
class fecha(models.Model):

    fecha=models.CharField(max_length=4)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name='fecha'
        verbose_name_plural='fechas'
        ordering=['-fecha']

    def __str__(self):
        return self.fecha
class calificacion(models.Model):

    calificacion=models.CharField(max_length=1)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name='calificacion'
        verbose_name_plural='calificaciones'
    def __str__(self):
        return self.calificacion
class tipo(models.Model):

    tipo=models.CharField(max_length=50)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name='tipo'
        verbose_name_plural='tipos'
    def __str__(self):
        return self.tipo
    

class servicio(models.Model):
    titulo1=models.CharField(max_length=50,unique=True)
    titulo2=models.CharField(max_length=50,null=True,blank=True)
    titulo3=models.CharField(max_length=50,null=True,blank=True)
    titulo4=models.CharField(max_length=50,null=True,blank=True)
    tlim1=models.CharField(max_length=50,null=True,blank=True)
    tlim2=models.CharField(max_length=50,null=True,blank=True)
    tlim3=models.CharField(max_length=50,null=True,blank=True)
    tlim4=models.CharField(max_length=50,null=True,blank=True)
    precio=models.FloatField(null=True,blank=True)
    genero=models.ManyToManyField(genero)
    calidad=models.ForeignKey(calidad,on_delete=models.PROTECT,null=True,blank=True)
    tipo=models.ForeignKey(tipo,on_delete=models.PROTECT,null=True,blank=True)
    fecha=models.ForeignKey(fecha,on_delete=models.PROTECT,null=True,blank=True)
    calificacion=models.ForeignKey(calificacion,on_delete=models.PROTECT,null=True,blank=True)
    calif=models.CharField(max_length=1,null=True,blank=True)
    sinop=models.CharField(max_length=200,null=True,blank=True)
    peso=models.FloatField()
    imagen=models.ImageField(upload_to='servicios')
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name='servicio'
        verbose_name_plural='servicios'
        ordering=['fecha','-created']
    def __str__(self):
        return f'{self.titulo1}'

class Pedidos(models.Model):
    user=models.CharField(max_length=100,null=True,blank=True)
    timestamp=models.DateTimeField(default=timezone.now)
    content=models.TextField(null=True,blank=True)
    comentarios=models.TextField(null=True,blank=True)
    entregado=models.BooleanField(default=False)
    memorias=models.TextField(null=True,blank=True)
    masinfo=models.TextField(null=True,blank=True)

    class Meta:
        ordering=['-timestamp']
    def __str__(self):
        return f'{self.user}:{self.content}'
class Gastos(models.Model):
    created=models.DateTimeField(auto_now_add=True)
    cantidad=models.FloatField(null=True,blank=True)
    ganoper=models.BooleanField(default=False)
    concep=models.CharField(max_length=50,null=True,blank=True)
    importancia=models.BooleanField(default=False)
    class Meta:
        ordering=['-created']
    def __str__(self):
        return f'{self.cantidad}'
class Cuentas(models.Model):
    create=models.DateTimeField(auto_now_add=True)
    canti=models.FloatField(null=True,blank=True)
    ganper=models.BooleanField(default=False)
    conce=models.CharField(max_length=50,null=True,blank=True)
    importa=models.BooleanField(default=False)
    entraporcen=models.BooleanField(default=False)
    class Meta:
        ordering=['-create']
    def __str__(self):
        return f'{self.canti}'