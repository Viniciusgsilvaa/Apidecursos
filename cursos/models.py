from django.db import models


class Base(models.Model):

    criacao = models.DateTimeField(auto_now_add=True)
    atualizacao = models.DateTimeField(auto_now=True)
    ativo = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Curso(Base):

    titulo = models.CharField(max_length=255)
    url = models.URLField(unique=True)

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
        ordering = ['id']
    
    def __str__(self):
        return self.titulo


class Avaliacao(Base):

    curso = models.ForeignKey(Curso, related_name='avaliacoes', on_delete=models.CASCADE)
    nome = models.CharField(max_length=255)
    email = models.EmailField()
    comentario = models.TextField(blank=True, default='')
    avaliacao = models.DecimalField(decimal_places=1, max_digits=2)

    class Meta:
        verbose_name = 'Avaliação'
        verbose_name_plural = 'Avaliações'
        unique_together = ['email', 'curso']
        ordering = ['id']
    
    def __str__(self):
        return f'{self.nome} avaliou curso: {self.curso} com a nota {self.avaliacao}'


class Professor(Base):

    curso = models.ForeignKey(Curso, related_name='professores', on_delete=models.CASCADE)
    nome = models.CharField(max_length=255)
    registro = models.IntegerField(unique=True)

    class Meta:
        verbose_name = 'professor'
        verbose_name_plural = 'professores'
        ordering = ['id']
        
    def __str__(self):
        return self.nome