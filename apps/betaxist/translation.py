from modeltranslation.translator import register, TranslationOptions
from .models import Betaxist, EarnMoney

@register(Betaxist)
class BetaxistTranslationOptions(TranslationOptions):
    fields = ('title', 'title2', 'join_title', 'join_descriptions', 'earnmoney_title', 'earnmoney_descriptions')

@register(EarnMoney)
class EarnMoneyTranslationOptions(TranslationOptions):
    fields = ('title', 'descriptions', 'numbers')
