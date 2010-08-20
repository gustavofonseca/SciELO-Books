from django.contrib import admin
from catalogo.models import Livro, LivroAdmin, Autor, AutorAdmin, Editora, EditoraAdmin

admin.site.register(Livro, LivroAdmin)
admin.site.register(Autor, AutorAdmin)
admin.site.register(Editora, EditoraAdmin)