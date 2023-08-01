from django.contrib import admin
from escola.models import Aluno, Curso, Matricula

class Alunos(admin.ModelAdmin):
    list_display=('id','nome','rg','CPF','data_nascimento')
    list_display_links=('id','nome')
    search_fields=('nome',)
    list_per_page=20

admin.site.register(Aluno, Alunos)

class Cursos(admin.ModelAdmin):
    
    list_display=('id','codigo_curso','titulo_curso','descricao')
    list_display_link=('id','titulo_curso')
    search_fields=('titulo_curso',)
    list_per_page=20

admin.site.register(Curso, Cursos)

class Matriculas(admin.ModelAdmin):
    
    list_display=('id','curso')
    list_display_links=('curso',)
    search_fields=('curso',)
    list_per_page=20

admin.site.register(Matricula, Matriculas)