from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import (
    AvaliacoesApiView,
    AvaliacaoApiView,
    AvaliacaoViewSet, 
    CursosApiView,
    CursoApiView,
    CursoViewSet, 
    ProfessoresApiView,
    ProfessorApiView,
    ProfessorViewSet,
)

router = SimpleRouter()
router.register('avaliacoes', AvaliacaoViewSet, basename='avaliacoes')
router.register('cursos', CursoViewSet, basename='cursos')
router.register('professores', ProfessorViewSet, basename='professores')


urlpatterns = [
    
    path('avaliacao/<int:pk>/', AvaliacaoApiView.as_view(), name='avaliacao'),
    path('avaliacoes/', AvaliacoesApiView.as_view(), name='avaliacoes'),
    path('curso/<int:pk>/', CursoApiView.as_view(), name='curso'),
    path('cursos/', CursosApiView.as_view(), name='cursos'),
    path('professor/<int:pk>/', ProfessorApiView.as_view(), name='professor'),
    path('professores', ProfessoresApiView.as_view(), name='professores')
]