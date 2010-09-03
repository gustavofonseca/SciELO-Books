# coding: utf-8

from django.db import models
from django.contrib import admin
from scielo_livros.catalogue.fields import ThumbnailImageField
import datetime

class Book(models.Model):
    STATUS_CHOICES = (
        (1, u'Approved'),
        (2, u'Not Approved'),
    )
    
    title = models.CharField(max_length=256)
    credit = models.TextField()
    organizer = models.TextField()
    coordinator = models.TextField()
    translator = models.TextField()
    edition = models.CharField(max_length=64)
    collection = models.CharField(max_length=64)
    series = models.CharField(max_length=64)
    volume = models.CharField(max_length=64)
    book = models.CharField(max_length=256)
    author = models.ManyToManyField('Author', blank=True)
    publisher = models.ForeignKey('Publisher')
    year = models.IntegerField(max_length=4)
    language = models.CharField(max_length=32)
    format = models.CharField(max_length=32)
    pages = models.CharField(max_length=32)
    isbn = models.CharField(max_length=32)
    subject = models.CharField(max_length=256)
    synopsis = models.TextField()
    institutional_catalogue_link = models.CharField(max_length=256)
    cover_image = ThumbnailImageField(upload_to='images')
    feedback = models.CharField(max_length=256)
    summary = models.CharField(max_length=512)
    pdf = models.CharField(max_length=64)
    approved_at = models.DateField(default=datetime.datetime.now)
    created_at = models.DateTimeField(auto_now=True)
    status = models.IntegerField(max_length=1, choices=STATUS_CHOICES, default=1)
    
    def __unicode__(self):
        return self.title
        
    class Meta:
        ordering = ['title']
    
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'publisher', 'isbn', 'year', 'status',)
    list_filters = ('title', 'publisher', 'year',)
    search_fields = ('title', 'publisher', 'isbn')
    
class Author(models.Model):
    name = models.CharField(max_length=128)
    cv_lattes = models.URLField()
    email = models.EmailField()
    web_site = models.URLField()
    
    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']
    
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email',)
    search_fields = ('name', 'email',)
    
class Publisher(models.Model):
    name = models.CharField(max_length=256)
    
    def __unicode__(self):
        return self.name
    
class PublisherAdmin(admin.ModelAdmin):
    list_display = ('name',)