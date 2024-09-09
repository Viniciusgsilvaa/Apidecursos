from django.urls import path
from .views import AvaliacoesApiView, CursosApiView, ProfessorApiView

urlpatterns = [
    path('avaliacoes/', AvaliacoesApiView.as_view(), name='avaliacoes'),
    path('cursos/', CursosApiView.as_view(), name='cursos'),
    path('professor', ProfessorApiView.as_view(), name='professor')
]