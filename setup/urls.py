from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from escola.views import AlunosViewSet, CursosViewSet

"""definindo a rota principal """
router = routers.DefaultRouter()
router.register("alunos", AlunosViewSet, basename="Alunos")
router.register("cursos", CursosViewSet, basename="Cursos")
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
]
