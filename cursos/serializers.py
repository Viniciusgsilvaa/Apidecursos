from rest_framework import serializers

from . models import Avaliacao, Curso, Professor


class CursoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Curso
        extra_kwargs = {
            'email': {'write_only': True}
        }
        fields = (
            'titulo',
            'url'
        )


class AvaliacaoSerializer(serializers.ModelSerializer):
    curso = serializers.CharField(source='curso.titulo', read_only=True)

    class Meta:
        extra_kwargs = {
            'email': {'write_only': True}
        }
        model = Avaliacao
        fields = (
            'id',
            'curso',
            'email',
            'comentario',
            'avaliacao',
            'publicacao',
            'ativo'
        )


class ProfessorSerializer(serializers.ModelSerializer):
    curso = serializers.CharField(source='curso.titulo', read_only=True)

    class Meta:
        model = Professor
        fields = (
            'nome',
            'registro',
            'curso',
            'publicacao',
            'ativo'
        )