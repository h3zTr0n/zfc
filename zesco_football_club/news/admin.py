from __future__ import absolute_import

from django.contrib import admin
from .models import (Author, Post, Sponser,
                     JuvenilePlayer, VeteranPlayer,
                     SeniorPlayer, History, Ticket)

from image_cropping import ImageCroppingMixin

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created', 'modified', 'author',]
    prepopulated_fields = {'slug': ('title',)}

class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']

# class SponsersAdmin(admin.ModelAdmin):
#     list_display = ['name', 'logo', 'short_discr']

class SponserAdmin(ImageCroppingMixin, admin.ModelAdmin):
    list_display = ['name', 'logo']

class JuvenilePlayerAdmin(admin.ModelAdmin):
    list_display = ['name', 'number']

class VeteranPlayerAdmin(admin.ModelAdmin):
    list_display = ['name', 'number']

class SeniorPlayerAdmin(admin.ModelAdmin):
    list_display = ['name', 'number']

class HistoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'from_year', 'to_year']
admin.site.register(History, HistoryAdmin)

admin.site.register(JuvenilePlayer, JuvenilePlayerAdmin)

admin.site.register(VeteranPlayer, VeteranPlayerAdmin)
admin.site.register(SeniorPlayer, SeniorPlayerAdmin)
admin.site.register(Sponser, SponserAdmin)
# admin.site.register(Sponsers, SponsersAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Post,PostAdmin)

# image thumbnail settings

# class MyModelAdmin(ImageCroppingMixin, admin.ModelAdmin):
#     pass
#
# admin.site.register(MyModel, MyModelAdmin)


class TicketAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email_address',
                    'mobile', 'number_of_seats', 'town_city', 'timestamp']
admin.site.register(Ticket, TicketAdmin)
