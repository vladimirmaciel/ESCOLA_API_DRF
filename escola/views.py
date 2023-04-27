# from django.shortcuts import render
from rest_framework import generics, viewsets

from escola.serializer import (
    AlunoSerializer,
    CursoSerializer,
    ListaAlunosMatriculadosSerializer,
    ListaMatriculaAlunoSerializer,
    MatriculaSerializer,
)

from .models import Aluno, Curso, Matricula


class AlunosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os alunos e alunas"""

    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer


class CursosViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer


class MatriculaViewSet(viewsets.ModelViewSet):
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer


class ListaMatriculasAluno(generics.ListAPIView):
    """Listando as matrículas de um alunou ou aluna"""

    def get_queryset(self):
        return Matricula.objects.filter(aluno_id=self.kwargs["pk"])

    serializer_class = ListaMatriculaAlunoSerializer


class ListaAlunosMatriculados(generics.ListAPIView):
    """Listando alunos e alunas maticulados em um curso"""

    def get_queryset(self):
        return Matricula.objects.filter(curso_id=self.kwargs["pk"])

    serializer_class = ListaAlunosMatriculadosSerializer
    