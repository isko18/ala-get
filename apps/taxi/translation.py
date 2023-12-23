# core/translation.py
from modeltranslation.translator import translator, TranslationOptions
from .models import Taxi, TypesTaxi

class TaxiTranslationOptions(TranslationOptions):
    fields = ('title', 'title2', 'descriptions', 'advantage1', 'advantage2', 'advantage3', 'title_order', 'title_order2')

class TypesTaxiTranslationOptions(TranslationOptions):
    fields = ('slide_title', 'title', 'descriptions', 'title2', 'descriptions2')

translator.register(Taxi, TaxiTranslationOptions)
translator.register(TypesTaxi, TypesTaxiTranslationOptions)
