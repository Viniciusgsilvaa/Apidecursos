from django.views.generic import TemplateView
from rest_framework import generics

from .models import Avaliacao, Curso, Professor
from.serializers import AvaliacaoSerializer, CursoSerializer, ProfessorSerializer

class IndexView(TemplateView):
    template_name = 'index.html'
    

class AvaliacoesApiView(generics.ListCreateAPIView):
   queryset = Avaliacao.objects.all()
   serializer_class = AvaliacaoSerializer


class AvaliacaoApiView(generics.RetrieveUpdateDestroyAPIView):
   queryset = Avaliacao.objects.all()
   serializer_class = AvaliacaoSerializer


class CursosApiView(generics.ListCreateAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer


class CursoApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

class ProfessoresApiView(generics.ListCreateAPIView):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer


class ProfessorApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer