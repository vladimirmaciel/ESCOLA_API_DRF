from django.contrib import admin
from django.urls import include, path

from escola.routes import router
from escola.views import ListaAlunosMatriculados, ListaMatriculasAluno

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
    path("alunos/<int:pk>/matriculas/", ListaMatriculasAluno.as_view()),
    path("cursos/<int:pk>/matriculas/", ListaAlunosMatriculados.as_view()),
]
