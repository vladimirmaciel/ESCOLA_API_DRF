from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from escola.views import AlunosViewSet, CursosViewSet, MatriculaViewSet

"""definindo a rota principal """
router = routers.DefaultRouter()
router.register("alunos", AlunosViewSet, basename="Alunos")
router.register("cursos", CursosViewSet, basename="Cursos")
router.register("matricula", MatriculaViewSet, basename="Matriculas")
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
]
