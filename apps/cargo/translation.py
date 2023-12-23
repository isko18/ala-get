# core/translation.py
from modeltranslation.translator import register, TranslationOptions
from .models import Cargo, Profitable

@register(Cargo)
class CargoTranslationOptions(TranslationOptions):
    fields = ('title', 'descriptions', 'title2', 'descriptions2')

@register(Profitable)
class ProfitableTranslationOptions(TranslationOptions):
    fields = ('title2','title', 'descriptions')
