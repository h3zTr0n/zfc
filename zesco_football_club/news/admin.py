from __future__ import absolute_import

from django.contrib import admin
from .models import Author, Post 

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created', 'modified', 'author',]
    prepopulated_fields = {'slug': ('title',)}

class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']

# class SponsersAdmin(admin.ModelAdmin):
#     list_display = ['name', 'logo', 'short_discr']


# admin.site.register(Sponsers, SponsersAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Post,PostAdmin)
