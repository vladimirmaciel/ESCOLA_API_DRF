from django.contrib import admin

from .models import Aluno, Curso


@admin.register(Aluno) 
class AlunosAdmin(admin.ModelAdmin):
    list_display = ('id','nome','rg', 'cpf', 'data_nascimento')
    list_display_links = ('id','nome')
    search_fields =('nome',)
    list_per_page = 5
    
@admin.register(Curso) 
class CursoAdmin(admin.ModelAdmin):
    list_display = ('id','codigo_curso','descricao')
    list_display_links = ('id','descricao')
    search_fields =('descricao',)
    list_per_page = 5
