from django.forms import BaseModelForm
from django.http import HttpResponse
from django.views.generic import TemplateView
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Avaliacao, Curso, Professor
from.serializers import AvaliacaoSerializer, CursoSerializer, ProfessorSerializer
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.models import User
from .forms import UserRegisterForm

class IndexView(TemplateView):
    template_name = 'index.html'


class UserCreateView(CreateView):
    model = User
    forms = UserRegisterForm
    template_name = 'register.html'
    success_url = reverse_lazy('')

    def form_valid(self, form):

        return super().form_valid(form)
    
"""
API V1
"""

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


"""
API V2
"""

class AvaliacaoViewSet(viewsets.ModelViewSet):
    queryset =  Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer


class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

    @action(detail=True, methods=['get'])
    def avaliacoes(self, request, pk=None):
        curso = self.get_object()
        serializer = AvaliacaoSerializer(curso.avaliacoes.all(), many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def professores(self, request, pk=None):
        curso = self.get_object()
        serializer = ProfessorSerializer(curso.professores.all(), many=True)
        return Response(serializer.data)

class ProfessorViewSet(viewsets.ModelViewSet):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer


