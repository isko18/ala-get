from modeltranslation.translator import register, TranslationOptions
from .models import Delivery, Favorabledelivery


@register(Delivery)
class DeliveryTranslationOptions(TranslationOptions):
    fields = ('title', 'descriptions', 'trust_title', 'trust_descriptions', 'trust_descriptions2')

@register(Favorabledelivery)
class FavorabledeliveryTranslationOptions(TranslationOptions):
    fields = ('title_base', 'title', 'descriptions')


