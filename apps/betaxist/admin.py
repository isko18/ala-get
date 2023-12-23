from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Betaxist, EarnMoney

@admin.register(Betaxist)
class BetaxistAdmin(TranslationAdmin):
    list_display = ('title', 'title2', 'join_title', 'earnmoney_title', 'earnmoney_descriptions')


@admin.register(EarnMoney)
class EarnMoneyAdmin(TranslationAdmin):
    list_display = ('title', 'descriptions', 'numbers')

