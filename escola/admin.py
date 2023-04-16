from django.contrib import admin

from .models import Aluno, Curso, Matricula


@admin.register(Aluno)
class AlunosAdmin(admin.ModelAdmin):
    list_display = ("id", "nome", "rg", "cpf", "data_nascimento")
    list_display_links = ("id", "nome")
    search_fields = ("nome",)
    list_per_page = 5


@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ("id", "codigo_curso", "descricao")
    list_display_links = ("id", "descricao")
    search_fields = ("descricao",)
    list_per_page = 5


@admin.register(Matricula)
class MatriculaAdmin(admin.ModelAdmin):
    list_display = ("id", "aluno", "curso", "periodo")
    list_display_links = (
        "id",
        "aluno",
    )
    search_fields = ("aluno",)
    list_per_page = 5
