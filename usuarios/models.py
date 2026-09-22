from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    ROL_CHOICES = (
        ('ADMIN', 'administrador'),
        ('GUIA', 'Guia'),
        ('TURISTA', 'Turista'),
    )
    TIPO_DOCUMENTO_CHOICES = (
        ('CC', 'Cedula de Ciudadania'),
        ('CE', 'Cedula de Extranjeria'),
        ('PAS', 'Pasaporte'),
        ('PPT', 'Permiso temporal de permanencia'),
        ('TI', 'Tarjeta de Identidad'),
        ('NIT', 'NIT'),
    )
    first_name = models.CharField( max_length=50, blank = False, verbose_name="nombre")
    last_name = models.CharField(max_length=50, blank = False, verbose_name="apellido")
    tipo_documento = models.CharField(max_length=3,choices=TIPO_DOCUMENTO_CHOICES ,verbose_name="Tipo de Documento")
    documento = models.CharField(max_length=20,unique=True,verbose_name="Documento")
    fecha_nacimiento = models.DateField(blank=True, verbose_name="Fecha de Nacimiento")
    rol = models.CharField(max_length=10,choices=ROL_CHOICES,default='TURISTA',verbose_name="Rol")
    REQUIRED_FIELDS = ["first_name", "last_name", "tipo_documento", "documento", "fecha_nacimiento"] # Esta linea hace que sea obligatorio llenar los campos en la terminal para el super Admin
    
    
    
    
    