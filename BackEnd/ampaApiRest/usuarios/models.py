from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class UsuarioManager(BaseUserManager):
    def create_user(self, dni, password=None, nombre=None, apellido=None, telefono=None, direccion=None, is_staff=False, is_superuser=False,**extra_fields):
        if not dni:
            raise ValueError('El DNI es requerido')

        user = self.model(
            dni=dni,
            nombre=nombre,
            apellido=apellido,
            telefono=telefono,
            direccion=direccion,
            is_staff=is_staff,
            is_superuser=is_superuser
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, dni, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superusuario debe tener is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superusuario debe tener is_superuser=True.')

        return self.create_user(dni, password, **extra_fields)

class Usuario(AbstractBaseUser, PermissionsMixin):
    dni = models.CharField(primary_key=True, max_length=10, unique=True)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    telefono = models.CharField(max_length=15)
    direccion = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UsuarioManager()

    USERNAME_FIELD = 'dni'
    REQUIRED_FIELDS = ['nombre', 'apellido', 'telefono', 'direccion']

    def __str__(self):
        return f"{self.dni} - {self.apellido}, {self.nombre}"