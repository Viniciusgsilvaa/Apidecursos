from django.urls import path
from .views import (
    AvaliacoesApiView,
    AvaliacaoApiView, 
    CursosApiView,
    CursoApiView, 
    ProfessoresApiView,
    ProfessorApiView,
    IndexView
)

urlpatterns = [
    
    path('avaliacao/<int:pk>/', AvaliacaoApiView.as_view(), name='avaliacao'),
    path('avaliacoes/', AvaliacoesApiView.as_view(), name='avaliacoes'),
    path('curso/<int:pk>/', CursoApiView.as_view(), name='curso'),
    path('cursos/', CursosApiView.as_view(), name='cursos'),
    path('professor/<int:pk>/', ProfessorApiView.as_view(), name='professor'),
    path('professores', ProfessoresApiView.as_view(), name='professores')
]