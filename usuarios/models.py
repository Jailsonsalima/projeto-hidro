from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser
from empresas.models import Empresa



class Usuario(AbstractUser):
    TIPOS_USUARIO = [
        ('GERENTE_MATRIZ', 'Gerente Matriz'),
        ('GERENTE_FILIAL', 'Gerente Filial'),
        ('GESTOR_MATRIZ', 'Gestor Matriz'),
        ('GESTOR_FILIAL', 'Gestor Filial'),
        ('FUNCIONARIO', 'Funcionário'),
    ]
    

    id = models.BigAutoField(primary_key=True, verbose_name="ID")
    username = models.CharField(max_length=150, unique=True, verbose_name='username')
    password = models.CharField(max_length=128, verbose_name='password')
    email = models.EmailField(blank=True, max_length=254, verbose_name='email address')
    
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, null=True, blank=True)
    tipo_usuario = models.CharField(max_length=20, choices=TIPOS_USUARIO, null=True, blank=True)
    status_ativo = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.username} - {self.tipo_usuario}"