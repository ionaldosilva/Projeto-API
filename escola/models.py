from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length=30, blank=False, null=False)
    rg = models.CharField(max_length=10, blank=False, null=False)
    CPF = models.CharField(max_length=11, blank=False, null=False)
    data_nascimento = models.DateField(blank=False, null=False)

    def __str__(self):
        return self.nome

class Curso(models.Model):
    NIVEL = (
        ('B','Básico'),
        ('I','Intermediário'),
        ('A','Avançado')

    )
    codigo_curso = models.CharField(max_length=10, blank=False, null=False)
    titulo_curso = models.CharField(max_length=30, blank=False, null=False)
    descricao = models.TextField(max_length=150)
    nivel = models.CharField(max_length=1, blank=False, null=False, choices=NIVEL, default='B')

    def __str__(self):
        return self.titulo_curso
    
class Matricula(models.Model):
    PERIODO = [
        ('M','Matutino'),
        ('V','Vespertino'),
        ('N','Noturno')
    ]
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    periodo = models.CharField(max_length=1, blank=False, null=False, choices=PERIODO, default='M')