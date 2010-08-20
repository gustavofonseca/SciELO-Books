# coding: utf-8

from django.db import models
from django.contrib import admin
from scielo_livros.catalogo.fields import ThumbnailImageField

class Livro(models.Model):
    STATUS_CHOICES = (
        (1, u'Aprovado'),
        (2, u'Não Aprovado'),
    )
    
    titulo = models.CharField(max_length=256)
    credito = models.TextField()
    autor = models.ManyToManyField('Autor', blank=True)
    instituicao = models.ForeignKey('Editora')
    ano = models.IntegerField(max_length=4)
    idioma = models.CharField(max_length=32)
    formato = models.CharField(max_length=32)
    paginas = models.CharField(max_length=32)
    isbn = models.CharField(max_length=32)
    assunto = models.CharField(max_length=256)
    sinopse = models.TextField()
    link_catalogo_institucional = models.CharField(max_length=256)
    imagem_da_capa = ThumbnailImageField(upload_to='imagens')
    status = models.IntegerField(max_length=1, choices=STATUS_CHOICES)
    
    def __unicode__(self):
        return self.titulo
        
    class Meta:
        ordering = ['titulo']
    
class LivroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'instituicao', 'isbn', 'ano', 'status',)
    list_filters = ('titulo', 'instituicao', 'ano',)
    search_fields = ('titulo', 'instituicao', 'isbn')
    
class Autor(models.Model):
    nome = models.CharField(max_length=128)
    cv_lattes = models.URLField()
    email = models.EmailField()
    web_site = models.URLField()
    
    def __unicode__(self):
        return self.nome

    class Meta:
        ordering = ['nome']
        verbose_name_plural = 'Autores'
    
class AutorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email',)
    search_fields = ('nome', 'email',)
    
class Editora(models.Model):
    nome = models.CharField(max_length=256)
    
    def __unicode__(self):
        return self.nome
    
class EditoraAdmin(admin.ModelAdmin):
    list_display = ('nome',)