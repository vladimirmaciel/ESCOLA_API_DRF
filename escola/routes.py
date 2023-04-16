from rest_framework import routers

from escola.views import AlunosViewSet, CursosViewSet, MatriculaViewSet

router = routers.DefaultRouter()
router.register("alunos", AlunosViewSet, basename="Alunos")
router.register("cursos", CursosViewSet, basename="Cursos")
router.register("matricula", MatriculaViewSet, basename="Matriculas")
