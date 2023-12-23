# core/admin.py
from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from modeltranslation.admin import TranslationAdmin
from .models import Cargo, Profitable

@admin.register(Cargo)
class CargoAdmin(TranslationAdmin):
    list_display = ('title', 'descriptions', 'banner_image', 'title2', 'descriptions2')

@admin.register(Profitable)
class ProfitableAdmin(TranslationAdmin):
    list_display = ('title2','title', 'descriptions', 'image')
