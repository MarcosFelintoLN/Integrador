from django.db import models
from django.contrib.auth.models import AbstractUser

class Courses(models.Model):
    name = models.CharField("Nome do curso", max_length=120)

    def __str__(self):
        return self.name

class CustomUser(AbstractUser):
    gender_choice = (
        ('Masculino', 'Masculino'),
        ('Feminino', 'Feminino'),
    )
    
    shift_choice = (
        ('M', 'Matutino'),
        ('V', 'Vespertino'),
    )
    period_choice = (
        ('1', '1º Período'),
        ('2', '2º Período'),
        ('3', '3º Período'),
        ('4', '4º Período'),
    )
    course = models.ForeignKey(Courses, on_delete=models.CASCADE, blank=True, null=True)
    genero = models.CharField(max_length=9, choices=gender_choice)
    turno = models.CharField(max_length=1, choices=shift_choice)
    periodo = models.CharField(max_length=1, choices=period_choice)
    image = models.ImageField(upload_to='profile', null=True)
    
    def __str__(self):
        return self.username


class Competicao(models.Model):
    nome = models.CharField("Nome da competição", max_length=120)
    usuarios = models.ManyToManyField(CustomUser)

    def __str__(self):
        return self.nome


class Modalidade(models.Model):
    genero_modalidade_escolha = (
        ('Masculino', 'Masculino'),
        ('Feminino', 'Feminino'),
    )

    nome = models.CharField("Nome da modalidade", max_length=120)
    genero_modalidade = models.CharField(max_length=9, choices=genero_modalidade_escolha)
    competicao1 = models.ForeignKey(Competicao, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
    
class Equipes(models.Model):
    shift_choice = (
        ('M', 'Matutino'),
        ('V', 'Vespertino'),
    )
    period_choice = (
        ('1', '1º Período'),
        ('2', '2º Período'),
        ('3', '3º Período'),
        ('4', '4º Período'),
    )
    nome = models.CharField("Nome da Equipe", max_length=120)
    curso_equipe = models.ForeignKey(Courses, on_delete=models.CASCADE, default=None)
    turno = models.CharField(max_length=1, choices=shift_choice)
    periodo = models.CharField(max_length=1, choices=period_choice)
    participantes = models.ManyToManyField(CustomUser)
    modalidade_equipe = models.ForeignKey(Modalidade, on_delete=models.CASCADE, default=None)
    
    def __str__(self):
        return self.nome