from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Group, Permission
from django.contrib.auth.hashers import make_password


class UsuarioAdministrador(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('El email debe ser proporcionado')

        email = self.normalize_email(email)
        usuario = self.model(email=email, **extra_fields)
        contraseña_encriptada = usuario.set_password(password)
        usuario.make_password(contraseña_encriptada)
        usuario.save(using=self._db)

        return usuario

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields['password'] = make_password(password)
        return self.create_user(email, password, **extra_fields)


class Usuario(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    groups = models.ManyToManyField(
        Group, related_name='usuario_personalizado')
    user_permissions = models.ManyToManyField(
        Permission, related_name='usuario_personalizado')

    objects = UsuarioAdministrador()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nombre', 'apellido']
