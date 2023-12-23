# core/admin.py
from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Taxi, TypesTaxi

class TaxiAdmin(TranslationAdmin):
    list_display = ('title', 'title2', 'advantage1', 'advantage2', 'advantage3', 'title_order', 'title_order2')

class TypesTaxiAdmin(TranslationAdmin):
    list_display = ('slide_title', 'title', 'title2')

admin.site.register(Taxi, TaxiAdmin)
admin.site.register(TypesTaxi, TypesTaxiAdmin)
