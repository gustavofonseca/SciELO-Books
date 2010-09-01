from django.contrib import admin
from catalogue.models import Book, BookAdmin, Author, AuthorAdmin, Publisher, PublisherAdmin

admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Publisher, PublisherAdmin)