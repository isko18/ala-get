# core/translation.py

from modeltranslation.translator import register, TranslationOptions
from .models import Settings, Slider, Why, OrderСity, OrderIntercity, Earn, Base, Environment

@register(Settings)
class SettingsTranslationOptions(TranslationOptions):
    fields = ('title', 'title2', 'descriptions', 'advantage1', 'advantage2', 'advantage3', 'made_title', 'made_descriptions', 'install')

@register(Slider)
class SliderTranslationOptions(TranslationOptions):
    fields = ('title_slider', 'numbering', 'descriptions', 'title_slider2')

@register(Why)
class WhyTranslationOptions(TranslationOptions):
    fields = ('why', 'title', 'descriptions')

@register(OrderСity)
class OrderСityTranslationOptions(TranslationOptions):
    fields = ('title', 'numbers', 'descriptions')

@register(OrderIntercity)
class OrderIntercityTranslationOptions(TranslationOptions):
    fields = ('title', 'numbers', 'descriptions')

@register(Earn)
class EarnTranslationOptions(TranslationOptions):
    fields = ('title', 'descriptions')

@register(Base)
class BaseTranslationOptions(TranslationOptions):
    fields = (
        'title1', 'title2', 'title3', 'title4',
        'title5', 'title6', 'title7', 'title8',
        'title9', 'descriptions', 'req','req2',
        'req3'
    )

@register(Environment)
class EnvironmentTranslationOptions(TranslationOptions):
    fields = ('title', 'descriptions', 'descriptions2', 'descriptions3')