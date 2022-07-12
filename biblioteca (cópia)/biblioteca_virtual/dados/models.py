from django.db import models

# Create your models here.


class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    rg = models.CharField(max_length=20)
    cpf = models.CharField(max_length=20)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)

    def __str__(self):
        return self.nome
