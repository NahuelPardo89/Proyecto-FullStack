from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class UsuarioManager(BaseUserManager):
    def _create_user(self, dni, password, is_staff, is_superuser, **extra_fields):
        if not dni:
            raise ValueError('El DNI es obligatorio.')

        nombre = extra_fields.get('nombre')
        apellido = extra_fields.get('apellido')
        email = extra_fields.get('email')
        telefono = extra_fields.get('telefono')
        direccion = extra_fields.get('direccion')

        if not nombre:
            raise ValueError('El nombre es obligatorio.')
        if not apellido:
            raise ValueError('El apellido es obligatorio.')
        if not email:
            raise ValueError('El email es obligatorio.')
        
        

        usuario = self.model(
            dni=dni,
            is_staff=is_staff,
            is_superuser=is_superuser,
            **extra_fields
        )
        usuario.set_password(password)
        usuario.save(using=self._db)
        return usuario

    def create_user(self, dni, password=None, **extra_fields):
        return self._create_user(dni, password, False, False, **extra_fields)

    def create_superuser(self, dni, password=None, **extra_fields):
        return self._create_user(dni, password, True, True, **extra_fields)

class Usuario(AbstractBaseUser, PermissionsMixin):
    dni = models.IntegerField( unique=True)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email= models.EmailField()
    telefono = models.CharField(max_length=15)
    direccion = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    objects = UsuarioManager()

    USERNAME_FIELD = 'dni'
    REQUIRED_FIELDS = ['nombre', 'apellido', 'email']

    def __str__(self):
        return f"{self.dni} - {self.apellido}, {self.nombre}"