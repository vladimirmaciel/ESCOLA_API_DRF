# from django.shortcuts import render
from rest_framework import viewsets
from serializer import AlunoSerializer, CursoSerializer

from .models import Aluno, Curso


class AlunosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os alunos e alunas"""

    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer


class CursosViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
