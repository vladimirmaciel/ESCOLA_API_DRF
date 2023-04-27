# from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

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
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class CursosViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class MatriculaViewSet(viewsets.ModelViewSet):
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class ListaMatriculasAluno(generics.ListAPIView):
    """Listando as matrículas de um alunou ou aluna"""

    def get_queryset(self):
        return Matricula.objects.filter(aluno_id=self.kwargs["pk"])

    serializer_class = ListaMatriculaAlunoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class ListaAlunosMatriculados(generics.ListAPIView):
    """Listando alunos e alunas maticulados em um curso"""

    def get_queryset(self):
        return Matricula.objects.filter(curso_id=self.kwargs["pk"])

    serializer_class = ListaAlunosMatriculadosSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
