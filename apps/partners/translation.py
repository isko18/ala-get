from modeltranslation.translator import register, TranslationOptions
from .models import Partners, LocalTaxi, PartnersSlider, PartnersSlider2

@register(Partners)
class PartnersTranslationOptions(TranslationOptions):
    fields = (
        'title', 'title2', 'descriptions', 'become_title', 'become_descriptions',
        'local_title', 'local_title2', 'local_descriptions',
        'getting_title', 'getting_descriptions', 'getting_descriptions2', 'getting_descriptions3',
        'global_title', 'global_descriptions', 'global_title2'
    )

@register(LocalTaxi)
class LocalTaxiTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(PartnersSlider)
class PartnersSliderTranslationOptions(TranslationOptions):
    fields = ('title',)

@register(PartnersSlider2)
class PartnersSlider2TranslationOptions(TranslationOptions):
    fields = ('title',)