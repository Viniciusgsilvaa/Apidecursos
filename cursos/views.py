from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics

from .models import Avaliacao, Curso, Professor
from.serializers import AvaliacaoSerializer, CursoSerializer, ProfessorSerializer


class AvaliacoesApiView(APIView):
    """
    API Avaliacoes
    """
    def get(self, request):
        avaliacao = Avaliacao.objects.all()
        serializer = AvaliacaoSerializer(avaliacao, many=True)
        return Response(serializer.data)


class CursosApiView(APIView):
    
    def get(self, request):
        cursos = Curso.objects.all()
        serializer = CursoSerializer(cursos, many=True)
        return Response(serializer.data)


class ProfessorApiView(APIView):

    def get(self, request):
        professor = Professor.objects.all()
        serializer = ProfessorSerializer(professor, many=True)
        return Response(serializer.data)